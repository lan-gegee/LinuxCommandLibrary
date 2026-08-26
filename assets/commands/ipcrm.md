# TAGLINE

删除 System V IPC 资源

# TLDR

按 **ID** 删除共享内存段

```ipcrm -m [shmem_id]```

按**键**删除共享内存段

```ipcrm -M [shmem_key]```

按 **ID** 删除消息队列

```ipcrm -q [queue_id]```

按**键**删除消息队列

```ipcrm -Q [queue_key]```

按 **ID** 删除信号量

```ipcrm -s [semaphore_id]```

按**键**删除信号量

```ipcrm -S [semaphore_key]```

删除**所有** IPC 资源

```ipcrm -a```

# SYNOPSIS

**ipcrm** [_options_]

# PARAMETERS

**-m**, **--shmem-id** _ID_
> 按 ID 删除共享内存段

**-M**, **--shmem-key** _KEY_
> 按键删除共享内存段

**-q**, **--queue-id** _ID_
> 按 ID 删除消息队列

**-Q**, **--queue-key** _KEY_
> 按键删除消息队列

**-s**, **--semaphore-id** _ID_
> 按 ID 删除信号量集

**-S**, **--semaphore-key** _KEY_
> 按键删除信号量集

**-a**, **--all**
> 删除所有 IPC 资源

# DESCRIPTION

**ipcrm** 删除 System V IPC 资源（共享内存段、消息队列和信号量）。资源可通过其数字 ID 或键值来标识。

删除之前请先用 ipcs 列出现有资源及其 ID/键。不再需要的资源应及时删除以释放系统资源。

# CAVEATS

在进程仍在使用资源时将其删除，可能导致这些进程失败。需要适当的权限（所有者或 root）。-a 选项会删除所有可访问的资源。

# HISTORY

自 **1980 年代**初 System V IPC 引入以来，ipcrm 就一直是 Unix 系统的一部分。它为生命周期超出进程的 IPC 资源提供必要的清理功能。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ipcs](/man/ipcs)(1), [ipcmk](/man/ipcmk)(1), [lsipc](/man/lsipc)(1)
