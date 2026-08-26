# TAGLINE

向 Proxmox 虚拟机发送按键事件

# TLDR

向虚拟机**发送**按键事件

```qm sendkey [vmid] ctrl-alt-delete```

向虚拟机发送**单个按键**

```qm sendkey [vmid] ret```

发送按键事件时**忽略锁**（仅限 root）

```qm sendkey --skiplock [vmid] [key]```

# SYNOPSIS

**qm sendkey** [_options_] _vmid_ _key_

# PARAMETERS

_vmid_
> 唯一的 VM ID（100 到 999999999 之间的整数）。

_key_
> QEMU monitor 编码格式的按键名（如 `ctrl-alt-delete`、`ret`、`esc`、`f1`、`meta_l-r`）。

**--skiplock** _boolean_
> 忽略虚拟机锁并强制发送按键。需要 root 权限。

# DESCRIPTION

**qm sendkey** 向运行中的虚拟机发送 QEMU monitor 编码的按键事件。它可以直接把 `ctrl-alt-delete` 或功能键等键盘输入发送到虚拟机控制台，而无需图形界面访问。

按键名遵循 QEMU monitor 编码：字母数字字符直接书写，特殊键使用 `ret`、`esc`、`tab`、`spc`、`f1`–`f12`、`up`、`down`、`left`、`right` 之类的名称，修饰键组合用连字符连接（如 `ctrl-alt-delete`、`meta_l-r`）。

# CAVEATS

按键编码遵循 QEMU monitor 格式，而非标准按键名称。--skiplock 选项需要 root 权限。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-monitor](/man/qm-monitor)(1), [qm-start](/man/qm-start)(1), [qm-stop](/man/qm-stop)(1), [qm-terminal](/man/qm-terminal)(1)
