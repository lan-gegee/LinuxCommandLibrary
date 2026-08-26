# TAGLINE

视频字幕自动下载工具

# TLDR

**为视频下载字幕**

```subliminal download -l [en] [video.mkv]```

**为目录下载字幕**

```subliminal download -l [en] [videos/]```

**多种语言**

```subliminal download -l [en] -l [es] [video.mkv]```

**指定数据提供方**

```subliminal download -l [en] -p [opensubtitles] [video.mkv]```

**强制下载**

```subliminal download -l [en] -f [video.mkv]```

**带身份验证**

```subliminal --opensubtitles [user] [pass] download -l [en] [video.mkv]```

# SYNOPSIS

**subliminal** [_--provider auth_] **download** [_-l lang_] [_-p provider_] [_options_] _paths_

# PARAMETERS

**download**
> 下载字幕。

**-l**, **--language** _LANG_
> 语言代码。

**-p**, **--provider** _NAME_
> 字幕提供方。

**-f**, **--force**
> 强制重新下载。

**-a**, **--age** _AGE_
> 文件年龄过滤器。

**-d**, **--directory** _DIR_
> 输出目录。

**-e**, **--encoding** _ENC_
> 字幕编码。

# PROVIDERS

**opensubtitles** - OpenSubtitles.org
**addic7ed** - Addic7ed
**podnapisi** - Podnapisi
**thesubdb** - TheSubDB
**tvsubtitles** - TVSubtitles

# DESCRIPTION

**subliminal** 通过同时搜索多个在线提供方自动为视频文件下载字幕。它使用视频文件哈希来准确识别内容，匹配精确的发行版本以获得同步良好的字幕，而不是仅仅依赖文件名匹配。

该工具会查询 OpenSubtitles、Addic7ed、Podnapisi 等多个字幕提供方，提高找到字幕的可能性。如果某个提供方失败，它会自动回退到其他提供方。语言通过 ISO 639-1 代码指定，单条命令可以请求多种语言。

Subliminal 可以递归扫描整个目录，批量处理媒体库。除非强制重新下载，否则它会跳过已有字幕的视频。可配置提供方身份验证，以访问具有更高下载限额的付费字幕源。

# CAVEATS

某些提供方需要账户。受速率限制约束。并非所有视频都有字幕。

# HISTORY

**Subliminal** 是一个用于下载字幕的 Python 库和 CLI。它简化了为视频文件查找和下载字幕的过程。

# INSTALL

```brew: brew install subliminal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ffmpeg](/man/ffmpeg)(1), [vlc](/man/vlc)(1)
