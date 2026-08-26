# TAGLINE

获取或设置全局服务看门狗状态

# TLDR

显示当前**看门狗**状态

```systemctl service-watchdogs```

**启用**服务看门狗

```systemctl service-watchdogs yes```

**禁用**服务看门狗

```systemctl service-watchdogs no```

# SYNOPSIS

**systemctl service-watchdogs** [_BOOL_]

# PARAMETERS

**yes**
> 全局启用服务看门狗逻辑。

**no**
> 全局禁用服务看门狗逻辑。

# DESCRIPTION

**systemctl service-watchdogs** 获取或设置服务运行时看门狗的全局状态。启用后，systemd 会监控配置了 WatchdogSec= 的服务，如果它们未能在超时期限内发送保活通知，就发送 SIGABRT 将其终止。

全局禁用看门狗后，systemd 不再终止并重启无响应的服务，这在调试时很有用。

不带参数调用时会打印当前的全局看门狗状态。

# CAVEATS

禁用看门狗可能让挂起的服务无限期存续。更改是临时的，重启后会恢复原状。用 `yes` 重新启用看门狗并不会恢复对那些在看门狗被禁用期间已触发的服务的监控；这些服务必须重启。

# HISTORY

**service-watchdogs** 子命令为看门狗机制提供了一个全局开关，适用于调试那些否则会在调查完成前就被重启的服务。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-status](/man/systemctl-status)(1), [systemctl-restart](/man/systemctl-restart)(1), [journalctl](/man/journalctl)(1)
