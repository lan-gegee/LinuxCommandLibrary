# TAGLINE

显示磁盘使用量和配额限制

# TLDR

**显示用户配额**

```quota```

**显示特定用户的配额**

```quota -u [username]```

**显示组配额**

```quota -g [groupname]```

**详细输出**

```quota -v```

**显示所有文件系统**

```quota -A```

# SYNOPSIS

**quota** [_options_] [_user_]

# PARAMETERS

_USER_
> 要检查的用户。

**-u**
> 用户配额。

**-g**
> 组配额。

**-v**
> 详细输出。

**-s**
> 人类可读的大小。

**-A**
> 所有文件系统。

# DESCRIPTION

**quota** 显示启用了配额的文件系统上用户或组的当前磁盘使用量和限制。它读取内核的配额子系统，报告用户或组已消耗的空间和 inode 数量，以及配置的软限制和硬限制。

超出软限制后，工具会显示强制执行生效前的剩余宽限期。不带参数运行会显示调用用户在所有已挂载文件系统上的配额，而 **-u** 和 **-g** 标志可查询特定用户或组。**-v** 标志报告所有启用配额的文件系统，包括当前没有消耗空间的那些。

# CAVEATS

需要启用配额系统。文件系统需支持配额。

# HISTORY

quota 是 **Unix 配额**系统中用于磁盘用量限制的一部分。

# INSTALL

```apt: sudo apt install quota```

```dnf: sudo dnf install quota```

```pacman: sudo pacman -S quota-tools```

```apk: sudo apk add quota-tools```

```zypper: sudo zypper install quota```

```nix: nix profile install nixpkgs#quota```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[edquota](/man/edquota)(8), [repquota](/man/repquota)(8), [quotacheck](/man/quotacheck)(8)
