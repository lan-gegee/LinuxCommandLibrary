# TAGLINE

安装 TeX Live 软件包

# TLDR

**安装软件包**

```tlmgr install [package]```

**安装多个软件包**

```tlmgr install [package1] [package2]```

**连同文档和源码安装**

```tlmgr install --with-doc --with-src [package]```

**试运行**

```tlmgr install --dry-run [package]```

# SYNOPSIS

**tlmgr install** [_options_] _package_...

# PARAMETERS

**--with-doc**
> 包含文档。

**--with-src**
> 包含源文件。

**--dry-run**
> 显示将要安装的内容。

**--file**
> 软件包为本地文件。

**--reinstall**
> 重新安装软件包。

# DESCRIPTION

**tlmgr install** 从 CTAN 仓库安装 TeX Live 软件包。自动解析依赖。TeX Live Manager 的组成部分，用于管理 LaTeX 软件包和字体。

# SEE ALSO

[tlmgr-remove](/man/tlmgr-remove)(1), [tlmgr-update](/man/tlmgr-update)(1), [tlmgr](/man/tlmgr)(1)
