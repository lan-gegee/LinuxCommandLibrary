# TAGLINE

配合 CLOC 统计代码行数的 TUI 工具

# TLDR

**扫描**目录中的代码行数

```cloctui [path/to/directory]```

**扫描**当前目录

```cloctui .```

以全屏模式**扫描**

```cloctui [path/to/directory] -f```

通过 uvx **免安装试用**

```uvx cloctui .```

# SYNOPSIS

**cloctui** [_path_] [**-f**]

# PARAMETERS

**path**
> 要用 CLOC 分析的目录路径。如果省略，则显示用法说明。

**-f**, **--fullscreen**
> 以全屏模式运行，而非默认的内嵌模式。

# DESCRIPTION

**cloctui** 是 **cloc**（Count Lines of Code）工具的终端用户界面包装器。cloctui 不显示原始文本输出，而是将 CLOC 的分析结果呈现在可排序、可浏览的交互式表格中，对大型代码库尤其有用。

功能包括多种分组模式（按编程语言、按目录或作为单个文件）、通过点击表头或使用键盘快捷键进行列排序，以及两种显示模式（内嵌或全屏）。

# CAVEATS

需要系统单独安装 **cloc**；cloctui 只是一个前端，不是独立的代码分析器。需要 Python 3.10 或更高版本。CLOC 的许多原生选项尚未通过 TUI 暴露出来。

# HISTORY

**cloctui** 由 **Edward Jazzhands** 创建，于 **2025 年 8 月**发布。其核心的 CLOC 包装功能改编自 Stefano Stone 的 **pycloc** 项目，并增加了基于 Textual 的 TUI。该项目以 MIT 许可证发布，使用 Python 编写。

# SEE ALSO

[cloc](/man/cloc)(1), [tokei](/man/tokei)(1), [scc](/man/scc)(1)
