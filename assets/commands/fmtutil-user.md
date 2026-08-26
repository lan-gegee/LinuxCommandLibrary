# TAGLINE

为当前用户管理 TeX 格式和 Metafont 基础

# TLDR

**重建全部**用户本地格式

```fmtutil-user --all```

**创建缺失的**用户格式

```fmtutil-user --missing```

在用户树中**重建单个**格式

```fmtutil-user --byfmt pdflatex```

**列出**用户可见的格式配置

```fmtutil-user --listcfg```

# SYNOPSIS

**fmtutil-user** [_OPTION_]... [_COMMAND_]

# DESCRIPTION

**fmtutil-user** 是 **fmtutil** 的单用户形式。它将格式文件写入 TEXMFVAR（例如 **~/.texliveYYYY/texmf-var**），并可以从 TEXMFCONFIG / TEXMFHOME 读取额外配置。它等价于 **fmtutil --user**。

只有当格式需要对某个账户私有（例如 TEXMFHOME 下的实验性引擎）时，用户模式才合适。对于普通单用户或多用户机器，强烈建议使用 **fmtutil-sys**。

必须且只能给出一个命令。选项与 **fmtutil** / **fmtutil-sys** 相同。

# PARAMETERS

**--all**
> 在用户树中重新创建所有格式文件

**--missing**
> 创建所有缺失的格式文件

**--byfmt** _FORMAT_
> （重新）创建格式 FORMAT

**--byengine** _ENGINE_
> （重新）创建用 ENGINE 构建的格式

**--refresh**
> 仅重新创建已存在的格式文件

**--listcfg**
> 列出格式配置

**--enablefmt** _FORMAT_[/_ENGINE_]
> 启用 FORMAT

**--disablefmt** _FORMAT_[/_ENGINE_]
> 禁用 FORMAT

**--cnffile** _FILE_
> 读取替代的 **fmtutil.cnf**

**--dry-run**, **-n**
> 不实际构建格式

**--quiet**
> 静默模式

**--version**, **--help**
> 显示版本或帮助并退出

# CAVEATS

运行一次 **fmtutil-user** 之后，该账户的用户树格式将永远**覆盖**系统格式。此后系统格式的 **fmtutil-sys** 或软件包更新都不会生效，除非你（备份后）删除 TEXMFVAR/web2c 下生成的文件，或在系统格式变化时重新运行 **fmtutil-user**。除非理解这一取舍，否则请优先使用 **fmtutil-sys**。

# HISTORY

TeX Live 2017 中引入，作为 **fmtutil-sys** 的显式对应命令，使裸调用的 **fmtutil** 不再默认进行有歧义的树选择。

# INSTALL

```dnf: sudo dnf install texlive```

```apk: sudo apk add texlive```

```zypper: sudo zypper install texlive```

```brew: brew install texlive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fmtutil](/man/fmtutil)(1), [fmtutil-sys](/man/fmtutil-sys)(1), [mktexfmt](/man/mktexfmt)(1), [kpsewhich](/man/kpsewhich)(1)

# RESOURCES

```[Documentation](https://tug.org/texlive/scripts-sys-user.html)```

```[Homepage](https://tug.org/texlive/)```

<!-- verified: 2026-07-17 -->
