# TAGLINE

从命令行下载和观看动漫

# TLDR

**搜索**动漫

```animdl search "[anime name]"```

**在线观看**动漫

```animdl stream "[anime name]"```

**下载**动漫

```animdl download "[anime name]" -d [./downloads]```

观看指定的**剧集范围**

```animdl stream "[anime name]" -r [1-10]```

通过查询前缀使用特定**提供方**

```animdl stream "[provider]:[anime name]"```

**抓取**流媒体链接输出到标准输出供外部使用

```animdl grab "[anime name]"```

# SYNOPSIS

**animdl** _command_ [_options_] _query_

# DESCRIPTION

**animdl** 是一个高效的命令行动漫下载器和播放工具。它抓取多个动漫来源，可快速访问丰富的内容目录，并支持多种画质和字幕。

该工具注重速度和可靠性，具备并行下载能力和自动来源回退。

# PARAMETERS

**search** _query_
> 搜索动漫

**stream** _query_
> 在线播放动漫剧集

**download** _query_
> 下载动漫剧集

**-r** _range_, **--range** _range_
> 剧集范围（如 1-10、5、1-5,7,9）

**-d** _dir_, **--directory** _dir_
> 下载目录

**-q** _quality_, **--quality** _quality_
> 首选画质（best、720、1080）

**--provider** _name_
> 要使用的特定提供方

**--index** _n_
> 按索引选择搜索结果

**-a**, **--auto**
> 自动选择第一个结果

# CONFIGURATION

**~/.config/animdl/config.yml**
> 配置文件，用于默认提供方、画质、下载目录和播放器设置。

# CAVEATS

依赖可能失效的第三方流媒体站点。下载速度因来源而异。某些提供方可能存在地区限制。

# HISTORY

**animdl** 作为其他动漫命令行工具的 Python 替代品而开发，专注于速度、多提供方支持和批量下载能力。

# INSTALL

```brew: brew install animdl```

```nix: nix profile install nixpkgs#animdl```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ani-cli](/man/ani-cli)(1), [youtube-dl](/man/youtube-dl)(1), [mpv](/man/mpv)(1)

# RESOURCES

```[Source code](https://github.com/justfoolingaround/animdl)```

<!-- verified: 2026-06-11 -->
