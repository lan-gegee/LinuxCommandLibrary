# TAGLINE

进入默认系统 target

# TLDR

进入**默认**模式

```systemctl default```

**异步**进入默认模式

```systemctl default --no-block```

# SYNOPSIS

**systemctl default** [_OPTIONS_]

# PARAMETERS

**--no-block**
> 立即返回，不等待操作完成

# DESCRIPTION

**systemctl default** 将系统切换到默认 target，通常是 `graphical.target` 或 `multi-user.target`（取决于系统配置）。它等价于 `systemctl isolate default.target`。

该命令适合在救援或紧急模式之后将系统恢复到正常运行状态。

# CAVEATS

默认 target 由 `/etc/systemd/system/default.target` 处的符号链接决定。切换 target 可能会停止新 target 不需要的服务。

# HISTORY

**default** 子命令提供了一种便捷方式来返回正常系统操作，无需了解具体的默认 target 名称。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-rescue](/man/systemctl-rescue)(1), [systemctl-emergency](/man/systemctl-emergency)(1), [systemctl-get-default](/man/systemctl-get-default)(1)
