# TAGLINE

非交互式运行 R 脚本

# TLDR

**运行 R 脚本**

```Rscript [script.R]```

**带参数运行**

```Rscript [script.R] [arg1] [arg2]```

**执行表达式**

```Rscript -e "[print('hello')]"```

**Vanilla 模式（不加载初始化配置）**

```Rscript --vanilla [script.R]```

**设置默认加载的库**

```Rscript --default-packages=[ggplot2,dplyr] [script.R]```

# SYNOPSIS

**Rscript** [_--vanilla_] [_-e expr_] [_options_] [_script_] [_args_]

# PARAMETERS

**-e** _EXPR_
> 执行表达式。

**--vanilla**
> 不读取保存的数据和初始化配置。

**--default-packages** _PKGS_
> 加载指定的软件包。

**--verbose**
> 启动时输出详细信息。

**--no-init-file**
> 跳过 .Rprofile。

**--save**
> 保存工作区。

# DESCRIPTION

**Rscript** 是用于运行 R 脚本和表达式的非交互式命令行界面。它专为脚本编写和自动化而设计，可以直接执行 R 代码文件，返回恰当的退出码，并借助 shebang（#!/usr/bin/env Rscript）支持将其作为可执行脚本使用。

**-e** 标志会对内联的 R 表达式求值，适合一行式命令和管道集成。跟在脚本名之后传入的命令行参数可以在 R 中通过 **commandArgs()** 访问。**--vanilla** 标志不加载保存的工作区和启动文件，以确保干净、可重现的执行。

比起较旧的 **R CMD BATCH** 方式，Rscript 更快也更方便：它把输出直接写入 stdout/stderr，并返回有意义的退出码，便于与 shell 脚本和 CI/CD 流水线集成。

# CAVEATS

需要完整的 R 安装。包依赖必须单独安装（例如通过 `install.packages()`）。R 的默认内存限制依然适用；Windows 上可用 `--max-mem-size`、Unix 上可用 `ulimit` 进行调整。对于要求可重现性的脚本，推荐加上 `--vanilla` 标志，以免加载用户特定的设置。

# HISTORY

**Rscript** 于 R 2.5.0 中引入，作为 R CMD BATCH 的更简单替代方案，用于从命令行运行 R 脚本。

# SEE ALSO

[littler](/man/littler)(1), [python](/man/python)(1)
