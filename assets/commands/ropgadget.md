# TAGLINE

在二进制可执行文件中查找 ROP gadget

# TLDR

**在二进制文件中查找 gadget**

```ROPgadget --binary [binary]```

**搜索特定 gadget**

```ROPgadget --binary [binary] --string "[/bin/sh]"```

**按正则表达式过滤 gadget**

```ROPgadget --binary [binary] --re "[pop.*ret]"```

**过滤掉地址中含坏字节的 gadget**

```ROPgadget --binary [binary] --badbytes "[0a|0d|00]"```

**限制 gadget 深度**

```ROPgadget --binary [binary] --depth [5]```

**生成 ropchain**

```ROPgadget --binary [binary] --ropchain```

**输出到文件**

```ROPgadget --binary [binary] > [gadgets.txt]```

# SYNOPSIS

**ROPgadget** [_--binary file_] [_--string str_] [_--re pattern_] [_options_]

# PARAMETERS

**--binary** _FILE_
> 目标二进制文件。

**--string** _STR_
> 在二进制文件中查找字符串。

**--re** _REGEX_
> 按正则表达式过滤。

**--ropchain**
> 生成 ROP 链。

**--depth** _N_
> gadget 的指令深度。

**--badbytes** _BYTES_
> 拒绝地址中包含特定字节的 gadget（例如 "0a|0d|00"）。

**--opcode** _OPCODES_
> 在可执行段中搜索特定的操作码。

**--offset** _OFFSET_
> 为 gadget 地址添加偏移。

**--nojop**
> 排除 JOP（Jump-Oriented Programming）gadget。

**--nosys**
> 排除 syscall gadget。

**--multibr**
> 启用多分支 gadget。

**--all**
> 搜索所有段，而不仅是可执行段。

# DESCRIPTION

**ROPgadget** 在二进制文件中查找 ROP（Return-Oriented Programming，面向返回的编程）gadget。它用于漏洞利用开发和安全研究。

Gadget 是以返回指令结尾的小型指令序列。它们可以被串联起来构建漏洞利用。

字符串搜索可以在二进制文件中找到有用的数据，例如 shell 路径和其他字符串的位置。

自动 ropchain 生成会构建漏洞利用模板，为常见场景创建 execve 链。

深度选项限制指令序列长度。较短的 gadget 通常更有用。

# CAVEATS

仅限授权的安全研究使用。需要理解汇编语言。结果需要人工分析。

# HISTORY

**ROPgadget** 由 **Jonathan Salwan** 创建，用于 ROP 漏洞利用开发。它广泛应用于 CTF 竞赛和安全研究领域。

# INSTALL

```pacman: sudo pacman -S ropgadget```

```nix: nix profile install nixpkgs#ropgadget```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ropper](/man/ropper)(1), [objdump](/man/objdump)(1), [pwntools](/man/pwntools)(1), [radare2](/man/radare2)(1)
