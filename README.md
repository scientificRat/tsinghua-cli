# Tsinghua-cli
> 命令行连接清华校园网的工具   

* 没有显示器的设备连接校园网, 如树莓派等嵌入式设备
* 服务器连外网（风险自负）
* 其他不方便打开浏览器联网的设备连接校园网  


### requirements
* python>=3.5 (python>=2.7)
* requests
### 安装
```bash
pip install git+https://github.com/scientificRat/tsinghua-cli.git
```

### 使用说明  
可用于 登陆/退出/查询 校园网登陆状态  

```bash
usage: tsinghua_cli [-h] [--username USERNAME] [--password PASSWORD] action

Connection tool for Tsinghua

positional arguments:
  action                login / logout / status

optional arguments:
  -h, --help            show this help message and exit
  --username USERNAME, -u USERNAME
  --password PASSWORD, -p PASSWORD
``` 
### demo
```bash
$ tsinghua_cli status
$ tsinghua_cli login -u xxxx -p xxxxxx
$ tsinghua_cli logout
```
