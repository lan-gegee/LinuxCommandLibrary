# TAGLINE

Racket 的集成开发环境

# TLDR

**启动 DrRacket IDE**

```drracket```

**打开一个文件**

```drracket [file.rkt]```

**打开多个文件**

```drracket [file1.rkt] [file2.rkt]```

**直接运行 Racket 脚本**

```racket [script.rkt]```

# SYNOPSIS

**drracket** [_options_] [_file_...]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息。

**--version**
> 显示版本。

_file_
> 要打开的 Racket 源文件。

# DESCRIPTION

**DrRacket** 是 Racket 编程语言的集成开发环境。它提供带语法高亮的图形编辑器、REPL（读取-求值-打印循环）、调试工具以及教学功能。

该 IDE 通过语言声明支持多种 Racket 方言。它包含 check syntax（高亮变量绑定）、宏展开步进器和集成文档等功能。DrRacket 在编程教学中尤其流行。

# FEATURES

- 语法高亮与自动缩进
- 带定义窗口的交互式 REPL
- 带绑定箭头的 Check Syntax
- 宏展开步进器
- 集成的帮助与文档
- 面向教学的多种语言层级

# CAVEATS

DrRacket 是 GUI 应用，随 Racket 完整发行版提供，而非最小发行版；`racket-minimal` 安装完全没有 DrRacket。非交互式工作请用 **racket** 运行程序，用 **raco** 编译、测试和打包。

**语言层级**由文件顶部的 `#lang` 行决定，而不是 IDE——这一点常让照着教科书学习的初学者栽跟头：以 `#lang htdp/bsl` 开头的文件被刻意限制在教学子集内，不改动这一行的话，Racket 的大部分功能看起来就像不存在。*Beginning Student* 层级产生的错误信息也是为新手调校的，而非精确的报错。

它不是通用编辑器。处理大文件时反应迟缓；当 Emacs、Vim 和 VS Code 都有称职的 Racket 模式时，没必要和它较劲。DrRacket 的价值在于 Check Syntax、宏步进器和调试器——这些功能确实难以在其他地方复刻。

# HISTORY

DrRacket 始于 **DrScheme**，由 Matthias Felleisen 领导的 **PLT** 团队打造，起始于上世纪 **90 年代**中期的莱斯大学，后延续至东北大学。它与《How to Design Programs》教材同步设计，其核心理念是**语言层级**：初学者的错误应当产生一条针对其所写内容的报错，而不是来自尚未学到的语言深处的一条晦涩消息。这一理念催生了分级的学生语言，而 Racket 后来将 `#lang` 发展为定义新语言的通用机制，很大程度上也源于此。

**2010 年**，随着 PLT Scheme 更名为 Racket，它也改名为 DrRacket——彼时该项目早已超出"Scheme"这一名号的合理范畴。

# INSTALL

```apt: sudo apt install racket```

```dnf: sudo dnf install racket```

```pacman: sudo pacman -S racket```

```zypper: sudo zypper install racket```

```brew: brew install racket```

```nix: nix profile install nixpkgs#racket```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[racket](/man/racket)(1), [raco](/man/raco)(1), [guile](/man/guile)(1), [sbcl](/man/sbcl)(1)

# RESOURCES

```[Source code](https://github.com/racket/racket)```

```[Homepage](https://racket-lang.org)```

```[Documentation](https://docs.racket-lang.org/drracket/index.html)```

<!-- verified: 2026-07-14 -->
