# TAGLINE

在 SteamOS 的游戏模式与桌面模式之间切换

# TLDR

切换到**桌面**模式

```steamos-session-select plasma```

切换到**游戏模式**

```steamos-session-select```

切换到 **Wayland** 桌面

```steamos-session-select plasma-wayland```

**持久的** Wayland 桌面（启动默认项）

```steamos-session-select plasma-wayland-persistent```

**持久的** X11 桌面（启动默认项）

```steamos-session-select plasma-x11-persistent```

# SYNOPSIS

**steamos-session-select** [_SESSION_]

# SESSIONS

**plasma**
> KDE Plasma 桌面模式

**plasma-wayland**
> 基于 Wayland 的 KDE Plasma 桌面

**plasma-x11-persistent**
> X11 桌面，并设为启动默认项

**plasma-wayland-persistent**
> Wayland 桌面，并设为启动默认项

(无参数)
> 返回游戏模式（移除持久桌面选择）

# DESCRIPTION

**steamos-session-select** 在 SteamOS 会话之间切换，让用户可以从游戏界面切换到 KDE Plasma 桌面环境再切回来。带 `-persistent` 后缀的会话会使设备默认启动到该会话。

此命令相当于 Steam Deck 电源菜单中提供的会话切换功能的命令行版本。

# CAVEATS

会话更改在当前会话结束后生效。持久会话会改变启动默认项，直到再次更改。全新安装时默认会话为游戏模式。

# HISTORY

**steamos-session-select** 是 **Valve** 开发的 **SteamOS** 工具的一部分。双会话设计使 Steam Deck 既能作为游戏主机运行，又能充当完整的 Linux 桌面。

# INSTALL

```aur: yay -S steamos-session-select```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[steamos-devmode](/man/steamos-devmode)(1)
