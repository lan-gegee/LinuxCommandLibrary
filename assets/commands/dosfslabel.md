# TAGLINE

显示或设置 FAT 文件系统的卷标

# TLDR

**显示** FAT 文件系统的卷标

```dosfslabel [/dev/sdXN]```

**为 FAT 文件系统设置新卷标**

```dosfslabel [/dev/sdXN] "[NEW_LABEL]"```

**移除卷标**

```dosfslabel -r [/dev/sdXN]```

**显示卷 ID**而非卷标

```dosfslabel -i [/dev/sdXN]```

**设置新的卷 ID**（十六进制）

```dosfslabel -i [/dev/sdXN] [12345678]```

**使用指定代码页**进行编码

```dosfslabel -c [437] [/dev/sdXN] "[LABEL]"```

# SYNOPSIS

**dosfslabel** [_OPTIONS_] _DEVICE_ [_NEW_]

# PARAMETERS

**-i**, **--volume-id**
> 切换到卷 ID 模式而非卷标模式。

**-r**, **--reset**
> 在卷标模式下移除卷标，或在卷 ID 模式下生成新的随机 ID。

**-c** _PAGE_, **--codepage**=_PAGE_
> 使用 DOS 代码页 PAGE 来编码/解码卷标（默认：850）。

**-h**, **--help**
> 显示帮助信息并退出。

**-V**, **--version**
> 显示版本号并退出。

# DESCRIPTION

**dosfslabel** 显示或更改 MS-DOS FAT 文件系统（FAT12、FAT16、FAT32）上的卷标或卷 ID。它是指向 dosfstools 软件包中 **fatlabel** 的兼容性符号链接。

如果省略 NEW，当前卷标或卷 ID 将打印到标准输出。卷标不能超过 11 个字符，为了最佳兼容性应使用大写字母。不允许空字符串或纯空白卷标。卷 ID 以十六进制数表示（不带 0x 前缀），且须能放入 32 位。

由于历史原因，FAT 卷标存储在两个位置：引导扇区和根目录中的一个特殊条目。现代 Windows 系统从根目录读取卷标。自 4.2 版本起，dosfslabel 从根目录读取，但会同时写入两个位置。

# CAVEATS

更改卷标前应卸载文件系统，以免产生不一致。卷标限制为 11 个字符。不建议使用 3.0.16 之前的 dosfslabel，因为存在缺陷。如果不指定正确的代码页，某些特殊字符可能无法正确编码。

# HISTORY

dosfslabel 是 **dosfstools** 软件包的一部分，该包为 Linux 提供 MS-DOS FAT 文件系统工具。其中包括创建文件系统的 mkfs.fat、检查修复的 fsck.fat，以及管理卷标的 fatlabel。这些工具自 Linux 早期就一直得到维护，以确保与 DOS/Windows 文件系统的兼容性。

# INSTALL

```apt: sudo apt install dosfstools```

```dnf: sudo dnf install dosfstools```

```pacman: sudo pacman -S dosfstools```

```apk: sudo apk add dosfstools```

```zypper: sudo zypper install dosfstools```

```brew: brew install dosfstools```

```nix: nix profile install nixpkgs#dosfstools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fatlabel](/man/fatlabel)(8), [mkfs.fat](/man/mkfs.fat)(8), [e2label](/man/e2label)(8)
