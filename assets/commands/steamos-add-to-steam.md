# TAGLINE

将程序添加到 SteamOS 游戏库

# TLDR

将**程序**添加到 Steam 库

```steamos-add-to-steam [path/to/file]```

将**应用**添加到 Steam

```steamos-add-to-steam [path/to/application.desktop]```

# SYNOPSIS

**steamos-add-to-steam** _path/to/file_

# DESCRIPTION

**steamos-add-to-steam** 将非 Steam 程序添加到 SteamOS（Steam Deck）的 Steam 库中。这允许通过 Steam 的界面（包括大屏幕模式和 Game Mode）启动来自其他来源的游戏或应用程序。

该命令为指定的可执行文件或 desktop 文件创建 Steam 快捷方式，使其与 Steam 游戏并列可见。这对于通过 Steam 的统一界面运行模拟器、原生 Linux 游戏或其他应用程序很有用。

# CAVEATS

仅适用于 SteamOS/Steam Deck。目标文件必须是可执行的。Windows 可执行文件可能需要配置 Proton/Wine 兼容层。手柄配置在添加后通过 Steam 管理。

# HISTORY

**steamos-add-to-steam** 是 **Valve** 为 SteamOS 3.0 开发的实用工具，该系统驱动 **2022 年 2 月**发布的 **Steam Deck** 掌上游戏设备。此命令简化了向库中添加非 Steam 内容的过程，此前需要手动创建快捷方式。

# INSTALL

```aur: yay -S steamos-add-to-steam```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[steam](/man/steam)(1), [steamos-devmode](/man/steamos-devmode)(1), [steamos-readonly](/man/steamos-readonly)(1), [steamos-session-select](/man/steamos-session-select)(1), [steamos-update](/man/steamos-update)(1), [flatpak](/man/flatpak)(1)
