# TAGLINE

以格式化表格显示文件系统信息

# TLDR

获取磁盘的**标准概览**

```dysk```

**按剩余空间排序**

```dysk -s free```

只包含 **HDD** 磁盘

```dysk -f 'disk = HDD'```

**排除** SSD 磁盘

```dysk -f 'disk <> SSD'```

显示**利用率高或剩余空间少**的磁盘

```dysk -f 'use > 65% | free < 50G'```

# SYNOPSIS

**dysk** [_options_]

# DESCRIPTION

**dysk** 以格式化表格显示文件系统信息。它以彩色输出展示挂载点、磁盘类型、容量、使用情况和文件系统类型。

提供筛选和排序功能，便于聚焦分析。

# PARAMETERS

**-a, --all**
> 显示所有挂载点，包括伪文件系统、可移动和远程文件系统

**-s, --sort** _field_
> 按字段排序（free、size、used、filesystem 等）

**-f, --filter** _expr_
> 过滤表达式

**-c, --csv**
> 以 CSV 输出

**-j, --json**
> 以 JSON 输出

**--cols** _cols_
> 选择要显示哪些列

**-l, --list-cols**
> 列出可用列

**--units** _si|binary_
> 容量单位：SI（1M = 1,000,000 B）或二进制（1M = 1,048,576 B）

**--color** _auto|yes|no_
> 控制彩色输出

# FILTER EXPRESSIONS

**disk = HDD**
> 仅 HDD

**disk = SSD**
> 仅 SSD

**use > 65%**
> 使用率超过 65%

**free < 50G**
> 剩余空间少于 50 GB

# CAVEATS

仅支持 Linux：dysk 读取 /proc/mounts 和 sysfs，因此无法在 macOS 或 BSD 上运行。磁盘类型检测（SSD 还是 HDD）取决于内核暴露的信息，对于虚拟或远程文件系统可能为空。该项目此前名为 **lfs**。

# INSTALL

```apt: sudo apt install dysk```

```pacman: sudo pacman -S dysk```

```apk: sudo apk add dysk```

```zypper: sudo zypper install dysk```

```brew: brew install dysk```

```nix: nix profile install nixpkgs#dysk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[df](/man/df)(1), [lsblk](/man/lsblk)(8), [duf](/man/duf)(1)

# RESOURCES

```[Source code](https://github.com/Canop/dysk)```

```[Homepage](https://dystroy.org/dysk/)```

<!-- verified: 2026-07-14 -->
