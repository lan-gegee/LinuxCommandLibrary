# TAGLINE

PolicyKit 授权守护进程

# TLDR

**启动 PolicyKit 守护进程**

```polkitd```

**以调试输出运行**

```polkitd --debug```

**指定配置目录**

```polkitd --config-dir=[/etc/polkit-1]```

# SYNOPSIS

**polkitd** [_options_]

# PARAMETERS

**--debug**
> 启用调试输出。

**--config-dir** _DIR_
> 配置目录。

**--no-debug**
> 禁用调试输出。

# DESCRIPTION

**polkitd** 是 PolicyKit 授权守护进程，负责处理来自应用程序的授权请求。它评估以 JavaScript 或 .pkla 文件定义的策略规则，判断用户或进程是否有权执行特定操作。

该守护进程通常由 D-Bus 或 systemd 在需要授权检查时自动启动。**--debug** 标志启用详细日志输出，便于排查策略问题。

# CAVEATS

通常由 systemd 启动。属于系统服务。

# HISTORY

polkitd 是 **PolicyKit** 授权框架的守护进程组件。

# SEE ALSO

[polkit](/man/polkit)(8), [pkexec](/man/pkexec)(1), [systemctl](/man/systemctl)(1)
