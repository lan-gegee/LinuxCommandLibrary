# TAGLINE

启用 shadow 密码存储

# TLDR

**转换为 shadow 密码**

```pwconv```

以详细输出方式**转换**

```pwconv -R [/]```

# SYNOPSIS

**pwconv** [_options_]

# PARAMETERS

**-R** _ROOT_
> chroot 目录。

# DESCRIPTION

**pwconv** 根据 **/etc/passwd** 创建或更新 **/etc/shadow** 文件，将密码哈希从所有用户可读的 passwd 文件迁移到仅 root 可读的 shadow 文件。这是一项基础安全措施，可防止非特权用户获取密码哈希进行离线破解。

该命令是 **shadow-utils** 的一部分，通常在系统初始设置时运行一次，或在将旧式系统转换为 shadow 密码时使用。它会保留现有的 shadow 条目，只在需要时添加或更新条目。

# CAVEATS

需要 root 权限。一次性迁移。属于系统管理操作。

# HISTORY

pwconv 是用于 shadow 密码迁移的 **shadow-utils** 工具。

# INSTALL

```apt: sudo apt install passwd```

```apk: sudo apk add shadow-conv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwunconv](/man/pwunconv)(8), [grpconv](/man/grpconv)(8)
