# TAGLINE

切换 runit 服务目录

# TLDR

**切换服务目录**

```runsvchdir [multi-user]```

**切换到救援模式**

```runsvchdir [single]```

**查看当前运行级别**

```cat /etc/runit/runsvdir/current```

# SYNOPSIS

**runsvchdir** _name_

# DESCRIPTION

**runsvchdir** 切换 runsvdir 所监督的服务目录。它会更改系统的有效运行级别。

运行级别是 /etc/runit/runsvdir/ 下的目录。每个目录都包含指向服务的符号链接。

切换是平滑进行的。不在新级别中的服务会被停止，新的服务被启动。

常见的级别包括 default、single 和 multi-user。也可以创建自定义级别。

current 符号链接指向活动的级别。/etc/runit/runsvdir/current 即指向当前激活者。

# RUNLEVELS

**default** - 正常的多用户模式
**single** - 单用户/救援模式
**multi-user** - 网络服务
**custom** - 用户自定义

# CAVEATS

需要 root 权限。目标级别中必须存在相应服务。切换可能因停止服务而耗时。

# HISTORY

**runsvchdir** 是 **runit** 的一部分，提供类似运行级别的切换功能。它可以动态重新配置要监督哪些服务。

# INSTALL

```apt: sudo apt install runit```

```apk: sudo apk add runit```

```brew: brew install runit```

```nix: nix profile install nixpkgs#runit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[runsvdir](/man/runsvdir)(8), [runit](/man/runit)(8), [sv](/man/sv)(8)
