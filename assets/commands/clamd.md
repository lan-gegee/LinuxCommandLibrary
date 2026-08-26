# TAGLINE

多线程杀毒扫描守护进程

# TLDR

**启动 clamd** 守护进程

```clamd```

**在前台启动**

```clamd --foreground```

**使用指定配置文件启动**

```clamd -c [/etc/clamav/clamd.conf]```

**检查配置**后退出

```clamd --config-check```

**不重启而重载病毒数据库**

```clamdscan --reload```

# SYNOPSIS

**clamd** [_options_]

# DESCRIPTION

**clamd** 是 ClamAV 守护进程，一个多线程病毒扫描服务。它只将病毒数据库加载到内存一次，然后处理来自客户端的扫描请求，扫描速度远快于独立的 clamscan 工具。

该守护进程监听 Unix 套接字或 TCP 端口，接受扫描文件、目录或数据流的命令。多个客户端可以同时连接，因此适合邮件服务器、文件服务器和 Web 应用。

clamd 通常与邮件传输代理（Postfix、Exim、Sendmail）、Web 代理和文件上传处理程序配合使用，提供实时恶意软件扫描。客户端通过 **clamdscan** 与 clamd 交互，或直接向套接字发送命令。

# PARAMETERS

**-c** _file_, **--config-file=**_file_
> 使用指定的配置文件（默认：/etc/clamav/clamd.conf）。

**-F**, **--foreground**
> 在前台运行，不进行 daemon 化。

**--debug**
> 启用调试消息。

**--config-check**
> 读取配置、检查错误后退出。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# CONFIGURATION

**/etc/clamav/clamd.conf**
> 守护进程配置，包括套接字类型（LocalSocket 或 TCPSocket）、扫描限制（MaxFileSize、MaxScanSize）、线程数（MaxThreads）和日志选项（LogFile、LogSyslog）。

# CAVEATS

需要通过 **freshclam** 定期更新病毒数据库。内存占用取决于数据库大小（通常需要 1-2 GB 内存）。套接字权限必须允许客户端访问。必须删除或注释掉 clamd.conf 中的 **Example** 指令，守护进程才能启动。性能取决于可用内存和 CPU 核心数。

# HISTORY

**ClamAV** 由 **Tomasz Kojm** 于 **2001** 年创建，是一个开源杀毒引擎，最初设计用于 Unix 系统上的邮件网关扫描。它在 **2007** 年被 **Sourcefire** 收购；Sourcefire 在 **2013** 年被收购后又成为 **Cisco** 的一部分。ClamAV 仍然是部署最广泛的开源杀毒解决方案之一，尤其在邮件和 Web 网关环境中。

# INSTALL

```apt: sudo apt install clamav-daemon```

```dnf: sudo dnf install clamd```

```apk: sudo apk add clamav-daemon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clamscan](/man/clamscan)(1), [clamdscan](/man/clamdscan)(1), [freshclam](/man/freshclam)(1)
