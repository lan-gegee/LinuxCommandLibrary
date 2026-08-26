# TAGLINE

Korn shell，融合了 sh 和 csh 的特性

# TLDR

**启动 Korn shell**

```ksh```

**运行脚本**

```ksh [script.ksh]```

**运行命令字符串**

```ksh -c "[command]"```

**启动登录 Shell**

```ksh -l```

**启动受限 Shell**

```ksh -r```

**启用 POSIX 兼容模式**

```ksh -o posix```

**启用 vi 风格的行编辑**

```ksh -o vi```

# SYNOPSIS

**ksh** [_options_] [_script_] [_args_...]

# PARAMETERS

_SCRIPT_
> 要执行的脚本文件。

**-c** _CMD_
> 执行命令字符串。

**-l**
> 登录 Shell（读取 profile 文件）。

**-r**
> 受限 Shell（限制 `cd`、路径更改和重定向）。等同于以 `rksh` 调用。

**-s**
> 从标准输入读取命令。

**-o** _OPTION_
> 设置 Shell 选项（如 `vi`、`emacs`、`posix`、`noclobber`、`errexit`、`noglob`、`pipefail`）。

**+o** _OPTION_
> 取消给定的 Shell 选项。

**-i**
> 强制交互式 Shell 模式。

**-n**
> 读取命令但不执行（语法检查）。

**-x**
> 在执行时打印命令和参数（跟踪模式）。

**-e**
> 任一命令以非零状态退出时立即退出。

**-v**
> 在读取 Shell 输入行时将其打印出来。

**-a**
> 自动导出所有被赋值的变量。

**-u**
> 替换时把未设置的变量视为错误。

**-R** _file_
> 将交叉引用清单写入 _file_（仅 ksh93）。

# DESCRIPTION

**ksh** 是 Korn shell，结合了 Bourne shell (sh) 和 C shell (csh) 的特性。它提供高级脚本能力，并带有交互式命令行编辑、命令历史、作业控制和别名。

该 Shell 支持 vi 和 emacs 两种编辑模式，支持关联数组和索引数组、算术求值、协程（coprocess）以及模式匹配。ksh93 是使用最广泛的版本；ksh2020 是较新的发行版。

# CAVEATS

存在多种实现（ksh88、ksh93、mksh、pdksh）。各实现之间以及与 bash 之间的行为可能有细微差异。以 `-o posix` 调用时兼容 POSIX。

# HISTORY

Korn shell 由 **David Korn** 于 **20 世纪 80 年代初**在 **Bell Labs** 创建，影响了 bash 和 zsh 等许多现代 Shell。

# INSTALL

```dnf: sudo dnf install ksh```

```pacman: sudo pacman -S ksh```

```apk: sudo apk add loksh```

```zypper: sudo zypper install ksh```

```brew: brew install ksh```

```nix: nix profile install nixpkgs#loksh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bash](/man/bash)(1), [sh](/man/sh)(1), [zsh](/man/zsh)(1), [tcsh](/man/tcsh)(1)
