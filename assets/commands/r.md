# TAGLINE

统计计算与绘图语言

# TLDR

**启动 R 解释器**

```R```

**运行脚本**

```R --file=[script.R]```

**执行并打印**

```Rscript -e "[print(1+1)]"```

**静默运行脚本**

```R --slave --file=[script.R]```

**退出时不保存**

```R --no-save```

# SYNOPSIS

**R** [_options_] [_file_]

# PARAMETERS

_FILE_
> 要运行的 R 脚本。

**--file** _FILE_
> 执行脚本。

**--slave**
> 静默模式。

**--no-save**
> 不保存工作区。

**--vanilla**
> 不加载初始化文件。

**-e** _EXPR_
> 执行表达式。

# DESCRIPTION

**R** 是一门用于统计计算、数据分析和绘图的交互式语言与环境。它提供丰富的统计技术，包括线性和非线性建模、时间序列分析、分类和聚类，并配备强大的绘图系统，可生成达到出版质量的图表与可视化。

交互式控制台支持即时反馈的探索性数据分析；脚本则可以通过 **--file** 或配套的 **Rscript** 命令非交互式执行。CRAN 上的 R 包生态系统提供数千个社区贡献的库，将其能力扩展到生物信息学、计量经济学等众多领域。工作区系统会在会话之间保存对象，而 **--no-save** 和 **--vanilla** 标志可实现干净的无状态执行，适合可复现的工作流。

# CAVEATS

与 Rscript 是相互独立的工具。默认进入交互模式。

# HISTORY

R 由奥克兰大学的 **Ross Ihaka 和 Robert Gentleman** 创建。

# INSTALL

```apt: sudo apt install r-cran-littler```

```pacman: sudo pacman -S r```

```brew: brew install r```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1)
