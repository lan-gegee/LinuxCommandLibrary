# TAGLINE

输出文件的末尾部分

# TLDR

显示文件的**最后 10 行**

```tail [file]```

**显示最后 N 行**

```tail -n [20] [file]```

**显示从第 N 行开始的全部内容**

```tail -n +[10] [file]```

**跟踪文件**（监视新内容）

```tail -f [file]```

**跟踪多个文件**

```tail -f [file1] [file2]```

文件被重建时继续**跟踪并重试**

```tail -F [file]```

**显示最后 N 字节**

```tail -c [100] [file]```

# SYNOPSIS

**tail** [_options_] [_file_...]

# PARAMETERS

**-n** _N_, **--lines**=_N_
> 输出最后 N 行（+N 表示从第 N 行开始）

**-c** _N_, **--bytes**=_N_
> 输出最后 N 字节（+N 表示从第 N 字节开始）

**-f**, **--follow**
> 随文件增长输出新追加的数据

**-F**
> 等价于 --follow=name --retry

**--retry**
> 文件不可访问时持续尝试打开

**-s** _N_, **--sleep-interval**=_N_
> 配合 -f 时每次迭代之间休眠 N 秒

**--pid**=_PID_
> 与 -f 同用时，进程 PID 结束后即终止

**-q**, **--quiet**
> 从不输出带文件名的头部

**-v**, **--verbose**
> 总是输出带文件名的头部

# DESCRIPTION

**tail** 输出文件的末尾部分。默认显示最后 10 行。它常用于查看日志文件和实时监控文件变化。

**-f**（follow）选项在监控日志文件时特别有用。当新行被追加时，tail 会继续读取并立即显示。

使用 **-n +N** 会从第 N 行开始输出，而不是输出最后 N 行。这可用于跳过表头，或与 head 组合来提取特定范围的内容。

可以指定多个文件；tail 会显示标明输出来自哪个文件的头部。

# CAVEATS

**-f** 跟踪的是文件描述符。如果文件被删除又重建（日志轮转时很常见），请改用按名称跟踪并自动重试的 **-F**。

对于大文件，tail 非常高效——它会直接定位到接近文件末尾的位置，而不是读取整个文件。

-n 和 -c 的 **+** 语法从开头计数（行为 1 起始，字节为 0 起始）。**tail -n +1** 会输出整个文件。

# HISTORY

**tail** 起源于 **AT&T Unix** 第 1 版（1971 年）。它是 POSIX 的组成部分，在 Linux 上由 GNU coreutils 提供。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[head](/man/head)(1), [less](/man/less)(1), [cat](/man/cat)(1), [multitail](/man/multitail)(1)
