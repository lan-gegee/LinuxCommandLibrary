# TAGLINE

SELinux 强制模式检查工具

# TLDR

输出 SELinux 模式：**Enforcing**、**Permissive** 或 **Disabled**

```getenforce```

# SYNOPSIS

**getenforce**

# DESCRIPTION

**getenforce** 显示 SELinux（Security-Enhanced Linux）的当前模式。该命令输出三个可能的值之一：

**Enforcing** - SELinux 安全策略处于强制状态。违反访问规则的行为会被阻止并记录日志。

**Permissive** - SELinux 安全策略不强制执行，但违规行为会被记录。适用于故障排查和策略开发。

**Disabled** - SELinux 完全禁用。

这是快速检查 SELinux 状态的方式，无需解析配置文件或使用 **sestatus** 这类更冗长的工具。

# CAVEATS

如果 SELinux 未编译进内核或在启动时被禁用，则返回 "Disabled"。运行时可用 **setenforce** 更改模式（只能在 Enforcing 和 Permissive 之间切换），但切换到或离开 Disabled 需要重启系统。

# HISTORY

getenforce 属于 SELinux 项目。该项目由美国国家安全局（NSA）开发，于 **2000 年**开源发布，在 **2003 年**被集成进 Linux 内核 2.6 版本，并成为 Red Hat Enterprise Linux 和 Fedora 的默认安全模块。

# INSTALL

```apt: sudo apt install selinux-utils```

```dnf: sudo dnf install libselinux-utils```

```apk: sudo apk add libselinux-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setenforce](/man/setenforce)(1), [sestatus](/man/sestatus)(8)
