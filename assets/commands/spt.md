# TAGLINE

Spotify 的终端 UI 客户端

# TLDR

**打开**交互式界面

```spt```

**按名称播放**播放列表

```spt play --name "[Playlist]" --playlist```

**切换**播放状态

```spt playback --toggle```

**搜索**曲目

```spt search "[query]" --tracks```

**打印**Shell 补全脚本

```spt --completions [zsh]```

# SYNOPSIS

**spt** [*options*] [*command*]

# DESCRIPTION

**spt** 是 **spotify-tui** 的二进制名称，后者是一个基于 Rust 的 Spotify 终端客户端。不带参数运行时会打开多窗格 TUI（按 **?** 查看按键）。它还提供一套 CLI，可在不进入界面的情况下执行播放/暂停、搜索、媒体库列表和补全等操作。

首次运行时需要配置 Spotify API 凭据（client id/secret）；配置位于 **~/.config/spotify-tui/** 下（UI 用 **config.yml**，认证用单独的凭据文件）。

# PARAMETERS

**spt**

> 启动 TUI。

**play** **--name** *title* **--track**|**--playlist**|**--album**|**--artist** [**--random**]

> 开始播放名称匹配的内容。

**playback** [**--toggle**] [**--like**] [**--shuffle**] ...

> 控制当前播放器。

**list** [**--liked**] [**--limit** *n*]

> 列出媒体库条目。

**search** *query* **--tracks**|**--playlists**|... [**--format** *fmt*] [**--limit** *n*]

> 搜索曲库。

**--completions** *shell*

> 输出补全脚本。

# CONFIGURATION

**~/.config/spotify-tui/config.yml** 控制主题颜色、快进步长、音量增量及相关 UI 行为。OAuth 设备/浏览器流程完成后，认证令牌单独存放。

# CAVEATS

Spotify 多次限制第三方 API 访问；若上游不更新，功能可能失效。许多播放控制需要 Premium 账户。官方维护状态时好时坏——在依赖它之前请先查看 GitHub 仓库。

# INSTALL

```aur: yay -S spt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[spotify](/man/spotify)(1), [ncspot](/man/ncspot)(1), [playerctl](/man/playerctl)(1)

# RESOURCES

```[Source code](https://github.com/Rigellute/spotify-tui)```

<!-- verified: 2026-07-19 -->
