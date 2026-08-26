# TAGLINE

卸载所有 AppArmor 配置文件并停止强制执行

# TLDR

**禁用**所有 AppArmor 配置文件并停止强制执行

```sudo aa-teardown```

# SYNOPSIS

**aa-teardown**

# DESCRIPTION

**aa-teardown** 会拆除所有 AppArmor 配置文件并禁用 AppArmor 强制执行。该命令从内核中卸载所有当前已加载的配置文件，实际上等于移除了所有受约束进程上的 AppArmor 安全限制。

它通常用于排查 AppArmor 配置文件引发的问题，或在系统上彻底停用 AppArmor。

# CAVEATS

运行此命令会移除系统上的**全部 AppArmor 安全保护**。在重新加载配置文件之前，应用将在没有任何 AppArmor 约束的情况下运行。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apt: sudo apt install apparmor```

```pacman: sudo pacman -S apparmor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-status](/man/aa-status)(8), [aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [apparmor](/man/apparmor)(7)
