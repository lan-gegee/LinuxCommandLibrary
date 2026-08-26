# TAGLINE

汇总系统进程记账数据

# TLDR

显示每个用户的**可执行文件调用情况**

```sudo sa```

显示带**用户名**的调用情况

```sudo sa --print-users```

**按用户列出资源使用情况**

```sudo sa --user-summary```

# SYNOPSIS

**sa** [_options_] [_file_]

# PARAMETERS

**--print-users**
> 显示相关的用户名

**--user-summary**
> 显示按用户汇总的资源使用情况

# DESCRIPTION

**sa** 汇总用户执行命令的记账信息。它从进程记账数据中报告消耗的 CPU 时间、I/O 操作次数及其他资源使用情况。

该命令属于 acct 软件包，需要启用进程记账才能收集数据。

# CAVEATS

需要先启用进程记账（accton）。历史数据依赖于记账文件的轮转。

# HISTORY

属于 **acct**（进程记账）软件包的一部分，提供全系统的命令使用统计。

# INSTALL

```apt: sudo apt install acct```

```apk: sudo apk add acct```

```zypper: sudo zypper install acct```

```nix: nix profile install nixpkgs#acct```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lastcomm](/man/lastcomm)(1), [accton](/man/accton)(8), [ac](/man/ac)(1)
