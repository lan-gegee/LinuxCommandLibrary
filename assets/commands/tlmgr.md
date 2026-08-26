# TAGLINE

TeX Live 软件包管理器

# TLDR

**更新 TeX Live**

```tlmgr update --all```

**安装软件包**

```tlmgr install [package-name]```

**移除软件包**

```tlmgr remove [package-name]```

**搜索软件包**

```tlmgr search [pattern]```

**列出已安装的软件包**

```tlmgr list --only-installed```

**显示软件包信息**

```tlmgr info [package-name]```

**更新 tlmgr 自身**

```tlmgr update --self```

**备份软件包**

```tlmgr backup [package-name]```

# SYNOPSIS

**tlmgr** [_options_] _action_ [_args_]

# PARAMETERS

**install** _PKGS_
> 安装软件包。

**remove** _PKGS_
> 移除软件包。

**update**
> 更新软件包。

**search** _PATTERN_
> 搜索软件包。

**list**
> 列出软件包。

**info** _PKG_
> 软件包信息。

**--all**
> 所有软件包。

**--self**
> 更新 tlmgr。

**--only-installed**
> 仅已安装项。

# DESCRIPTION

**tlmgr**（TeX Live Manager）是 TeX Live 发行版的软件包管理器，负责 LaTeX 软件包和字体的安装、更新与移除。它在安装新软件包时自动解析依赖，并可通过 **update --all** 更新整个发行版。

该工具提供搜索和信息命令，可按名称或描述浏览数千个可用软件包。软件包可在更改前备份，如果更新出现问题则可恢复。**--self** 标志单独更新 tlmgr 本身，与其他软件包无关。

运行 **tlmgr** 需要原生 TeX Live 安装而不是发行版打包的版本，因为 Linux 发行版的软件包通常改用自身的包管理器来管理 TeX 软件包。

# CAVEATS

需要 TeX Live（而非发行版软件包）。部分发行版另行管理。更新需要联网。

# HISTORY

**tlmgr** 是 **TeX Live** 这一全面 TeX 发行版的组成部分。它为 LaTeX 生态系统提供软件包管理。

# SEE ALSO

[latex](/man/latex)(1), [pdflatex](/man/pdflatex)(1), [texdoc](/man/texdoc)(1)
