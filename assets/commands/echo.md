# TAGLINE

显示文本输出

# TLDR

**打印文本**

```echo "[Hello World]"```

**打印时不带末尾换行**

```echo -n "[text]"```

**解释转义序列**

```echo -e "[Line 1\nLine 2]"```

**打印环境变量**

```echo $[PATH]```

**将文本写入文件**

```echo "[content]" > [file.txt]```

**将文本追加到文件**

```echo "[more content]" >> [file.txt]```

# SYNOPSIS

**echo** [_options_] [_string_...]

# DESCRIPTION

**echo** 将一行文本输出到标准输出。它是最基础、最常用的命令之一，对脚本编写、日志记录以及向用户显示信息不可或缺。

该命令既作为 shell 内建命令存在，也有独立的可执行程序。

# PARAMETERS

**-n**
> 不输出末尾换行

**-e**
> 启用反斜杠转义的解释

**-E**
> 禁用反斜杠转义的解释（默认）

# ESCAPE SEQUENCES

（需配合 **-e** 标志）：

**\n** - 换行
**\t** - 制表符
**\r** - 回车
**\a** - 警示音（响铃）
**\b** - 退格
**\\\\** - 反斜杠
**\\"** - 双引号
**\xHH** - 十六进制字节
**\0NNN** - 八进制字节

# CAVEATS

不同 shell 之间、shell 内建命令与 `/bin/echo` 之间的行为存在差异。**-e** 标志不是 POSIX 标准的一部分，并非所有实现都支持。要编写可移植脚本，建议使用 **printf**，它在各平台上的行为一致。大多数 shell（bash、zsh、dash）都将 echo 作为内建命令提供，其行为可能与外部二进制程序不同。

# HISTORY

**echo** 自 **1972 年**的 Unix Version 2 起就是 Unix 的一部分，但其行为在不同 Unix 变体间有所差异。

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

[printf](/man/printf)(1), [cat](/man/cat)(1), [tee](/man/tee)(1)
