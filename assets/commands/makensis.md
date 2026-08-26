# TAGLINE

编译 NSIS 安装程序脚本

# TLDR

**编译安装程序脚本**

```makensis [script.nsi]```

**以最高详细级别编译**

```makensis /V4 [script.nsi]```

**定义一个符号**

```makensis /D[NAME=value] [script.nsi]```

**添加包含路径**

```makensis /I[/path/to/includes] [script.nsi]```

**将编译器输出记录到文件**

```makensis /O[logfile.txt] [script.nsi]```

**将警告视为错误**

```makensis /WX [script.nsi]```

**显示某个命令的帮助**

```makensis /CMDHELP [command]```

# SYNOPSIS

**makensis** [_options_] _script_

# PARAMETERS

_SCRIPT_
> NSIS 脚本文件（.nsi）。使用 **-** 表示标准输入。

**/V** _LEVEL_
> 详细级别：0=无，1=错误，2=警告，3=信息，4=全部。

**/D** _NAME[=VALUE]_
> 为脚本预处理器定义一个符号。

**/I** _DIR_
> 为 !include 指令添加包含路径。

**/O** _FILE_
> 将编译器输出记录到文件。

**/X** _"command param"_
> 内联执行 NSIS 命令。

**/NOCONFIG**
> 不包含 nsisconf.nsh。

**/NOCD**
> 不切换到 .nsi 文件所在目录。

**/WX**
> 将警告视为错误。

**/P** _LEVEL_
> 编译器优先级：0=空闲，1=低于正常，2=正常，3=高于正常，4=高，5=实时。

**/CMDHELP** [_command_]
> 打印特定命令或所有命令的帮助。

**/HDRINFO**
> 打印 makensis 的编译期选项。

**/PPO**
> 仅运行预处理器，并将结果打印到 stdout。

# DESCRIPTION

**makensis** 将 NSIS（Nullsoft Scriptable Install System）脚本编译为 Windows 安装程序可执行文件。它可以在 Linux、macOS 和 Windows 上原生运行，因此非常适合跨平台构建流水线。

# CAVEATS

生成 Windows 格式的安装程序。NSIS 脚本语法需要另行学习。在 Linux 上选项使用 / 前缀（如 /V4）而不是 - 前缀。

# HISTORY

NSIS（Nullsoft Scriptable Install System）由 Winamp 的开发商 **Nullsoft** 创建。

# INSTALL

```apt: sudo apt install nsis```

```brew: brew install nsis```

```nix: nix profile install nixpkgs#nsis```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wine](/man/wine)(1)
