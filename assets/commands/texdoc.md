# TAGLINE

查看 TeX Live 中的 TeX/LaTeX 软件包文档

# TLDR

**打开软件包的文档**

```texdoc [package-name]```

**列出匹配的文档**而不打开

```texdoc -l [package-name]```

跨文档进行**全文搜索**

```texdoc -s [query]```

**用指定的 PDF 查看器打开**

```texdoc --viewer=[evince] [package-name]```

**显示文件路径**而不打开

```texdoc -f [package-name]```

在多个匹配之间**交互式选择**

```texdoc -I [package-name]```

一次**打开多个软件包**

```texdoc [package1] [package2] [package3]```

# SYNOPSIS

**texdoc** [_options_] _name_...

# PARAMETERS

**-l**, **--list**
> 显示带编号的匹配列表；提示用户选择其一。

**-s**, **--search**
> 跨文档树进行全文搜索。

**-I**, **--interact**
> 强制交互模式（与 **--nointeract** 相对）。

**-M**, **--machine**
> 机器可读输出：每个匹配一行（文件路径、得分、名称）。

**-f**, **--files**
> 打印匹配文件的路径而不打开它们。

**-w**, **--view**
> 查看文档（默认动作）。

**-m**, **--mixed**
> 结合名称搜索与全文搜索（当名称与内容重叠时有用）。

**--viewer** _CMD_
> 覆盖已配置的 PDF 查看器。

**-D**, **--debug**
> 将调试输出打印到 stderr。

**-q**, **--quiet**
> 抑制信息性消息。

**-v**, **--verbose**
> 提高详细程度。

**-V**, **--version**
> 显示 texdoc 版本。

# DESCRIPTION

**texdoc** 用于查找并显示 TeX Live 发行版中安装的 TeX、LaTeX、ConTeXt 及相关软件包的文档。它在 **TEXMF** 树中搜索与某个软件包关联的文件——通常是 PDF 手册，有时是 README、.txt 或 .html——并在配置的查看器中打开最佳匹配。

当存在多个匹配时，**-l** 会提示选择，而 **-s** 会把搜索范围扩大到文档内容（使用 texdoc-fulltext 索引）。查看器从配置文件（**~/.texlive*/texmf-config/texdoc/texdoc.cnf**）或 **PDFVIEWER** / **BROWSER** 环境变量中选择。

# CONFIGURATION

**texdoc.cnf**
> 按用户的配置文件，控制查看器选择、模式别名和语言偏好。在 **TEXMFCONFIG**、**TEXMFVAR**、**TEXMFHOME** 等位置查找。

**TEXDOCS**
> kpathsea 变量，控制 texdoc 在何处查找文档文件。

# CAVEATS

需要安装了文档包的 TeX Live（或 MiKTeX）；最小化的 "scheme-small" 安装不附带文档。并非所有软件包都提供 PDF 格式的文档。全文搜索依赖于已安装的 **texdoc-fulltext** 软件包。

# HISTORY

**texdoc** 是 TeX Live 的一部分，用 Lua 编写并随 **luatex** 捆绑发布。早期的 shell 脚本版本在 **TeX Live 2009** 中被 Lua 实现取代。

# INSTALL

```pacman: sudo pacman -S texlive-binextra```

```apk: sudo apk add texlive-binextra```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tlmgr](/man/tlmgr)(1), [latex](/man/latex)(1), [pdflatex](/man/pdflatex)(1)
