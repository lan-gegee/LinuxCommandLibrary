# TAGLINE

为命令输出添加时间戳前缀

# TLDR

**为每一行输出加上耗时前缀**

```[command] | gnomon```

**显示自命令启动以来的总耗时**

```[command] | gnomon --type=elapsed-total```

**为每一行显示绝对时间戳**

```[command] | gnomon --type=absolute```

**高亮显示**超过 1.5 秒的行

```[command] | gnomon --high=1.5```

同时设置颜色编码的**高、中阈值**

```[command] | gnomon --high=3.0 --medium=1.0```

**忽略**短于阈值的行

```[command] | gnomon --ignore-blank --high=0.5```

# SYNOPSIS

**gnomon** [_options_]

# PARAMETERS

**--type** _TYPE_
> 时间戳类型：**elapsed-line**（默认）、**elapsed-total** 或 **absolute**。

**--ignore-blank**
> 不为空白行添加时间戳前缀。

**--real-time** _THRESHOLD_
> 设定一个以秒为单位的阈值，超过后 gnomon 实时打印输出而不是缓冲。

**--high** _SECONDS_
> 高（红色）时间着色的阈值（秒）。默认：**1.0**。

**--medium** _SECONDS_
> 中（黄色）时间着色的阈值（秒）。默认：**0.5**。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gnomon** 是一个命令行工具，通过 stdin 接收另一条命令的输出并在前面添加时间戳信息。默认情况下，它会显示每一行输出出现所耗费的时间，因此适合用来定位构建过程、测试套件或日志输出中缓慢的步骤。

该工具根据可配置的时间阈值对输出进行着色：超过 **--high** 阈值的行显示为红色，超过 **--medium** 的显示为黄色，其余保持默认颜色。

# CAVEATS

需要 **Node.js**，并通过 npm 安装（`npm install -g gnomon`）。会给输出带来轻微延迟。更适合诊断缓慢的过程，而非精确的性能基准测试。

# INSTALL

```pacman: sudo pacman -S gnomon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ts](/man/ts)(1), [time](/man/time)(1), [pv](/man/pv)(1)
