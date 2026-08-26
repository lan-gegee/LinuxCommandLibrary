# TAGLINE

切换 SteamOS 文件系统写保护

# TLDR

**禁用**只读模式（使文件系统可写）

```sudo steamos-readonly disable```

**启用**只读模式

```sudo steamos-readonly enable```

# SYNOPSIS

**steamos-readonly** _enable_|_disable_

# COMMANDS

**enable**
> 将文件系统设为只读模式

**disable**
> 将文件系统设为可写模式

# DESCRIPTION

**steamos-readonly** 控制 Steam Deck 上 SteamOS 根文件系统的只读状态。默认情况下，SteamOS 使用不可变的根文件系统来维护系统完整性并简化更新。此命令允许在进行系统修改时临时禁用该保护。

禁用只读模式后，可以安装软件包、修改配置文件以及进行其他原本会被阻止的系统级更改。

# CAVEATS

对文件系统的更改可能被系统更新覆盖。滥用只读模式的禁用功能可能影响系统稳定性。完成更改后应重新启用。尽可能考虑使用 Flatpak 或其他容器化方案。需要 root 权限。

# HISTORY

**steamos-readonly** 属于 **SteamOS 3.0**，由 **Valve** 为 **2022 年 2 月**发布的 **Steam Deck** 开发。这种不可变文件系统的设计受到 Fedora Silverblue 等其他现代 Linux 发行版的启发，在提供可靠性的同时允许高级用户在需要时选择退出。

# SEE ALSO

[steamos-devmode](/man/steamos-devmode)(1), [btrfs](/man/btrfs)(8), [mount](/man/mount)(8)
