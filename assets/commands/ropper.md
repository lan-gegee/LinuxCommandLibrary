# TAGLINE

在二进制文件中搜索 ROP 和 JOP gadget

# TLDR

**查找 gadget**

```ropper -f [binary]```

**搜索 gadget**

```ropper -f [binary] --search "[pop rdi]"```

**查找字符串**

```ropper -f [binary] --string "[/bin/sh]"```

**交互模式**

```ropper```

**生成 ropchain**

```ropper -f [binary] --chain [execve]```

**显示所有 gadget**

```ropper -f [binary] --all```

**设置架构**

```ropper -f [binary] -a [x86_64]```

# SYNOPSIS

**ropper** [_-f file_] [_--search pattern_] [_--chain type_] [_options_]

# PARAMETERS

**-f**, **--file** _FILE_
> 二进制文件。

**--search** _PATTERN_
> 搜索 gadget。

**--string** _STR_
> 查找字符串。

**--chain** _TYPE_
> 生成 ROP 链。

**-a**, **--arch** _ARCH_
> 架构。

**--all**
> 所有 gadget。

**--type** _TYPE_
> gadget 类型（rop、jop）。

**-I** _OFFSET_
> 映像基址。

**--depth** _N_
> 最大指令数。

# DESCRIPTION

**ropper** 为 ROP/JOP/COP 漏洞利用查找 gadget。它支持多种架构和二进制格式。

交互式 Shell 提供探索环境，可通过命令搜索和分析 gadget。

链生成用于构建漏洞利用载荷。提供 execve、mprotect 和 virtualprotect 等链。

语义搜索按功能查找 gadget：只需描述需求，而不必给出精确指令。

多文件支持可以同时分析多个库，跨二进制文件构建链。

# CAVEATS

仅限授权的安全研究使用。工具较为复杂，需要漏洞利用知识。结果需要验证。

# HISTORY

**Ropper** 由 **Sascha Schirra** 创建，是一个功能全面的 gadget 查找工具。它为 ROP 链开发同时提供 CLI 和交互式界面。

# INSTALL

```pacman: sudo pacman -S ropper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwntools](/man/pwntools)(1), [radare2](/man/radare2)(1)
