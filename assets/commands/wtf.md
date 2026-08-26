# TAGLINE

缩写词查询与展开

# TLDR

**展开**缩写词

```wtf [IMO]```

搜索**计算机**术语

```wtf -t comp [WWW]```

# SYNOPSIS

**wtf** [_OPTIONS_] _ACRONYM_

# PARAMETERS

_ACRONYM_
> 要查询的一个或多个缩写词。多个单词会被拼接在一起；大小写不敏感。

**-f** _FILE_
> 使用 _FILE_ 作为额外的缩写词数据库（每行一条 _ACRONYM<TAB>expansion_）。

**-o**
> 即使在 **is** 别名模式下（_what is_ acronym）也打印展开结果。

**-t** _TYPE_
> 将查询限定到指定的缩写词类别。默认类别包括 _comp_（计算机），以及安装在 **/usr/share/games/bsdgames/wtf/** 目录下的额外文件或你本地的 **acronyms** 文件。

# DESCRIPTION

**wtf** 通过查找本地数据库来展开缩写词，返回其所有已知含义。它是 **bsdgames** 的一部分，附带一份通用缩写列表和多份专题列表（例如用于计算机行话的 **comp**）。

不带选项直接调用会搜索默认数据库；**-t** 可将搜索范围缩小到特定的缩写列表。要扩充数据库，可以把额外的缩写文件放入同一目录，或用 **-f** 传入。

# CAVEATS

数据库可能未收录所有缩写词。某些缩写有多种含义。内容主要聚焦于 Unix/黑客圈行话。

# HISTORY

**wtf** 是 "What The F..." 的缩写，属于 bsdgames 软件包，源自 BSD Unix 文化。

# INSTALL

```apk: sudo apk add wmutils```

```zypper: sudo zypper install wmutils```

```brew: brew install wtf```

```nix: nix profile install nixpkgs#wtf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[whatis](/man/whatis)(1), [apropos](/man/apropos)(1)
