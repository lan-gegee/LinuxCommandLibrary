# TAGLINE

在 MS-DOS FAT 和 VFAT 文件系统上添加、显示或移除卷标

# TLDR

在 FAT/VFAT 文件系统上**设置卷标**

```mlabel -i [/dev/sda] ::"[new_label]"```

**显示当前卷标**

```mlabel -s -i [/dev/sda] ::```

**清除**已有的卷标

```mlabel -c -i [/dev/sda] ::```

设置**新的随机序列号**

```mlabel -n -i [/dev/sda] ::```

设置**指定的序列号**（8 位十六进制数字）

```mlabel -N [12345678] -i [/dev/sda] ::```

# SYNOPSIS

**mlabel** [**-v**] [**-c**] [**-s**] [**-n**] [**-N** _serial_] _drive:_[_new_label_]

# PARAMETERS

**-c**
> 清除已有卷标且不提示

**-s**
> 显示已有卷标且不提示

**-n**
> 为磁盘分配新的随机序列号

**-N _serial_**
> 设置指定的序列号；8 位十六进制，不含空格

**-v**
> 详细模式；卷标有更改时显示新卷标

**-i _device_**
> 直接指定设备而不使用驱动器字母

# DESCRIPTION

**mlabel** 在 MS-DOS FAT 和 VFAT 文件系统上添加、显示或移除卷标。不带选项调用时，它会显示当前卷标并提示输入新卷标。

卷标限制为 11 个单字节字符。该工具会验证并调整卷标以确保 MS-DOS 兼容性。输入空卷标（在提示处直接按回车）会删除已有卷标。

mlabel 属于 **mtools** 软件包，该软件包提供无需挂载即可从 Unix/Linux 访问 MS-DOS 文件系统的工具。

# CAVEATS

卷标限制为 11 个字符且必须是有效的 MS-DOS 格式。无效字符会被自动修正。序列号存储在引导扇区中，Windows 用它来识别卷。

# HISTORY

**mlabel** 属于 **mtools**，最初由 Emmet P. Gray 于 20 世纪 80 年代末开发。Mtools 为 Unix 系统提供 MS-DOS 文件系统工具，无需挂载即可访问 FAT 文件系统。

# INSTALL

```apt: sudo apt install mtools```

```dnf: sudo dnf install mtools```

```pacman: sudo pacman -S mtools```

```apk: sudo apk add mtools```

```zypper: sudo zypper install mtools```

```brew: brew install mtools```

```nix: nix profile install nixpkgs#mtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fatlabel](/man/fatlabel)(8)
