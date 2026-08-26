# TAGLINE

列出并查看 PolicyKit 授权操作

# TLDR

**列出所有操作**

```pkaction```

**显示操作详情**

```pkaction --verbose --action-id [org.freedesktop.login1.reboot]```

**列出匹配模式的操作**

```pkaction | grep [pattern]```

**以详细模式显示操作**

```pkaction -v -a [action.id]```

# SYNOPSIS

**pkaction** [_options_]

# PARAMETERS

**--action-id**, **-a** _id_
> 显示特定操作。

**--verbose**, **-v**
> 详细输出。

**--help**
> 显示帮助。

**--version**
> 显示版本。

# DESCRIPTION

**pkaction** 列出并显示系统上注册的 PolicyKit（polkit）授权操作。每个操作代表一个特权操作，如重启系统、挂载磁盘或安装软件包，并附带针对不同会话类型的身份验证要求。

在详细模式下，它会显示每个操作的描述、供应商以及隐式授权级别。这些级别决定了对于活动、非活动以及任意用户的会话，某项操作是被允许、被拒绝还是需要身份验证。

该工具便于系统管理员了解有哪些特权操作可用及其配置方式，也可用于验证自定义 polkit 规则是否已正确安装。

# EXAMPLES

```bash
# List all actions
pkaction

# Show reboot action details
pkaction -v -a org.freedesktop.login1.reboot

# Find package manager actions
pkaction | grep -i package

# Show details for all actions
pkaction --verbose
```

# OUTPUT

```
$ pkaction -v -a org.freedesktop.login1.reboot
org.freedesktop.login1.reboot:
  description:       Reboot the system
  message:           Authentication is required to reboot
  vendor:            The systemd Project
  implicit any:      auth_admin_keep
  implicit inactive: auth_admin_keep
  implicit active:   yes
```

# CAVEATS

需要 PolicyKit。操作定义于 /usr/share/polkit-1/actions/。修改策略需要 pkexec 或 root 权限。

# HISTORY

pkaction 是 **PolicyKit**（polkit）的一部分，后者是由 **Red Hat** 开发的细粒度访问控制授权框架。

# INSTALL

```apt: sudo apt install polkitd```

```apk: sudo apk add polkit-common```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pkexec](/man/pkexec)(1), [pkcheck](/man/pkcheck)(1), [polkit](/man/polkit)(8)
