# TAGLINE

禁用 unit 开机自启

# TLDR

**禁用**服务开机运行

```systemctl disable [unit]```

禁用服务开机运行并**立即停止**它

```systemctl disable --now [unit]```

禁用**用户级**服务在登录时运行

```systemctl --user disable [unit]```

一次禁用**多个** unit

```systemctl disable [unit1] [unit2]```

**临时**禁用 unit，直到下次重启

```systemctl disable --runtime [unit]```

# SYNOPSIS

**systemctl** [_OPTIONS_...] **disable** _UNIT_...

# PARAMETERS

**--now**
> 禁用后同时停止该 unit

**--user**
> 禁用用户服务管理器的 unit 而非系统 unit

**--no-reload**
> 禁用后不重新加载 systemd 配置

**--runtime**
> 仅临时禁用，直到下次重启。

**--force**
> 禁用时即使 unit 文件不存在也移除符号链接。

**--global**
> 对所有用户禁用（用于 --user 模式的 unit）。

# DESCRIPTION

**systemctl disable** 移除使 unit 在启动或登录时自动启动的符号链接。这会阻止该 unit 今后自动启动，但不会停止当前正在运行的实例，除非使用 **--now**。

该命令通过移除 target.wants 目录中的符号链接来逆转 **systemctl enable** 的效果。unit 文件本身不会被修改或删除。

# CAVEATS

系统 unit 需要 root 权限。禁用不会停止正在运行的 unit；请使用 **--now** 或 **systemctl stop**。某些 unit 由其他机制启动（socket 激活、路径触发），可能需要额外步骤才能完全禁用。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-enable](/man/systemctl-enable)(1), [systemctl-stop](/man/systemctl-stop)(1), [systemctl-mask](/man/systemctl-mask)(1), [systemctl-is-enabled](/man/systemctl-is-enabled)(1)
