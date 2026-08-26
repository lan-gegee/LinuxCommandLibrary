# TAGLINE

漏洞利用开发与 CTF 工具集

# TLDR

将汇编代码转换为**字节**

```pwn asm "xor edi, edi"```

创建特定长度的**循环模式（cyclic pattern）**

```pwn cyclic 100```

将数据**编码**为十六进制

```pwn hex deadbeef```

从十六进制**解码**数据

```pwn unhex 6c4f7645```

输出用于启动 shell 的 x64 Linux **shellcode**

```pwn shellcraft amd64.linux.sh```

检查 ELF 文件的**二进制安全**设置

```pwn checksec path/to/file```

检查**更新**

```pwn update```

显示**版本**

```pwn version```

# SYNOPSIS

**pwn** _command_ [_arguments_...]

# PARAMETERS

**asm** _code_
> 将汇编代码转换为字节

**cyclic** _length_
> 创建循环模式

**hex** _data_
> 将数据编码为十六进制

**unhex** _hex_
> 解码十六进制数据

**shellcraft** _arch.os.shellcode_
> 生成 shellcode

**checksec** _file_
> 检查二进制安全设置

**update**
> 检查更新

**version**
> 显示版本

# DESCRIPTION

**pwn** 是 Pwntools 的命令行界面。Pwntools 是一个为快速原型开发和 CTF 题目设计的漏洞利用开发库。它提供汇编、shellcode 生成、二进制分析和数据编码等实用功能。

该工具支持多种架构和操作系统，适用于安全研究和渗透测试。

# CAVEATS

仅用于经授权的安全测试和教育目的。生成的 shellcode 和 exploit 只应在受控环境中使用。

# HISTORY

**Pwntools** 的一部分，这是一个为 CTF 选手和安全研究人员开发的 Python 库。它为常见的漏洞利用开发任务提供便捷的命令行访问。

# INSTALL

```apk: sudo apk add pwntools```

```brew: brew install pwntools```

```nix: nix profile install nixpkgs#pwntools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gdb](/man/gdb)(1), [objdump](/man/objdump)(1), [readelf](/man/readelf)(1)
