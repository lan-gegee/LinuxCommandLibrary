# TAGLINE

符合策略的 POSIX shell

# TLDR

**启动交互式** posh 会话

```posh```

**执行** shell 脚本

```posh [script.sh]```

**运行命令**字符串后退出

```posh -c "[command]"```

对脚本进行**语法检查**而不执行

```posh -n [script.sh]```

从标准输入**读取命令**

```echo "[commands]" | posh -s```

# SYNOPSIS

**posh** [_+-aCefilnuvx_] [_+-o option_] [_[-c command-string [command-name] | -s | file] [argument...]_]

# PARAMETERS

**-c** _command_
> 执行给定字符串中的命令

**-i**
> 强制交互模式并启用作业控制

**-l**
> 作为登录 shell 运行，读取 profile 文件

**-n**
> 读取命令但不执行（仅语法检查）

**-s**
> 从标准输入读取命令；将剩余参数视为位置参数

**-p**
> 特权模式：读取 `/etc/suid_profile` 而不是用户 profile

**-e**
> 如果某条命令以非零状态退出则立即退出

**-u**
> 替换时把未设置的变量视为错误

**-v**
> 在读取输入行时将其打印到 stderr

**-x**
> 执行前将每条命令及其参数打印到 stderr（跟踪模式）

**-a**
> 导出所有被赋值或修改的变量

# DESCRIPTION

**posh**（Policy-compliant Ordinary SHell）是从 pdksh 派生的 Bourne shell 重新实现，设计目标是严格遵循 POSIX/SUSv3 规范和 Debian 策略。它有意排除超出 POSIX 标准的扩展，因此非常适合测试脚本的可移植性。

能在 posh 下正确运行的脚本更有可能在不同类 Unix 环境之间移植。在 posh 下运行脚本相当于做一次合规检查：如果使用了 bash 特有的特性，posh 会拒绝执行，从而在部署到精简系统之前暴露可移植性问题。

Posh 支持标准 shell 特性，包括参数替换、命令替换、算术表达式、管道、文件名通配、here-document 以及交互会话中的作业控制。

# CAVEATS

Posh 有意省略了许多常见的 bash 扩展：数组、进程替换（`<()`）、`[[ ]]` 复合测试、`local` 声明以及其他各种 bashism。依赖这些特性的脚本必须重写才能兼容 posh。该 shell 并非用于日常交互，而是作为可移植性测试工具。

# HISTORY

**posh** 由 Clint Adams 为 **Debian** 项目创建，用于提供严格符合 POSIX 和 Debian 策略手册要求的 shell。它派生自 **pdksh**（Public Domain Korn Shell），后者最初由 Eric Gisin 于 20 世纪 80 年代编写，是一个自由的 Korn shell 实现。

# INSTALL

```apt: sudo apt install posh```

```brew: brew install posh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sh](/man/sh)(1), [bash](/man/bash)(1), [dash](/man/dash)(1), [ksh](/man/ksh)(1)

# RESOURCES

```[Homepage](https://packages.debian.org/posh)```

<!-- verified: 2026-06-20 -->
