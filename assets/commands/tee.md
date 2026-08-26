# TAGLINE

从标准输入读取并同时写入标准输出和文件

# TLDR

**将 stdin 写入文件和 stdout**

```echo "text" | tee [file]```

**追加到文件**而不是覆盖

```echo "text" | tee -a [file]```

**写入多个文件**

```echo "text" | tee [file1] [file2]```

**在查看命令输出的同时**将其写入文件

```[command] | tee [output.log]```

**配合 sudo 使用**以写入受保护的文件

```echo "text" | sudo tee [/etc/file]```

**写入文件并管道**给另一个命令

```[command] | tee [file] | [another_command]```

**抑制 stdout**（只写入文件）

```[command] | tee [file] > /dev/null```

# SYNOPSIS

**tee** [_options_] [_file_...]

# PARAMETERS

**-a**, **--append**
> 追加到文件而非覆盖

**-i**, **--ignore-interrupts**
> 忽略 SIGINT（中断信号）

**-p**
> 以更适合与管道搭配的模式运行（默认 MODE 为 warn-nopipe）

**--output-error**[=_mode_]
> 设置写入出错时的行为（warn、warn-nopipe、exit、exit-nopipe）

**--help**
> 显示帮助并退出

**--version**
> 显示版本并退出

# DESCRIPTION

**tee** 从标准输入读取数据，同时写入标准输出和一个或多个文件。它的名字来自水管中的 T 形接头，作用是"分流"数据流。

常见用途包括：在查看命令输出的同时记录日志、保存管道中的中间结果以便调试，以及通过 sudo 写入需要提升权限的文件。

不带 **-a** 时，tee 会覆盖已存在的文件。指定多个文件时，相同的内容会写入所有文件。若某个 FILE 是 **-**，tee 会再次复制到标准输出。

tee 会让管道继续下去——输出同时进入文件和 stdout，因此可以继续用后续的管道阶段处理。

# CAVEATS

要用 sudo 写入受保护的文件时，应使用 **sudo tee** 而非 **sudo echo >**，因为重定向发生在当前 Shell 中、先于 sudo 执行。

在启用了 **set -o pipefail** 的管道中，tee 的失败可能被忽视。需要严格的错误处理时可使用 **--output-error=exit**。

与带输出缓冲的命令组合使用时，可能看不到即时结果。必要时可使用 **stdbuf** 或命令自带的去缓冲选项。

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

[cat](/man/cat)(1), [script](/man/script)(1), [pv](/man/pv)(1), [sponge](/man/sponge)(1)
