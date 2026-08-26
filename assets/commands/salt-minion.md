# TAGLINE

Salt 受管节点代理守护进程

# TLDR

在前台**启动 Salt minion 守护进程**

```salt-minion```

在后台**启动 Salt minion**（守护进程化）

```salt-minion -d```

**使用指定的配置目录启动**

```salt-minion -c [/etc/salt]```

向控制台输出 **debug 日志**启动

```salt-minion -l debug```

**不使用 keepalive 重启包装器启动**

```salt-minion --disable-keepalive```

# SYNOPSIS

**salt-minion** [_options_]

# PARAMETERS

**-d**, **--daemon**
> 以守护进程方式在后台运行 Salt minion

**-c** _DIR_, **--config-dir**=_DIR_
> 指定配置目录（默认：/etc/salt）

**-l** _LEVEL_, **--log-level**=_LEVEL_
> 控制台日志级别：info、warning、error、debug、trace、garbage、quiet（默认：warning）

**--log-file**=_FILE_
> 指定日志文件路径（默认：/var/log/salt/minion）

**--log-file-level**=_LEVEL_
> 日志文件的记录级别

**--pidfile**=_FILE_
> 指定 pidfile 的位置（默认：/var/run/salt-minion.pid）

**-u** _USER_, **--user**=_USER_
> 指定运行 salt-minion 的用户

**--disable-keepalive**
> 禁用自动重启机制；直接运行守护进程

**-h**, **--help**
> 打印帮助信息并退出

**--version**
> 打印版本信息

# DESCRIPTION

**salt-minion** 是在 SaltStack 基础设施的受管系统上运行的代理守护进程。它连接到 Salt master，接收命令，在本地执行并返回结果。

启动时，minion 会生成密钥对并将公钥发送给 master 以待接受。密钥被接受后，minion 订阅 master 的 ZeroMQ 发布套接字来接收命令。配置存储在 **/etc/salt/minion** 或 **/etc/salt/minion.d/** 目录中。

minion 也可以通过 **salt-call --local** 以无 master 模式运行，在没有 master 的情况下进行本地配置管理。设置 **master_type: disable** 可以在没有 master 连接的情况下运行 beacons 和 engines。

# CONFIGURATION

**/etc/salt/minion**
> minion 主配置文件，定义 master 地址、minion ID、grains 和模块设置。

**/etc/salt/minion.d/**
> 存放额外配置文件的目录，这些文件与主配置合并，按字母顺序应用。

**/var/log/salt/minion**
> minion 日志文件的默认位置。

# CAVEATS

minion 密钥必须先在 master 上被接受，才能执行命令。默认情况下，该守护进程带有自动重启包装器运行；由 systemd 或容器运行时管理时请使用 **--disable-keepalive**。minion.d/ 中的配置按字母顺序应用，重复的设置可能产生意外的覆盖。

# HISTORY

salt-minion 属于 **SaltStack**，由 Thomas Hatch 于 **2011 年**创建。minion 代理让 Salt 能够在整个基础设施范围内实现大规模的远程执行和配置管理。

# INSTALL

```dnf: sudo dnf install salt-minion```

```apk: sudo apk add salt-lts-minion```

```zypper: sudo zypper install salt-minion```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[salt](/man/salt)(1), [salt-master](/man/salt-master)(8), [salt-key](/man/salt-key)(1), [salt-call](/man/salt-call)(1)
