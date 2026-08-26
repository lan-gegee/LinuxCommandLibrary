# TAGLINE

从影子组格式恢复为传统格式

# TLDR

**从影子组转换回来**

```sudo grpunconv```

**之后验证状态**

```ls -la /etc/gshadow```

# SYNOPSIS

**grpunconv** [_options_]

# PARAMETERS

**-R** _DIR_
> chroot 目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grpunconv** 将影子组格式转换回传统格式。它把密码信息从 /etc/gshadow 移回 /etc/group 并删除 /etc/gshadow。

该工具执行 grpconv 的逆操作，恢复到传统的组密码存储方式。现代系统上很少需要这样做。

# CAVEATS

需要 root 权限。会降低安全性。现代系统上很少用到。

# HISTORY

grpunconv 作为 **shadow** 密码工具套件的一部分开发，用于撤销影子组的相关更改。

# INSTALL

```apt: sudo apt install passwd```

```apk: sudo apk add shadow-conv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grpconv](/man/grpconv)(8), [grpck](/man/grpck)(8), [pwunconv](/man/pwunconv)(8)

# RESOURCES

```[Source code](https://github.com/shadow-maint/shadow)```

<!-- verified: 2026-07-17 -->
