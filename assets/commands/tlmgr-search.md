# TAGLINE

搜索 TeX Live 软件包

# TLDR

**搜索软件包**

```tlmgr search [keyword]```

**在描述中搜索**

```tlmgr search --global [keyword]```

**搜索文件**

```tlmgr search --file [filename]```

# SYNOPSIS

**tlmgr search** [_options_] _pattern_

# PARAMETERS

**--global**
> 搜索描述和名称。

**--file**
> 搜索文件。

**--word**
> 仅匹配完整单词。

**--all**
> 搜索所有软件包，而不只是已安装的。

# DESCRIPTION

**tlmgr search** 按名称、描述或所含文件查找 TeX Live 软件包。TeX Live Manager 的组成部分，用于发现 LaTeX 软件包。

# SEE ALSO

[tlmgr-info](/man/tlmgr-info)(1), [tlmgr-install](/man/tlmgr-install)(1)
