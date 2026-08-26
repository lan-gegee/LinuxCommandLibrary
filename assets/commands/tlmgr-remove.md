# TAGLINE

卸载 TeX Live 软件包

# TLDR

**移除软件包**

```tlmgr remove [package]```

**移除多个软件包**

```tlmgr remove [package1] [package2]```

**强制移除**

```tlmgr remove --force [package]```

**试运行**

```tlmgr remove --dry-run [package]```

# SYNOPSIS

**tlmgr remove** [_options_] _package_...

# PARAMETERS

**--force**
> 即使其他软件包依赖它也强制移除。

**--dry-run**
> 显示将要移除的内容。

**--no-depends**
> 不移除依赖。

**--no-depends-at-all**
> 更加激进：即使同一集合内的依赖软件包也不检查、不移除。

# DESCRIPTION

**tlmgr remove** 卸载 TeX Live 软件包、集合或方案。默认情况下，它会阻止移除其他已安装组件所需的软件包，以保证 TeX Live 安装的完整性，除非使用 `--force` 覆盖。TeX Live 以系统级方式安装时需要 root 权限。

# SEE ALSO

[tlmgr-install](/man/tlmgr-install)(1), [tlmgr-update](/man/tlmgr-update)(1), [tlmgr](/man/tlmgr)(1)
