# TAGLINE

输出 Mercurial 仓库的根目录

# TLDR

**显示仓库根目录**

```hg root```

**在脚本中使用**

```cd $(hg root)```

# SYNOPSIS

**hg root** [_options_]

# PARAMETERS

**--share-source**
> 当仓库是通过 **share** 扩展创建时，改为输出共享源仓库的根目录。

**-T**, **--template** _TEMPLATE_
> 使用给定模板显示输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hg root** 输出 Mercurial 仓库的根目录，即 .hg 目录的上一级的绝对路径。

在脚本中，无论当前工作目录是什么，该命令都能定位到仓库根目录，非常实用。不在仓库内时会报错。

# CAVEATS

不在仓库内时会失败。返回绝对路径。是一个简单的实用命令。

# HISTORY

root 是 **Mercurial** 中用于定位仓库顶层目录的实用命令。

# SEE ALSO

[hg](/man/hg)(1), [git-rev-parse](/man/git-rev-parse)(1), [pwd](/man/pwd)(1)

# RESOURCES

```[Source code](https://foss.heptapod.net/mercurial/mercurial-devel)```

```[Documentation](https://wiki.mercurial-scm.org/)```

<!-- verified: 2026-07-19 -->
