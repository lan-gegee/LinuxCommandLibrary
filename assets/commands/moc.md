# TAGLINE

终端音频播放器

# TLDR

**启动 MOC**

```mocp```

**只启动服务器**

```mocp -S```

**播放文件**

```mocp -l [file.mp3]```

**加入播放列表**

```mocp -a [file.mp3]```

**播放/暂停**

```mocp -G```

**下一曲**

```mocp -f```

**停止服务器**

```mocp -x```

# SYNOPSIS

**mocp** [_options_] [_files_]

# PARAMETERS

_FILES_
> 要播放的音频文件。

**-S**
> 启动服务器。

**-l** _FILE_
> 播放文件。

**-a** _FILE_
> 加入播放列表。

**-G**
> 切换播放/暂停。

**-f**
> 下一曲。

**-x**
> 停止服务器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**moc**（Music On Console）是一个终端音频播放器。它采用客户端-服务器架构。

该工具在后台播放，通过插件支持多种音频格式，界面基于 ncurses。

# CAVEATS

服务器独立运行。界面基于 ncurses。格式支持基于插件实现。

# HISTORY

MOC 的诞生是为了提供一个支持后台播放的基于控制台的**音乐播放器**。

# INSTALL

```apt: sudo apt install qtchooser```

```dnf: sudo dnf install qtchooser```

```apk: sudo apk add qt5-qtbase-dev```

```zypper: sudo zypper install moc```

```brew: brew install moc```

```nix: nix profile install nixpkgs#moc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpd](/man/mpd)(1), [cmus](/man/cmus)(1), [mpv](/man/mpv)(1)
