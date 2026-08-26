# TAGLINE

创建和管理静态库归档

# TLDR

从文件**创建**归档

```ar rcs [archive.a] [file1.o] [file2.o]```

**列出**归档内容

```ar t [archive.a]```

**解压**所有文件

```ar x [archive.a]```

**解压**指定文件

```ar x [archive.a] [file.o]```

向归档中**添加**文件

```ar r [archive.a] [newfile.o]```

从归档中**删除**文件

```ar d [archive.a] [file.o]```

# SYNOPSIS

**ar** [_-X32_64_] [_-_]_operation_[_modifiers_] _archive_ [_files_...]

# DESCRIPTION

**ar** 用于创建、修改归档以及从中提取文件。它主要用于从目标文件创建静态库（.a 文件），供链接器使用。

归档包含多个文件并带有目录表，便于快速访问。与 tar 不同，ar 针对单个成员的随机访问做了优化。

# PARAMETERS

**r**
> 插入（替换）文件

**c**
> 创建归档

**s**
> 创建/更新归档索引（相当于 ranlib）

**t**
> 显示目录表

**x**
> 提取文件

**d**
> 删除文件

**p**
> 将文件内容打印到标准输出

**q**
> 快速追加（不检查）

**v**
> 详细输出

**u**
> 只更新较新的文件

# CAVEATS

主要用于静态库。一般性归档请改用 tar。链接器要使用该库需要归档索引（s）。不提供压缩。

# HISTORY

**ar** 可追溯到 **1970 年代**的早期 Unix。它比 tar 更早出现，最初是通用归档工具，后来专门用于库创建。

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

[ranlib](/man/ranlib)(1), [nm](/man/nm)(1), [objdump](/man/objdump)(1), [tar](/man/tar)(1), [ld](/man/ld)(1)
