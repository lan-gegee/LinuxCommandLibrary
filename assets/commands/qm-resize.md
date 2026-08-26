# TAGLINE

调整 Proxmox 虚拟机的磁盘卷大小

# TLDR

此命令是 **qm disk resize** 的别名

查看原始命令的文档

```tldr qm disk```

# SYNOPSIS

**qm resize** _vmid_ _disk_ _size_

# DESCRIPTION

**qm resize** 是 **qm disk resize** 的别名，用于更改虚拟机磁盘的大小。它可以扩大磁盘容量，但不能缩小磁盘。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-disk](/man/qm-disk)(1)
