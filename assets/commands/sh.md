# TAGLINE

符合 POSIX 标准的命令解释器

# TLDR

**启动交互式 Shell**

```sh```

**执行脚本**

```sh [script.sh]```

**执行字符串中的命令**

```sh -c "[command1; command2]"```

**以详细输出执行脚本**（显示命令）

```sh -x [script.sh]```

**只检查语法而不执行**

```sh -n [script.sh]```

**从 stdin 读取命令**

```echo "echo hello" | sh```

# SYNOPSIS

**sh** [**-aCefimnsuvx**] [_script_ [_argument_...]]

# PARAMETERS

**-a**
> 将所有被修改或创建的变量导出到环境

**-C**
> 防止输出重定向覆盖已有文件（noclobber）

**-c** _string_
> 执行字符串中的命令

**-e**
> 命令以非零状态退出时立即退出

**-f**
> 禁用文件名通配符展开（globbing）

**-i**
> 交互式 Shell

**-m**
> 启用作业控制（交互式 Shell 的默认行为）

**-n**
> 读取命令但不执行（语法检查）

**-s**
> 从标准输入读取命令

**-u**
> 将未设置的变量视为错误

**-v**
> 在读取 shell 输入行时将其打印出来

**-x**
> 在执行时打印命令和参数

**+**_option_
> 关闭选项

# DESCRIPTION

**sh** 是符合 POSIX 标准的命令解释器（Shell）。它提供标准的 Shell 脚本环境，并保证在所有类 Unix 系统上都可用。

在许多 Linux 系统上，**/bin/sh** 是指向另一个 Shell（dash、bash 等）的符号链接，并以 POSIX 兼容模式运行。这同时带来了兼容性和性能上的好处。

以 **#!/bin/sh** 开头的 Shell 脚本使用 POSIX sh，可确保最大的可移植性。需要 bash 特有功能的脚本应改用 **#!/bin/bash**。

该 Shell 从标准输入、文件或 **-c** 参数读取命令。它支持变量、控制流（if、while、for、case）、函数、管道和 I/O 重定向。

# POSIX FEATURES

**变量**: NAME=value, $NAME, ${NAME}
**引号**: 'literal', "interpolated", \escape
**条件**: if-then-elif-else-fi, case-esac
**循环**: while-do-done, for-in-do-done, until-do-done
**函数**: name() { commands; }
**测试**: [ condition ], test condition
**算术**: $((expression))

# CONFIGURATION

**~/.profile**
> 每个用户的登录 Shell 初始化文件，在登录 Shell 时执行。

**/etc/profile**
> 系统级登录 Shell 初始化文件，在 ~/.profile 之前执行。

**ENV**
> 环境变量，指向一个在交互式 Shell 启动时执行的文件。

# CAVEATS

POSIX sh 缺少许多 bash 功能：数组、[[ ]]、花括号展开、进程替换以及大量字符串操作。要么编写可移植脚本，要么明确要求 bash。

**-e** 选项可能导致意外的退出。条件中的命令（if、while）或与 || / && 连用的命令失败时不会触发退出。

不同系统将 /bin/sh 链接到不同的实现（dash、bash、ksh）。请在目标系统上测试脚本，或使用明确的解释器。

# INSTALL

```apt: sudo apt install dash```

```dnf: sudo dnf install dash```

```pacman: sudo pacman -S dash```

```apk: sudo apk add busybox-binsh```

```zypper: sudo zypper install dash```

```brew: brew install dash```

```nix: nix profile install nixpkgs#dash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [dash](/man/dash)(1), [zsh](/man/zsh)(1), [ksh](/man/ksh)(1), [csh](/man/csh)(1)
