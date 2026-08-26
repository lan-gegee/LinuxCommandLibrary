# TAGLINE

从终端获取 Wikipedia 摘要

# TLDR

**搜索 Wikipedia**

```wikit [topic]```

**多词查询**

```wikit "[linux kernel]"```

**指定语言**

```wikit -l [es] [topic]```

**在浏览器中打开**

```wikit -b [topic]```

**显示完整文章**

```wikit -a [topic]```

**禁用换行**

```wikit -n [topic]```

# SYNOPSIS

**wikit** [_-l lang_] [_-b_] [_-a_] [_options_] _query_

# PARAMETERS

**-l**, **--lang** _LANG_
> Wikipedia 语言。

**-b**, **--browser**
> 在浏览器中打开。

**-a**, **--all**
> 完整文章。

**-n**, **--line**
> 不自动换行。

**-d**, **--disambig**
> 显示消歧义页面。

# DESCRIPTION

**wikit** 是一个命令行工具，可直接在终端获取 Wikipedia 文章摘要。默认情况下它显示匹配文章的第一段，让你无需离开命令行就能快速了解任何主题。

完整文章模式会显示开头摘要之外的扩展内容。语言选择功能可查询 Wikipedia 的任意语言版本；浏览器模式则在网页浏览器中打开完整文章以便通读。当一个查询匹配到多篇文章时，消歧义模式会列出所有可能的含义，方便你进一步细化搜索。

# CAVEATS

需要联网。受 Wikipedia API 限制。并非所有语言的数据都完整。

# HISTORY

**wikit** 为在终端快速查阅 Wikipedia 而生。它提供对百科知识的即时访问。

# INSTALL

```nix: nix profile install nixpkgs#wikit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [w3m](/man/w3m)(1)
