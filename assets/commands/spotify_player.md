# TAGLINE

功能丰富的终端 Spotify 客户端

# TLDR

**启动**播放器 TUI

```spotify_player```

**CLI** 播放辅助命令（见帮助）

```spotify_player [command] --help```

# SYNOPSIS

**spotify_player** [*command*] [*options*]

# DESCRIPTION

**spotify_player** 是一个 Rust 编写的 Spotify TUI，支持流媒体播放、Spotify Connect 控制、歌词、音频可视化以及媒体键控制。二进制文件名中使用下划线。可通过 **cargo install spotify_player** 或发行版软件包安装。

需要 Spotify 身份验证（OAuth / 会话）。许多功能（如播放）需要 Spotify Premium 订阅。

# PARAMETERS

默认调用会打开 TUI。另有用于非交互控制的子命令——运行 **spotify_player --help** 查看。配置位于 XDG 配置目录下（**app.toml** / 主题文件详见上游文档）。

# CAVEATS

受 Spotify API 和服务条款约束；Spotify 更改 API 时功能可能失效。流媒体质量和设备数量限制取决于账户类型。

# INSTALL

```brew: brew install spotify_player```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[spt](/man/spt)(1), [ncspot](/man/ncspot)(1), [playerctl](/man/playerctl)(1)

# RESOURCES

```[Source code](https://github.com/aome510/spotify-player)```

<!-- verified: 2026-07-19 -->
