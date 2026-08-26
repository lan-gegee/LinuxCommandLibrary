# TAGLINE

离线文档搜索引擎

# TLDR

跨所有来源**搜索**文档

```wikiman [query]```

**仅搜索指定来源**（逗号分隔）

```wikiman -s [man,arch] [query]```

**列出**可用来源

```wikiman -S```

以快速搜索模式**搜索**

```wikiman -q [query]```

使用 AND 运算符**搜索**（所有关键词都必须匹配）

```wikiman -a [query]```

**打印**原始输出而不进入交互选择

```wikiman -R [query]```

在 HTML 查看器而非分页器中**打开**结果

```wikiman -H [w3m] [query]```

# SYNOPSIS

**wikiman** [_options_] [_keyword..._]

# PARAMETERS

**-s** _SOURCES_
> 要搜索的来源列表，逗号分隔（默认：所有可用来源）。

**-l** _LANGUAGES_
> 搜索语言，逗号分隔（默认：en）。

**-f** _FINDER_
> 要使用的模糊查找器（默认：fzf）。

**-H** _VIEWER_
> 用于 wiki 页面的 HTML 查看器（默认：w3m）。

**-q**
> 启用快速搜索模式。

**-a**
> 启用 AND 运算符模式（所有关键词都必须匹配）。

**-p**
> 禁用快速结果预览。

**-k**
> 查看某个结果后保持 wikiman 打开。

**-c**
> 在结果中显示来源列。

**-R**
> 打印原始输出而不进入交互选择。

**-S**
> 列出可用来源并退出。

**-W** _SHELL_
> 为指定 shell（bash、zsh、fish）打印小部件代码并退出。

**-v**
> 打印版本并退出。

**-h**
> 显示帮助并退出。

# SOURCES

**man** - Man 手册页
**arch** - Arch Wiki
**gentoo** - Gentoo Wiki
**tldr** - TLDR 页面
**fbsd** - FreeBSD 文档
**devdocs** - DevDocs

# DESCRIPTION

**wikiman** 是一个离线文档搜索引擎，它把 man 手册页、Arch Wiki、Gentoo Wiki、TLDR 页面、FreeBSD 文档和 DevDocs 等多个来源聚合到一个可搜索的界面中。查询会同时在所有已配置的来源中匹配，并通过模糊匹配按相关性对结果排序。

来源过滤可将搜索范围缩小到特定的文档类型，例如只搜 wiki 文章或只搜 man 手册页。结果可以在终端分页器中查看，也可以在浏览器中打开，wiki 内容会保留完整的 HTML 格式。

首次同步后所有文档都存储在本地，无需网络即可快速搜索。如果不提供关键词，则显示所有页面。

# CONFIGURATION

**~/.config/wikiman/wikiman.conf**
> 用户配置文件。若不存在则回退到 /etc/wikiman.conf。遵循 XDG_CONFIG_HOME。

通过 source 来自 /usr/share/wikiman/widgets/ 的小部件文件（支持 bash、zsh 或 fish），可以启用 shell 按键绑定（默认 Ctrl+F）。

# CAVEATS

初始来源同步需要网络访问，且根据启用的来源可能下载数量可观的数据。交互式选择需要 fzf 或其他模糊查找器。

# INSTALL

```pacman: sudo pacman -S wikiman```

```nix: nix profile install nixpkgs#wikiman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [tldr](/man/tldr)(1), [apropos](/man/apropos)(1), [fzf](/man/fzf)(1), [w3m](/man/w3m)(1)
