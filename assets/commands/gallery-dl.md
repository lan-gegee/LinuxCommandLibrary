# TAGLINE

支持多站点的图片画廊下载器

# TLDR

**从 URL 下载**

```gallery-dl [https://example.com/gallery]```

**设置输出目录**

```gallery-dl -d [/path/to/downloads] [url]```

**列出支持的站点**

```gallery-dl --list-extractors```

**连同元数据一起下载**

```gallery-dl --write-metadata [url]```

**身份验证**

```gallery-dl -u [username] -p [password] [url]```

# SYNOPSIS

**gallery-dl** [_options_] _urls_...

# PARAMETERS

_URLS_
> 画廊或图片 URL。

**-d** _PATH_, **--dest** _PATH_
> 目标目录。

**-u** _USER_, **--username** _USER_
> 站点用户名。

**-p** _PASS_, **--password** _PASS_
> 站点密码。

**--write-metadata**
> 将元数据保存为 JSON。

**--list-extractors**
> 列出支持的站点。

**-o** _KEY=VALUE_
> 设置配置选项。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.config/gallery-dl/config.json**
> 主配置文件，定义输出路径、文件名模式、身份验证和站点专属选项。

# DESCRIPTION

**gallery-dl** 用于从网站下载图片画廊。它通过针对特定站点的提取器，支持数百个图床网站、社交媒体和艺术社区。

该工具自动处理分页、身份验证、速率限制和元数据提取。下载内容可通过自定义的目录和文件名模式进行组织。

gallery-dl 常用于归档图片论坛、艺术家作品集和社交媒体上的内容。

# CAVEATS

站点支持可能随更新失效。请尊重各站点的服务条款。大量下载可能被限速。

# HISTORY

gallery-dl 作为图片版的 youtube-dl 对应工具而诞生。它通过基于 Python 的提取器支持数百个网站，提供全面的图片下载能力。

# INSTALL

```apk: sudo apk add gallery-dl```

```brew: brew install gallery-dl```

```nix: nix profile install nixpkgs#gallery-dl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[youtube-dl](/man/youtube-dl)(1), [wget](/man/wget)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/mikf/gallery-dl)```

<!-- verified: 2026-07-15 -->
