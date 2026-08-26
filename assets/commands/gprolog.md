# TAGLINE

GNU Prolog 编译器和解释器

# TLDR

**启动 GNU Prolog 解释器**

```gprolog```

**加载并运行文件**

```gprolog --consult-file [program.pl]```

**编译为可执行文件**

```gplc [program.pl] -o [program]```

**从命令行运行查询**

```gprolog --query-goal "[goal]"```

# SYNOPSIS

**gprolog** [_options_]

**gplc** [_options_] _files_

# PARAMETERS

**--consult-file** _file_
> 启动时加载 Prolog 文件。

**--query-goal** _goal_
> 加载后执行目标。

**--init-goal** _goal_
> 执行初始化目标。

**--entry-goal** _goal_
> 入口点目标。

**--no-top-level**
> 执行完目标后退出。

# DESCRIPTION

**GNU Prolog** 是一个支持有限域约束求解的 Prolog 编译器。它将 Prolog 编译为原生代码，并提供交互式解释器。

GNU Prolog 支持 ISO Prolog 并带有约束逻辑编程扩展，适用于组合问题、调度和 AI 应用。

# INTERPRETER COMMANDS

```prolog
?- consult('file.pl').    % Load file
?- listing.               % Show predicates
?- halt.                  % Exit
?- trace.                 % Enable tracing
```

# COMPILING

```bash
# Compile to executable
gplc program.pl -o program

# Produce WAM file
gplc -W program.pl

# Strip executable
gplc program.pl -o program -s

# Compile without top-level
gplc --no-top-level program.pl -o program
```

# CAVEATS

语法与 SWI-Prolog 略有不同。原生编译增加了启动的复杂度。约束求解需要有限域声明。交互式调试需要跟踪模式。

# HISTORY

GNU Prolog 由 INRIA 的 **Daniel Diaz** 创建，首次发布于 **1996 年**。它强调原生代码编译和约束求解，这使它有别于解释型的 Prolog 系统。

# INSTALL

```dnf: sudo dnf install gprolog```

```nix: nix profile install nixpkgs#gprolog```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[swipl](/man/swipl)(1), [sicstus](/man/sicstus)(1)
