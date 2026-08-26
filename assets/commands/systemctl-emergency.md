# TAGLINE

进入最小化的紧急恢复模式

# TLDR

进入**紧急**模式

```systemctl emergency```

**异步**进入紧急模式

```systemctl emergency --no-block```

# SYNOPSIS

**systemctl emergency** [_OPTIONS_]

# PARAMETERS

**--no-block**
> 立即返回，不等待操作完成

# DESCRIPTION

**systemctl emergency** 将系统切换到紧急模式（`emergency.target`）。紧急模式以只读方式挂载根文件系统，只启动系统恢复所需的必要服务。它为修复损坏的系统提供一个最小化环境。

紧急模式比救援模式更精简，通常在救援模式无法正常启动时使用。

# CAVEATS

需要 root 权限。大多数服务会被停止。网络将不可用。根文件系统默认以只读方式挂载；如需修复，可用 `mount -o remount,rw /` 重新挂载为可写。

# HISTORY

**emergency** 子命令提供了一种标准化的方式来进入最精简的恢复模式，取代了传统的 init=/bin/sh 引导参数。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-rescue](/man/systemctl-rescue)(1), [systemctl-default](/man/systemctl-default)(1)
