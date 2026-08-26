# TAGLINE

创建并更新手册页索引缓存

# TLDR

**更新** man page 数据库

```mandb```

更新**单条记录**

```mandb --filename [path/to/file]```

**从头创建**数据库

```mandb --create```

仅处理**用户数据库**

```mandb --user-db```

**不清除**过期条目

```mandb --no-purge```

**测试** man page 的有效性

```mandb --test```

# SYNOPSIS

**mandb** [_options_] [_manpath_]

# DESCRIPTION

**mandb** 创建并更新手册页索引缓存。man 和 apropos 使用这些缓存来快速查找手册页。它会扫描手册页目录，并构建一个包含页面名称和描述的数据库。

# PARAMETERS

**--filename FILE**
> 更新单个文件的条目

**-c, --create**
> 从头创建数据库

**-u, --user-db**
> 仅处理用户数据库

**-p, --no-purge**
> 不清除过期条目

**-t, --test**
> 只测试有效性而不更新

**-q, --quiet**
> 抑制警告

**-d, --debug**
> 打印调试信息

# CAVEATS

通常由软件包管理器自动运行。更新系统级数据库可能需要 root 权限。

# INSTALL

```apt: sudo apt install man-db```

```dnf: sudo dnf install man-db```

```pacman: sudo pacman -S man-db```

```apk: sudo apk add man-db```

```brew: brew install man-db```

```nix: nix profile install nixpkgs#man-db```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [apropos](/man/apropos)(1), [whatis](/man/whatis)(1), [manpath](/man/manpath)(1)
