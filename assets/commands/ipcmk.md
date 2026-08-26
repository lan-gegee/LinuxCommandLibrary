# TAGLINE

创建 System V IPC 资源

# TLDR

创建**共享内存**段

```ipcmk -M [segment_size_in_bytes]```

创建**信号量**集

```ipcmk -S [element_size]```

创建**消息队列**

```ipcmk -Q```

以指定**权限**创建共享内存

```ipcmk -M [segment_size] -p [0644]```

# SYNOPSIS

**ipcmk** [_options_]

# PARAMETERS

**-M**, **--shmem** _SIZE_
> 创建指定字节数大小的共享内存段

**-S**, **--semaphore** _COUNT_
> 创建含指定元素数量的信号量集

**-Q**, **--queue**
> 创建消息队列

**-p**, **--mode** _MODE_
> 设置权限（八进制，默认 0644）

# DESCRIPTION

**ipcmk** 创建 System V IPC（进程间通信）资源。这些资源允许进程之间进行通信和同步：共享内存支持直接共享数据，信号量协调对资源的访问，消息队列支持异步消息传递。

创建的资源由键和 ID 标识，可用 ipcs 查看、用 ipcrm 删除。资源会一直存在，直到被显式删除或系统重启。

# CAVEATS

System V IPC 对资源的数量和大小有内核限制。创建这些资源的进程退出后，资源不会被自动清理。现代应用程序通常更倾向于使用 POSIX IPC 或其他机制。

# HISTORY

System V IPC 于 **1980 年代**初在 AT&T UNIX System V 中引入。虽然比 POSIX 替代方案更古老，但它在各类类 Unix 系统上仍被广泛使用和支持。

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

[ipcs](/man/ipcs)(1), [ipcrm](/man/ipcrm)(1), [lsipc](/man/lsipc)(1)
