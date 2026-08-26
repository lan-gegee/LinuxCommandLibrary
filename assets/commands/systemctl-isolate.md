# TAGLINE

切换到指定的 target

# TLDR

切换到某个 **target**

```systemctl isolate [target]```

切换到**图形界面** target

```systemctl isolate graphical.target```

切换到**救援**模式

```systemctl isolate rescue.target```

切换到**紧急**模式

```systemctl isolate emergency.target```

# SYNOPSIS

**systemctl isolate** _UNIT_

# DESCRIPTION

**systemctl isolate** 启动指定单元及其依赖，同时停止该单元不需要的所有其他单元。这类似于在 SysV init 系统中更改运行级别。

带有 `IgnoreOnIsolate=yes` 的单元在隔离期间不会被停止。如果不提供后缀，则默认为 `.target` 后缀。

# COMMON TARGETS

**graphical.target** — 完整的图形界面环境（对应 SysV 运行级别 5）。

**multi-user.target** — 文本模式多用户环境（运行级别 3）。

**rescue.target** — 单用户救援模式（运行级别 1），大多数文件系统已挂载。

**emergency.target** — 最小化的紧急 Shell，仅以只读方式挂载根文件系统。

**reboot.target**、**poweroff.target**、**halt.target** — 过渡性 target，用于让系统干净地进入相应的最终状态。

# CAVEATS

只有设置了 **AllowIsolate=yes** 的单元才能被隔离切换到。这是一种具有破坏性的操作，会停止新 target 不需要的所有正在运行的单元（声明了 **IgnoreOnIsolate=yes** 的除外）。需要 root 权限。若要将某个 target 设为开机默认，请改用 **systemctl set-default**。

# HISTORY

**isolate** 子命令在 systemd 中提供了类似运行级别的行为，允许在不同系统状态之间切换，同时保持与基于 target 的启动模型的兼容性。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-default](/man/systemctl-default)(1), [systemctl-rescue](/man/systemctl-rescue)(1)
