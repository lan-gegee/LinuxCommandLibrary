# TAGLINE

移除 Void Linux 软件包

# TLDR

**移除**一个软件包

```xbps-remove [package]```

**移除**软件包及其依赖

```xbps-remove -R [package]```

**移除**孤立软件包

```xbps-remove -o```

**从缓存中移除**过时的软件包

```xbps-remove -O```

# SYNOPSIS

**xbps-remove** [_options_] [_package_...]

# PARAMETERS

**-R, --recursive**
> 移除软件包及其依赖

**-o, --remove-orphans**
> 移除孤立软件包（不再使用的依赖）

**-O, --clean-cache**
> 从缓存中移除过时的软件包

**-y, --yes**
> 对所有提问自动回答 yes

**-n, --dry-run**
> 显示将要执行的操作

**-f, --force**
> 强制移除

**-v, --verbose**
> 详细输出

# DESCRIPTION

**xbps-remove** 从 Void Linux 系统中移除软件包。它可以移除单个软件包、递归移除软件包及其依赖，以及清理孤立软件包。

**-o** 选项适用于移除那些作为依赖安装、但已不再被任何已安装软件包需要的软件包。

# CAVEATS

需要 root 权限。使用 **-R** 时要小心，因为它可能会移除你想保留的软件包。定期运行 **-o** 有助于保持系统整洁。属于 Void Linux 的 XBPS 包管理系统的一部分。

# INSTALL

```apk: sudo apk add xbps```

```nix: nix profile install nixpkgs#xbps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xbps-install](/man/xbps-install)(1), [xbps-query](/man/xbps-query)(1)
