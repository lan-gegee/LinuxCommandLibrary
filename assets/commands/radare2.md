# TAGLINE

逆向工程与二进制分析框架

# TLDR

**打开二进制文件进行分析**

```r2 [binary]```

打开时**运行完整分析**

```r2 -A [binary]```

**以写入模式打开**

```r2 -w [binary]```

打开时**定位到指定地址**

```r2 -s [0x1000] [binary]```

**调试二进制文件**

```r2 -d [binary]```

按 PID **附加到正在运行的进程**

```r2 -d [pid]```

**不做任何分析直接打开**（原始文件）

```r2 -n [binary]```

**执行命令后退出**

```r2 -qc "[pdf]" [binary]```

**设置架构与位宽**

```r2 -a [x86] -b [64] [binary]```

# SYNOPSIS

**r2** [_-a arch_] [_-b bits_] [_-B baddr_] [_-c cmd_] [_-e k=v_] [_-i file_] [_-I prefile_] [_-k kernel_] [_-m addr_] [_-p project_] [_-P patch_] [_-r rarun2_] [_-R rr2rule_] [_-s addr_] [_-0AdfDjLMnNqStTuVwxX_] _file_

# PARAMETERS

**-A**
> 在给出提示符前运行 'aaa' 命令分析所有被引用的代码。

**-a** _arch_
> 强制指定 asm.arch（x86、ppc、arm、mips、bf、java 等）。

**-b** _bits_
> 强制指定 asm.bits（16、32、64）。

**-B** _baddr_
> 指定加载新二进制文件时的基地址。

**-c** _cmd_
> 在给出提示符前执行给定命令。

**-d**
> 以调试器模式启动。

**-D** _backend_
> 使用指定的调试后端启用调试模式。

**-e** _k=v_
> 设置配置 eval 变量 key=value。

**-f**
> 将块大小设置为文件大小。

**-i** _file_
> 在文件加载后运行脚本文件。

**-I** _file_
> 在文件加载前运行脚本文件。

**-k** _kernel_
> 选择用于系统调用解析的内核（asm.os）。

**-l** _plugfile_
> 加载给定的插件文件。

**-L**
> 列出已加载的 IO 插件。

**-m** _addr_
> 将文件映射到指定地址。

**-M**
> 禁用符号名反修饰（demangling）。

**-n**
> 不执行任何分析，仅加载原始文件。

**-nn**
> 仅加载 rbin 结构（elf、mach0 等）。

**-N**
> 不从 ~/.radare2rc 加载用户设置或项目。

**-p** _project_
> 设置项目文件。

**-P** _file_
> 应用 rapatch 文件后退出。

**-q**
> 安静模式。运行完 -c 命令后退出。

**-qq**
> 类似 -q，但会在所有命令（包括 -c、-i 脚本）执行完后退出。

**-r** _rarun2_
> 为生成（spawn）程序指定 dbg.profile rarun2 配置文件。

**-R** _directive_
> 无需创建配置文件即可指定自定义的 rarun2 指令。

**-s** _addr_
> 从该地址开始定位（seek）。

**-S**
> 启用沙盒模式。

**-T**
> 避免计算文件哈希。

**-v**
> 显示版本信息并退出。

**-w**
> 以写入模式打开。

# COMMANDS

**pdf**
> 反汇编函数。

**afl**
> 列出函数。

**aaa**
> 全量分析（函数、引用、字符串等）。

**s** _addr_
> 定位到地址。

**V**
> 进入可视化模式。

**VV**
> 进入图形模式。

**px** _N_
> 以十六进制打印 N 个字节。

**iz**
> 列出数据段中的字符串。

**ii**
> 列出导入项。

**ie**
> 列出入口点。

**db** _addr_
> 设置断点。

**dc**
> 继续执行。

**ds**
> 单步执行一条指令。

**dr**
> 显示寄存器。

**?**
> 显示帮助。在任何命令前缀后附加 ? 可查看子命令帮助。

**q**
> 退出。

# DESCRIPTION

**radare2**（r2）是一个开源的逆向工程框架，用于二进制分析、调试和漏洞利用。它支持对多种架构和格式的二进制文件进行反汇编、分析和修补。

该工具通过命令行界面操作，包含数百个命令。命令通常是简短的助记符：'p' 表示打印（print），'a' 表示分析（analyze），'s' 表示定位（seek）。在任何命令前缀后附加 '?' 即可获取帮助。

分析过程会识别函数、字符串、交叉引用和控制流。'aaa' 命令执行全面分析。结果会填充到可通过命令查询的数据库中。

可视化模式提供基于光标的导航和图形视图。函数图展示控制流及各代码块之间的连接。十六进制编辑模式允许直接修改二进制内容。

调试功能原生集成，可以附加到进程或启动新程序。断点、单步执行、寄存器操作和内存检查在所有受支持的平台上均可用。

脚本方面支持通过 r2pipe 进行外部自动化（Python、JavaScript 等），也支持内部 radare2 脚本。丰富的插件 API 支持自定义分析。

# CONFIGURATION

**~/.radare2rc**
> 启动时执行的启动配置文件，包含默认设置和自动运行的命令。使用 -N 可跳过加载。

**-e key=value**
> 运行时配置变量，控制分析深度、显示格式和工具行为。在 r2 内部使用 `e??` 可列出全部选项。

**~/.local/share/radare2/projects/**
> 项目文件，保存分析状态，包括函数名、注释和标志（flag），便于继续处理同一个二进制文件。

# CAVEATS

学习曲线陡峭——命令语法需要时间掌握。文档可能不够完善。分析可能遗漏混淆过的代码。部分功能依赖特定平台。内存占用随分析深度增长。

# HISTORY

**radare2** 由 **pancake**（Sergi Alvarez）于 **2006 年**前后创建，由最初的 radare 演化而来。它从一个十六进制编辑器发展为完整的逆向工程平台。该项目强调自由、可移植性和 Unix 哲学。尽管复杂，它拥有忠实的社区，被广泛用于 CTF 竞赛和安全研究。

# INSTALL

```dnf: sudo dnf install radare2```

```pacman: sudo pacman -S radare2```

```apk: sudo apk add radare2```

```zypper: sudo zypper install radare2```

```brew: brew install radare2```

```nix: nix profile install nixpkgs#radare2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[objdump](/man/objdump)(1), [gdb](/man/gdb)(1), [ltrace](/man/ltrace)(1), [strace](/man/strace)(1), [readelf](/man/readelf)(1), [strings](/man/strings)(1), [xxd](/man/xxd)(1)
