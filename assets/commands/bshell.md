# TAGLINE

Bourne Shell 解释器

# TLDR

**启动交互式 Bourne shell**

```bshell```

**执行 shell 脚本**

```bshell [path/to/script.sh]```

**执行一条命令**

```bshell -c "[command]"```

**以调试模式运行，显示已执行的命令**

```bshell -x [path/to/script.sh]```

**作为受限 shell 运行**

```bshell -r```

# SYNOPSIS

**bshell** [**-ruvx**] [**-c** _command_] [_script_] [_arguments..._]

# DESCRIPTION

**bshell** 是 Schily-Tools 工具集中的 Bourne Shell 解释器，提供传统的 POSIX 兼容 shell 环境。它执行从标准输入、命令字符串或脚本文件中读取的命令。

Bourne Shell 是 Stephen Bourne 在贝尔实验室编写的原始 Unix shell。此实现在现代系统上运行的同时，保持了与经典 shell 行为的兼容性。

# PARAMETERS

**-c** _command_
> 执行指定的命令字符串

**-r**
> 以受限 shell 模式启动，出于安全考虑限制某些操作

**-u**
> 将未设置的变量视为错误并退出

**-v**
> 在读取 shell 输入行时将其打印出来（详细输出模式）

**-x**
> 在命令和参数被执行时将其打印出来（调试模式）

# CAVEATS

**bshell** 命令是 Schily-Tools 软件包的一部分，在大多数 Linux 发行版上可能默认未安装。多数系统使用 **bash** 或 **dash** 作为 **/bin/sh** 来实现 Bourne shell 兼容性。

# HISTORY

最初的 Bourne Shell 由 **Stephen Bourne** 在贝尔实验室开发，首次出现于 **1979 年的 Version 7 Unix**。它取代了 Thompson shell，并成为后续各种 shell（包括 **ksh**、**bash** 和 **zsh**）的基础。Jörg Schilling 开发的 Schily-Tools 实现为经典 Bourne Shell 提供了现代化移植版本。

# INSTALL

```apt: sudo apt install avahi-ui-utils```

```dnf: sudo dnf install avahi-ui-tools```

```apk: sudo apk add avahi-ui-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sh](/man/sh)(1), [bash](/man/bash)(1), [dash](/man/dash)(1), [ksh](/man/ksh)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/schilytools/)```

<!-- verified: 2026-06-22 -->
