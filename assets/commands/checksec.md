# TAGLINE

审计 ELF 二进制文件的安全特性

# TLDR

**检查二进制文件的安全属性**

```checksec --file=[path/to/binary]```

**以 JSON 输出检查安全属性**

```checksec --file=[path/to/binary] --output=json```

**检查运行中内核的安全特性**

```checksec --kernel```

**检查运行中进程的安全属性**

```checksec --proc [pid]```

**扫描目录中的所有二进制文件**

```checksec --dir [path/to/directory]```

**检查所有运行中的进程**

```checksec --proc-all```

# SYNOPSIS

**checksec** [**--file** _binary_] [**--dir** _directory_] [**--proc** _pid_] [**--kernel**] [**--output** _format_]

# DESCRIPTION

**checksec** 审计编译后的 Linux 可执行文件（ELF 文件）、内核或运行中进程所启用的安全特性。它通过检查常见的缓解措施，帮助安全研究人员和管理员评估二进制文件的可利用性态势。

**检查的安全属性：**

**RELRO** (Relocation Read-Only) - 保护 GOT/PLT 不被覆写。Full RELRO 在动态链接完成后将这些区域标记为只读。

**Stack Canary** - 放置在返回地址之前的随机值，用于检测缓冲区溢出。

**NX** (No eXecute) - 将内存区域标记为不可执行，防止从栈/堆执行代码。

**PIE** (Position Independent Executable) - 允许随机加载基址，从而启用 ASLR。

**FORTIFY** - 针对常见函数的编译期缓冲区溢出检查。

# PARAMETERS

**--file** _binary_
> 检查指定二进制文件的安全属性

**--dir** _directory_
> 扫描目录中的所有二进制文件

**--proc** _pid_
> 按 PID 检查运行中的进程

**--proc-all**
> 检查所有运行中的进程

**--kernel**
> 检查内核安全特性

**--output** _format_
> 输出格式：cli、csv、json、xml

**--fortify-file** _binary_
> 详细的 fortify 分析

# CAVEATS

彩色输出表示安全状态：绿色表示保护已启用，红色表示缺失。红色并不总是意味着存在漏洞——发行版厂商可能在编译二进制文件时做了有意取舍。

# HISTORY

最初由 trapkit.de 的 **Tobias Klein** 编写。该工具一直得到积极维护和扩展，从 Bash 移植到了 Golang，当前版本由 github.com/slimm609/checksec 维护。

# INSTALL

```dnf: sudo dnf install checksec```

```pacman: sudo pacman -S checksec```

```apk: sudo apk add checksec-rs```

```zypper: sudo zypper install checksec```

```brew: brew install checksec```

```nix: nix profile install nixpkgs#checksec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[readelf](/man/readelf)(1), [objdump](/man/objdump)(1), [file](/man/file)(1)

# RESOURCES

```[Source code](https://github.com/slimm609/checksec)```

<!-- verified: 2026-06-22 -->
