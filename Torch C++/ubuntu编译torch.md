# ubuntu 上编译安装torch

1. 使用conda 下载 pytorch 这里我用的是pytorch-cpu

2. 使用cmake编译

   - 首先将git设置socks5代理以下载加速

     ```bash
     git config --global http.proxy 'socks5://192.168.127.1:7891'
     git config --global https.proxy 'socks5://192.168.127.1:7891'
     
     # 下载完毕后清除系统代理
     git config --global --unset http.proxy
     ```

     

   ```bash
   git clone --recursive https://github.com/pytorch/pytorch
   ```

   