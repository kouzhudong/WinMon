### 驱动支持的操作（记录和阻断）有：

    u8"PipeOpen",
    u8"PipeCreate",

    u8"MailslotOpen",
    u8"MailslotCreate",

    u8"StreamOpen",
    u8"StreamCreate",

    u8"RawAccessOpen",

    u8"FileCreated",
    u8"FileSuperseded",
    u8"FileOverwritten",

    u8"FileSystemControl",
    u8"DeviceControl",
    //u8"InternalDeviceControl",
    //u8"SystemControl",

    u8"FileDeleted",
    u8"FileRenamed",

    u8"FileImpersonate",
    u8"FileOpenById",
    u8"FileHardlinkCreate",

    u8"Section",

    u8"LoadKey",
    u8"UnLoadKey",

    u8"RestoreKey",
    u8"SaveKey",
    u8"ReplaceKey",

    u8"CreateKey",
    u8"DeleteKey",
    u8"RenameKey",

    u8"SetValueKey",    这个能识别出符号链接的创建
    u8"DeleteValueKey",

    u8"Arp",
    u8"Icmp",

    u8"Listen",
    u8"Accept",
    u8"Connect",

    u8"ProcessAccess",
    u8"ThreadAccess",
    u8"DesktopAccess",

    //u8"CreateRemoteThread",
    //u8"ShellcodeExecute",
    //u8"CreateKernelThread",
    u8"ThreadStart",    这个能识别出几个操作

    //u8"LoadDriver",
    //u8"LoadMemoryModule",
    u8"LoadImage",      这个能识别出几个操作

    //u8"ProcessTampering",
    u8"ProcessStart",   这个能识别出几个操作

应用层能识别的更多些。

---

### DNS暂时处理：
1. A
2. AAAA
3. PTR
4. SRV

过滤条件是标准的ETW DNS选项。

---

### ThreatIntelligence支持的有（仅仅支持VIP版本）：

ProtectVmLocal  
ProtectVmRemote  
ProtectVmLocalKernelCaller  

AllocVmLocal  
AllocVmRemote  
AllocVmLocalKernelCaller  

MapViewLocal  

ReadVmRemote  
WriteVmRemote  
WriteVmLocal  

DeviceObjectLoad  
DeviceObjectUnload  
DriverObjectLoad  

SuspendThread  
ResumeThread  

QueueUserApcRemoteKernelCaller  
QueueUserApcRemote  

过滤条件是标准的ETW TI选项，尽管有好几个版本。

---

### 可配置的条件有（适用于驱动的）：

    u8"FilePath",
    u8"FileSourcePath",
    u8"FileTargetPath",
    u8"DevicePath",
    u8"StreamPath",

    u8"KeyPath",
    u8"KeySourcePath",
    u8"KeyTargetPath",
    u8"KeyValueName",

    u8"PipePath",
    u8"MailslotPath",

    u8"ProcessPath",
    u8"ProcessSourcePath",
    u8"ProcessTargetPath",
    u8"CommandLine",
    u8"ParentCommandLine",

    u8"User",
    u8"ClientUser",
    u8"PrimaryUser",

    u8"Image",
    u8"ParentImage",

    u8"DesktopName",

    u8"Object",

    u8"Issuer",
    u8"Subject",

    u8"",//PATH_MAX MEMBER_MIN

    //整数

    u8"IsDirectory",
    u8"IsCreate",
    u8"IsSigned",
    u8"IsKernelThread",
    u8"IsRemoteThread",
    u8"IsShellcode",
    u8"IsDriver",
    u8"IsMemoryModule",

    u8"Protocol",
    u8"Checksum",
    u8"LocalPort",
    u8"RemotePort",

    u8"IsDuplicatHandle",
    u8"NtStatus",
    u8"Flags",
    u8"Index",
    u8"Type",
    u8"Code",
    u8"SessionId",
    u8"DesiredAccess",
    u8"OriginalDesiredAccess",
    u8"RemainingDesiredAccess",
    u8"PreviouslyGrantedAccess",
    u8"GrantedAccess",
    u8"ShareAccess",
    u8"ImpersonationLevel",
    u8"FsControlCode",
    u8"IoControlCode",
    u8"IntegrityLevel",
    u8"PageProtection",
    u8"Direction",
    u8"Protected",

    u8"Address",
    u8"Data",
    u8"ProcessId",
    u8"SourceProcessId",
    u8"TargetProcessId",
    u8"ParentProcessId",
    u8"CreatingProcessId",
    u8"ThreadId",
    u8"SourceThreadId",
    u8"TargetThreadId",
    u8"CreatingThreadId",
    u8"ImageBase",
    u8"ImageSize",

    u8"UtcTime",

    u8"",//MEMBER_MAX

    //二进制

    u8"LocalIPv4",//IPv4地址或者IPv4子网掩码（CIDR格式）。
    u8"LocalIPv6",//IPv6地址或者IPv6子网前缀（CIDR格式）。
    u8"LocalMac", //短横间隔，形如：F4-CE-46-2D-90-8C。

    u8"RemoteIPv4",//IPv4地址或者IPv4子网掩码（CIDR格式）。
    u8"RemoteIPv6",//IPv6地址或者IPv6子网前缀（CIDR格式）。
    u8"RemoteMac", //短横间隔，形如：F4-CE-46-2D-90-8C。

    u8"LogonId",
    u8"Guid",
    u8"Md5",
    u8"Sha256",
    u8"Sid",
    u8"Sd",

