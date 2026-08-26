# TAGLINE

带编辑功能的增强版 C Shell

# TLDR

**启动交互式 tcsh shell**

```tcsh```

**执行一条命令**

```tcsh -c "[command]"```

**运行脚本**

```tcsh [script.csh]```

**以登录 Shell 启动**

```tcsh -l```

**不读取启动文件启动**（快速启动）

```tcsh -f```

**只解析命令而不执行**（语法检查）

```tcsh -n [script.csh]```

**启用详细模式**，在历史替换之后回显命令

```tcsh -v```

# SYNOPSIS

**tcsh** [_-bcefinstvVxX_] [_-l_] [_command_]

# PARAMETERS

**-c** _command_
> 从随后的参数字符串中读取命令。

**-e**
> 若某条命令以非零状态退出则立即退出。

**-f**
> 快速启动；不读取 ~/.tcshrc 或 ~/.cshrc 启动文件。

**-i**
> 即使输入不是终端也强制进入交互模式。

**-l**
> 作为登录 Shell 运行；读取 .login 并在退出时执行 .logout 文件。

**-n**
> 解析命令但不执行（用于调试脚本）。

**-s**
> 从标准输入读取命令输入。

**-t**
> 读取并执行单行输入。

**-v**
> 设置详细模式；在历史替换之后回显命令。

**-x**
> 设置回显模式；在执行之前回显命令。

**-V**
> 在读取 ~/.tcshrc 之前设置详细模式。

**-X**
> 在读取 ~/.tcshrc 之前设置回显模式。

**-b**
> 强制中断选项处理。

**-m**
> 即使 ~/.tcshrc 不属于当前有效用户也加载它。

**-q**
> 接受 SIGQUIT；用于在禁用作业控制的调试器下运行。

**--help**
> 打印帮助信息并退出。

**--version**
> 打印版本信息并退出。

# DESCRIPTION

**tcsh** 是伯克利 C Shell（csh）的增强版本。它提供命令行编辑器、可编程的单词补全、拼写纠正、历史机制、作业控制以及类 C 的语法。

交互式 Shell 启动时读取 **~/.tcshrc**（或 ~/.cshrc）。登录 Shell 还会额外读取 **~/.login**，并在退出时执行 **~/.logout**。该 Shell 支持 **!** 语法的命令历史、别名和 Shell 变量。

功能包括用 Tab 进行文件名补全、命令历史编辑、使用 **pushd/popd** 操作目录栈，以及针对命令和参数的可编程补全。

# CONFIGURATION

**~/.tcshrc**
> 所有交互式 tcsh 都会读取的主启动文件；若未找到则回退到 ~/.cshrc

**~/.login**
> 登录 Shell 在读取 ~/.tcshrc 之后读取；通常用于设置环境变量并执行登录时的命令

**~/.logout**
> 登录 Shell 退出时执行

**~/.cshdirs**
> 保存的目录栈，当设置了 savedirs Shell 变量时在启动时恢复

# CAVEATS

tcsh 使用 C Shell 语法，与 POSIX sh/bash 不同。为 tcsh 编写的脚本可能不具备可移植性。C Shell 家族在复杂脚本方面存在已知问题，对于可移植脚本一般建议使用兼容 POSIX 的 Shell。

# HISTORY

C Shell（csh）由 **Bill Joy** 于 20 世纪 70 年代末在加州大学伯克利分校为 BSD Unix 创建。tcsh 是作为增加了命令行编辑和补全等功能的增强版本开发的。"tcsh" 这一名字来自启发了部分特性的 TENEX 操作系统。tcsh 曾是 FreeBSD 的默认 Shell，并在 bash 流行之前被 Unix 系统广泛使用。

# INSTALL

```apt: sudo apt install tcsh```

```dnf: sudo dnf install tcsh```

```pacman: sudo pacman -S tcsh```

```apk: sudo apk add tcsh```

```zypper: sudo zypper install tcsh```

```brew: brew install tcsh```

```nix: nix profile install nixpkgs#tcsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[csh](/man/csh)(1), [bash](/man/bash)(1), [zsh](/man/zsh)(1), [sh](/man/sh)(1), [ksh](/man/ksh)(1), [fish](/man/fish)(1)
