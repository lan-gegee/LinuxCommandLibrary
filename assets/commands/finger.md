# TAGLINE

显示用户信息和状态

# TLDR

**查找本地**用户

```finger [username]```

**查找远程**用户

```finger [username]@[host]```

**列出所有已登录的用户**

```finger```

**长格式输出**

```finger -l [username]```

**短格式输出**

```finger -s [username]```

# SYNOPSIS

**finger** [_options_] [_user_...] [_user@host_...]

# PARAMETERS

_USER_
> 要查询的用户名。

_USER@HOST_
> 查询远程主机上的用户。

**-l**
> 长格式输出。

**-s**
> 短格式输出。

**-m**
> 只匹配完全相同的用户名。

**-p**
> 忽略 .plan 和 .project 文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**finger** 显示系统用户的信息，包括姓名、终端、登录时间和联系方式。它的数据来自系统数据库和用户主目录。

用户可以用自己主目录下的 .plan 和 .project 文件来定制 finger 的显示内容。远程 finger 查询会联系目标主机端口 79 上的 finger 守护进程。

finger 曾是多用户系统和早期互联网上查询联系人信息的常用方式。

# CAVEATS

出于隐私考虑，大多数系统已经禁用了它。远程 finger 通常会被封锁。泄露用户信息可能构成安全风险。

# HISTORY

finger 于 1971 年诞生于**斯坦福大学**，随后成为标准的 Unix 工具。它曾一度无处不在地用于用户查询，如今因隐私与安全问题已基本弃用。

# INSTALL

```apt: sudo apt install finger```

```dnf: sudo dnf install finger```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[who](/man/who)(1), [w](/man/w)(1), [pinky](/man/pinky)(1)
