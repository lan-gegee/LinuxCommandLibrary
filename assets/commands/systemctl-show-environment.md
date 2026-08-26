# TAGLINE

显示服务管理器的环境

# TLDR

显示**系统**服务管理器的环境

```systemctl show-environment```

显示**用户**服务管理器的环境

```systemctl show-environment --user```

**过滤**特定变量

```systemctl show-environment | grep [PATH]```

# SYNOPSIS

**systemctl show-environment** [_OPTIONS_]

# PARAMETERS

**--user**
> 显示用户服务管理器的环境

**--system**
> 显示系统管理器的环境（默认）

# DESCRIPTION

**systemctl show-environment** 显示 systemd 服务管理器环境块中设置的所有环境变量。这些变量会被管理器启动的所有服务继承。

输出每行一个变量，格式为 NAME=VALUE。使用 **systemctl set-environment** 添加变量，使用 **systemctl unset-environment** 移除变量。

# CAVEATS

显示的是管理器的环境，而不是 Shell 的环境。通过 `set-environment` 或 `import-environment` 设置的变量会出现在这里。

# HISTORY

**show-environment** 子命令展示服务将继承哪些环境变量，便于调试服务配置。

# SEE ALSO

[systemctl-set-environment](/man/systemctl-set-environment)(1), [systemctl-unset-environment](/man/systemctl-unset-environment)(1), [systemctl-import-environment](/man/systemctl-import-environment)(1)
