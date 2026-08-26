# TAGLINE

终端 Spotify 客户端

# TLDR

**启动 ncspot**

```ncspot```

**搜索音乐**

```ncspot -s "[search query]"```

**播放指定 URI**

```ncspot play [spotify:track:...]```

# SYNOPSIS

**ncspot** [_options_]

# PARAMETERS

**-s** _QUERY_
> 搜索音乐。

**play** _URI_
> 播放 Spotify URI。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ncspot** 是一款终端 Spotify 客户端。它通过 Spotify API 播放音乐。

该工具提供 ncurses 界面。是官方客户端的轻量替代品。

# CAVEATS

需要 Spotify Premium。基于 Rust 编写。配置文件位于 ~/.config/ncspot。

# HISTORY

ncspot 是用 Rust 基于 librespot 编写的**轻量级终端** Spotify 客户端。

# INSTALL

```pacman: sudo pacman -S ncspot```

```apk: sudo apk add ncspot```

```zypper: sudo zypper install ncspot```

```brew: brew install ncspot```

```nix: nix profile install nixpkgs#ncspot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[spotify_player](/man/spotify_player)(1), [cmus](/man/cmus)(1), [mpd](/man/mpd)(1)
