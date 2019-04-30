# EasyCMDB基础版## 离线安装方式1.	上传安装器（cmdb-community-xxxx.tar.gz）到机器上2.	请将其解压，并mv到/usr/local/ucpro，目录结构如：![s2](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/ucpro_目录结构.png)3.	启动安装器./bin/start.sh，并在浏览器登陆http://ip:4200（ip为该机器ip，用chrome浏览器）![s3](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/离线安装首页.png)4.	点击离线安装，并输入安装的主机IP及主机密码![s4](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/离线安装_输入主机名:密码.png)5.	点击下一步，他会做环境检查。如果有问题，请按提示处理![s5](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/离线安装_环境检查.png)6.	点击上传部署包（因为我们的这个部署包是已经带有部署包的了，所以可以直接点击下一步）![s6](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/离线安装_上传部署包.png)7.	安装，请耐心等待勿刷新浏览器，一般安装时间为2~3分钟
![s7](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/离线安装_安装ing.png)
安装完成后，将会显示默认用户名密码。该密码保存在/root/.easyops文件，也可以在上面查看
![s7](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/离线安装_安装成功.png)
8. 服务检查![s8](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/离线安装_服务状态.png)9.	登录平台请登录http://ip（该ip为刚才安装机器的ip）
![s9](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/离线安装_登录首页.png)
![s9](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/离线安装_登录成功.png)
恭喜你，已经可以正常使用了！10.	卸载，如果需要卸载，请执行如下命令sh /data/easyops/tmp/uc/tools/easyops_uninstall.sh
![s9](https://raw.githubusercontent.com/easycmdb/easycmdb/master/img/离线安装_卸载.png)