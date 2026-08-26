# TAGLINE

带哈希功能的取证磁盘镜像工具

# TLDR

**创建磁盘镜像**并显示进度

```dcfldd if=[/dev/sda] of=[disk.img]```

**创建镜像并进行 MD5 哈希校验**

```dcfldd if=[/dev/sda] of=[disk.img] hash=md5 hashlog=[hash.txt]```

**创建带多种哈希的镜像**

```dcfldd if=[/dev/sda] of=[disk.img] hash=md5,sha256```

**同时写入多个输出**

```dcfldd if=[/dev/sda] of=[disk1.img] of=[disk2.img]```

**将输出拆分**为多个文件

```dcfldd if=[/dev/sda] of=[disk.img] split=[1G] splitformat=aa```

**用指定模式擦除磁盘**

```dcfldd pattern=[00] of=[/dev/sda]```

**对照源设备校验镜像**

```dcfldd if=[/dev/sda] vf=[disk.img]```

**每 256 个块显示一次状态**

```dcfldd if=[/dev/sda] of=[disk.img] statusinterval=[256]```

# SYNOPSIS

**dcfldd** [_options_]

# DESCRIPTION

**dcfldd** 是 GNU dd 的增强版本，由国防部计算机取证实验室（DCFL）开发。它增加了对取证镜像至关重要的功能，包括实时哈希计算、状态输出、拆分输出和校验。

该工具可在复制的同时计算多种哈希类型（MD5、SHA1、SHA256 等），确保数据完整性。它支持同时写入多个输出，以便创建重复的取证镜像。

dcfldd 在复制过程中提供进度输出，解决了 dd 最常被诟病的问题之一。它广泛应用于数字取证、事件响应和数据恢复工作中。

# PARAMETERS

**if=** _file_
> 输入文件或设备。

**of=** _file_
> 输出文件（可指定多个）。

**vf=** _file_
> 对照输入校验文件。

**hash=** _types_
> 哈希算法（md5、sha1、sha256、sha384、sha512）。

**hashlog=** _file_
> 将哈希写入文件。

**hashwindow=** _n_
> 每 n 字节计算一次哈希。

**pattern=** _hex_
> 用于擦除的填充模式。

**split=** _size_
> 按大小间隔拆分输出。

**splitformat=** _fmt_
> 拆分文件的后缀格式。

**statusinterval=** _n_
> 每 n 个块显示一次状态。

**bs=** _size_
> 读写的块大小。

**count=** _n_
> 仅复制 n 个块。

**skip=** _n_
> 跳过输入开头的 n 个块。

**seek=** _n_
> 跳过输出开头的 n 个块。

**conv=** _options_
> 转换选项（noerror、sync 等）。

# CAVEATS

由于哈希计算的开销，速度比 dd 慢。哈希校验需要读取数据两次。取证镜像应在源介质上使用写保护器。某些功能的行为可能与标准 dd 不同。

# HISTORY

**dcfldd** 由 **Nick Harbour** 于 **2000 年代初**在**国防部计算机取证实验室**（DCFL）开发。它的诞生是为了满足取证调查人员对可验证、有记录的磁盘镜像能力的需求。该工具已成为数字取证培训与实践中的标准工具。

# INSTALL

```apt: sudo apt install dcfldd```

```dnf: sudo dnf install dcfldd```

```brew: brew install dcfldd```

```nix: nix profile install nixpkgs#dcfldd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [ddrescue](/man/ddrescue)(1), [md5sum](/man/md5sum)(1), [sha256sum](/man/sha256sum)(1)
