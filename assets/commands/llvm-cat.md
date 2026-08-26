# TAGLINE

将多个 LLVM 位码文件拼接为单个位码文件

# TLDR

将位码文件**拼接为单个输出**

```llvm-cat -o [output.bc] [file1.bc] [file2.bc]```

使用 glob **拼接多个位码文件**

```llvm-cat -o [combined.bc] [*.bc]```

**生成包含内嵌模块的模块**（二进制捆绑包）

```llvm-cat -b -o [bundle.bc] [file1.bc] [file2.bc]```

# SYNOPSIS

**llvm-cat** [_-o_ _output_] [_-b_] _files_...

# PARAMETERS

**-o** _file_
> 将输出位码写入 _file_（默认写到标准输出）。

**-b**
> 生成二进制捆绑包。将每个输入模块作为独立模块内嵌到输出中，而不是把它们链接在一起。

**--help**
> 显示帮助信息。

# DESCRIPTION

**llvm-cat** 用于拼接 LLVM 位码文件。默认情况下，它生成一个包含所有输入链接后内容的单个位码模块。使用 **-b** 时，它生成一个捆绑包，其中每个输入仍保持为独立的内嵌模块，适用于需要操作多个模块但不合并它们的工具。

它属于 LLVM 工具链，通常用于需要在链接、优化或分析之前聚合位码的构建系统，配合 **llvm-link**、**opt** 或 **llc** 使用。

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

[llvm-dis](/man/llvm-dis)(1), [llvm-as](/man/llvm-as)(1), [llvm-bcanalyzer](/man/llvm-bcanalyzer)(1)
