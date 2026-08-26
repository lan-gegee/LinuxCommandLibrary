# TAGLINE

Salt 中央管理守护进程

# TLDR

在前台**启动 Salt master 守护进程**

```salt-master```

在后台**启动 Salt master**（守护进程化）

```salt-master -d```

**使用指定的配置目录启动**

```salt-master -c [/etc/salt]```

向控制台输出 **debug 日志**启动

```salt-master -l debug```

**使用指定的日志文件启动**

```salt-master --log-file=[/var/log/salt/master]```

# SYNOPSIS

**salt-master** [_options_]

# PARAMETERS

**-d**, **--daemon**
> 以守护进程方式在后台运行 Salt master

**-c** _DIR_, **--config-dir**=_DIR_
> 指定配置目录（默认：/etc/salt）

**-l** _LEVEL_, **--log-level**=_LEVEL_
> 控制台日志级别：info、warning、error、debug、trace、garbage、none

**--log-file**=_FILE_
> 指定日志文件路径

**--log-file-level**=_LEVEL_
> 日志文件的记录级别

**--pidfile**=_FILE_
> 指定 pidfile 的位置

**-u** _USER_, **--user**=_USER_
> 指定运行 salt-master 的用户

**-h**, **--help**
> 打印帮助信息并退出

**--version**
> 打印版本信息

# DESCRIPTION

**salt-master** 是 SaltStack 基础设施的中央控制守护进程。它管理 minion 密钥、分发配置、执行远程命令，并向已连接的 minion 提供文件服务。

master 监听两个端口：4505 用于通过 ZeroMQ 向 minion 发布命令，4506 用于接收返回结果和文件服务器请求。配置存储在 **/etc/salt/master**。

关键组件包括用于跟踪命令执行的作业缓存、用于分发状态和文件的文件服务器，以及用于安全验证 minion 身份的 PKI 基础设施。master 支持工作线程以处理大量 minion。

# CONFIGURATION

**/etc/salt/master**
> master 主配置文件，控制工作线程数、文件服务器根目录、pillar 数据和网络设置。

**/etc/salt/master.d/**
> 存放额外配置文件的目录，这些文件会与主 master 配置合并。

**/srv/salt/**
> 文件服务器的默认根目录，存放提供给 minion 的 Salt 状态、公式和文件。

**/srv/pillar/**
> pillar 数据的默认目录，提供安全的按 minion 配置变量。

# CAVEATS

防火墙规则必须放行端口 4505 和 4506 以支持 master-minion 通信。大型部署可能需要调整配置中的 worker_threads。必须先运行 master，minion 才能连接并让其密钥被接受。

# HISTORY

salt-master 属于 **SaltStack**，由 Thomas Hatch 于 **2011 年**创建。SaltStack 最初在一家初创公司中开发，后来成长为主要的配置管理平台。VMware 于 **2020 年**收购了 SaltStack，该项目如今以开源的 Salt Project 形式继续发展。

# INSTALL

```dnf: sudo dnf install salt-master```

```apk: sudo apk add salt-lts-master```

```zypper: sudo zypper install salt-master```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[salt](/man/salt)(1), [salt-minion](/man/salt-minion)(8), [salt-key](/man/salt-key)(1), [salt-call](/man/salt-call)(1)
