# TAGLINE

启用 unit 开机自启

# TLDR

启用 unit 使其**开机自启**

```systemctl enable [unit]```

启用并**立即启动**

```systemctl enable --now [unit]```

为当前用户会话生命周期启用**用户级** unit

```systemctl enable --user [unit]```

# SYNOPSIS

**systemctl** [_OPTIONS_...] **enable** _UNIT_...

# PARAMETERS

**--now**
> 启用后同时启动该 unit

**--user**
> 启用用户服务管理器的 unit 而非系统 unit

**--no-reload**
> 启用后不重新加载 systemd 配置

**--force**
> 即使 unit 被 mask 也强制启用

**--runtime**
> 仅临时启用，直到下次重启

# DESCRIPTION

**systemctl enable** 在 systemd 目录中创建符号链接，使 unit 能够在启动时（系统 unit）或登录时（用户 unit）自动启动。这不会立即启动该 unit；请使用 **--now** 同时完成启用和启动。

符号链接根据 unit 文件的 [Install] 节创建，通常链接到 target.wants 目录。启用操作是幂等的；重复启用已启用的 unit 没有任何效果。

# CAVEATS

系统 unit 需要 root 权限。启用不会启动该 unit；请配合 **--now** 或单独使用 **systemctl start**。被 mask 的 unit 无法在缺少 **--force** 时启用。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-disable](/man/systemctl-disable)(1), [systemctl-start](/man/systemctl-start)(1)
