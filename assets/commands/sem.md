# TAGLINE

用于并行作业控制的计数信号量

# TLDR

使用默认信号量**运行命令**（互斥锁，一次一个）

```sem [command]```

使用命名信号量**最多并行运行 4 个作业**

```sem -j 4 --id [myid] [command]```

在前台**运行命令**并等待完成

```sem --fg [command]```

**等待**某个信号量中的所有命令完成

```sem --id [myid] --wait```

按 CPU 核心数加 2 **运行作业**

```sem -j +2 [command]```

**设置获取信号量的超时时间**

```sem --semaphore-timeout [10] [command]```

对日志文件进行**并行压缩**

```for i in *.log; do sem -j+0 gzip $i; done; sem --wait```

# SYNOPSIS

**sem** [**--fg**] [**--id** _id_] [**--semaphore-timeout** _secs_] [**-j** _num_] [**--wait**] _command_

# PARAMETERS

**--bg**
> 在后台运行命令。这是默认行为。sem 不会等待命令完成即退出。

**--fg**
> 在前台运行命令。sem 会等待信号量可用、执行命令、等待其完成后才退出。

**-j** _N_
> 允许最多 N 个命令并行运行。默认为 1（互斥模式）。使用 **-j+N** 表示在 CPU 核心数上加 N，**-j-N** 表示减 N，或 **-jN%** 表示使用 N% 的核心。

**--id** _name_, **--semaphorename** _name_
> 使用 name 作为信号量标识符。默认为控制终端（tty）的名称。相同 id 的命令共享同一个信号量。

**--semaphore-timeout** _secs_
> 若 secs > 0：超时后强制获取信号量。若 secs < 0：若超时内无法获取信号量则退出。

**--wait**
> 等待该信号量中的所有命令完成后才退出。

**--pipe**
> 将标准输入传给命令。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**sem** 是 **GNU parallel --semaphore** 的别名。它作为一个计数信号量，以受控的并发度并行执行 shell 命令。当达到最大并行作业数时，sem 会等待其中一个完成，然后才启动下一条命令。

sem 可用于限制对资源的并发访问、在 shell 脚本中并行化循环同时防止系统过载，以及为不能同时运行的进程实现互斥。信号量状态存储在 **~/.parallel/semaphores/** 中。

与 GNU parallel 不同，sem 不会解析命令参数来构造作业；它只是在信号量允许时直接执行所提供的命令。

# CAVEATS

信号量标识符默认取自控制终端，因此从不同终端运行的命令会使用不同的信号量，除非指定 **--id**。如果进程被异常终止，**~/.parallel/semaphores/** 中可能残留失效的信号量。需要 Perl 及多个 Perl 模块（Getopt::Long、Symbol、Fcntl）。

# HISTORY

**sem** 属于 GNU Parallel，由 Ole Tange 创建和维护。GNU Parallel 于 **2010 年**首次发布，是一款利用多 CPU 核心并行执行作业的工具。信号量功能（sem）的加入提供了一种限制 shell 命令并发执行的简单方式。该项目在 GNU 计划下开发并持续活跃维护。

# INSTALL

```dnf: sudo dnf install parallel```

```pacman: sudo pacman -S parallel```

```apk: sudo apk add parallel```

```brew: brew install parallel```

```nix: nix profile install nixpkgs#parallel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[parallel](/man/parallel)(1), [xargs](/man/xargs)(1), [flock](/man/flock)(1), [nohup](/man/nohup)(1)
