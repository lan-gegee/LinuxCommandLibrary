# TAGLINE

升级 Slackware 软件包

# TLDR

**升级**软件包

```sudo upgradepkg [path/to/package.tgz]```

若不存在则**安装**

```sudo upgradepkg --install-new [path/to/package.tgz]```

**重装**软件包

```sudo upgradepkg --reinstall [path/to/package.tgz]```

**试运行**预览

```upgradepkg --dry-run [path/to/package.tgz]```

带**详细输出**升级

```sudo upgradepkg --verbose [path/to/package.tgz]```

# SYNOPSIS

**upgradepkg** [_OPTIONS_] _PACKAGE_...

# PARAMETERS

**--install-new**
> 如果软件包尚未安装则安装它

**--reinstall**
> 即使相同版本已存在也重新安装

**--dry-run**
> 预览操作而不实际更改

**--verbose**
> 显示详细进度

# DESCRIPTION

**upgradepkg** 通过用新版本替换已有软件包来升级 Slackware 软件包。它会移除旧软件包并安装新软件包，同时尽可能保留原有配置。

属于 Slackware pkgtools 软件包管理系统的一部分。

# CAVEATS

Slackware 特有。需要 root 权限。不处理依赖关系。旧软件包会在新软件包安装之前先被移除。

# SEE ALSO

[installpkg](/man/installpkg)(8), [removepkg](/man/removepkg)(8), [makepkg](/man/makepkg)(8), [pkgtool](/man/pkgtool)(8)
