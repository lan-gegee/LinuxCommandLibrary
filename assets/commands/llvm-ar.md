# TAGLINE

用于创建和操作静态库归档的归档工具

# TLDR

**从目标文件创建归档**

```llvm-ar rcs [libname.a] [file1.o] [file2.o]```

**列出归档内容**

```llvm-ar t [archive.a]```

**从归档中提取文件**

```llvm-ar x [archive.a]```

**向归档添加文件**

```llvm-ar r [archive.a] [file.o]```

**从归档删除文件**

```llvm-ar d [archive.a] [file.o]```

# SYNOPSIS

**llvm-ar** [_options_] _operation_ _archive_ [_files_...]

# PARAMETERS

**r**
> 替换或向归档添加文件。

**c**
> 创建归档时不发出警告。

**s**
> 创建归档索引。

**t**
> 列出归档内容。

**x**
> 从归档提取文件。

**d**
> 从归档删除文件。

**--format** _type_
> 归档格式（gnu、darwin、bsd）。

# DESCRIPTION

**llvm-ar** 是 LLVM 的归档工具，用于创建和操作静态库归档。它是 GNU ar 的直接替代品，创建的归档与系统链接器兼容，可用于静态链接。

# INSTALL

```apt: sudo apt install llvm```

```dnf: sudo dnf install llvm```

```pacman: sudo pacman -S llvm```

```apk: sudo apk add llvm```

```zypper: sudo zypper install llvm```

```brew: brew install llvm```

```nix: nix profile install nixpkgs#llvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ar](/man/ar)(1)
