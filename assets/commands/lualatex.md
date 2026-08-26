# TAGLINE

将 LaTeX 与 Lua 编程语言相结合的 TeX 引擎

# TLDR

**编译 LaTeX 文档**

```lualatex [document.tex]```

**编译到指定的输出目录**

```lualatex -output-directory=[output/] [document.tex]```

**以草稿模式编译**（更快，不处理图片）

```lualatex -draftmode [document.tex]```

**启用 shell 转义编译**（用于外部命令）

```lualatex -shell-escape [document.tex]```

**以指定交互模式编译**

```lualatex -interaction=[nonstopmode] [document.tex]```

**以指定作业名编译**

```lualatex -jobname=[output] [document.tex]```

**显示版本号**

```lualatex --version```

# SYNOPSIS

**lualatex** [_-output-directory=dir_] [_-shell-escape_] [_-interaction=mode_] [_options_] [_file.tex_]

# PARAMETERS

**-output-directory**=_DIR_
> 将输出文件写入该目录。

**-jobname**=_NAME_
> 设置输出文件的基本名。

**-interaction**=_MODE_
> 设置交互模式（batchmode、nonstopmode、scrollmode、errorstopmode）。

**-shell-escape**
> 启用 \\write18 shell 命令。

**-no-shell-escape**
> 禁用 shell 命令。

**-draftmode**
> 不生成输出运行，用于语法检查。

**-halt-on-error**
> 在第一个错误处停止。

**-file-line-error**
> 以 file:line:error 格式显示错误。

**-synctex**=_N_
> 生成 SyncTeX 数据以便与编辑器集成。

**-fmt**=_FORMAT_
> 使用指定的格式文件。

**--version**
> 打印版本信息。

**--help**
> 显示帮助。

# DESCRIPTION

**lualatex** 是一种将 LaTeX 与 Lua 编程语言相结合的 TeX 引擎。它在编译 LaTeX 文档的同时允许在文档中使用 Lua 脚本。

Lua 集成支持动态内容生成、复杂计算和程序化的文档操作。fontspec 宏包可以无缝处理 OpenType 和 TrueType 字体。

与 pdflatex 不同，lualatex 原生使用 UTF-8，无需额外的宏包。它可以直接访问系统字体，使字体管理更简单。

包含交叉引用、目录或参考文献的文档可能需要多次编译。latexmk 等工具可以自动化这一过程。

shell 转义模式允许执行外部程序，minted 等用于代码高亮的宏包需要此功能。在处理不受信任的文档时请谨慎使用。

# CAVEATS

由于 Lua 的开销，速度比 pdflatex 慢。部分宏包与 LuaTeX 不兼容。内存占用高于其他 TeX 引擎。处理引用时可能需要多次运行。

# HISTORY

**LuaTeX** 的开发始于 **2007 年**左右，由 **Hans Hagen**、**Hartmut Henkel** 和 **Taco Hoekwater** 主导。它将 pdfTeX 引擎与嵌入的 Lua 解释器相结合。lualatex 为 LuaTeX 提供 LaTeX 格式，已成为现代 LaTeX 开发的推荐引擎。

# INSTALL

```dnf: sudo dnf install texlive-luatex```

```pacman: sudo pacman -S texlive-luatex```

```apk: sudo apk add texlive-luatex```

```zypper: sudo zypper install texlive-luatex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pdflatex](/man/pdflatex)(1), [xelatex](/man/xelatex)(1), [latexmk](/man/latexmk)(1), [luatex](/man/luatex)(1), [texdoc](/man/texdoc)(1)
