# TAGLINE

从命令行控制 MPRIS 媒体播放器

# TLDR

**切换**播放/暂停

```playerctl play-pause```

跳到**下一**曲

```playerctl next```

回到**上一**曲

```playerctl previous```

**列出**所有播放器

```playerctl -l```

控制**特定**播放器

```playerctl -p [player_name] [command]```

控制**所有**播放器

```playerctl -a [command]```

显示**元数据**

```playerctl metadata -f "Now playing: {{artist}} - {{title}}"```

# SYNOPSIS

**playerctl** [**-p** _player_] [**-a**] [**-l**] _command_

# COMMANDS

**play-pause**
> 切换播放状态

**play**
> 开始播放

**pause**
> 暂停播放

**stop**
> 停止播放

**next**
> 下一曲

**previous**
> 上一曲

**position**
> 获取或设置进度位置

**volume**
> 获取或设置音量

**status**
> 获取播放状态

**metadata**
> 获取曲目元数据

# PARAMETERS

**-p, --player _player_**
> 定向控制特定播放器

**-a, --all-players**
> 控制所有播放器

**-l, --list-all**
> 列出可用的播放器

**-f, --format _format_**
> 输出格式模板

# DESCRIPTION

**playerctl** 控制实现了 MPRIS D-Bus 规范的媒体播放器。它提供统一的命令行接口，可以控制 Spotify、VLC、Firefox 以及许多其他媒体应用。

该工具常用于键盘快捷键和脚本中，无需将焦点切到播放器窗口即可控制媒体播放。

# CAVEATS

需要兼容 MPRIS 的播放器。某些播放器的 MPRIS 支持有限。播放器必须正在运行才能被控制。元数据的可用性因播放器而异。

# HISTORY

**playerctl** 由 **Tony Crisci** 开发，旨在提供一种简单可靠的方式，让脚本和快捷键控制媒体播放器。它在平铺式窗口管理器配置中被广泛采用。

# INSTALL

```apt: sudo apt install playerctl```

```dnf: sudo dnf install playerctl```

```pacman: sudo pacman -S playerctl```

```apk: sudo apk add playerctl```

```zypper: sudo zypper install playerctl```

```nix: nix profile install nixpkgs#playerctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pactl](/man/pactl)(1), [mpc](/man/mpc)(1)
