# TAGLINE

管理 TeX 格式文件和 Metafont 基础

# TLDR

**重建全部**格式（优先使用 sys/user 包装器）

```fmtutil --sys --all```

仅**创建缺失的**格式

```fmtutil --sys --missing```

按名称**重建一个**格式

```fmtutil --sys --byfmt pdflatex```

为指定引擎**重建格式**

```fmtutil --sys --byengine pdftex```

**列出**已配置的格式

```fmtutil --sys --listcfg```

# SYNOPSIS

**fmtutil** [**-user**|**-sys**] [_OPTION_]... [_COMMAND_]

# DESCRIPTION

**fmtutil** 重建并管理 TeX 格式文件与 Metafont 基础（统称"formats"）。格式是预先转储的引擎状态（例如 **pdflatex.fmt**），可让后续 TeX 运行快得多。

自 TeX Live 2017 起，应优先使用显式包装器 **fmtutil-sys** 和 **fmtutil-user**，或传入 **-sys** / **-user**。不带模式调用裸 **fmtutil** 会打印警告。对几乎所有安装而言，最佳实践是使用**系统模式**，让生成的文件落在 TEXMFSYSVAR 下并与软件包更新保持一致。

必须给出恰好一个命令（**mktexfmt** 模式除外）。配置由通过 **kpsewhich** 找到的所有 **fmtutil.cnf** 文件合并而来。

# PARAMETERS

**-sys**
> 使用系统树 TEXMFSYSVAR / TEXMFSYSCONFIG（同 **fmtutil-sys**）

**-user**
> 使用用户树 TEXMFVAR / TEXMFCONFIG（同 **fmtutil-user**）

**--all**
> 重新创建所有格式文件

**--missing**
> 创建所有缺失的格式文件

**--byfmt** _FORMAT_
> （重新）创建格式 FORMAT

**--byengine** _ENGINE_
> （重新）创建用 ENGINE 构建的格式

**--byhyphen** _HYPHENFILE_
> （重新）创建依赖 HYPHENFILE 的格式

**--refresh**
> 仅重新创建已存在的格式

**--enablefmt** _FORMAT_[/_ENGINE_]
> 启用 FORMAT（可针对特定引擎）

**--disablefmt** _FORMAT_[/_ENGINE_]
> 禁用 FORMAT

**--listcfg**
> 列出可用格式的启用与禁用配置

**--showhyphen** _FORMAT_
> 打印 FORMAT 对应的连字符文件名

**--cnffile** _FILE_
> 读取 FILE 而非默认的 **fmtutil.cnf**（可重复）

**--fmtdir** _DIR_
> 将格式写入 DIR 而非 TEXMF[SYS]VAR

**--dry-run**, **-n**
> 不实际构建格式

**--quiet**
> 静默模式

**--nohash**
> 不更新 ls-R 文件

**--no-strict**
> 即使某个格式构建失败也正常退出

**--version**, **--help**
> 显示版本或帮助并退出

# CAVEATS

以**用户**模式运行一次后，TEXMFVAR 下写入的格式会永久覆盖系统格式，直到删除这些用户文件为止。除非有意维护私有格式，否则请优先使用 **fmtutil-sys** / **-sys**。构建全部格式可能耗时很长，并且需要完整的 TeX Live 引擎集合。

# HISTORY

最初由 Thomas Esser 为 teTeX 编写；现作为 TeX Live 的一部分维护。**-user** / **-sys** 的划分以及专用的 **fmtutil-user** / **fmtutil-sys** 命令大约在 TeX Live 2017 中引入。

# INSTALL

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fmtutil-sys](/man/fmtutil-sys)(1), [fmtutil-user](/man/fmtutil-user)(1), [mktexfmt](/man/mktexfmt)(1), [kpsewhich](/man/kpsewhich)(1), [pdflatex](/man/pdflatex)(1), [latex](/man/latex)(1)

# RESOURCES

```[Documentation](https://tug.org/texlive/doc/fmtutil.html)```

```[Homepage](https://tug.org/texlive/)```

<!-- verified: 2026-07-17 -->
