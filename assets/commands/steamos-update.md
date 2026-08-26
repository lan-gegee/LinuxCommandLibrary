# TAGLINE

更新 SteamOS 系统映像

# TLDR

将 SteamOS **更新**到最新版本

```sudo steamos-update```

仅**检查**是否有可用更新而不安装

```steamos-update check```

先启用可写模式（如果在更新前修改根文件系统）

```sudo steamos-readonly disable```

# SYNOPSIS

**steamos-update** [_COMMAND_]

# COMMANDS

(无参数)
> 下载并安装可用更新

**check**
> 检查是否有可用更新而不安装

# DESCRIPTION

**steamos-update** 将 SteamOS 更新到所选分支上的最新可用版本。更新会被下载并安装到非活动的 A/B 分区，然后系统重启进入已更新的分区。

A/B 分区方案确保了更新失败时有可靠的回退——上一个正常工作的分区仍可用于恢复。

当应用了更新或有可用更新时（取决于子命令），**steamos-update** 返回退出码 **0**；当系统已是最新时返回 **7**（便于脚本处理）。

# CAVEATS

应用更新需要网络连接和 root 权限。更新的体积可能很大。安装完成后系统会重启进入已更新的分区。更新可用性取决于所选分支（stable、beta 或 main），可通过 **steamos-select-branch** 选择。不支持在非 SteamOS 系统上运行。

# HISTORY

**steamos-update** 是 **Valve** 开发的 **SteamOS** 工具的一部分。SteamOS 3.0 使用类似 Chrome OS 和 Android 的基于映像的更新系统，确保原子化更新和轻松回滚。

# SEE ALSO

[steamos-select-branch](/man/steamos-select-branch)(1), [steamos-finalize-install](/man/steamos-finalize-install)(1), [steamos-readonly](/man/steamos-readonly)(1)
