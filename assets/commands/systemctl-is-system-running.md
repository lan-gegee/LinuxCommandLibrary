# TAGLINE

检查系统整体运行状态

# TLDR

检查**系统状态**

```systemctl is-system-running```

**安静**模式（仅返回退出码）

```systemctl is-system-running -q```

**等待**启动完成

```systemctl is-system-running --wait```

# SYNOPSIS

**systemctl is-system-running** [_OPTIONS_]

# PARAMETERS

**-q, --quiet**
> 不输出内容，仅返回退出码

**--wait**
> 等待启动过程完成后才返回

# DESCRIPTION

**systemctl is-system-running** 检查系统的整体运行状态。它会报告系统是否已完成启动，以及所有单元是否运行正常。

可能的状态：initializing、starting、running、degraded、maintenance、stopping、offline、unknown。"running" 表示启动成功且所有单元健康。

# SYSTEM STATES

**initializing** — 启动早期，尚未到达 basic.target。

**starting** — 启动后期，尚未等所有服务完成。

**running** — 系统完全正常运行，所有单元健康。

**degraded** — 系统正在运行，但至少有一个单元失败。

**maintenance** — 救援/紧急模式。

**stopping** — 正在关机。

**offline** — 系统未在 systemd 下启动（如 chroot 环境）。

**unknown** — 无法确定状态。

# EXIT STATUS

只有当系统状态为 `running` 时才返回 **0**。其他任何状态都返回非零值，因此 `systemctl is-system-running -q` 是脚本中便捷的健康检查原语。

# CAVEATS

`--wait` 选项适用于需要等系统完全启动后再继续的脚本。"degraded"（降级）状态表示至少有一个单元失败。

# HISTORY

**is-system-running** 子命令为整个系统提供高级健康检查，可用于自动化监控和检测启动是否完成。

# SEE ALSO

[systemctl-status](/man/systemctl-status)(1), [systemctl](/man/systemctl)(1)
