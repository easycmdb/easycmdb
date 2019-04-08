EasyCMDB安装指南
================


安装资源准备
------------

### 获取安装包

[http://cdn.uwintech.cn/data/release_package/packed_pkgs/cmdb-community-ucpro-build.latest.tar.gz]

安装环境准备
------------

### 系统版本

系统版本:CentOS/RHEL 6.5\~6.8

### 硬件选择

最低配置: 4GB以上内存，磁盘空间50GB以上

### 系统环境

1.保证系统环境干净，如有运 mysql、nginx、apache、mongodb
等程序，会导致安装失败

2.开放服务器端口22、5511、8820

3.安装nc，安装命令：yum install -y nc

完整安装
========

ucpro可视化安装
---------------

### 下载ucpro安装包

[http://cdn.uwintech.cn/data/release_package/packed_pkgs/cmdb-community-ucpro-build.latest.tar.gz]

### 部署ucpro

将下载的ucpro包，例如:enterprise-ucpro-build.38.tar.gz，(建议将UCpro放在easyCMDB部署服务器上)，解压后重命名为ucpro,并拷贝至/usr/local目录下

解压后的目录

/usr/local/ucpro

├── bin

├── log

├── nginx

├── package.conf.yaml

├── tools

├── ucpro_service

├── ucpro_web

└── version.ini

### ucpro启动停止命令

-   启动：进入/usr/local/ucpro, 执行./bin/start.sh；

-   停止：进入/usr/local/ucpro，执行./bin/stop.sh；

-   重启：进入/usr/local/ucpro，执行./bin/restart.sh；

### 启动ucpro

>   注意：确保端口4200已经开通的，然后确保nginx没有启动。

>   1）cd /usr/local/ucpro/ 首先进入ucpro安装目录下

>   2）./bin/start.sh 启动ucpro

>   如果是新用户，部署完ucpro,启动ucpro,然后使用chrome浏览器打开端口访问)

>   新安装客户，可以点击【平台安装】按钮

![](https://github.com/easycmdb/easycmdb/blob/master/img/平台安装.png)

### 主机选择

1.点击【平台安装】，系统判断可联网，则进入“在线安装”流程；

![C:\\Users\\wehat\\Desktop\\image2019-3-6 19_7_49.png](https://github.com/easycmdb/easycmdb/blob/master/img/在线安装.png)

注意：如果出现报错可能是/usr/local/ucpro/ucpro_service/conf下没有license,需要卸载重新部署，然后把license放到conf目录下

2.环境检查完成后然后会出现组件下载。

![](https://github.com/easycmdb/easycmdb/blob/master/img/组件下载.png)

3.已经安装完成。

![](https://github.com/easycmdb/easycmdb/blob/master/img/安装完成.png)

4.环境检测完成证明已经安装完成。

![](https://github.com/easycmdb/easycmdb/blob/master/img/环境检测完成.png)




