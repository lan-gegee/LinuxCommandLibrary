# TAGLINE

将目标文件的内容复制到另一个文件，并可选择进行转换

# TLDR

**复制**目标文件到新路径

```objcopy [source] [dest]```

**剥离所有符号**到新文件

```objcopy --strip-all [source] [dest]```

仅剥离 **debug** 区段

```objcopy --strip-debug [source] [dest]```

只复制**单个区段**

```objcopy --only-section=[section] [source] [dest]```

在目标文件**格式**之间转换

```objcopy --input-target=[in_fmt] --output-target=[out_fmt] [source] [dest]```

# SYNOPSIS

**objcopy** [**-F** _bfdname_ | **--target=**_bfdname_] [**-I** _bfdname_ | **--input-target=**_bfdname_] [**-O** _bfdname_ | **--output-target=**_bfdname_] [_options_] _infile_ [_outfile_]

# PARAMETERS

**-I** _bfdname_, **--input-target=**_bfdname_
> 将源文件的目标格式视为 _bfdname_

**-O** _bfdname_, **--output-target=**_bfdname_
> 以目标格式 _bfdname_ 写出输出文件

**-F** _bfdname_, **--target=**_bfdname_
> 输入和输出都使用 _bfdname_ 格式

**-j** _name_, **--only-section=**_name_
> 仅将指定区段复制到输出

**-R** _name_, **--remove-section=**_name_
> 从输出中移除指定区段

**-S**, **--strip-all**
> 移除所有符号和重定位信息

**-g**, **--strip-debug**
> 仅移除调试符号

**--only-keep-debug**
> 剥离除调试信息之外的所有内容

**--add-gnu-debuglink=**_file_
> 添加指向 _file_ 的 .gnu_debuglink 区段

**--dump-section** _name_=_file_
> 将区段 _name_ 的内容转储到 _file_

**--rename-section** _old_=_new_[,_flags_]
> 将区段 _old_ 重命名为 _new_，可带标志

**-B** _bfdarch_, **--binary-architecture=**_bfdarch_
> 当输入为二进制格式时设置架构

**-i**, **--info**
> 列出所有可用的 BFD 目标格式

# DESCRIPTION

**objcopy** 将一个目标文件的内容复制到另一个文件，并可在过程中进行转换。它使用 GNU BFD 库读写多种格式的目标文件，包括 ELF、COFF、S-records 和原始二进制。

常见用途包括：剥离符号以减小二进制体积、将调试信息提取到单独的文件、在可执行格式之间转换（例如为嵌入式系统将 ELF 转为原始二进制），以及复制或移除目标文件中的特定区段。

# CAVEATS

无法更改输入文件的字节序；目标格式的字节序必须与源一致或本身无字节序（如 S-records）。在不同格式间复制可重定位目标文件可能无法完整保留所有信息。完全链接的可执行文件跨格式复制的可靠性更高。

# HISTORY

属于 **GNU Binutils**，于 **1991 年**与 objdump、nm 等其他二进制工具一同首次发布。其开发目的是配合 GNU 工具链（GCC、GAS、ld）进行跨平台开发和嵌入式系统编程。

# INSTALL

```apt: sudo apt install binutils```

```dnf: sudo dnf install binutils```

```pacman: sudo pacman -S binutils```

```apk: sudo apk add binutils```

```zypper: sudo zypper install binutils```

```brew: brew install binutils```

```nix: nix profile install nixpkgs#binutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[objdump](/man/objdump)(1), [strip](/man/strip)(1), [readelf](/man/readelf)(1), [nm](/man/nm)(1), [ld](/man/ld)(1)
