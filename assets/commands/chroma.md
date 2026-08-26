# TAGLINE

通用语法高亮工具

# TLDR

**高亮源文件**

```chroma [file.go]```

**指定语言**

```chroma -l python [file.py]```

**HTML 输出**

```chroma --html [file.js] > [output.html]```

**列出可用的词法分析器**

```chroma --list```

**使用特定样式**

```chroma -s monokai [file.rb]```

**带内联样式的 HTML**

```chroma --html --html-inline-styles [file.c]```

# SYNOPSIS

**chroma** [_options_] [_file_...]

# DESCRIPTION

**chroma** 是一个通用语法高亮工具，支持约 250 种语言。它可将源代码转换为带语法高亮的 HTML、ANSI 彩色终端输出、SVG 等格式。

该工具基于 Pygments 高亮引擎，但用 Go 重新实现，速度更快且易于嵌入。它支持众多配色样式（monokai、dracula、github 等），并能根据文件名和内容自动检测语言。Chroma 也可以作为 Go 库使用，Hugo 等工具就用它做代码高亮。

# PARAMETERS

**-l**, **--lexer** _name_
> 要使用的词法分析器（默认：自动检测）

**-s**, **--style** _name_
> 高亮样式

**-f**, **--formatter** _name_
> 输出格式化器：terminal、terminal256、terminal16m、html

**--html**
> 启用 HTML 模式

**--html-only**
> 仅输出 HTML 片段

**--html-inline-styles**
> 内联 CSS 样式（不使用 class）

**--list**
> 列出词法分析器、样式和格式化器

**--fail**
> 找不到词法分析器时以状态码 1 退出

# USAGE WITH LESS

```bash
export LESSOPEN='| chroma --fail "$1" || cat "$1"; "%s"'
```

# CAVEATS

根据文件名和内容自动检测语言。在回退管道中使用 --fail。

# INSTALL

```apt: sudo apt install golang-chroma```

```brew: brew install chroma```

```nix: nix profile install nixpkgs#chroma```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[highlight](/man/highlight)(1), [pygmentize](/man/pygmentize)(1), [bat](/man/bat)(1)

# RESOURCES

```[Source code](https://github.com/alecthomas/chroma)```

<!-- verified: 2026-06-22 -->
