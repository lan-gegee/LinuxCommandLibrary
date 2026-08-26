# TAGLINE

从 Instagram 主页下载图片、视频、文字说明和元数据

# TLDR

**下载**某个主页的帖子

```instaloader [profile_name]```

下载主页的**精选集**（highlights）

```instaloader --highlights [profile_name]```

安静地下载带**地理标签**的帖子

```instaloader -q -G [profile_name]```

使用**登录**凭据下载（用于私密主页）

```instaloader -l [username] -p [password] [profile_name]```

**快速更新** —— 若第一个文件已下载过则跳过

```instaloader -F [profile_name]```

下载**快拍**（stories）和 IGTV（需登录）

```instaloader -l [username] -p [password] -s --igtv [profile_name]```

# SYNOPSIS

**instaloader** [_options_] _target_

# PARAMETERS

**-l**, **--login** _USER_
> 以 _USER_ 身份登录。会交互式提示输入密码并在本地缓存会话。

**-p**, **--password** _PASS_
> 在命令行提供密码。**不建议**：密码会泄漏到 shell 历史和进程列表中；建议改用交互式提示。

**-f**, **--sessionfile** _FILE_
> 从 _FILE_ 读取/写入会话 cookie，而非默认位置。

**--load-cookies** _BROWSER_
> 导入已登录浏览器的 Instagram cookie（如 **firefox**、**chrome**）。

**-s**, **--stories**
> 同时下载每个目标的快拍（需要登录）。

**--igtv**
> 同时下载 IGTV/Reels 视频。

**--highlights**
> 下载快拍精选集。

**-G**, **--geotags**
> 在帖子旁保存地理标签信息的 .txt 文件。

**-F**, **--fast-update**
> 一旦遇到第一个已下载的条目就停止迭代目标。

**--post-filter** _EXPR_, **--only-if** _EXPR_
> 对每条帖子求值的 Python 表达式（例如 `--post-filter=viewer_has_liked`）；只下载匹配的帖子。

**--storyitem-filter** _EXPR_
> 同上，但应用于快拍条目。

**--no-pictures**, **--no-videos**, **--no-captions**, **--no-metadata-json**, **--no-profile-pic**, **--no-posts**
> 排除特定内容类型。

**--dirname-pattern** _PATTERN_, **--filename-pattern** _PATTERN_
> 使用 Python 格式字符串自定义输出路径。

**-q**, **--quiet**
> 抑制交互式提示和进度消息。

**--user-agent** _UA_
> 发送自定义 HTTP **User-Agent** 头。

# DESCRIPTION

**instaloader** 从 Instagram 主页下载图片、视频、文字说明和元数据。它可以归档完整主页，包括帖子、快拍、IGTV 和精选集。

目标可以是主页名称、话题标签（**"#tag"**）、位置 ID（**%id**），或特殊选择器 **:feed**、**:stories**、**:saved**。给主页名加 **@** 前缀则会下载其关注列表。要获取最佳画质媒体以及访问私密主页或快拍，需要登录凭据。下载内容包括文字说明、评论和地理位置等元数据（如果可用）。

# CAVEATS

Instagram 可能对发出大量请求的账号进行限速或封禁。下载快拍、私密主页和全画质内容需要登录凭据。Instagram 的服务条款可能限制自动下载行为。

# HISTORY

instaloader 是一款用于归档 Instagram 内容的 Python 工具。它为下载自己的内容或公开主页供个人使用提供了合法途径。

# INSTALL

```brew: brew install instaloader```

```nix: nix profile install nixpkgs#instaloader```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[youtube-dl](/man/youtube-dl)(1), [gallery-dl](/man/gallery-dl)(1)
