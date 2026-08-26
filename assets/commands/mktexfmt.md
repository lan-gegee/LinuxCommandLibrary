# TAGLINE

按需创建单个 TeX 格式或 Metafont 基础文件

# TLDR

**构建** **pdflatex** 格式

```mktexfmt pdflatex.fmt```

**用纯格式名构建**

```mktexfmt latex```

**构建** Metafont 基础文件

```mktexfmt mf.base```

# SYNOPSIS

**mktexfmt** _FORMAT.fmt_|_BASE.base_|_FMTNAME_

# DESCRIPTION

**mktexfmt** 是 **fmtutil** 的受限前端，用于创建**恰好一个**格式或 Metafont 基础文件。当所需的 **.fmt** 文件缺失时，TeX 引擎会自动调用它（即时格式生成）。

参数可以是带扩展名的完整转储名（**pdflatex.fmt**、**mf.base**），也可以是纯格式名——此时等同于传入 **--byfmt** 参数。成功时，**mktexfmt** 仅将生成文件的完整路径写入标准输出，不输出任何其他内容。选项只接受 **--help** 和 **--version**。

如果系统格式目录（TEXMFSYSVAR）可写，格式就写在那里；否则使用用户目录（TEXMFVAR）。

# PARAMETERS

_FORMAT.fmt_ | _BASE.base_ | _FMTNAME_
> 要构建的格式或基础文件的名称。带扩展名时按转储文件名处理；不带时视为 **--byfmt** 参数

**--help**
> 显示帮助并退出

**--version**
> 显示版本并退出

# CAVEATS

与 **fmtutil** 不同，每次调用只能构建一个格式。构建失败通常会导致触发 **mktexfmt** 的引擎无法启动；请修复底层的 **fmtutil.cnf** / 引擎安装问题，然后用 **fmtutil-sys --byfmt** 重新构建。输出刻意保持精简，以便调用方捕获生成的路径。

# HISTORY

属于围绕 **fmtutil** 的 TeX Live / kpathsea 工具链，在格式未预先生成时用作按需的格式构建器。

# INSTALL

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fmtutil](/man/fmtutil)(1), [fmtutil-sys](/man/fmtutil-sys)(1), [fmtutil-user](/man/fmtutil-user)(1), [kpsewhich](/man/kpsewhich)(1), [pdflatex](/man/pdflatex)(1)

# RESOURCES

```[Documentation](https://tug.org/texlive/doc/fmtutil.html)```

```[Homepage](https://tug.org/texlive/)```

<!-- verified: 2026-07-17 -->
