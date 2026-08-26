# TAGLINE

转换为影子组格式

# TLDR

**转换为影子组**

```sudo grpconv```

**先检查当前状态**

```ls -la /etc/gshadow```

# SYNOPSIS

**grpconv** [_options_]

# PARAMETERS

**-R** _DIR_
> chroot 目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grpconv** 将传统组格式转换为影子组格式。它根据 /etc/group 中的信息创建 /etc/gshadow。

该工具把加密的组密码从 /etc/group 移到 /etc/gshadow，通过限制对密码数据的访问来提升安全性。

# CAVEATS

需要 root 权限。请先运行 grpck 验证完整性。没有备份时操作不可逆。

# HISTORY

grpconv 作为 **shadow** 密码工具套件的一部分开发，用于提升组密码的安全性。

# INSTALL

```apt: sudo apt install passwd```

```apk: sudo apk add shadow-conv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grpunconv](/man/grpunconv)(8), [grpck](/man/grpck)(8), [pwconv](/man/pwconv)(8)

# RESOURCES

```[Source code](https://github.com/shadow-maint/shadow)```

<!-- verified: 2026-07-17 -->
