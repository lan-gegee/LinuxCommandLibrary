# TAGLINE

基于终端的十六进制编辑器，可在字节级别查看和编辑二进制文件

# TLDR

在十六进制编辑器中**打开文件**

```hexedit [path/to/file]```

**以只读模式打开**

```hexedit -r [path/to/file]```

**以指定扇区大小打开**（用于磁盘）

```hexedit -s [512] [/dev/sda]```

**打开时不显示 ASCII 列**

```hexedit --nocolor [path/to/file]```

# SYNOPSIS

**hexedit** [_-s sectorsize_] [_-r_] [_-h_] [_file_]

# PARAMETERS

**-s**, **--sector** _size_
> 设置磁盘编辑的扇区大小（默认：512）。

**-r**, **--readonly**
> 以只读模式打开文件。

**-h**, **--help**
> 显示帮助信息。

**--nocolor**
> 禁用彩色输出。

# KEYBOARD COMMANDS

**方向键**
> 在文件中导航。

**Page Up/Down**
> 向上/向下翻一页。

**Home/End**
> 跳到文件的开头/结尾。

**Tab**
> 在十六进制和 ASCII 编辑之间切换。

**Ctrl-G**
> 跳转到指定偏移量（十六进制或十进制）。

**Ctrl-S**
> 保存更改。

**Ctrl-X**
> 保存并退出。

**Ctrl-C**
> 不保存直接退出。

**Ctrl-F** 或 **/**
> 向前搜索（十六进制或 ASCII）。

**Ctrl-R**
> 向后搜索。

**Ctrl-Space**
> 设置标记。

**Ctrl-Y**
> 粘贴（用复制的字节填充）。

**Ctrl-U**
> 撤销所有更改。

**F2**
> 保存。

**F3**
> 查看已修改的字节。

# DESCRIPTION

**hexedit** 是一个基于终端的十六进制编辑器，用于在字节级别查看和编辑二进制文件。它以十六进制并辅以 ASCII 表示来显示文件内容，允许直接修改单个字节。

界面显示三列：左侧是字节偏移量，中间是十六进制值，右侧是 ASCII 字符。按 Tab 可在编辑十六进制值和编辑 ASCII 字符之间切换。被修改的字节会高亮显示。

无论小文件还是大型二进制文件（甚至块设备），导航都很高效。Ctrl-G 命令接受十六进制（加 0x 前缀）或十进制的偏移量。搜索同时支持十六进制模式和 ASCII 字符串。

对于磁盘编辑，扇区大小选项（-s）会影响编辑器的读写方式。修改块设备需要相应权限，且须格外谨慎。

hexedit 采用简单的内存模型——更改保存在内存中，直到显式保存为止。Ctrl-U 命令可撤销所有未保存的更改。对大文件，它会使用内存映射以实现高效访问。

# CAVEATS

编辑块设备或系统文件需要 root 权限。没有撤销历史——只能撤销全部更改。仅限于能放入虚拟内存（或可内存映射）的文件。不能插入或删除字节，只能覆盖。搜索的模式必须连续。

# HISTORY

**hexedit** 由 Pixel（Pascal Rigaux）编写，发布于 20 世纪 90 年代。它满足了 Unix 终端上一个简单、快速的十六进制编辑器的需求。尽管年代久远，它仍因其简单、低资源占用以及几乎在所有 Linux 发行版软件仓库中都可用而广受欢迎。

# INSTALL

```apt: sudo apt install hexedit```

```dnf: sudo dnf install hexedit```

```pacman: sudo pacman -S hexedit```

```zypper: sudo zypper install hexedit```

```brew: brew install hexedit```

```nix: nix profile install nixpkgs#hexedit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xxd](/man/xxd)(1), [hexdump](/man/hexdump)(1), [od](/man/od)(1), [dd](/man/dd)(1)
