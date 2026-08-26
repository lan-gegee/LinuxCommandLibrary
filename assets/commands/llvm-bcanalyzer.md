# TAGLINE

分析 LLVM 位码文件

# TLDR

**分析位码文件**

```llvm-bcanalyzer [file.bc]```

**显示详细转储**

```llvm-bcanalyzer --dump [file.bc]```

**仅显示块信息统计**

```llvm-bcanalyzer --dump-blockinfo [file.bc]```

# SYNOPSIS

**llvm-bcanalyzer** [_options_] _file_

# PARAMETERS

**--dump**
> 转储底层位码内容。

**--dump-blockinfo**
> 显示块信息统计。

**--show-binary-blobs**
> 显示二进制 blob 数据。

# DESCRIPTION

**llvm-bcanalyzer** 用于分析 LLVM 位码文件。它显示关于位码结构的统计信息，包括块类型、记录数量和位分布。可用于调试位码生成以及理解 LLVM IR 的序列化方式。

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

[llvm-dis](/man/llvm-dis)(1), [llvm-as](/man/llvm-as)(1)
