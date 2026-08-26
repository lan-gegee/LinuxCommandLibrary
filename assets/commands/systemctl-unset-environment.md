# TAGLINE

移除服务管理器的环境变量

# TLDR

**移除**环境变量

```systemctl unset-environment [VAR]```

移除**多个**变量

```systemctl unset-environment [VAR1 VAR2 ...]```

在**用户**管理器中移除

```systemctl unset-environment [VAR] --user```

# SYNOPSIS

**systemctl unset-environment** _VARIABLE_...

# PARAMETERS

**--user**
> 从用户服务管理器的环境中移除

**--system**
> 从系统管理器的环境中移除（默认）

# DESCRIPTION

**systemctl unset-environment** 从 systemd 服务管理器的环境中移除环境变量。这会撤销 `systemctl set-environment` 的效果。

在移除之后启动的服务将不再收到这些变量。

# CAVEATS

只影响更改之后启动的服务。已在运行的服务保留其环境。更改是临时的，重启后会丢失。

# HISTORY

**unset-environment** 子命令与 `set-environment` 互为补充，提供对服务管理器环境的完整运行时控制。

# SEE ALSO

[systemctl-set-environment](/man/systemctl-set-environment)(1), [systemctl-show-environment](/man/systemctl-show-environment)(1), [systemctl](/man/systemctl)(1)
