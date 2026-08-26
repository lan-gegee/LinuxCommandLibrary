# TAGLINE

基于守护进程的病毒扫描客户端

# TLDR

**扫描文件或目录**

```clamdscan [/path/to/scan]```

**以详细输出扫描**

```clamdscan -v [/path/to/scan]```

**将受感染的文件移至隔离区**

```clamdscan --move=[/quarantine] [/path/to/scan]```

**删除受感染的文件**

```clamdscan --remove [/path/to/scan]```

**并行扫描（multiscan）**

```clamdscan -m [/path/to/scan]```

**将结果记录到文件**

```clamdscan -l [scan.log] [/path/to/scan]```

**重载病毒数据库**

```clamdscan --reload```

# SYNOPSIS

**clamdscan** [_options_] [_file_|_directory_]...

# DESCRIPTION

**clamdscan** 是 ClamAV 守护进程（clamd）的客户端。它不自己加载病毒特征库，而是将文件路径或数据流发送给 clamd 守护进程进行扫描，因此在重复或批量扫描场景下比 clamscan 快得多。

由于 clamd 将病毒数据库常驻内存，clamdscan 避免了每次调用时加载特征的启动开销。**--multiscan** 选项启用多守护进程线程并行扫描，进一步提高多核系统上的吞吐量。

clamdscan 需要正在运行的 clamd 守护进程，并从守护进程配置继承大部分扫描设置。它通过 Unix 套接字或 TCP 连接与 clamd 通信，支持与 clamscan 相同的隔离操作（移动、复制、删除）。

# PARAMETERS

**-v**, **--verbose**
> 输出详细信息

**-l** _file_, **--log** _file_
> 将扫描报告保存到文件

**-f** _file_, **--file-list** _file_
> 扫描文件中列出的文件

**--remove**
> 删除受感染的文件

**--move** _dir_
> 将受感染的文件移动到指定目录

**--copy** _dir_
> 将受感染的文件复制到指定目录

**-m**, **--multiscan**
> 使用多线程并行扫描

**-i**, **--infected**
> 只打印受感染的文件

**--no-summary**
> 禁用结尾的摘要

**--fdpass**
> 将文件描述符传递给 clamd

**--stream**
> 强制以流方式发送给 clamd

**--reload**
> 请求重载数据库

**--ping** _attempts_
> 持续 ping clamd 直到其响应

**--wait**
> 最长等待 clamd 30 秒

**--config-file** _file_
> 使用指定的 clamd 配置

# CAVEATS

需要正在运行的 clamd 守护进程。大多数 clamscan 选项会被忽略，因为设置来自 clamd.conf。若 clamd 以其他用户身份运行，请使用 --fdpass。

# INSTALL

```apt: sudo apt install clamdscan```

```apk: sudo apk add clamav-clamdscan```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clamscan](/man/clamscan)(1), [clamd](/man/clamd)(8), [freshclam](/man/freshclam)(1)

# RESOURCES

```[Source code](https://github.com/Cisco-Talos/clamav)```

```[Documentation](https://docs.clamav.net/)```

<!-- verified: 2026-06-22 -->
