EasyCMDB快速上手手册
====================

### 平台登录

-   登录页面

首先我们进入平台页面，登录进去，看到平台的首页

![登录页面](https://github.com/easycmdb/easycmdb/blob/master/img/登录页面.png)

-   平台首页

![平台首页](https://github.com/easycmdb/easycmdb/blob/master/img/平台首页.png)

### 创建模型

>   首先，【在右上角处】---【单击小齿轮】---【模型管理】---【新建资源模型】---【输入模型内容】

![](https://github.com/easycmdb/easycmdb/blob/master/img/输入模型内容.png)

>   根据模型相对应的关系，输入内容，点击保存，则创建成功。如下图

![](https://github.com/easycmdb/easycmdb/blob/master/img/模型创建成功.png)

>   安装流程：

![](https://github.com/easycmdb/easycmdb/blob/master/img/安装流程.png)

### 建立模型关系

>   资源通过某种方式建立起两者之间联系，这种联系叫做关系，首先【右上角】---【模型管理】---【选择创建的模型】---【关系】---【添加】

>   流程：

![](https://github.com/easycmdb/easycmdb/blob/master/img/添加模型关系.png)

>   下图是建立好的模型关系

![](https://github.com/easycmdb/easycmdb/blob/master/img/模型关系.png)

### 创建实例

>   实例是资源模型中管理的数据的具体展现，用户可以对这些实例数据进行维护，以达到管理IT资源的能力。创建步骤【IT资源管理】---【自动采集】---【管理】---【选择模型】---【新建插件】---【填好配置信息】---【保存】

>   下图是流程：

![](https://github.com/easycmdb/easycmdb/blob/master/img/创建实例流程.png)

>   首先我们新建插件脚本格式：

```\#!/usr/local/easyops/python/bin/python

\# encoding: utf-8

json_data = [{

"name": "host_name",\#这个是定义属性自带并且唯一的名称

"ip": "192.168.1.1",\#这个是定义模型IP的字段

"port": 22, \#这个是定义模型端口的字段

}, ]

AutoDiscoveryJson(json_data,object_id="HOST_DAEMO") \#object_id
后面接的是模型的ID```

![](https://github.com/easycmdb/easycmdb/blob/master/img/新建插件脚本格式.png)

>   然后点【执行】，会提示上传成功。这个时候还没有成功，然后点击自动采集，

>   启动规则，这个时候我们的实例就创建成功了。

![](https://github.com/easycmdb/easycmdb/blob/master/img/实例创建成功.png)

### 安装Agent录入主机信息

>   安装Agent有两种方法，一种是通过平台直接安装Agent,一种是通过手动去安装Agent。

>   安装步骤:【右边单击小齿轮】---【选择Agent管理】---【选择安装Agent】

>   流程：

![](https://github.com/easycmdb/easycmdb/blob/master/img/选择安装agent.png)

>   Agent安装完成后，对机器进行采集，成功后。入下图

![](https://github.com/easycmdb/easycmdb/blob/master/img/安装agent成功.png)

### 自动发现

>   自动发现功能是用工具或者插件去采集机器上的静态信息或者配置信息,使用步骤【单击-IT资源管理】---【自动采集】---【右上角-管理】---【选择采集的模型】---【新建插件】---【跳转到工具库】---【根据规则填好采集脚本】，如果不懂规则，可以在脚本代码旁边单机【说明】，里面就有帮助信息。

>   流程：

![](https://github.com/easycmdb/easycmdb/blob/master/img/自动发现.png)

下图是自动采集上报的数据成功的图

![](https://github.com/easycmdb/easycmdb/blob/master/img/自动采集.png)
