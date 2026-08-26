# TAGLINE

启动并监视 runit 服务目录

# TLDR

在目录中**开始监督服务**

```runsvdir [/etc/service]```

让每个服务**在新会话中运行**并拥有独立进程组

```runsvdir -P [/etc/service]```

**附带日志命令启动**以记录错误输出

```runsvdir [/etc/service] "log: ........................................."```

# SYNOPSIS

**runsvdir** [**-P**] _dir_ [_log_]

# PARAMETERS

**-P**
> 使用 setsid 让每个 runsv 进程在新会话和独立进程组中运行。

_dir_
> 要监视的服务目录。每个子目录（或指向目录的符号链接）都会通过 runsv 作为受监督的服务启动。

_log_
> 可选的日志命令。如果指定（至少七个字符），runsvdir 会把自身的错误输出通过该命令管道处理，类似于 daemontools 的 readproctitle。

# DESCRIPTION

**runsvdir** 启动并监视一组 **runsv**(8) 进程。它至少每五秒扫描一次 _dir_。当出现新的子目录或指向目录的符号链接时，runsvdir 会为其启动一个新的 runsv 进程。当某个子目录被移除时，相应的 runsv 进程会收到 TERM 信号。

名称以点开头的子目录会被忽略。服务的最大数量为 1000。

向 runsvdir 发送 TERM 信号会使它以状态码 0 退出。发送 HUP 信号会使它向所有正在运行的 runsv 进程发送 TERM 信号，然后以状态码 111 退出。

# SERVICE MANAGEMENT

- 在目录中创建符号链接：服务会在下次扫描时自动启动
- 移除符号链接：服务通过 TERM 信号停止
- 使用 **sv** 命令控制单个服务

# CAVEATS

通常由 runit init 在系统启动时拉起。runsvdir 运行期间不应卸载相关文件系统。服务目录的权限必须正确，runsv 才能启动。

# HISTORY

**runsvdir** 是 **runit** 中的服务目录监督器，由 Gerrit Pape 创建。它负责监视服务目录并为每个服务管理 runsv 进程。

# INSTALL

```apt: sudo apt install runit```

```apk: sudo apk add runit```

```brew: brew install runit```

```nix: nix profile install nixpkgs#runit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[runit](/man/runit)(8), [runsv](/man/runsv)(8), [sv](/man/sv)(8), [runsvchdir](/man/runsvchdir)(8), [chpst](/man/chpst)(8), [svlogd](/man/svlogd)(8)
