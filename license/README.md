证书更新步骤
1. 在服务端所有机器上备份原有证书文件
    ```bash
    cp /usr/local/easyops/etc/easyops.lic /usr/local/easyops/etc/easyops.lic.`date +%s`
    ```
2. 在服务端所有机器上,用最新的easyops.lic文件替换 /usr/local/easyops/etc/easyops.lic文件
3. 修改文件属主和权限
    ```bash
   chown easyops:easyops /usr/local/easyops/etc/easyops.lic 
   chmod 644 /usr/local/easyops/etc/easyops.lic 
    ```


20210413更新证书步骤:
  1. 将20210314中license_pkg.tar.gz放到服务端机器一个目录中，比如~/easyosp_license/
  2. 备份原有证书文件 
    cp /usr/local/easyops/etc/easyops.lic /usr/local/easyops/etc/easyops.lic.bak 
  3. 解压执行证书替换脚本 
  4. 执行命令
    tar xf license_pkg.tar.gz && cd license_pkg && ./start.sh
