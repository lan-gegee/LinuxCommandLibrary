# TAGLINE

采用类 C 语法的 Unix shell

# TLDR

**启动交互式** C shell 会话

```csh```

**执行 C shell 脚本**

```csh [script.csh]```

执行字符串中的命令

```csh -c "[echo Hello; echo World]"```

**启动登录 shell**

```csh -l```

以详细输出方式**执行脚本**

```csh -v [script.csh]```

带命令跟踪地**执行脚本**

```csh -x [script.csh]```

# SYNOPSIS

**csh** [_options_] [_script_ [_arguments_]]

# PARAMETERS

**-c** _STRING_
> 执行字符串中的命令。

**-e**
> 任一命令失败立即退出。

**-f**
> 快速启动；不读取 .cshrc。

**-i**
> 强制交互模式。

**-l**
> 作为登录 shell 运行。

**-n**
> 只解析不执行命令（语法检查）。

**-s**
> 从标准输入读取命令。

**-v**
> 详细模式；在执行前打印命令。

**-x**
> 在变量替换之后回显命令。

**-V**
> 在读取 .cshrc 之前即启用详细模式。

**-X**
> 在读取 .cshrc 之前即启用回显模式。

# DESCRIPTION

**csh**（C shell）是一种采用类 C 语法的 Unix shell，具备作业控制、命令历史和别名功能。它的设计目标是比 Bourne shell 更易用，同时提供 C 程序员熟悉的语法。

该 shell 提供历史替换（!!、!$）、命令补全和别名等交互特性。其脚本语法与 Bourne 系 shell 差异很大，条件判断和循环都使用类似 C 的构造。

配置文件包括 **~/.cshrc**（每个 shell 都会读取）和 **~/.login**（登录 shell 读取）。shell 会设置各种环境变量，并提供用于作业控制和目录切换的内建命令。

# CONFIGURATION

**~/.cshrc**
> 每个 shell 都会读取，用于设置别名和环境变量。

**~/.login**
> 登录 shell 读取，用于设置环境。

# CAVEATS

csh 脚本存在众所周知的缺陷，不建议用于复杂脚本。变量处理和引号行为与 Bourne shell 不同。现代系统通常改用 tcsh，它在 csh 的基础上扩展了更多功能。csh 脚本的可移植性有限。

# HISTORY

C shell 由 Bill Joy 于 **1978** 年在加州大学伯克利分校编写，是 BSD Unix 的一部分。它为 Unix shell 引入了命令历史和作业控制。虽然影响深远，但其在脚本方面的局限使人们普遍建议不要用它写脚本，这在一篇著名文章《Csh Programming Considered Harmful》中有详细论述。

# INSTALL

```dnf: sudo dnf install tcsh```

```pacman: sudo pacman -S tcsh```

```apk: sudo apk add tcsh```

```zypper: sudo zypper install tcsh```

```brew: brew install tcsh```

```nix: nix profile install nixpkgs#tcsh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tcsh](/man/tcsh)(1), [bash](/man/bash)(1), [sh](/man/sh)(1), [zsh](/man/zsh)(1)

# RESOURCES

```[Source code](https://github.com/tcsh-org/tcsh)```

```[Homepage](https://www.tcsh.org)```

<!-- verified: 2026-06-26 -->
