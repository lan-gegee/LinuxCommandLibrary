# TAGLINE

源代码文档生成器

# TLDR

**生成默认配置**文件

```doxygen -g [Doxyfile]```

**生成文档**

```doxygen [Doxyfile]```

**生成并更新**配置

```doxygen -u [Doxyfile]```

**生成不带解释性注释的最小配置**

```doxygen -g -s [Doxyfile]```

**从标准输入读取配置**并生成

```cat [Doxyfile] | doxygen -```

**启动 GUI** 前端

```doxywizard```

# SYNOPSIS

**doxygen** [_configfile_]

**doxygen** [**-g**|**-u**|**-s**|**-l**|**-w**|**-x**] [_file_]

# PARAMETERS

_CONFIGFILE_
> 要使用的配置文件。默认为当前目录下的 `Doxyfile`。单独一个 **-** 表示从标准输入读取配置。

**-g** [_FILE_]
> 生成带有完整注释的模板配置文件。未给出名称时写入 `Doxyfile`。

**-u** [_FILE_]
> 将现有配置文件更新到当前 Doxygen 版本，保留你的设置并为新增选项填入默认值。

**-s**
> 省略解释性注释。与 **-g** 和 **-u** 组合可生成短小的配置，更利于放入版本控制。

**-x** [_FILE_]
> 打印给定配置与默认值之间的差异。这是查看项目实际改动了什么的最快方式。

**-l** [_FILE_]
> 生成布局文件（`DoxygenLayout.xml`），控制输出中各区块的顺序与有无。

**-w** _FORMAT_ ...
> 生成样式表或模板文件。_FORMAT_ 为 `html`、`latex` 或 `rtf`。

**-d** _MODE_
> 启用某种调试模式，如 `Preprocessor` 或 `FilterOutput`。

**-b**
> 以无缓冲输出运行，管道传输时进度能立即显现。

**-v**, **--version**
> 显示版本并退出。

**--help**
> 显示帮助信息。

# CONFIGURATION

**Doxyfile**
> 主配置文件，包含项目文档设置、输出格式和解析选项。

# DESCRIPTION

**Doxygen** 是 C++、C、Java、Python 等语言的标准文档生成器。它从源代码中特殊格式的注释提取文档，并生成 HTML、LaTeX、RTF 等格式的输出。

该工具解析源代码、构建交叉引用的文档结构，并以类图、调用图和继承树的形式呈现。特殊注释标记（///、/** 等）用于标识文档块。

Doxygen 能理解注释中的 Markdown，而且即使代码库完全没有文档注释，它也能照常工作——仅凭声明就生成每个类、函数和文件的可浏览交叉引用索引。这往往就是在陌生项目上运行它的充分理由。

除 C++ 和 C 外，它还支持 Java、Python、C#、PHP、Objective-C、Fortran 和 IDL，并且既能读取自己的注释风格，也能识别 Javadoc 和 Qt 风格的注释块。

# CAVEATS

生成的 `Doxyfile` 体量巨大，数百个设置配上连篇累牍的注释。用 **-g -s** 生成并只保留你改动的部分才便于审阅；继承来的配置到底改了什么，用 **-x** 一看便知。

图示是最常见的失望点。类层次、协作图、调用图和包含图都需要 **Graphviz**，因此必须把 `HAVE_DOT` 设为 `YES` 并保证 `dot` 在 PATH 中，否则 Doxygen 会静默退回到粗糙的内置图像。在大代码库上生成调用图还会产生海量图片，甚至让构建耗时数小时。

Doxygen 只记录它能解析的内容。大量预处理器用法、模板元编程以及展开成声明的宏常常让它困惑，`ENABLE_PREPROCESSING`、`MACRO_EXPANSION` 和 `PREDEFINED` 正是为绕过这些问题而存在的。另外输出的质量完全取决于注释的质量：如果希望文档保持完整，请在 CI 中启用 `WARN_IF_UNDOCUMENTED` 和 `WARN_AS_ERROR`。

# HISTORY

Doxygen 由 **Dimitri van Heesch** 编写，**1997 年**首次发布，最初只是一个为自己的 C++ 代码生成 Qt 风格文档的工具。它填补了一个明显的空白——Java 有 Javadoc 而 C++ 没有对应物——于是几乎顺理成章地成为 C 和 C++ 文档的事实标准。近三十年过去，它仍由 van Heesch 维护，如今托管在 GitHub 上。

# INSTALL

```apt: sudo apt install doxygen```

```dnf: sudo dnf install doxygen```

```pacman: sudo pacman -S doxygen```

```apk: sudo apk add doxygen```

```zypper: sudo zypper install doxygen```

```brew: brew install doxygen```

```nix: nix profile install nixpkgs#doxygen```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dot](/man/dot)(1), [cppcheck](/man/cppcheck)(1), [javadoc](/man/javadoc)(1), [sphinx-build](/man/sphinx-build)(1)

# RESOURCES

```[Source code](https://github.com/doxygen/doxygen)```

```[Homepage](https://www.doxygen.nl)```

```[Documentation](https://www.doxygen.nl/manual/index.html)```

<!-- verified: 2026-07-14 -->
