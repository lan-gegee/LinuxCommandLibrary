# TAGLINE

快速文件空间预分配工具

# TLDR

**分配**一个 700 MiB 的文件

```fallocate -l 700M path/to/file```

将文件**缩小** 200 MiB

```fallocate -c -l 200M path/to/file```

在指定**偏移处**缩小

```fallocate -c -o 100M -l 20M path/to/file```

# SYNOPSIS

**fallocate** [_OPTIONS_] _filename_

# DESCRIPTION

**fallocate** 为文件预分配或释放空间。与写入零不同，fallocate 使用文件系统特定的操作快速分配空间而不初始化数据，因此创建大文件非常快。

# PARAMETERS

**-l, --length** _size_
> 要分配或释放的范围长度

**-o, --offset** _offset_
> 范围相对文件开头的偏移量

**-c, --collapse-range**
> 从文件中移除一段范围且不留空洞

**-d, --dig-holes**
> 检测零块并将其转换为空洞

**-p, --punch-hole**
> 释放文件中的空间（创建空洞）

**-z, --zero-range**
> 将范围清零但保留已分配的空间

**-n, --keep-size**
> 扩展分配时保持表面上的文件大小不变

# CAVEATS

并非所有文件系统都支持所有操作。折叠操作需要文件系统支持（ext4 4.2+、XFS 4.15+）。不清零的空间分配意味着文件中可能包含磁盘上以前的数据。

# HISTORY

**fallocate** 是 Linux 特有的工具，使用内核 2.6.23 引入的 fallocate() 系统调用。

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

[truncate](/man/truncate)(1), [dd](/man/dd)(1), [fstrim](/man/fstrim)(8)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

```[Documentation](https://man7.org/linux/man-pages/man1/fallocate.1.html)```

<!-- verified: 2026-07-15 -->
