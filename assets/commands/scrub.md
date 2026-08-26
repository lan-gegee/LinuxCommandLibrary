# TAGLINE

安全覆写文件、块设备或磁盘空闲空间

# TLDR

使用默认模式安全**覆写文件**

```scrub [path/to/file]```

安全覆写**多个文件**

```scrub [path/to/file1] [path/to/file2]```

安全覆写**块设备**或分区

```sudo scrub [/dev/sdX]```

以**单次随机**模式覆写文件

```scrub -p random [path/to/file]```

使用 **DoD 5220.22-M** 模式覆写文件

```scrub -p dod [path/to/file]```

使用 **Gutmann** 模式覆写文件

```scrub -p gutmann [path/to/file]```

成功覆写后**删除**文件

```scrub -r [path/to/file]```

安全覆写目录下的**空闲空间**

```scrub -X [path/to/directory]```

# SYNOPSIS

**scrub** [_OPTIONS_] _special-file_ ...

**scrub** [_OPTIONS_] _file_ ...

**scrub** **-X** [_OPTIONS_] _directory_

# PARAMETERS

**-v**, **--version**
> 打印 scrub 版本并退出

**-r**, **--remove**
> 清除完成后删除文件

**-p**, **--pattern** _PATTERN_
> 选择覆写模式（默认为 **nnsa**）。参见下方的模式列表

**-b**, **--blocksize** _size_
> I/O 块大小（字节），允许 **K**/**M**/**G** 后缀。默认：4M

**-f**, **--force**
> 即使目标已带有 scrub 签名也进行清除

**-S**, **--no-signature**
> 完成后不写入 scrub 签名

**-X**, **--freespace**
> 填充 _directory_ 直到文件系统占满，然后清除这些文件

**-D**, **--dirent** _newname_
> 清除后覆写目录项名称并将其重命名为 _newname_

**-s**, **--device-size** _size_
> 覆盖检测到的设备大小（字节），允许 **K**/**M**/**G** 后缀

**-L**, **--no-link**
> 若目标是符号链接，则不清除链接指向的目标（若指定 **-r** 仍会删除）

**-R**, **--no-hwrand**
> 即使硬件随机数生成器可用也不使用

**-t**, **--no-threads**
> 不与 I/O 并行生成随机数据

**-n**, **--dry-run**
> 只执行检查和报告，不写入目标

**-h**, **--help**
> 打印选项摘要

# DESCRIPTION

**scrub** 通过在文件或磁盘设备上反复写入特定模式的数据，使数据恢复更加困难。它有三种工作模式：

1. **块设备/字符设备** — 清除整个设备（效果最好）。
2. **普通文件** — 仅覆写文件数据（以及可选的目录项名称）；大小会向上取整到最后一个文件系统块。
3. **空闲空间**（**-X**） — 在已有目录下创建文件直到文件系统占满，然后清除这些文件。

默认模式 **nnsa** 遵循 NNSA Policy Letter NAP-14.1-C（两次随机写入，再写入 0x00 并校验），对现代 PRML/EPRML 磁盘而言是合理的。其他标准还包括 **dod**、**bsi**、**gutmann**、**schneier**、**usarmy**、单次的 **random**/**fillzero**/**fillff**，以及 **custom=**_string_。

# PATTERNS

**nnsa** — 4 轮 NNSA：random(x2)、0x00、校验（默认）

**dod** — 4 轮 DoD 5220.22-M：random、0x00、0xff、校验

**bsi** — 9 轮德国 BSI 方法

**gutmann** — 35 轮 Gutmann 序列

**schneier** — 7 轮 Schneier：0x00、0xff、random(x5)

**pfitzner7** / **pfitzner33** — 7 或 33 轮随机写入

**usarmy** — 美国陆军 AR380-19：0x00、0xff、random

**fillzero** / **fillff** / **random** / **random2** — 短的固定值或随机轮次

**old** / **fastold** — 传统多轮序列

**custom=**_string_ — 单轮写入，支持 C 风格转义（\xnn、\nnn）

# CAVEATS

通过文件系统进行清除的效果受操作系统和文件系统类型限制。日志式、日志结构、写时复制、版本化及网络文件系统可能在别处保留旧数据；尽可能直接清除原始设备。

**scrub** 无法触及被磁盘控制器重映射/替换的块。对于 ATA 硬盘，通过 **hdparm** 执行固件安全擦除可能更彻底。物理销毁仍然是抵御实验室级数据恢复的唯一有力保障。

空闲空间清除（**-X**）只对文件系统重新分配给新文件的块有效。清除原始设备前务必核实设备大小——目标错误将不可逆地破坏数据。

# HISTORY

**scrub** 起源于劳伦斯利弗莫尔国家实验室（UCRL-CODE-2003-006），是一款实现已公开介质清理方法（NNSA、DoD、Gutmann 等）的 GPL 磁盘/文件覆写工具。

# INSTALL

```apt: sudo apt install scrub```

```dnf: sudo dnf install scrub```

```aur: yay -S scrub```

```zypper: sudo zypper install scrub```

```brew: brew install scrub```

```nix: nix profile install nixpkgs#scrub```

<!-- packages: 2026-07-29 -->

# SEE ALSO

[shred](/man/shred)(1), [wipe](/man/wipe)(1), [wipefs](/man/wipefs)(8), [hdparm](/man/hdparm)(8), [dd](/man/dd)(1)

# RESOURCES

```[Source code](https://github.com/chaos/scrub)```

```[Documentation](https://manned.org/scrub)```

<!-- verified: 2026-07-29 -->
