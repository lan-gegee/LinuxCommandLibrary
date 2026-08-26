# TAGLINE

控制 runit 监管的服务

# TLDR

**查看服务状态**

```sv status [servicename]```

**启动服务**

```sv up [servicename]```

**停止服务**

```sv down [servicename]```

**重启服务**

```sv restart [servicename]```

**发送 HUP 信号**以重新加载配置

```sv hup [servicename]```

**只运行一次服务**（停止后不再重启）

```sv once [servicename]```

带超时地**强制停止**

```sv force-stop [servicename]```

以详细输出**检查状态**

```sv -v status [servicename]```

# SYNOPSIS

**sv** [**-v**] [**-w** _sec_] _command_ _services_...

# PARAMETERS

**-v**
> 最多等待 7 秒使命令生效，并报告状态

**-w** _sec_
> 将超时设为 sec 秒（隐含 -v）

# COMMANDS

**status**
> 报告服务及其日志服务的当前状态

**up**
> 启动服务；若它停止则重新启动

**down**
> 用 TERM 和 CONT 信号停止服务；不再重启

**once**
> 启动服务一次；停止后不重启

**restart**
> 重启服务（兼容 LSB，等待完成）

**start**
> 启动服务（兼容 LSB）

**stop**
> 停止服务（兼容 LSB）

**reload**
> 发送 HUP 信号（兼容 LSB）

**hup**, **cont**, **pause**, **term**, **kill**
> 发送相应信号（HUP、CONT、STOP、TERM、KILL）

**1**, **2**
> 发送 USR1 或 USR2 信号

**alarm**, **interrupt**, **quit**
> 发送 ALRM、INT 或 QUIT 信号

**exit**
> 停止服务且不再重启；退出 runsv

**check**
> 验证服务是否处于请求的状态；若存在 ./check 脚本则执行之

**force-stop**, **force-restart**, **force-reload**, **force-shutdown**
> stop/restart/reload/shutdown 的强制版本

# DESCRIPTION

**sv** 用于控制和管理 runit init 系统中由 **runsv** 监管的服务。它向服务目录发送命令并报告其状态。服务通常位于 **/service/** 或自定义的服务目录中。

每个服务是一个目录，其中包含供 runsv 执行和监管的 **run** 脚本。当服务意外停止时，runsv 会自动将其重启。**down** 命令会阻止自动重启，而 **once** 则在不监管重启的情况下运行服务。

**sv** 命令可以符号链接到 **/etc/init.d/** 以提供 LSB init 脚本兼容性。以这种方式调用时，服务名取自脚本的基名。

状态输出显示服务的状态（run、down、finish）、PID 和运行时长。若存在 **log/** 子目录，还会显示日志服务的状态。

# CAVEATS

退出码含义各异：0 表示成功，1 表示超时，100 表示出错。作为 init 脚本使用时，退出码 3 表示服务已停止，4 表示状态未知。**down** 等命令默认发送信号但不等待；需要等待请使用 **-v**。

# HISTORY

**sv** 是 **runit** 的组成部分。runit 由 **Gerrit Pape** 于 **2004 年**前后创建，是一套带服务监管的 Unix init 方案。Runit 被设计为 sysvinit 的替代品，是 **Void Linux** 的默认 init 系统，在许多其他发行版上也可作为 systemd 的替代方案使用。

# INSTALL

```apt: sudo apt install runit```

```apk: sudo apk add runit```

```brew: brew install runit```

```nix: nix profile install nixpkgs#runit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[runsv](/man/runsv)(8), [runsvdir](/man/runsvdir)(8), [svlogd](/man/svlogd)(8), [chpst](/man/chpst)(8), [systemctl](/man/systemctl)(1)
