# TAGLINE

从简单的标记语言生成 man page

# TLDR

**生成 man page**

```scdoc < [input.scd] > [output.1]```

**编译为 roff**

```scdoc < [file.scd]```

**查看生成的页面**

```scdoc < [file.scd] | man -l -```

# SYNOPSIS

**scdoc** < _input_ > _output_

# DESCRIPTION

**scdoc** 从一种简单易读的标记语法生成 roff 格式的 man page。作者无需编写原始的 roff 宏，只需使用带有类 Markdown 标题、段落和列表的轻量格式，即可编译为排版规范的 man page。

每篇文档的第一行定义元数据，包括命令名和 section 编号。各节使用 **#** 标题标记，与标准 man page 约定一致（NAME、SYNOPSIS、DESCRIPTION 等）。文本格式化采用 **\*bold\*** 和 **\_italic\_** 语法，输出是标准 roff，可由 **man** 命令直接渲染。

该工具从标准输入读取并写到标准输出，天然适合构建系统流水线。这使得它很容易集成到项目中，让文档与代码一同编译。

# SYNTAX

```
command(1)

# NAME

command - description

# SYNOPSIS

*command* [_options_]

# DESCRIPTION

Text paragraph.

*bold* _italic_
```

# CAVEATS

语法简单、功能有限。不支持表格。不如完整 roff 强大。

# HISTORY

**scdoc** 由 **Drew DeVault** 为 sway 项目创建。它为编写 man page 提供了比手写 roff 更简单的选择。

# INSTALL

```apt: sudo apt install scdoc```

```dnf: sudo dnf install scdoc```

```pacman: sudo pacman -S scdoc```

```apk: sudo apk add scdoc```

```zypper: sudo zypper install scdoc```

```brew: brew install scdoc```

```nix: nix profile install nixpkgs#scdoc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [groff](/man/groff)(1), [pandoc](/man/pandoc)(1), [ronn](/man/ronn)(1)
