# TAGLINE

释放未使用虚拟终端占用的内存

# TLDR

**释放所有未使用的虚拟终端**

```sudo deallocvt```

**释放指定的虚拟终端**

```sudo deallocvt [7]```

**释放一组虚拟终端**

```sudo deallocvt [7] [8] [9]```

**针对特定的控制台设备**

```sudo deallocvt -C [/dev/tty1]```

**显示版本信息**

```deallocvt -V```

# SYNOPSIS

**deallocvt** [_options_] [_N_...]

# PARAMETERS

_N_
> 要释放的虚拟终端编号。不带参数时，释放所有未使用的终端。

**-C**, **--console=**_DEV_
> 对指定的控制台设备操作（例如 `/dev/tty1`）。

**-V**, **--version**
> 打印版本信息并退出。

**-h**, **--help**
> 打印用法信息并退出。

# DESCRIPTION

**deallocvt** 释放未使用虚拟控制台的内核内存和数据结构。当虚拟控制台既不是活动控制台，也没有进程或文本选区引用它时，即被视为未使用。

不带参数调用时会释放所有未使用的虚拟终端。给定具体终端编号（对应 `/dev/ttyN`）时则只释放那些终端。当前终端或存在活动进程的终端无法被释放。

# CAVEATS

需要 root 权限。无法释放当前 VT 或有活动进程的 VT。释放后的 VT 下次被使用时会重新分配，带来少量开销。主要对内存受限的系统有用。

# HISTORY

**deallocvt** 属于 Linux 控制台实用程序集 **kbd** 软件包，最初由 **Andries Brouwer** 编写。它提供 Linux 虚拟终端资源的底层管理能力。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chvt](/man/chvt)(1), [fgconsole](/man/fgconsole)(1)
