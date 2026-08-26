# TAGLINE

支持 vim 按键绑定的终端音乐播放器

# TLDR

打开**指定**目录

```termusic [path/to/directory]```

禁用**专辑封面**显示

```termusic -c```

显示**帮助**

```termusic --help```

**扫描**媒体库并更新数据库

```termusic scan```

# SYNOPSIS

**termusic** [_OPTIONS_] [_PATH_]

# PARAMETERS

**-c**
> 禁用专辑封面显示

**-m** _DEPTH_
> 文件夹扫描的最大深度（默认：4）

**scan**
> 扫描媒体库并更新数据库

**config**
> 在编辑器中打开配置文件

**--help**
> 显示帮助信息

# DESCRIPTION

**termusic** 是一款用 Rust 编写的终端音乐播放器，特色是类似 vim 的按键绑定。它支持多种音频格式，并提供 TUI（终端用户界面）用于浏览和播放音乐。

配置存储在 `~/.config/termusic/config.toml` 中，可在其中设置默认目录和偏好选项。

# KEY BINDINGS

**j/k** - 上/下导航

**Enter** - 播放所选曲目

**Space** - 暂停/继续

**n/p** - 下一首/上一首

**s** - 切换随机播放

**f** - 向前快进

**F1** - 帮助

**q** - 退出

# CAVEATS

专辑封面显示需要兼容的终端。某些音频格式可能需要额外的编解码器支持。

# HISTORY

**termusic** 是由 **tramhao** 开发的一款现代终端音乐播放器，灵感来自 vim 的模态编辑理念，专为键盘驱动的音乐播放而设计。

# INSTALL

```pacman: sudo pacman -S termusic```

```brew: brew install termusic```

```nix: nix profile install nixpkgs#termusic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmus](/man/cmus)(1), [ncmpcpp](/man/ncmpcpp)(1), [mpv](/man/mpv)(1)
