# TAGLINE

以系统级方式管理 TeX 格式文件和 Metafont 基础库

# TLDR

**重建所有**系统格式文件

```fmtutil-sys --all```

只创建**缺失的**系统格式文件

```fmtutil-sys --missing```

**重建 pdflatex** 格式

```fmtutil-sys --byfmt pdflatex```

**重建 pdftex** 引擎的**格式文件**

```fmtutil-sys --byengine pdftex```

**列出**格式配置

```fmtutil-sys --listcfg```

# SYNOPSIS

**fmtutil-sys** [_OPTION_]... [_COMMAND_]

# DESCRIPTION

**fmtutil-sys** 是 **fmtutil** 的系统级形式。它将 TeX 格式文件和 Metafont 基础库重建到 TEXMFSYSVAR 中（通常位于 TeX Live 目录树下），并从 TEXMFSYSCONFIG、TEXMFLOCAL 和 TEXMFDIST 等目录树读取系统配置。

对于几乎所有安装而言，这都是推荐的模式：软件包管理器和 **tlmgr** 更新都期望格式文件位于系统位置。除非你有意维护私有的按用户格式，否则请优先使用 **fmtutil-sys** 而非 **fmtutil-user**。

必须且只能给出一个命令（**--all**、**--missing**、**--byfmt** 等）。完整的选项集参见 **fmtutil**；**fmtutil-sys** 等同于 **fmtutil --sys**。

# PARAMETERS

**--all**
> 重新创建所有格式文件

**--missing**
> 创建所有缺失的格式文件

**--byfmt** _FORMAT_
> （重新）创建 FORMAT 格式

**--byengine** _ENGINE_
> （重新）创建用 ENGINE 构建的格式

**--byhyphen** _HYPHENFILE_
> （重新）创建依赖 HYPHENFILE 的格式

**--refresh**
> 仅重新创建已存在的格式文件

**--listcfg**
> 列出经过滤的可用格式配置

**--enablefmt** _FORMAT_[/_ENGINE_]
> 启用 FORMAT

**--disablefmt** _FORMAT_[/_ENGINE_]
> 禁用 FORMAT

**--cnffile** _FILE_
> 读取替代的 **fmtutil.cnf**（可重复使用）

**--fmtdir** _DIR_
> 将格式写入 DIR 目录下

**--dry-run**, **-n**
> 不实际构建格式

**--quiet**
> 保持静默

**--version**, **--help**
> 显示版本或帮助并退出

# CAVEATS

通常需要对 TeX Live 系统目录树的写权限（root 或 texlive 管理员账户）。如果用户此前运行过 **fmtutil-user**，那么在该账户下其 TEXMFVAR 中的格式文件仍会覆盖系统版本，直到被删除。执行 **--all** 构建可能需要几分钟。

# HISTORY

属于 TeX Live 多 **fmtutil** 设计的一部分；**fmtutil-sys** 选择系统目录树的方式与 **updmap-sys** 处理字体映射的方式一致。迁移细节请参阅 TeX Live 的 sys-vs-user 文档。

# INSTALL

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fmtutil](/man/fmtutil)(1), [fmtutil-user](/man/fmtutil-user)(1), [mktexfmt](/man/mktexfmt)(1), [kpsewhich](/man/kpsewhich)(1), [tlmgr](/man/tlmgr)(1)

# RESOURCES

```[Documentation](https://tug.org/texlive/scripts-sys-user.html)```

```[Homepage](https://tug.org/texlive/)```

<!-- verified: 2026-07-17 -->
