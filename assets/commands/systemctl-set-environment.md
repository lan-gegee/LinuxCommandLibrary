# TAGLINE

设置服务管理器的环境变量

# TLDR

**设置**环境变量

```systemctl set-environment [VAR=value]```

设置**多个**变量

```systemctl set-environment [VAR1=val1 VAR2=val2 ...]```

为**用户**管理器设置

```systemctl set-environment [VAR=value] --user```

# SYNOPSIS

**systemctl set-environment** _VARIABLE=VALUE_...

# PARAMETERS

**--user**
> 设置到用户服务管理器的环境中

**--system**
> 设置到系统管理器的环境中（默认）

# DESCRIPTION

**systemctl set-environment** 在 systemd 服务管理器的环境中添加或更新环境变量。这些变量会被传递给更改之后启动的所有服务。

这适用于在不修改单元文件的情况下向服务注入配置。

# CAVEATS

只影响更改之后启动的服务。更改是临时的，重启后会丢失。已经在运行的服务不受影响。要从 Shell 导入环境变量，请使用 `import-environment`。

# HISTORY

**set-environment** 子命令支持为服务动态配置环境，与单元文件中的 Environment= 指令互为补充。

# SEE ALSO

[systemctl-show-environment](/man/systemctl-show-environment)(1), [systemctl-unset-environment](/man/systemctl-unset-environment)(1), [systemctl-import-environment](/man/systemctl-import-environment)(1)