---

### 支持的运算有：

    u8"Is",             支持字符串（单/宽）和整数（BYTE/WORD/DWORD/LONGLONG）
    u8"IsNot",          上面的反操作

    u8"LessThan",       支持字符串（单/宽）和整数（BYTE/WORD/DWORD/LONGLONG）
    u8"MoreThan",       上面的反操作

    u8"BeginWith",      支持字符串（单/宽）
    u8"EndWith",        支持字符串（单/宽）

    u8"Contain",        支持字符串（单/宽） 
    u8"Exclude",        上面的反操作

    u8"BitAnd",         支持整数（BYTE/WORD/DWORD/LONGLONG）
    u8"BitAndNot",      上面的反操作

    u8"IPv4SubNetMask",         仅仅支持IPv4
    u8"IPv4SubNetMaskNot",      上面的反操作

    u8"IPv6SubNetPrefix",       仅仅支持IPv6
    u8"IPv6SubNetPrefixNot",    上面的反操作

---

### 规则设计要点：
1. 设计简单点。  
   只有开关（总开关和细分开关），黑名单和白名单以及灰名单（既非白名单也不是黑名单）。  
2. 规则要分开。  
   记录（日志）规则和阻断规则及网络规则（暂时在DPC上，需要非分页内存）。
3. 支持Procmon和SysMon的比较规则。  
   如：大于，等于，小于，包含，以XXX开头，以XXX结尾等。
4. 只有黑名单。日志：符合配置的不上报，阻断的只要匹配都阻断。
5. 多条规则之间是或的关系，一条规则的几个条件之间是与的关系。  
6. 文件路径不支持盘符，而是类似于：\Device\HarddiskVolume3\Windows\System32\svchost.exe
7. 注册表的路径，是内核路径，如：\REGISTRY\MACHINE\SYSTEM\ControlSet001\Control\hivelist
8. 一条规则最多有5个条件。
9. 规则/条件里的字符数不能超过260。本想设计为32767/1024/PAGE_SIZE，其实没这个必要。
10. 规则/条件里的二进制（字节）不能超过520。
11. 规则的个数最大是999条（日志规则999条，网络日志999条，阻断日志999条，网络阻断日志999条）。

### 规则配置要点：
1. 文件，注册表，网络，应该基于进程操作，相信进程。
2. 线程，模块，进程，这时，这些操作，要谨慎，预防恶意攻击。严格审查。有传染性。
3. 以文件或目录为结尾的配置，要在文件或目录的前面加个斜杠。
4. 以目录为开头的配置，要在目录的后面加个斜杠。
5. 尽量少配置字符串，或者字符串的放在后面，会快点。
6. 数字匹配的规则放前面，字符串匹配的放后面。
7. 以后可能设计普通版本的规则条数限制为99条，VIP版本限制为999-99999条。

### 安全原则和配置指导思想：  
什么是威胁(病毒)？  
各个杀毒厂家的标准（和结果）不一样，有时命名都不一样，在国内甚至出现相互视对方为恶意文件的情况。  
笔者的看法和中医类似：是人体内都有病毒，西医也发现：人人体内都有癌细胞。  
所以和威胁/病毒共存是常态，不是危险，否则病毒杀死了，人也完蛋了。  
关键是不能让病毒发作，即使发作，人有能力去抵抗，这都够了。  
所以：  
1. 微软官方的文件都是可信的。  
   尽管它有成千上万个漏洞。  
   有漏洞和漏洞利用是两个概念。  
   发现漏洞和检测漏洞利用是两个功能。  
2. 攻击外部(访问别的进程，注入DLL等)，和容纳外部（加载DLL/shellcode等）都是危险的行为。  
   如有此行为，立即标为恶意的行为（自身和对方）。  
   排除系统行为，除非系统有漏洞利用和加载驱动的行为。  
   权限的提升是危险操作的前奏。  
3. 加载驱动是危险的行为。  
   这个，不必细讲。  
4. 抢占本地的硬件资源，如：CPU，内存，磁盘，网络等。  
   属于危险较低的行为，这是对系统来说的。  
   如：勒索，DDOS，挖矿，炸弹，爆破等。  
   这里，加上用户都有基本的常识和防护，如：加密，权限，配置等。  
5. 再举例：  
   有危险/漏洞的文件是刀（刀不是罪因）  
   有恶意想法，但无权限和能力  
   有恶意的行动且造成危害的（尽管是无意的）。  

---
