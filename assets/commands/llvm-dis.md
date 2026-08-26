# TAGLINE

LLVM 位码反汇编器

# TLDR

**将位码反汇编为 LLVM IR**

```llvm-dis [file.bc]```

**输出到指定文件**

```llvm-dis [file.bc] -o [output.ll]```

**从 stdin 反汇编到 stdout**

```llvm-dis -o - < [file.bc]```

**反汇编并显示每个 pass 的耗时**

```llvm-dis --time-passes [file.bc]```

**显示版本**

```llvm-dis --version```

# SYNOPSIS

**llvm-dis** [_options_] [_file_]

# PARAMETERS

**-o** _file_
> 输出文件名。若省略，则使用带 .ll 扩展名的输入文件名。

**-f**, **--force**
> 允许在终端上输出二进制数据并覆盖已有的输出文件。

**--show-annotations**
> 在输出中显示注解。

**--disable-output**
> 丢弃输出（与 --time-passes 配合可用于基准测试）。

**--time-passes**
> 在反汇编期间统计每个 pass 的耗时。

**--help**
> 显示可用选项。

**--version**
> 显示 LLVM 版本。

# DESCRIPTION

**llvm-dis** 是 LLVM 反汇编器，将 LLVM 位码（.bc）文件转换为人类可读的 LLVM 汇编语言（.ll）格式。如果未给出文件名或文件名为 -，则从 stdin 读取。适用于检查编译后的代码以及调试 LLVM 优化 pass。

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

[llvm-as](/man/llvm-as)(1), [llc](/man/llc)(1), [opt](/man/opt)(1), [llvm-bcanalyzer](/man/llvm-bcanalyzer)(1), [llvm-objdump](/man/llvm-objdump)(1), [clang](/man/clang)(1)
