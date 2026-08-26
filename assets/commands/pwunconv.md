# TAGLINE

禁用 shadow 密码存储

# TLDR

**恢复为非 shadow 密码**

```pwunconv```

**指定根目录**

```pwunconv -R [/]```

# SYNOPSIS

**pwunconv** [_options_]

# PARAMETERS

**-R** _ROOT_
> chroot 目录。

# DESCRIPTION

**pwunconv** 撤销 shadow 密码设置：将密码哈希从 **/etc/shadow** 移回 **/etc/passwd** 并删除 shadow 文件。它是 **pwconv** 的逆操作，实际上会禁用系统上的 shadow 密码保护。

该命令是 **shadow-utils** 的一部分，实际中很少使用，因为 shadow 密码是现代 Linux 系统的基础安全特性。移除 shadow 保护会使密码哈希对所有用户可读，显著削弱系统安全性。

# CAVEATS

有安全风险。很少使用。需要 root 权限。

# HISTORY

pwunconv 是用于撤销 shadow 密码的 **shadow-utils** 工具。

# INSTALL

```apt: sudo apt install passwd```

```apk: sudo apk add shadow-conv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwconv](/man/pwconv)(1), [grpunconv](/man/grpunconv)(1), [passwd](/man/passwd)(1)
