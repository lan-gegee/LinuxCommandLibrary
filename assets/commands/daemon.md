# TAGLINE

将进程转换为 Unix 守护进程

# TLDR

以守护进程方式**运行命令**

```daemon --name="[name]" [command]```

崩溃后**自动重启**运行

```daemon --name="[name]" -r [command]```

以**有限次数和延迟**重启

```daemon --name="[name]" -r --attempts=2 --delay=10 [command]```

以**错误日志记录**方式运行守护进程

```daemon --name="[name]" --errlog=[path/to/file.log] [command]```

**停止**守护进程

```daemon --name="[name]" --stop```

**列出**所有守护进程

```daemon --list```

# SYNOPSIS

**daemon** [_options_] [_--_] _command_ [_args_]

# DESCRIPTION

**daemon** 将其他进程转换为规范的 Unix 守护进程。它处理标准的守护化任务：fork、创建新会话、更改目录、关闭文件描述符，并可选地在退出时重新拉起进程。

适用于在不修改程序本身的情况下，将脚本或程序作为后台服务运行。

# PARAMETERS

**-n**, **--name**=_name_
> 保证只有一个具名的实例；同时启用 --running、--restart、--stop 和 --signal

**-r**, **--respawn**
> 客户端终止时重新拉起

**-A**, **--attempts**=_#_
> 出错时先尝试重新拉起 # 次，再进入延迟等待（默认 5）

**-L**, **--delay**=_seconds_
> 每轮重新拉起尝试之间的延迟时间

**-M**, **--limit**=_#_
> 重新拉起尝试的最大轮数（0 = 无限制）

**-l**, **--errlog**=_spec_
> 将守护进程的错误输出发送到 syslog 或文件

**-o**, **--output**=_spec_
> 将客户端的 stdout 和 stderr 发送到 syslog 或文件

**-E**, **--stderr**=_spec_
> 仅将客户端的 stderr 发送到 syslog 或文件

**-u**, **--user**=_user[:group]_
> 以指定用户身份运行客户端（仅限 root）

**-f**, **--foreground**
> 在前台运行客户端（不守护化）

**--running**
> 检查指定的守护进程是否正在运行

**--restart**
> 重启指定守护进程的客户端

**--stop**
> 终止指定的守护进程

**--list**
> 打印具名守护进程列表

# CAVEATS

与 systemd 服务不同。生产环境服务建议改用 systemd 单元。具名守护进程的 pidfile 默认存放在 /var/run（root）或 /tmp（普通用户）；可用 --pidfiles 覆盖该位置。

# CONFIGURATION

**/etc/daemon.conf**, **/etc/daemon.conf.d/***
> 系统级默认选项，除非提供 --noconfig 否则一律生效。

**~/.daemonrc**, **~/.daemonrc.d/***
> 每用户默认选项，在系统配置之后读取。

# INSTALL

```apt: sudo apt install daemon```

```brew: brew install daemon```

```nix: nix profile install nixpkgs#daemon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[daemonize](/man/daemonize)(1), [nohup](/man/nohup)(1), [systemctl](/man/systemctl)(1)

# RESOURCES

```[Source code](https://github.com/raforg/daemon)```

```[Homepage](https://libslack.org/daemon)```

<!-- verified: 2026-07-11 -->
