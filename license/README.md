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
