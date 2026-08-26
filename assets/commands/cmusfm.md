# TAGLINE

面向 cmus 音乐播放器的 Last.fm scrobbler

# TLDR

**初始化** cmusfm 并完成 Last.fm 认证

```cmusfm init```

将 cmusfm **设置为** cmus 的状态显示程序

```cmus -C "set status_display_program=cmusfm"```

**重启** cmusfm 后台服务器

```pkill cmusfm```

**编辑 cmusfm** 配置文件

```$EDITOR ~/.config/cmus/cmusfm.conf```

# SYNOPSIS

**cmusfm** [**init**]

# DESCRIPTION

**cmusfm** 是一款为 **cmus** 音乐播放器设计的独立 Last.fm scrobbler。它以后台服务器进程运行，通过 **status_display_program** 接口从 cmus 接收曲目信息，然后提交 "正在播放" 通知并向 Last.fm 或兼容服务提交 scrobble 记录。

首次使用前，先运行 **cmusfm init** 完成 Last.fm API 认证。然后在 cmus 中通过设置 **status_display_program=cmusfm** 将 cmus 配置为使用 cmusfm。当 cmus 发出第一条状态更新时，cmusfm 服务器会自动启动。

# CONFIGURATION

配置保存在 **~/.config/cmus/cmusfm.conf** 中。编辑该文件可自定义 scrobble 行为。

**format-localfile**
> 用于解析本地音频文件元数据的正则表达式模式（默认：`"^(?A.+) - (?T.+)\.[^.]+$"`）

**format-shoutcast**
> 用于解析流媒体元数据的正则表达式模式（默认：`"^(?A.+) - (?T.+)$"`）

**format-coverfile**
> 用于检测封面图片文件的匹配模式（例如 `"^(cover|folder)\.jpg$"`）

**now-playing-localfile**
> 为本地文件启用 "正在播放" 通知（默认：yes）

**now-playing-shoutcast**
> 为流媒体启用 "正在播放"（默认：no）

**submit-localfile**
> 提交本地文件的 scrobble 记录（默认：yes）

**submit-shoutcast**
> 提交流媒体的 scrobble 记录（默认：no）

**notification**
> 曲目切换时显示桌面通知（默认：禁用）

**service-api-url**
> 自定义 scrobbling 服务 API 端点，用于 Last.fm 替代品（如 Libre.fm）

**service-auth-url**
> 替代服务的自定义认证 URL

# CAVEATS

cmusfm 服务器以后台进程运行，配置更改后必须重启（通过 **pkill cmusfm**）。默认的文件名解析模式可能无法匹配所有命名约定 — 可以为非标准文件名配置自定义正则表达式模式。仅适用于 cmus；与其他音乐播放器不兼容。

# HISTORY

**cmusfm** 是一款专为 **cmus** 终端音乐播放器打造的轻量级独立 Last.fm scrobbler。它以 **C** 编写，使用 Last.fm API 进行认证和 scrobbling。该项目由 **arkq** 在 GitHub 上维护。

# INSTALL

```brew: brew install cmusfm```

```nix: nix profile install nixpkgs#cmusfm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmus](/man/cmus)(1), [mpd](/man/mpd)(1), [ncmpcpp](/man/ncmpcpp)(1), [mpc](/man/mpc)(1)
