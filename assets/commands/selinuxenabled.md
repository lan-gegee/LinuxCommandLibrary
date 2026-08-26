# TAGLINE

检查系统是否启用了 SELinux

# TLDR

**检查** SELinux 是否启用（无输出）

```selinuxenabled```

检查并**打印结果**

```selinuxenabled && echo "SELinux is enabled" || echo "SELinux is disabled"```

在 **shell 脚本**中按条件使用

```if selinuxenabled; then echo "SELinux is running"; fi```

# SYNOPSIS

**selinuxenabled**

# DESCRIPTION

**selinuxenabled** 检查系统是否启用了 SELinux。它不产生任何输出，但如果 SELinux 已启用则返回退出码 0，若被禁用则返回 1。

这适用于需要根据 SELinux 状态有条件地执行命令的脚本。

# CAVEATS

仅检查 SELinux 是否启用，不检查它处于 enforcing 还是 permissive 模式。模式信息请使用 getenforce。

# HISTORY

属于 **libselinux-utils**，提供 SELinux 状态检查工具。

# INSTALL

```apt: sudo apt install selinux-utils```

```dnf: sudo dnf install libselinux-utils```

```apk: sudo apk add libselinux-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[getenforce](/man/getenforce)(1), [setenforce](/man/setenforce)(8), [sestatus](/man/sestatus)(8)
