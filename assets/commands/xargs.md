# TAGLINE

从 stdin 构建并执行命令

# TLDR

**使用来自 stdin 的参数运行命令**

```echo [file1 file2] | xargs rm```

**使用自定义分隔符**

```echo "[a:b:c]" | xargs -d ":" echo```

**配合占位符运行**

```find . -name "*.txt" | xargs -I {} cp {} [/backup/]```

**并行运行**

```find . -name "*.jpg" | xargs -P [4] -I {} convert {} {}.png```

**处理带空格的文件名**

```find . -name "*.txt" -print0 | xargs -0 rm```

**限制每条命令的参数数量**

```echo {1..100} | xargs -n [10] echo```

**执行前提示确认**

```find . -name "*.tmp" | xargs -p rm```

**输入为空时跳过执行**（GNU 扩展）

```echo "" | xargs -r echo "not empty"```

# SYNOPSIS

**xargs** [_-I replace_] [_-n max-args_] [_-P max-procs_] [_-0_] [_-d delim_] [_command_]

# PARAMETERS

**-I** _REPLACE_
> 替换命令中的字符串。

**-n** _NUM_, **--max-args** _NUM_
> 每条命令的最大参数个数。

**-P** _NUM_, **--max-procs** _NUM_
> 并行进程数。

**-0**, **--null**
> 输入项以 null 字符结尾。

**-d** _DELIM_, **--delimiter** _DELIM_
> 输入分隔符字符。

**-p**, **--interactive**
> 每次执行前提示确认。

**-t**, **--verbose**
> 执行前先打印命令。

**-r**, **--no-run-if-empty**
> 输入为空时不运行。

**-L** _NUM_, **--max-lines** _NUM_
> 每条命令最多使用 NUM 行输入。

**-s** _NUM_, **--max-chars** _NUM_
> 命令行的最大长度。

**-a** _FILE_, **--arg-file** _FILE_
> 从文件读取参数。

**-x**, **--exit**
> 命令行过长时退出。

**--show-limits**
> 显示系统限制。

# DESCRIPTION

**xargs** 从标准输入构建并执行命令。它将输入转换为命令的参数，并处理分批、并行化和参数数量限制。

默认情况下，xargs 将所有输入作为参数附加到单次命令调用中。-n 选项限制每次调用的参数数量，从而多次运行该命令。

-I 选项允许把参数放在命令中的任意位置。{}（或任意占位符）会被替换为每个输入项。这样每个输入项都会运行一次命令。

并行执行（-P）同时运行多条命令。与 -n 或 -I 结合使用时可以并发处理各项，充分利用多个 CPU 核心。

以 null 分隔的输入（-0）可以安全地处理包含空格、换行符或特殊字符的文件名。可与 find -print0 或类似工具搭配使用。

如果不加 -r，即使输入为空 xargs 也会运行命令。-r 标志可避免这种情况，在空输入会导致错误时很有用。

# CAVEATS

不加 -0 时文件名中的特殊字符会引发问题。Shell 特性（管道、重定向）需要借助包装脚本。参数数量上限取决于系统。跨并行作业的错误处理能力有限。使用 -P 时不保证顺序。

# HISTORY

**xargs** 起源于 **1970 年代**的 **PWB/UNIX**。它解决了 shell 命令行长度的限制——程序无法接受无限多的参数。这个工具成为串联 Unix 命令的重要手段，实现了定义 Unix 哲学的"对许多文件做某件事"的模式。

# INSTALL

```apt: sudo apt install findutils```

```dnf: sudo dnf install findutils```

```pacman: sudo pacman -S findutils```

```apk: sudo apk add findutils```

```zypper: sudo zypper install findutils```

```brew: brew install findutils```

```nix: nix profile install nixpkgs#findutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[find](/man/find)(1), [parallel](/man/parallel)(1), [apply](/man/apply)(1)
