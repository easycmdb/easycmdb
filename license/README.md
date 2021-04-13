证书更新步骤
  1. 将license_pkg.tar.gz放到服务端机器一个目录中，比如~/easyosp_license/
  2. 备份原有证书文件 
    cp /usr/local/easyops/etc/easyops.lic /usr/local/easyops/etc/easyops.lic.bak 
  3. 解压执行证书替换脚本 
  4. 执行命令
    tar xf license_pkg.tar.gz && cd license_pkg && ./start.sh
