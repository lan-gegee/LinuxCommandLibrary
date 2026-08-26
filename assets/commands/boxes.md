# TAGLINE

围绕文本绘制 ASCII 字符画边框。

# TLDR

为文本**创建**边框

```echo ["Hello World"] | boxes```

使用**指定**样式

```echo ["Text"] | boxes -d [stone]```

**列出**可用样式

```boxes -l```

**移除**边框

```cat [boxed.txt] | boxes -r```

# SYNOPSIS

**boxes** [_options_] [_file_]

# DESCRIPTION

**boxes** 是一个文本过滤器，可以在文本周围绘制 ASCII 字符画边框。它支持大量边框样式，既能添加也能移除边框，适合在源代码和文档中创建醒目的注释、标题或装饰性文本。

该工具提供 50 多种预定义的边框样式，并支持自定义选项。

# PARAMETERS

**-d** _design_
> 要使用的边框样式。

**-l**
> 列出可用样式及示例。

**-r**
> 移除已有的边框（自动检测样式；可与 -d 结合以提示样式）。

**-a** _format_
> 文本在边框内的对齐/定位方式（如 `hcvc` 表示水平和垂直居中）。

**-s** _WxH_
> 所需的边框尺寸：列数（宽）× 行数（高）。

**-p** _format_
> 输入周围的填充（如 `a1l3` = 四周各 1 个空格，左侧再加 3 个空格）。

**-f** _file_
> 使用备用配置文件。

**-i** _indent_
> 输入内容的缩进模式（`box`、`text` 或 `none`）。

**-n** _encoding_
> 输入/输出的字符编码。

**-t** _tabopts_
> 制表符处理选项（展开/保留/还原）。

**-k** _bool_
> 处理输入中首尾空行的方式。

**-e** _eol_
> 强制指定换行风格（`unix`、`dos`、`mac`）。

**-c** _string_
> 快捷方式：用给定字符作为边框创建一个基本边框。

**-h**
> 打印用法信息。

**-v**
> 打印版本信息。

# POPULAR DESIGNS

- **stone** - 石墙风格
- **dog** - ASCII 小狗
- **cat** - ASCII 小猫
- **parchment** - 卷轴/羊皮纸
- **spring** - 弹簧/线圈
- **santa** - 圣诞老人
- **c-cmt** - C 注释块
- **java-cmt** - Java 注释块

# WORKFLOW

```bash
# Simple box
echo "Hello" | boxes

# Specific design
echo "Warning" | boxes -d stone

# List all designs
boxes -l

# Remove box
cat file.txt | boxes -r

# Custom alignment
echo "Centered" | boxes -a c
```

# CAVEATS

过宽的文本可能超出终端宽度。某些样式需要等宽字体。自定义样式的配置文件语法较为复杂。对已被修改过的边框，移除效果并不完美。

# HISTORY

**boxes** 由 Thomas Jensen 于 **1999 年**创建，受类似 DOS 实用工具的启发，用于为文本绘制装饰性 ASCII 边框。

# INSTALL

```apt: sudo apt install boxes```

```dnf: sudo dnf install boxes```

```brew: brew install boxes```

```nix: nix profile install nixpkgs#boxes```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(6), [cowsay](/man/cowsay)(1), [banner](/man/banner)(6)
