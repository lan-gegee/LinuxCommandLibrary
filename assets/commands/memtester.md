# TAGLINE

用于压力测试内存子系统的用户空间工具

# TLDR

**测试 1GB 内存**

```sudo memtester [1G] [1]```

**以 5 次迭代测试 512MB**

```sudo memtester [512M] [5]```

**从物理地址开始测试内存**

```sudo memtester -p [0x10000000] [256M] [1]```

**无限循环测试**直到手动中断

```sudo memtester [1G] [0]```

**测试 2GB 内存**以进行全面检查

```sudo memtester [2G] [3]```

# SYNOPSIS

**memtester** [**-p** _PHYSADDR_] _MEMORY_ [_ITERATIONS_]

# PARAMETERS

_MEMORY_
> 要测试的内存量（例如 100K、256M、1G）。

_ITERATIONS_
> 测试循环次数。设为 0 表示无限测试。

**-p** _PHYSADDR_
> 从物理地址 PHYSADDR 开始测试内存。

# DESCRIPTION

**memtester** 是一个用于压力测试内存子系统的用户空间工具。它会分配指定数量的内存并运行一系列模式测试来检测 RAM 故障，包括地址位粘连、耦合故障和位翻转等。

测试项目包括：stuck address（地址粘连）、random value（随机值）、compare XOR、compare SUB、compare MUL、compare DIV、compare OR、compare AND、sequential increment（顺序递增）、solid bits（固定位）、block sequential（块顺序）、checkerboard（棋盘）、bit spread（位扩散）、bit flip（位翻转）、walking ones（走 1）、walking zeroes（走 0）。

memtester 在用户空间运行并测试虚拟内存。要测试特定地址的物理 RAM（例如确认硬件故障），请配合物理地址使用 **-p** 选项。

# CAVEATS

锁定内存页并防止换出通常需要 root 权限。测试使用的内存不能超过可用量；如果内存耗尽，内核可能会终止进程。memtester 从用户空间测试内存，可能无法发现 memtest86+ 这类内核级工具能检测到的所有硬件故障。

# HISTORY

memtester 由 Charles Cazabon 编写，作为开机内存测试工具的用户空间替代方案。它无需重启即可测试内存，并且可以针对特定内存区域，适合诊断运行中系统的间歇性故障。

# INSTALL

```apt: sudo apt install memtester```

```dnf: sudo dnf install memtester```

```pacman: sudo pacman -S memtester```

```apk: sudo apk add memtester```

```brew: brew install memtester```

```nix: nix profile install nixpkgs#memtester```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[free](/man/free)(1), [vmstat](/man/vmstat)(8), [stress](/man/stress)(1)
