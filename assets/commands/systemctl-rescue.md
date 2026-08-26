# TAGLINE

进入单用户救援模式

# TLDR

将系统切换到**救援** target（类似单用户模式）

```systemctl rescue```

请求救援模式时**不等待**完成

```systemctl --no-block rescue```

# SYNOPSIS

**systemctl rescue** [_OPTIONS_]

# PARAMETERS

**--no-block**
> 立即返回而不等待

# DESCRIPTION

**systemctl rescue** 将系统切换到救援模式（`rescue.target`），这是一个用于系统维护的单用户环境。大多数服务会被停止，但比紧急模式下可用的功能更多。

救援模式提供一个带有基本系统服务的 Shell，网络可能可用，所有文件系统通常以读写方式挂载。

# CAVEATS

需要 root 权限。大多数用户服务和网络服务会被停止。请将救援模式用于文件系统修复或软件包恢复等系统维护任务。

# HISTORY

**rescue** 子命令提供 systemd 版本的传统单用户模式（运行级别 1），提供一个精简但可用的恢复环境。

# SEE ALSO

[systemctl-emergency](/man/systemctl-emergency)(1), [systemctl-default](/man/systemctl-default)(1), [systemctl](/man/systemctl)(1)
