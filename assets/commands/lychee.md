# TAGLINE

快速链接检查器

# TLDR

**检查文件中的链接**

```lychee [README.md]```

**检查整个目录**

```lychee [docs/]```

**检查网站**

```lychee [https://example.com]```

**排除匹配模式**

```lychee --exclude [example.com] [file.md]```

**输出格式**

```lychee --format json [file.md]```

**跳过联网检查**

```lychee --offline [file.md]```

# SYNOPSIS

**lychee** [_options_] _inputs_

# PARAMETERS

_INPUTS_
> 文件、目录或 URL。

**--exclude** _PATTERN_
> 排除匹配的 URL。

**--format** _FMT_
> 输出格式（plain、json、markdown）。

**--offline**
> 跳过网络检查。

**--cache**
> 对结果使用缓存。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lychee** 是一款快速链接检查器。它可以校验 markdown、HTML 和纯文本中的链接。

该工具用 Rust 编写以保证速度，能够并发地检查本地链接与远程链接。

# CAVEATS

网络检查可能受到速率限制。有些网站会拦截自动化请求。基于 Rust 实现。

# HISTORY

lychee 是为文档和网站打造的一款快速的现代化链接检查器，基于 **Rust** 实现。

# INSTALL

```pacman: sudo pacman -S lychee```

```zypper: sudo zypper install lychee```

```brew: brew install lychee```

```nix: nix profile install nixpkgs#lychee```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[linkchecker](/man/linkchecker)(1), [wget](/man/wget)(1), [curl](/man/curl)(1)
