# WinMon
Windows Monitor Blocker Hider

### 设计目标：
1. Procmon.exe有的，这里一般不添加，除非它识别的不友好。这个程序不能长时间运行。  
   不一定比Procmon好用，但一定比Procmon有用（特别对于特别的，稀少的查询和阻断）。  
2. Sysmon.exe有的一般都添加。
3. 其他奇特的，别的工具少有的监控。
4. 自己喜欢的，觉得有用的。
5. 应用层能实现的一般不添加，除非自己喜欢。
6. 尽量实现阻断的功能。
7. 无GUI。
8. 支持Windows 7 SP1(Windows server 2008 R2)及以后的版本.
9. 使用需授权：SHA512 + ECDSA_P521，在驱动验签。
10. 收集（如果联网的话）信息（一条）到服务器（debian + nginx + php + mysql）。

### 具体的功能：
1. ICMP，ARP，RARP通讯的进程信息。没有关联进程信息的也显示。  
   既非IPv4也不是IPv6的网络信息。用WFP实现。  
2. Obmon。监控进程，线程，桌面的访问。  
3. 命名管道和邮件槽的监控。  
4. 线程注入的监控。  
   如：CreateRemoteThread，还有APC等，以线程启动的shellcode（内核的SHELLCODE）。  
   进程创建的第一个线程（主线程）属于线程注入，可以考虑不显示。  
5. 磁盘级别的文件访问。RawAccessRead。  
6. 一些特殊且重要的设备的操作。附加设备。  
7. 无文件的模块的加载。  
   这里承诺只能拦截自己能拦截的，不是保证所有的。  
8. 进程的特殊启动（有待实现）。  
   如：ProcessTampering，herpaderp，hollow。  
9. 权限，令牌，用户，登录相关的，想想。
10. DNSLOG.  
11. ETW-TI(ThreatIntelligence)。这个有点占用CPU。

### 日志类型：
1. 少许信息Dbgview.exe输出。
2. 机密信息使用WPP，用traceview.exe查看。
3. 启动信息（exe/sys的日志系统初始化之前）在事件查看器。
4. 驱动日志在：%systemdrive%\winmon目录下。
5. winmon.exe的日志在：这个文件所在目录的log目录下。

### 设计框架：
1. 驱动采集信息并阻断。如：minifilter，wfp，以及各种回调，附加设备进行过滤等。
2. 应用层采集部分信息。如：ETW。
3. 应用层封装一个DLL。对外提供服务。
4. 驱动和应用层的通讯采用minifilter的CommunicationPort。
5. 驱动和应用层的通讯格式是TLV。
6. 应用层的DLL对外输出的格式是JSON。
7. winmon.exe输出是SQLite。
8. 配置文件的格式也是JSON。
9. 开关加持便于控制CPU，内存，磁盘，网速等。

### 版本功能

| 功能 | FREE版本 | VIP版本 |
| :--- | :--- | :--- |
| 驱动采集 | 有 | 有 |
| 驱动阻断 | 有 | 有 |
| DNS记录 | 有 | 有 |
| 威胁情报 | 无 | 有 |
| 文件隐藏 | 有 | 有 |
| 注册表隐藏 | 有 |有 |
| 端口隐藏 | 无 | 有 |
| 进程隐藏 | 无 | 有 |
| 驱动隐藏 | 无 | 有 |
| 模块隐藏 | 无 | 有 |
| WSK + TLS 客户端 | 有 | 有 |
| WSK + TLS 服务端 | 无 | 有 |
| 驱动停止 | 是 | 否 |
| 最大规则条数 | 999 | 99999 |

2024/1/29
