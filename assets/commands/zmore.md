# TAGLINE

使用 more 分页器查看压缩文件

# TLDR

**逐屏查看压缩文件**

```zmore [file.gz]```

**以指定的每屏行数查看**

```zmore -[20] [file.gz]```

**显示有用的提示**而不是对无效按键发出蜂鸣

```zmore -d [file.gz]```

**将多个空行压缩为一行**

```zmore -s [file.gz]```

**从模式的首次出现处开始**

```zmore +/[pattern] [file.gz]```

# SYNOPSIS

**zmore** [_-dfls_] [_+linenum_] [_+/pattern_] [_file ..._]

# PARAMETERS

**-_number_**
> 每屏显示的行数

**-d**
> 出错时显示有用的提示信息而不是响铃

**-f**
> 按逻辑行而不是屏幕行计数（不折叠长行）

**-l**
> 在换页符之后不暂停

**-s**
> 将连续的空行压缩为一行

**+_linenum_**
> 从指定行号开始

**+/_pattern_**
> 从模式首次匹配行的前两行开始

# DESCRIPTION

**zmore** 是一个分页器，用于逐屏查看压缩的文本文件。它支持用 gzip、compress 或 pack 压缩的文件，也能处理未压缩的文件。

如果文件不存在，zmore 会自动查找带 .gz、.z 或 .Z 扩展名的版本。该命令将解压功能与 more 分页器结合在一起，在每一屏的底部显示 --More--。

按空格键前进一屏，按 Enter 前进一行，或按 q 退出。当输出不是终端时，zmore 的行为如同 zcat，将内容解压到 stdout。

# CAVEATS

zmore 无法向后翻看文件；需要双向滚动请使用 **zless**。在 SSD 上反复查看压缩文件造成的磨损微乎其微，但解压文件则会带来磨损。可设置 PAGER 环境变量来改用 less 等其他分页器。

# HISTORY

zmore 于 20 世纪 90 年代初作为 **gzip** 软件包的一部分被创建，用于方便地查看压缩文件。它在传统 more 分页器的基础上增加了即时解压能力。

# INSTALL

```apt: sudo apt install gzip```

```dnf: sudo dnf install gzip```

```pacman: sudo pacman -S gzip```

```apk: sudo apk add gzip```

```zypper: sudo zypper install gzip```

```brew: brew install gzip```

```nix: nix profile install nixpkgs#gzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zless](/man/zless)(1), [zcat](/man/zcat)(1), [more](/man/more)(1), [gzip](/man/gzip)(1)
