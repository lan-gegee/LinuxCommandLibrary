# TAGLINE

搜索可用的 Homebrew 软件包

# TLDR

**搜索** formula 或 cask

```brew search [text]```

仅**搜索** formula

```brew search --formula [text]```

仅**搜索** cask

```brew search --cask [text]```

使用正则表达式**搜索**

```brew search /[regex]/```

列出所有可用的 formula

```brew search```

搜索并以 JSON 格式输出

```brew search --json [text]```

搜索时附带描述

```brew search --desc [text]```

# SYNOPSIS

**brew search** [_options_] [_text|/regex/_]

# DESCRIPTION

**brew search** 在本地 Homebrew 仓库中查询与搜索词匹配的 formula 和 cask。它搜索软件包名称、token 和描述。搜索还会在线扩展到 homebrew/core 和 homebrew/cask 仓库。

不带参数时，它会列出本地所有可用的 formula。

# PARAMETERS

**--formula**
> 仅搜索 formula（命令行软件包）。

**--cask**
> 仅搜索 cask（图形界面应用）。

**--desc**
> 搜索时包含软件包描述。

**--json**
> 以 JSON 格式输出结果。

**--pull-request**
> 搜索包含指定文本的 GitHub pull request。

**--open**
> 仅搜索处于打开状态的 pull request。

**--closed**
> 仅搜索已关闭的 pull request。

# REGULAR EXPRESSIONS

将搜索词用斜杠包裹即可启用正则表达式：

```brew search /^python@/```

搜索以 "python@" 开头的软件包。

# CAVEATS

搜索结果同时包含已安装和可安装的软件包。要了解特定软件包的详细信息请使用 brew info。搜索默认不区分大小写。

# SEE ALSO

[brew](/man/brew)(1), [brew-info](/man/brew-info)(1), [brew-install](/man/brew-install)(1), [brew-list](/man/brew-list)(1)

# RESOURCES

```[Source code](https://github.com/Homebrew/brew)```

```[Homepage](https://brew.sh)```

```[Documentation](https://docs.brew.sh)```

<!-- verified: 2026-06-22 -->
