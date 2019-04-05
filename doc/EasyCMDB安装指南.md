EasyCMDB安装指南
================

快速安装EasyCMDB平台
==========================

安装资源准备
------------

### 获取安装包

git clone xxxxxxxxxxxxxxxxxxxxxxxx

安装环境准备
------------

### 系统版本

1.  系统版本:CentOS/RHEL 6.5\~6.8

### 硬件选择

1.  最低配置: 4GB以上内存，磁盘空间50GB以上

### 系统环境

（1）保证系统环境干净，如有运 mysql、nginx、apache、mongodb
等程序，会导致安装失败

（2）开放服务器端口22、5511、8820

（3）安装nc，安装命令：yum install -y nc

完整安装
========

ucpro可视化安装
---------------

### 下载ucpro安装包

git clone xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

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

1.  点击【平台安装】，系统判断可联网，则进入“在线安装”流程；

![C:\\Users\\wehat\\Desktop\\image2019-3-6 19_7_49.png](https://github.com/easycmdb/easycmdb/blob/master/img/在线安装.png)

C:\\Users\\wehat\\Desktop\\image2019-3-6 19_7_49.png

C:\\Users\\wehat\\Desktop\\image2019-3-6 19_7_49.png

注意：如果出现报错可能是/usr/local/ucpro/ucpro_service/conf下没有license,需要卸载重新部署，然后把license放到conf目录下

2.环境检查完成后然后会出现组件下载。

![](https://github.com/easycmdb/easycmdb/blob/master/img/组件下载.png)

3.已经安装完成。

![](https://github.com/easycmdb/easycmdb/blob/master/img/安装完成.png)

4.环境检测完成证明已经安装完成。

![](https://github.com/easycmdb/easycmdb/blob/master/img/环境检测完成.png)

手动安装
--------

### 安装步骤

（1）上传安装包到机器上

（2）进入安装目录cd EasyOps-xx.xx.xx

（3）安装EasyOps平台

-   a）进入安装包的目录下，执行./bin/easyuc -h可查看帮助文档

-   b）单机安装EasyOps平台,进入到解压后的目录下，参数说明: -ip (127.0.0.1), -org
    (default 8888), -p (本机可不填), -port(default 22),-u(default
    “root”),-license(选填)

-   执行例子：./bin/easyuc -ip 127.0.0.1 -license
    /tmp/easyops_Enterprise_0715.lic

-   （一定要在bin的同级目录执行）-license
    参数选填！（如果不填，默认用php_license组件里的license文件(其中org是分配给您的组织编号,
    -port, -u有默认值，-h 可以查看帮助文档, license可以找EasyOps人员获取)）

-   c)通过conf/EasyOps.yaml查看安装的组件，以及组件依赖关系

### 查看UC命令参数

（1）-h可以查看UC命令参数

![](https://github.com/easycmdb/easycmdb/blob/master/img/查看uc命令参数.png)

### 单机部署EasyOps平台

（1）单机安装easyops平台，进入解压后的首层目录下.

（2）参数说明：-ip(127.0.0.1 -org(default 8888) -p(本机可不填) -port(default 22)
-u(default "root") -license）

执行命令例子：./bin/easyuc -ip 127.0.0.1 -license
/tmp/easyops_Enterprise_0715.zl

![](https://github.com/easycmdb/easycmdb/blob/master/img/单机部署.png)

### EasyOps平台卸载

（1）把准备装的压缩包放到部署服务器随意目录下，例如：/tmp目录或者/root目录；

（2）解压要部署的安装包，进入解压后的首层目录下，例如：/tmp/easyops-5.build.001，不能进入bin目录下。

（3）用-ip参数指定机器，如果给本机安装，那么参数值是127.0.0.1；

执行命令例子:

./bin/easyuc -ip 127.0.0.1 -uninstall(一定要在bin的同级目录执行)

### 安装完成

1.  安装成功后,在浏览器中输入对应IP进入即可。

2.  管理员用户名为EasyOps，初始密码为随机密码，保存在 \~/.EasyOps中, 执行"cat
    \~/.EasyOps"命令查看密码。

3.  程序安装的目录在/usr/local/easyops/下。
