# TAGLINE

显示包括共享内存在内的 System V IPC 设施信息

# TLDR

显示**所有 IPC** 设施

```lsipc```

显示**共享内存**段

```lsipc --shmems```

显示**消息队列**

```lsipc --queues```

显示**信号量**集合

```lsipc --semaphores```

显示**特定 ID** 的详情

```lsipc --shmems --id [resource_id]```

以 **JSON** 输出

```lsipc --json```

# SYNOPSIS

**lsipc** [_options_]

# DESCRIPTION

**lsipc** 显示 System V IPC（进程间通信）设施的信息，包括系统当前活跃的共享内存段、消息队列和信号量集合。

# PARAMETERS

**--shmems, -m**
> 显示共享内存段

**--queues, -q**
> 显示消息队列

**--semaphores, -s**
> 显示信号量集合

**-i, --id ID**
> 显示特定资源 ID 的详情

**-o, --output COLUMNS**
> 选择输出的列

**-J, --json**
> JSON 输出格式

**-r, --raw**
> 原始输出，无格式化

**--notruncate**
> 不截断输出

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

[ipcs](/man/ipcs)(1), [ipcrm](/man/ipcrm)(1), [ipcmk](/man/ipcmk)(1)
