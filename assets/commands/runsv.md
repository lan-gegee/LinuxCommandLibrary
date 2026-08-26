# TAGLINE

监督单个 runit 服务进程

# TLDR

**监督一个服务**

```runsv [/etc/service/myservice]```

**检查服务状态**

```sv status [myservice]```

**发送信号**

```sv signal [myservice]```

# SYNOPSIS

**runsv** _servicedir_

# DESCRIPTION

**runsv** 监督单个服务。它会运行并监视目录中定义的服务。

run 脚本会被执行并被监视。如果它退出，runsv 会重新启动它。

可选的 finish 脚本在服务退出后运行。清理操作放在这里。

可选的 log 目录用于运行日志服务。捕获 stdout/stderr。

控制接口位于 supervise 目录。sv 命令通过它进行通信。

# SERVICE DIRECTORY

**run** - 可执行的服务脚本（必需）
**finish** - 清理脚本（可选）
**log/run** - 日志服务（可选）
**supervise/** - 由 runsv 创建，用于控制

# CONTROL COMMANDS

写入 _service_/supervise/control（通常通过 **sv**）：

**u** - Up：启动服务，停止时自动重启
**d** - Down：发送 TERM+CONT 且不再重启
**o** - Once：启动一次，退出后不重启
**p** - Pause：暂停（SIGSTOP）
**c** - Continue：继续（SIGCONT）
**h** - Hangup：挂断（SIGHUP）
**a** - Alarm：报警（SIGALRM）
**i** - Interrupt：中断（SIGINT）
**q** - Quit：退出（SIGQUIT）
**1** - SIGUSR1
**2** - SIGUSR2
**t** - Terminate：终止（SIGTERM）
**k** - Kill：强制杀死（SIGKILL）
**x** - 退出 runsv 并关闭日志管道

# CAVEATS

通常由 **runsvdir** 运行，而非直接调用。服务目录必须具有正确的权限和一个可执行的 **run** 脚本。服务目录中的 **down** 文件会阻止自动启动。启动出错或已有另一个 runsv 在监督同一目录时，会以状态码 111 退出。

# HISTORY

**runsv** 是 **Gerrit Pape** 所著 **runit** 套件的一部分。它为单个服务提供核心监督功能。

# INSTALL

```apt: sudo apt install runit```

```apk: sudo apk add runit```

```brew: brew install runit```

```nix: nix profile install nixpkgs#runit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[runit](/man/runit)(8), [sv](/man/sv)(8), [runsvdir](/man/runsvdir)(8), [svlogd](/man/svlogd)(8), [chpst](/man/chpst)(8)
