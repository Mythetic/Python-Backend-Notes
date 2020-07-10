## `Canal`的介绍及安装

### 1. 简介

![canal_desc](./pic/canal_1.png)

**canal [kə'næl]**，译意为水道/管道/沟渠，主要用途是基于 `MySQL` 数据库**增量日志**解析，提供增量数据**订阅和消费**。

早期阿里巴巴因为杭州和美国双机房部署，存在跨机房同步的业务需求，实现方式主要是基于业务 trigger 获取增量变更。从 2010 年开始，业务逐步尝试数据库日志解析获取增量变更进行同步，由此衍生出了大量的数据库增量订阅和消费业务。

基于日志增量订阅和消费的业务包括：

- 数据库镜像
- 数据库实时备份
- 索引构建和实时维护(拆分异构索引、倒排索引等)
- 业务 cache 刷新
- 带业务逻辑的增量数据处理

当前的 canal 支持源端 MySQL 版本包括 5.1.x , 5.5.x , 5.6.x , 5.7.x , 8.0.x

### 2. 工作原理

#### 2.1 `MySQL`主备赋值原理

![mysql_dump](./pic/canal_2.png)

- MySQL master 将数据变更写入二进制日志( binary log, 其中记录叫做二进制日志事件binary log events，可以通过 `show binlog events` 进行查看)
- MySQL slave 将 master 的 binary log events 拷贝到它的中继日志(relay log)
- MySQL slave 重放 relay log 中事件，将数据变更反映它自己的数据

#### 2.2 canal 工作原理

- canal 模拟 MySQL slave 的交互协议，伪装自己为 MySQL slave ，向 MySQL master 发送dump 协议
- MySQL master 收到 dump 请求，开始推送 binary log 给 slave (即 canal )
- canal 解析 binary log 对象(原始为 byte 流)

### 3. Canal的安装

#### 3.1 MySQL准备工作

- 对于自建 MySQL , 需要先开启 `Binlog` 写入功能，配置 `binlog-format` 为 `ROW` 模式，`my.cnf` 中配置如下

  ```sql
  [mysqld]
  log-bin=mysql-bin # 开启 binlog
  binlog-format=ROW # 选择 ROW 模式
  server_id=1 # 配置 MySQL replaction 需要定义，不要和 canal 的 slaveId 重复
  ```

- 授权 canal 链接 MySQL 账号具有作为 `MySQL slave` 的权限, 如果已有账户可直接 grant

  ```mysql
  CREATE USER canal IDENTIFIED BY 'canal';  
  GRANT SELECT, REPLICATION SLAVE, REPLICATION CLIENT ON *.* TO 'canal'@'%';
  -- GRANT ALL PRIVILEGES ON *.* TO 'canal'@'%' ;
  FLUSH PRIVILEGES;
  ```

#### 3.2 下载安装Canal

- 下载 canal, 访问 [release 页面](https://github.com/alibaba/canal/releases) , 选择需要的包下载, 如以 1.0.17 版本为例

  ```bash
  wget https://github.com/alibaba/canal/releases/download/canal-1.0.17/canal.deployer-1.0.17.tar.gz
  ```

- 解压缩

  ```bash
  mkdir /usr/lcoal/canal
  tar zxvf canal.deployer-$version.tar.gz  -C /usr/lcoal/canal
  ```

- 解压完成后，进入 `/usr/lcoal/canal`目录，可以看到如下结构

  ```bash
  drwxr-sr-x  2 root staff 4096 Jul  7 16:28 bin
  drwxr-sr-x  5 root staff 4096 Jul  7 16:17 conf
  drwxr-sr-x  2 root staff 4096 Jul  7 16:17 lib
  drwxrwxrwx  4 root root  4096 Jul  7 16:22 logs
  ```

- 配置修改

  ```
  vim conf/example/instance.properties
  ```

  ```
  ## mysql serverId
  canal.instance.mysql.slaveId = 1234
  #position info，需要改成自己的数据库信息
  canal.instance.master.address = 127.0.0.1:3306 
  canal.instance.master.journal.name = 
  canal.instance.master.position = 
  canal.instance.master.timestamp = 
  #canal.instance.standby.address = 
  #canal.instance.standby.journal.name =
  #canal.instance.standby.position = 
  #canal.instance.standby.timestamp = 
  #username/password，需要改成自己的数据库信息
  canal.instance.dbUsername = canal  
  canal.instance.dbPassword = canal
  canal.instance.defaultDatabaseName =
  canal.instance.connectionCharset = UTF-8
  #table regex
  canal.instance.filter.regex = .\*\\\\..\*
  ```

  - `canal.instance.connectionCharset` 代表数据库的编码方式对应到 java 中的编码类型，比如 UTF-8，GBK , ISO-8859-1
  - 如果系统是1个`cpu`，需要将 `canal.instance.parser.parallel` 设置为 false

- 启动

  ```bash
  sh bin/startup.sh
  ```

- 查看 server 日志 

  ```
  vim logs/canal/canal.log</pre>
  ```

  ```bash
  2013-02-05 22:45:27.967 [main] INFO  com.alibaba.otter.canal.deployer.CanalLauncher - ## start the canal server.
  2013-02-05 22:45:28.113 [main] INFO  com.alibaba.otter.canal.deployer.CanalController - ## start the canal server[10.1.29.120:11111]
  2013-02-05 22:45:28.210 [main] INFO  com.alibaba.otter.canal.deployer.CanalLauncher - ## the canal server is running now ......
  ```

- 查看 `instance` 的日志

  ```bash
  vim logs/example/example.log
  ```

  ```bash
  2013-02-05 22:50:45.636 [main] INFO  c.a.o.c.i.spring.support.PropertyPlaceholderConfigurer - Loading properties file from class path resource [canal.properties]
  2013-02-05 22:50:45.641 [main] INFO  c.a.o.c.i.spring.support.PropertyPlaceholderConfigurer - Loading properties file from class path resource [example/instance.properties]
  2013-02-05 22:50:45.803 [main] INFO  c.a.otter.canal.instance.spring.CanalInstanceWithSpring - start CannalInstance for 1-example 
  2013-02-05 22:50:45.810 [main] INFO  c.a.otter.canal.instance.spring.CanalInstanceWithSpring - start successful....
  ```

- 关闭

  ```bash
  sh bin/stop.sh
  ```

### 4. **canal-python**的安装

`canal-python` 是阿里巴巴开源项目 [Canal](https://github.com/alibaba/canal)是阿里巴巴`mysql`数据库`binlog`的增量订阅&消费组件 的 `python` 客户端。为 python 开发者提供一个更友好的使用 Canal 的方式。

**应用场景**:

`canal-python` 作为Canal的客户端，其应用场景就是Canal的应用场景。关于应用场景在Canal介绍一节已有概述。举一些实际的使用例子：

1. 代替使用轮询数据库方式来监控数据库变更，有效改善轮询耗费数据库资源。

2. 根据数据库的变更**实时更新搜索引擎**，比如电商场景下商品信息发生变更，实时同步到商品搜索引擎 `Elasticsearch`、`solr`等

3. 根据数据库的变更**实时更新缓存**，比如电商场景下商品价格、库存发生变更实时同步到`redis`

4. 数据库异地备份、数据同步

5. 根据数据库变更触发某种业务，比如电商场景下，创建订单超过xx时间未支付被自动取消，我们获取到这条订单数据的状态变更即可向用户推送消息。

6. 将数据库变更整理成自己的数据格式发送到`kafka`等消息队列，供消息队列的消费者进行消费。

**工作原理**：

`canal-python`  是 Canal 的 python 客户端，它与 Canal 是采用的Socket来进行通信的，传输协议是TCP，交互协议采用的是 `Google Protocol Buffer 3.0`。

**工作流程**:

1. Canal连接到`mysql`数据库，模拟slave

2. `canal-python` 与 `Canal` 建立连接
3. 数据库发生变更写入到`binlog`
4. Canal向数据库发送`dump`请求，获取`binlog`并解析
5. canal-python 向 Canal 请求数据库变更
6. Canal 发送解析后的数据给canal-python
7. canal-python收到数据，消费成功，发送回执。（可选）
8. Canal记录消费位置。

**环境要求**:

`python >= 3`

**构建canal python客户端**:

```shell
pip install canal-python
```

**示例**：

1. 下载`canal-python-master`，执行`example.py`，可见`canal-python`与`Canal`建立了连接：

**终端1**：

```python
root@debian8:/home/jason/share/canal-python-master/canal# python3.7 example.py 
connected to 127.0.0.1:11111		# 11111是canal的监听端口
Auth succed
Subscribe succed
```

2. 连接`MySQL`，执行`DML`语句：

**终端2**：

```mysql
mysql> insert into canal_test (name) values ("111");
Query OK, 1 row affected (0.01 sec)

mysql> delete from canal_test where name="111";
Query OK, 1 row affected (0.01 sec)

mysql> insert into canal_test (name) values ("555");
Query OK, 1 row affected (0.01 sec)

mysql> update canal_test set name="111" where name="555";
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0
```

此时**终端1**为：

```shell
root@debian8:/home/jason/share/canal-python-master/canal# python3.7  example.py 
connected to 127.0.0.1:11111
Auth succed
Subscribe succed

{'db': 'test', 'table': 'canal_test', 'event_type': 1, 'data': {'name': '111'}}
{'db': 'test', 'table': 'canal_test', 'event_type': 3, 'data': {'name': '111'}}
{'db': 'test', 'table': 'canal_test', 'event_type': 1, 'data': {'name': '555'}}
{'db': 'test', 'table': 'canal_test', 'event_type': 2, 'data': {'before': {'name': '111'}, 'after': {'name': '111'}}}
```

由此可见，`MySQL`的`DML`语句被`canal_python_client`所捕获。

![](./pic/canal.png)







