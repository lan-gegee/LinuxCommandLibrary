# TAGLINE

报告 Debian 系统上的非自由软件包

# TLDR

**列出**非自由软件包

```vrms```

仅输出软件包**名称**

```vrms --sparse```

# SYNOPSIS

**vrms** [_OPTIONS_]

# PARAMETERS

**-s**, **--sparse**
> 只输出软件包名称，适合通过管道传给其他工具。

**-e**, **--explain**
> 显示软件包为何被视为非自由（仅当前上游打包版本有此选项——旧版本中不存在）。

**-q**, **--quiet**
> 不输出非必要信息。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**vrms**（Virtual Richard M. Stallman）报告基于 Debian 的系统上安装的非自由（non-free）和 contrib 软件包。它有助于识别不符合 Debian 自由软件准则的软件。

该工具会列出来自 non-free 和 contrib 软件仓库的软件包及其描述。

# CAVEATS

仅适用于基于 Debian 的系统。软件包的分类取决于仓库元数据。某些软件包可能被错误归类。

# HISTORY

**vrms** 以自由软件基金会创始人 Richard M. Stallman 的名字命名，他一直倡导软件自由。

# SEE ALSO

[apt](/man/apt)(8), [dpkg](/man/dpkg)(1)
