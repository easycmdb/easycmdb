EasyCMDB安装指南
================

第1章 快速安装EasyCMDB平台
==========================

安装资源准备
------------

### 获取安装包

Curl -I xxxx.easyops.com

git clone …………………

安装环境准备
------------

### 系统版本

系统版本:CentOS/RHEL 6.5\~6.8

### 硬件选择

 最低配置: 4核CPU、16GB以上内存，/data/可用空间100GB以上，/usr/local/空间10GB以上 ，/tmp/ 可用空间10GB以上

### 系统环境

- 保证系统环境干净，如有运行 mysql、nginx、apache、mongodb等程序，会导致安装失败
- 开放服务器端口22、5511、8820
- 安装nc，安装命令：yum install -y nc

安装步骤
--------

（1）上传安装包到机器上

（2）进入安装目录cd EasyOps-xx.xx.xx

（3）安装EasyOps平台

a）进入安装包的目录下，执行./bin/easyuc -h可查看帮助文档

b）单机安装EasyOps平台,进入到解压后的目录下，参数说明: -ip (127.0.0.1), -org
(default 8888), -p (本机可不填), -port(default 22),-u(default
“root”),-license(选填)

执行例子：./bin/easyuc -ip 127.0.0.1 -license /tmp/easyops_Enterprise_0715.lic

（一定要在bin的同级目录执行）-license
参数选填！（如果不填，默认用php_license组件里的license文件(其中org是分配给您的组织编号,
-port, -u有默认值，-h 可以查看帮助文档, license可以找EasyOps人员获取)）

c)通过conf/EasyOps.yaml查看安装的组件，以及组件依赖关系

安装完成
--------

- 安装成功后,在浏览器中输入对应IP进入即可。
- 管理员用户名为EasyOps，初始密码为随机密码，保存在 \~/.EasyOps中, 执行"cat
    \~/.EasyOps"命令查看密码。
- 程序安装的目录在/usr/local/easyops/下。

第2章 完整安装及卸载
==============

查看UC命令参数
--------------

-h可以查看UC命令参数

![查看参数](https://github.com/easycmdb/easycmdb/blob/master/img/uc命令参数1.png)

单机部署EasyOps平台
-------------------

（1）单机安装easyops平台，进入解压后的首层目录下.

（2）参数说明：-ip(127.0.0.1 -org (default 8888) -p(本机可不填) -port(default
22) -u(default "root") -license）

执行命令例子：./bin/easyuc -ip 127.0.0.1 -license
/tmp/easyops_Enterprise_0715.zl

![单机部署](https://github.com/easycmdb/easycmdb/blob/master/img/单机部署.png)

## EasyOps平台卸载

（1）把准备装的压缩包放到部署服务器**随意**目录下，例如：/tmp目录或者/root目录；

（2）解压要部署的安装包，进入解压后的**首层目录**下，例如：/tmp/easyops-5.build.001，不能进入bin目录下。

（3）用-ip参数指定机器，如果给本机安装，那么参数值是127.0.0.1；

执行命令例子:

./bin/easyuc -ip 127.0.0.1 -uninstall(一定要在bin的同级目录执行)

集群部署EasyOps平台
-------------------

### 修改平台安装包下的easyops_hosts.ini

(1) 进入平台安装包的conf目录下（如:/tmp/easyopsCMDB.build.001/conf）

![修改安装包](https://github.com/easycmdb/easycmdb/blob/master/img/修改平台安装包.png)

(2) 根据集群机器数选用哪个easyops_hosts-X.ini，执行命令“cp easyops_hosts-X.ini
easyops_hosts.ini”，例如：5机的集群，执行命令“cp easyops_hosts-5.ini
easyops_hosts.ini”

执行实例：

cp easyops_hosts-5.ini easyops_hosts.ini

3）修改easyops_hosts.ini，正确填写IP、密码和端口，配置集群所有机器的ip地址（内网ip）；注：外网IP机器一定要装console

4) 如果是初始安装的，以easyops_hosts.ini里[hostX]分配为准，就是说[host4]是mongo
primary，[host5]是mongo
secondary，IP地址按需分配下去就行（如果内网测试，按顺序编排下去就行）

但如果是升级集群，先要看现网mongo
primary和mongo secondary在什么IP上，根据现网实际使用把对应的IP填写到[host3]、[host4]和[host5]

## 集群卸载

只需要在集群一台机器上执行下面命令，可以用于卸载旧uc安装的easyops平台，参数-hosts
指定卸载哪些机器（easyops_hosts.ini 的配置看上面1的描述）；

执行命令例子：./bin/easyuc –hosts
/tmp/easyops-3.build.001/conf/easyops_hosts.ini
-uninstall(一定要在bin的同级目录执行)

![集群卸载](https://github.com/easycmdb/easycmdb/blob/master/img/集群卸载.png)
