# TAGLINE

更新 TeX Live 软件包

# TLDR

**更新所有软件包**

```tlmgr update --all```

**更新特定软件包**

```tlmgr update [package]```

**检查更新**

```tlmgr update --list```

**更新自身**

```tlmgr update --self```

# SYNOPSIS

**tlmgr update** [_options_] [_package_...]

# PARAMETERS

**--all**
> 更新所有已安装的软件包。

**--self**
> 更新 tlmgr 本身。

**--list**
> 列出可用更新。

**--dry-run**
> 显示将要更新的内容。

**--backup**
> 在更新前备份软件包。

**--exclude** _pkg_
> 将软件包排除在更新之外。

# DESCRIPTION

**tlmgr update** 将 TeX Live 软件包更新到最新版本。可以更新整个发行版或特定软件包。TeX Live Manager 的组成部分。

# SEE ALSO

[tlmgr-install](/man/tlmgr-install)(1), [tlmgr](/man/tlmgr)(1)
