# TAGLINE

从模板生成 gitignore 文件

# TLDR

**为某种语言生成 gitignore**

```git ignore-io [Python]```

**为多种类型生成**

```git ignore-io [Python] [macOS] [vim]```

**追加到当前目录的 .gitignore**

```git ignore-io -a [Python] [vim]```

**替换当前目录的 .gitignore**

```git ignore-io -r [Python] [macOS]```

**以表格形式列出可用模板**

```git ignore-io -l```

**搜索模板**

```git ignore-io -s [node]```

# SYNOPSIS

**git ignore-io** [_options_] _templates_

# PARAMETERS

_TEMPLATES_
> 来自 gitignore.io 的模板名称。

**-a**, **--append** _TYPES_
> 将新内容追加到当前目录下的 .gitignore。

**-r**, **--replace** _TYPES_
> 用新内容替换当前目录中的 .gitignore。

**-l**, **--list-in-table**
> 以表格形式列出可用的模板。

**-L**, **--list-alphabetically**
> 按字母顺序列出可用的模板。

**-s**, **--search** _WORD_
> 在可用类型中搜索单词。

**-t**, **--show-update-time**
> 显示缓存的类型列表的最后修改时间。

**-u**, **--update-list**
> 更新缓存的类型列表。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git ignore-io** 从 gitignore.io 模板生成 .gitignore 内容。它通过 gitignore.io API 获取针对语言、框架、IDE 和操作系统精心整理的忽略模式。

多个模板可以在一次请求中组合，实现全面覆盖。它是 git-extras 套件的组成部分，为庞大的 gitignore.io 模板数据库提供了快捷的命令行入口。

# CAVEATS

属于 git-extras 软件包。需要网络连接。模板可能需要自行定制。

# HISTORY

git ignore-io 是 **git-extras** 的组成部分，为生成 gitignore 文件的网络服务 **gitignore.io** 提供命令行访问。

# INSTALL

```brew: brew install git-ignore```

```nix: nix profile install nixpkgs#git-ignore```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-ignore](/man/git-ignore)(1), [gibo](/man/gibo)(1), [git-extras](/man/git-extras)(1)
