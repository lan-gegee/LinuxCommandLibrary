# TAGLINE

完全阻止单元启动

# TLDR

**屏蔽**一个服务（防止它被启动）

```systemctl mask [service_name]```

屏蔽一个服务，若正在运行则同时**停止**它

```systemctl mask [service_name] --now```

屏蔽一个**用户**服务

```systemctl mask [service_name] --user```

# SYNOPSIS

**systemctl** [_OPTIONS_...] **mask** _UNIT_...

# PARAMETERS

**--now**
> 屏蔽之后同时停止该单元

**--user**
> 屏蔽用户服务管理器的单元而不是系统单元

**--runtime**
> 仅临时屏蔽，到下次重启为止

# DESCRIPTION

**systemctl mask** 将单元链接到 /dev/null，完全阻止它以任何方式被启动。这比 **disable** 更强，后者只是阻止自动启动。被屏蔽的单元无法手动启动、无法被依赖拉起，也无法被任何触发器激活。

屏蔽适用于与你现有配置冲突的单元，或者你想确保永远不会运行的单元。使用 **systemctl unmask** 可以撤销该操作。

# CAVEATS

对系统单元操作需要 root 权限。被屏蔽的单元在解除屏蔽之前完全无法启动。请谨慎使用；屏蔽关键单元可能破坏系统功能。屏蔽前应先检查依赖关系，避免影响其他服务。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-unmask](/man/systemctl-unmask)(1), [systemctl-disable](/man/systemctl-disable)(1)
