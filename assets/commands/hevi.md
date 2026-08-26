# TAGLINE

带语法高亮的十六进制查看器

# TLDR

以十六进制**查看文件**

```hevi [path/to/file]```

**从 stdin 读取**

```cat [path/to/file] | hevi```

**禁用彩色输出**

```hevi --no-color [path/to/file]```

**使用大写十六进制数字**

```hevi --uppercase [path/to/file]```

**强制指定解析器**（例如 elf、pe）

```hevi --parser [elf] [path/to/file]```

**原始模式**（禁用大小、偏移、ASCII 列）

```hevi --raw [path/to/file]```

**显示当前使用的调色板**

```hevi --show-palette```

# SYNOPSIS

**hevi** _file_ [_flags_]

# DESCRIPTION

**hevi**（读音同 "heavy"）是一个类似于 **xxd** 或 **hexdump** 的十六进制查看器，额外增加了对 **ELF** 和 **PE** 可执行文件等结构化文件格式的解析能力，并能对识别出的区域进行**语法高亮**。这使你更容易从视觉上辨认二进制文件中的头部、节和数据区域。

可以使用标准 ANSI 颜色或 truecolor 自定义调色板。查看器以整洁的彩色布局显示偏移地址、十六进制值和 ASCII 表示。行为可以通过标志、配置文件或环境变量（包括 **NO_COLOR**）控制，标志优先级最高。

# PARAMETERS

**-h**, **--help**
> 显示帮助信息

**-v**, **--version**
> 打印版本信息

**--color**, **--no-color**
> 启用或禁用彩色输出

**--lowercase**, **--uppercase**
> 选择十六进制数字的大小写

**--size**, **--no-size**
> 显示或隐藏大小列

**--offset**, **--no-offset**
> 显示或隐藏偏移列

**--ascii**, **--no-ascii**
> 显示或隐藏 ASCII 表示

**--skip-lines**, **--no-skip-lines**
> 折叠或保留重复的相同行

**--raw**
> 原始输出，禁用大部分修饰

**--parser** _NAME_
> 强制使用指定的文件格式解析器（例如 elf、pe）

**--show-palette**
> 打印当前使用的调色板并退出

# CAVEATS

只读查看器，无法编辑文件。格式解析仅限于受支持的文件类型（ELF、PE）。自定义调色板需要支持 truecolor 的终端才能完整呈现。

# HISTORY

**hevi** 由 **Arnau478** 创建，使用 **Zig** 编写。其设计目标是在传统十六进制查看器的基础上，增加对常见二进制格式的结构感知能力。

# INSTALL

```brew: brew install hevi```

```nix: nix profile install nixpkgs#hevi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hexyl](/man/hexyl)(1), [xxd](/man/xxd)(1), [hexdump](/man/hexdump)(1), [readelf](/man/readelf)(1)
