# TAGLINE

挂起 Proxmox 虚拟机

# TLDR

按 ID **挂起**虚拟机

```qm suspend 100```

挂起时跳过**锁**检查

```qm suspend 100 --skiplock```

挂起时跳过**存储锁**检查

```qm suspend 100 --skiplockstorage```

# SYNOPSIS

**qm suspend** _vmid_ [_options_]

# PARAMETERS

**--skiplock**
> 挂起时跳过锁检查

**--skiplockstorage**
> 挂起时跳过存储锁检查

# DESCRIPTION

**qm suspend** 挂起 Proxmox VE 中运行中的虚拟机。虚拟机的状态被保存在内存中，之后可用 qm resume 恢复。

挂起只是暂停虚拟机执行，不会关闭客户机操作系统。

# CAVEATS

--skiplock 和 --skiplockstorage 在某些情况下可能导致数据损坏，请谨慎使用。挂起的虚拟机仍占用内存资源。

# HISTORY

属于 **Proxmox VE** 的 QEMU/KVM 管理工具，用于虚拟机管理。

# INSTALL

```dnf: sudo dnf install qm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[qm](/man/qm)(1), [qm-resume](/man/qm-resume)(1), [qm-shutdown](/man/qm-shutdown)(1)
