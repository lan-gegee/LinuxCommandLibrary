# TAGLINE

以不同的组 ID 执行命令

# TLDR

以其他组**启动 Shell**

```sg [group]```

以其他组**执行特定命令**

```sg [group] -c "[command]"```

以 www-data **组运行命令**

```sg www-data -c "touch [/var/www/html/file.txt]"```

以其他组**启动登录 Shell**，并重新初始化环境

```sg - [group]```

# SYNOPSIS

**sg** [**-**] [_group_] [[**-c**] _command_]

# PARAMETERS

_group_
> 要切换到的组名。用户必须属于该组（或知道该组的密码）。

**-c** _command_
> 以新的组 ID 执行指定命令，而不是启动交互式 Shell。

**-**
> 将 Shell 作为登录 Shell 启动，重新初始化环境。

# DESCRIPTION

**sg** 以不同的组 ID 执行命令或启动 Shell。它在功能上与 **newgrp** 类似，但允许只运行单条命令而不必启动新的 Shell 会话。

不带命令调用时，**sg** 会以指定组作为有效组 ID 启动新 Shell。带 **-c** 调用时，它以新组执行给定命令后返回。

用户必须是目标组的成员，或者该组设置了密码（通过 **gpasswd**）且用户提供该密码。root 用户可以不受限制地切换到任何组。

# CAVEATS

**sg** 命令是 shadow-utils 软件包的一部分。如果用户不属于指定的组且未设置组密码，访问将被拒绝。环境变量可能会因 Shell 的调用方式而被重置。在某些系统上，**sg** 这个名称可能与 ast-grep 工具的别名冲突；如有需要请使用完整路径 /usr/bin/sg。

# INSTALL

```apt: sudo apt install login```

```apk: sudo apk add shadow-login```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[newgrp](/man/newgrp)(1), [groups](/man/groups)(1), [id](/man/id)(1), [gpasswd](/man/gpasswd)(1), [su](/man/su)(1), [chgrp](/man/chgrp)(1)
