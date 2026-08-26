# TAGLINE

在命令行中搜索网站

# TLDR

**搜索 Google**

```surfraw google [search terms]```

**搜索 Wikipedia**

```surfraw wikipedia [article]```

**搜索 DuckDuckGo**

```surfraw duckduckgo [query]```

**列出可用的 elvi**

```surfraw -elvi```

**仅打印 URL**

```surfraw -p google [query]```

**用浏览器搜索**

```surfraw -browser=[firefox] google [query]```

**搜索 YouTube**

```surfraw youtube [video]```

# SYNOPSIS

**surfraw** [_-elvi_] [_-p_] [_-browser=browser_] _elvi_ _query_

# PARAMETERS

**-elvi**
> 列出搜索引擎。

**-p**, **--print**
> 仅打印 URL。

**-browser** _BROWSER_
> 使用指定的浏览器。

**-g**, **--graphical**
> 使用图形界面浏览器。

**-t**, **--text**
> 使用文本浏览器。

# ELVI (SEARCH ENGINES)

**google** - Google
**duckduckgo** - DuckDuckGo
**wikipedia** - Wikipedia
**youtube** - YouTube
**github** - GitHub
**amazon** - Amazon
**stack** - Stack Overflow

# DESCRIPTION

**surfraw**（Shell Users' Revolutionary Front Rage Against the Web）提供了搜索网站和网络服务的命令行接口。它采用名为 "elvi" 的插件系统，每个 elvi 定义特定网站（如 Google、Wikipedia、DuckDuckGo 或 GitHub）的搜索接口。

该工具根据命令行参数构造搜索 URL，并在配置好的网页浏览器中打开。打印模式输出构造好的 URL 而不打开浏览器，便于管道传给其他命令或脚本。同时支持图形界面浏览器和文本模式浏览器。

自定义 elvi 可以写成简单的 Shell 脚本，为任何带查询式 URL 模式的网站添加支持。该工具自带数十个预配置的 elvi，覆盖常用的搜索引擎、参考站点和软件仓库。

# CAVEATS

部分 elvi 可能已过时。网站会更改它们的 URL。必须配置好浏览器。

# HISTORY

**Surfraw** 由 **Julian Assange** 等人于 **2000 年**创建。它体现了用于网页搜索的 Unix 哲学。

# INSTALL

```dnf: sudo dnf install surfraw```

```pacman: sudo pacman -S surfraw```

```zypper: sudo zypper install surfraw```

```brew: brew install surfraw```

```nix: nix profile install nixpkgs#surfraw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[w3m](/man/w3m)(1), [lynx](/man/lynx)(1), [firefox](/man/firefox)(1)
