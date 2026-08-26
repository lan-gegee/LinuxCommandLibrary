# TAGLINE

在终端中进行 Google 搜索

# TLDR

**搜索 Google**

```googler [search terms]```

**搜索新闻**

```googler -N [query]```

**搜索指定网站**

```googler -w [site.com] [query]```

**限制结果数量**

```googler -n [5] [query]```

**在浏览器中打开结果**

```googler --open [query]```

# SYNOPSIS

**googler** [_options_] [_query_]

# PARAMETERS

_QUERY_
> 搜索词。

**-n** _NUM_
> 结果数量。

**-N**, **--news**
> 搜索新闻。

**-w** _SITE_
> 限定在某个网站内搜索。

**--open**
> 在浏览器中打开。

**-l** _LANG_
> 语言代码（例如 en、fr、de）。

**-t** _PERIOD_
> 时间过滤：h（小时）、d（天）、w（周）、m（月）、y（年）。

**-c** _COUNTRY_
> 用于获取本地化结果的国家代码。

**--json**
> 以 JSON 格式输出结果。

**--noprompt**
> 非交互模式（无提示符，打印结果后退出）。

# DESCRIPTION

**googler** 是一款在终端里搜索 Google 的高效工具。它会显示结果的标题、URL 和摘要，并提供交互界面用于浏览结果及在浏览器中打开。

该工具支持站点限定搜索、新闻搜索和多种输出定制，且无需 API 密钥即可使用。

# CONFIGURATION

**BROWSER**
> 用于指定打开搜索结果所用浏览器的环境变量。

# CAVEATS

依赖网页抓取实现。Google 页面结构变化可能导致其失效。无需 API 密钥。

# HISTORY

googler 由 **Arun Prakash Jana** 创建，旨在从命令行提供完整的 Google 搜索功能。

# INSTALL

```dnf: sudo dnf install googler```

```zypper: sudo zypper install googler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ddgr](/man/ddgr)(1), [w3m](/man/w3m)(1)
