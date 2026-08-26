# TAGLINE

VCDIFF 二进制差量编码

# TLDR

**创建差量文件**

```xdelta3 -e -s [old_file] [new_file] [patch.xd3]```

**应用补丁**

```xdelta3 -d -s [old_file] [patch.xd3] [new_file]```

**高压缩比**

```xdelta3 -9 -e -s [old_file] [new_file] [patch.xd3]```

**编码到 stdout（便于管道）**

```xdelta3 -e -c -s [old_file] [new_file] > [patch.xd3]```

**显示差量信息**

```xdelta3 printdelta [patch.xd3]```

**不依赖源文件解码**

```xdelta3 -d [patch.xd3] [output_file]```

# SYNOPSIS

**xdelta3** [_command_] [_options_] [_input_ [_output_]]

# COMMANDS

**encode**
> 压缩输入（默认）。也可用 **-e** 设置。

**decode**
> 解压输入。也可用 **-d** 设置。

**printdelta**
> 打印整个差量的信息。

**printhdr**
> 打印第一个窗口的信息。

**printhdrs**
> 打印所有窗口的信息。

**config**
> 打印 xdelta3 配置。

**recode**
> 用新的 application/secondary 设置重新编码。

# PARAMETERS

**-e**
> 编码（压缩/创建差量）。

**-d**
> 解码（解压/应用差量）。

**-s** _FILE_
> 作为拷贝来源的源文件。

**-0** 到 **-9**
> 压缩级别。

**-f**
> 强制覆盖已有文件。

**-c**
> 输出到 stdout。

**-v**
> 详细输出（最多可指定 2 次）。

**-q**
> 安静模式，抑制输出消息。

**-B** _bytes_
> 源窗口大小。

**-W** _bytes_
> 输入窗口大小。

**-S** [**djw**|**fgk**]
> 启用/禁用二级压缩。

**-n**
> 禁用校验和。

**-V**
> 显示版本。

# DESCRIPTION

**xdelta3** 使用 RFC 3284 定义的 VCDIFF 格式创建和应用二进制差量补丁。编码时将源文件与目标文件比较，生成仅记录差异的紧凑差量；解码时则通过将差量应用到原始源文件来重建目标文件。

0 到 9 的压缩级别以处理速度换取更小的差量体积。流式模式分块处理数据，可以高效处理超大文件的内存占用。还可以创建自包含的补丁，把必要的数据嵌入差量本身，解码时无需原始源文件。

# CAVEATS

除非创建差量时未使用源文件，否则解码时必须能访问源文件。处理非常大的文件时可能需要调整内存选项（**-B**、**-W**）。命令行语法与 gzip 类似。

# HISTORY

**xdelta3** 是 xdelta 的第三个版本，实现了 RFC 3284 VCDIFF。它提供高效的二进制差量压缩。

# INSTALL

```apt: sudo apt install xdelta3```

```pacman: sudo pacman -S xdelta3```

```apk: sudo apk add xdelta3```

```zypper: sudo zypper install xdelta3```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdelta](/man/xdelta)(1), [bsdiff](/man/bsdiff)(1), [diff](/man/diff)(1), [patch](/man/patch)(1), [gzip](/man/gzip)(1)
