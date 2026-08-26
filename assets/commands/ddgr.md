# TAGLINE

在命令行中进行 DuckDuckGo 搜索

# TLDR

**从终端搜索 DuckDuckGo**

```ddgr [search terms]```

**直接在浏览器打开第一个结果**（I'm Feeling Ducky）

```ddgr -j [search terms]```

**搜索特定网站**

```ddgr -w [amazon.com] [digital camera]```

**将结果限制在近期**（d=天，w=周，m=月，y=年）

```ddgr -t [w] [search terms]```

**设置每页结果数量**

```ddgr -n [25] [search terms]```

**使用 DuckDuckGo bang**快捷方式

```ddgr ![w] [wikipedia search]```

**以 JSON 格式输出结果**

```ddgr --json [search terms]```

**通过代理搜索**

```ddgr --proxy [localhost:8118] [search terms]```

# SYNOPSIS

**ddgr** [_OPTIONS_] [_KEYWORD_ [_KEYWORD_...]]

# PARAMETERS

**-n**, **--num**=_N_
> 每页显示 N 个结果（0-25，默认：10）。

**-r**, **--reg**=_REG_
> 按地区搜索（例如 us-en、uk-en、in-en）。

**-j**, **--ducky**
> 在浏览器中打开第一个结果；隐含 --noprompt。

**-t**, **--time**=_SPAN_
> 按时间限制搜索：d（天）、w（周）、m（月）、y（年）。

**-w**, **--site**=_SITE_
> 搜索特定网站。

**-x**, **--expand**
> 显示完整 URL 而非仅域名。

**-p**, **--proxy**=_URI_
> 通过 HTTP 代理转发流量。

**--unsafe**
> 关闭安全搜索。

**--json**
> 以 JSON 格式输出结果；隐含 --noprompt。

**--np**, **--noprompt**
> 完成搜索后直接退出，不进入交互提示。

**--colors**=_COLORS_
> 设置自定义输出配色方案。

**-C**, **--nocolor**
> 禁用彩色输出。

**-h**, **--help**
> 显示帮助并退出。

# OMNIPROMPT

**n**, **p**, **f**
> 跳转到下一页、上一页或第一页。

_index_
> 在浏览器中打开对应编号的结果。

**o** [_index_|_range_|**a**]
> 在浏览器中打开一个或多个结果。

**d** _keywords_
> 以相同选项进行新搜索。

**c** _index_
> 将 URL 复制到剪贴板。

**x**
> 切换 URL 展开状态。

**q**, **^D**, double Enter
> 退出 ddgr。

# DESCRIPTION

**ddgr** 是一个在终端中搜索 DuckDuckGo 的命令行工具。它以标题、URL 和文本摘要的形式显示搜索结果。结果分页并带编号，可以快速导航并按编号在浏览器中打开。

该工具支持 DuckDuckGo bang 快捷方式（如指向 Wikipedia 的 !w、指向 YouTube 的 !yt）以及 filetype: 和 site: 等关键词。结果可按时间段或地区过滤。DuckDuckGo 以隐私为先，不做跟踪，ddgr 还可以通过 Tor 网络工作。

# ENVIRONMENT

**BROWSER**
> 覆盖默认网页浏览器。

**DDGR_COLORS**
> 自定义配色方案（类似 BSD LSCOLORS 的六字母字符串）。

**HTTPS_PROXY**
> HTTP 代理配置。

# CONFIGURATION

**~/.config/ddgr/config**
> 配置文件，用于设置每页结果数、地区、代理等默认选项。

# CAVEATS

需要 Python 3。结果依赖 DuckDuckGo 的 HTML 界面，该界面可能变化。即时答案等功能在 ddgr 使用的 HTML 版本中不可用。

# HISTORY

ddgr 由 Arun Prakash Jana 创建，是 googler（类似的 Google 搜索工具）的注重隐私替代品。该项目借助 DuckDuckGo 的无跟踪政策和对 Tor 网络的支持来强调用户隐私。

# INSTALL

```dnf: sudo dnf install ddgr```

```pacman: sudo pacman -S ddgr```

```zypper: sudo zypper install ddgr```

```brew: brew install ddgr```

```nix: nix profile install nixpkgs#ddgr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[googler](/man/googler)(1), [surfraw](/man/surfraw)(1), [w3m](/man/w3m)(1), [lynx](/man/lynx)(1)

# RESOURCES

```[Source code](https://github.com/jarun/ddgr)```

<!-- verified: 2026-07-11 -->
