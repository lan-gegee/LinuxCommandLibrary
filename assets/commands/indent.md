# TAGLINE

按指定的风格规范重新排版 C 源代码

# TLDR

**格式化 C 源文件**

```indent [source.c]```

**按特定风格格式化**

```indent -kr [source.c]```

**GNU 风格格式化**

```indent -gnu [source.c]```

**BSD 风格格式化**

```indent -orig [source.c]```

**输出到另一个文件**

```indent [input.c] -o [output.c]```

**将制表符宽度设为 4 个空格**

```indent -ts4 [source.c]```

**将每级缩进设为 4 个空格**

```indent -i4 [source.c]```

# SYNOPSIS

**indent** [_options_] _file_ [_output_]

# PARAMETERS

**-kr**
> Kernighan & Ritchie 风格。

**-gnu**
> GNU 编码风格。

**-orig**
> 原始 BSD 风格。

**-linux**
> Linux 内核风格。

**-ts** _N_
> 设置制表符大小。

**-i** _N_
> 设置缩进级别。

**-l** _N_
> 最大行长度。

**-o** _FILE_
> 输出文件。

**-npro**
> 不读取 .indent.pro 配置文件。

**-bad**
> 强制在声明后加空行。

**-bap**
> 强制在过程体后加空行。

**-nbc**
> 不强制在声明中的逗号后换行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**indent** 会按指定的风格规范重新排版 C 源代码，处理缩进、花括号位置、空格和换行等。

该工具支持预定义风格（K&R、GNU、BSD）以及大量自定义选项。它可以直接修改原文件，也可以写入新文件。

# CAVEATS

仅针对 C 语言，不能很好地处理 C++ 或其他语言。处理复杂宏或预处理指令时可能改变语义。默认直接修改文件；使用 **-o** 可写入单独的文件。配置可保存在 **.indent.pro** 文件中，会自动从当前目录或主目录加载。

# HISTORY

indent 起源于 **BSD Unix**。GNU 版本是 GNU 项目的一部分，扩展了更多选项。

# INSTALL

```apt: sudo apt install indent```

```dnf: sudo dnf install indent```

```pacman: sudo pacman -S indent```

```apk: sudo apk add indent```

```zypper: sudo zypper install indent```

```nix: nix profile install nixpkgs#indent```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clang-format](/man/clang-format)(1), [astyle](/man/astyle)(1), [cb](/man/cb)(1)
