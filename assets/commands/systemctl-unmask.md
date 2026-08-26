# TAGLINE

重新启用被屏蔽的 systemd 单元

# TLDR

**解除屏蔽**一个服务

```systemctl unmask [service_name]```

解除屏蔽并立即**启动**它

```systemctl unmask --now [service_name]```

**解除用户**单元的屏蔽

```systemctl --user unmask [service_name]```

仅在本次运行内**解除屏蔽**（运行时屏蔽）

```systemctl unmask --runtime [service_name]```

一次性**解除多个单元**的屏蔽

```systemctl unmask [unit1] [unit2] [unit3]```

# SYNOPSIS

**systemctl unmask** [_OPTIONS_] _UNIT_...

# DESCRIPTION

**systemctl unmask** 移除一个或多个 systemd 单元的屏蔽，使其可以再次被启动。屏蔽单元时，其单元文件会被链接到 `/dev/null`，导致该单元完全无法启动（手动或作为依赖都不行）；解除屏蔽会移除该符号链接并恢复原始单元文件。

如果单元之前是在运行时被屏蔽的（使用 `--runtime`），则只能在运行时解除屏蔽。解除屏蔽不会自动启动单元——配合 `--now` 可在解除屏蔽后立即启动。

# PARAMETERS

_UNIT_
> 要解除屏蔽的一个或多个单元名称（如 `nginx.service`、`getty@tty1.service`）。

**--now**
> 解除屏蔽后同时启动这些单元。

**--user**
> 操作调用用户的单元而不是系统单元。

**--system**
> 操作系统单元（默认）。

**--global**
> 对所有用户解除屏蔽（在 `/etc/systemd/user/` 中启用）。

**--runtime**
> 更改仅对本次启动生效；重启后重置。

**--no-block**
> 不等待（配合 `--now` 使用的）启动任务完成即返回。

**-q**, **--quiet**
> 抑制提示性消息。

# CAVEATS

除非指定 `--now`，否则解除屏蔽不会启动单元。如果单元是在运行时被屏蔽的，只能用 `--runtime` 解除屏蔽；持久屏蔽则需要不带 `--runtime` 来解除。解除屏蔽后，可能需要执行 `systemctl daemon-reload` 才能让管理器识别恢复的单元文件。通过 drop-in 文件（而非符号链接）屏蔽的单元，必须通过编辑或删除那些文件来解除屏蔽。

# HISTORY

**systemctl unmask** 是 **systemd** 的一部分，由 **Lennart Poettering** 等人开发。mask/unmask 语义的引入取代了 SysV init 脚本时代旧的 `/dev/null` 符号链接技巧。

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-mask](/man/systemctl-mask)(1), [systemctl-enable](/man/systemctl-enable)(1), [systemctl-disable](/man/systemctl-disable)(1)
