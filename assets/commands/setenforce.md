# TAGLINE

切换 SELinux 的 enforcing 与 permissive 模式

# TLDR

将 SELinux 置于 **enforcing 模式**

```setenforce 1```

将 SELinux 置于 **permissive 模式**

```setenforce 0```

# SYNOPSIS

**setenforce** [**0**|**1**|**Permissive**|**Enforcing**]

# PARAMETERS

**0, Permissive**
> 切换到 permissive 模式（记录违规但不强制执行）

**1, Enforcing**
> 切换到 enforcing 模式（记录并强制执行策略）

# DESCRIPTION

**setenforce** 在运行时切换 SELinux 的 enforcing 和 permissive 模式。在 **enforcing** 模式下，SELinux 会依据策略规则拒绝访问。在 **permissive** 模式下，违规行为只会被记录而不会被阻止。

此更改是临时的，重启后不会保留。要永久更改 SELinux 模式，请编辑 **/etc/selinux/config** 并设置 **SELINUX** 变量。

# CAVEATS

需要 root 权限。无法完全启用/禁用 SELinux；只能在 enforcing 和 permissive 之间切换。要查看当前模式，使用 **getenforce**。切换到 permissive 模式会降低系统安全性。

# HISTORY

**setenforce** 是由 NSA 和 Red Hat 开发的 SELinux 用户空间工具的一部分。自 Linux 2.6 内核引入 SELinux 起它就一直可用。

# INSTALL

```apt: sudo apt install selinux-utils```

```dnf: sudo dnf install libselinux-utils```

```apk: sudo apk add libselinux-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getenforce](/man/getenforce)(8), [semanage-permissive](/man/semanage-permissive)(8), [sestatus](/man/sestatus)(8)
