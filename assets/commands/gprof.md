# TAGLINE

GNU 执行性能分析器

# TLDR

**生成性能分析报告**

```gprof [program] [gmon.out]```

**仅输出平铺性能报告**

```gprof -p [program]```

**仅输出调用图**

```gprof -q [program]```

**不显示静态函数**

```gprof -a [program]```

**输出到文件**

```gprof [program] > [profile.txt]```

# SYNOPSIS

**gprof** [_options_] [_executable_] [_profile-data_]

# PARAMETERS

**-p**, **--flat-profile**
> 仅打印平铺性能报告。

**-q**, **--graph**
> 仅打印调用图。

**-b**, **--brief**
> 不输出说明性文字。

**-a**, **--no-static**
> 不显示静态函数。

**-z**, **--display-unused-functions**
> 显示从未被调用的函数。

**-c**, **--static-call-graph**
> 通过扫描机器代码来发现子函数，即使它们在运行时从未被调用。

**-A**, **--annotated-source**
> 打印带注释的源码。

**-l**, **--line**
> 逐行性能分析。

**-s**, **--sum**
> 将多个性能数据文件累加到汇总文件 `gmon.sum` 中。

**-i**, **--file-info**
> 打印关于性能数据文件的摘要信息，然后退出。

# DESCRIPTION

**gprof** 分析程序执行的性能剖析数据，以识别性能瓶颈。它要求程序使用 **-pg** 标志编译，生成的报告会显示每个函数所花费的时间以及调用关系。

该工具生成两种主要报告：显示各函数耗时情况的平铺报告（flat profile），以及展示函数间关系和累计时间的调用图（call graph）。

# WORKFLOW

```bash
# 1. Compile with profiling
gcc -pg -o program program.c

# 2. Run program (generates gmon.out)
./program

# 3. Analyze profile
gprof program gmon.out > analysis.txt
```

# CAVEATS

需要用 -pg 重新编译。会给执行带来额外开销。基于采样；运行时间短的函数可能被低估。现代替代方案包括 perf 和 valgrind。

# HISTORY

gprof 由 Susan Graham、Peter Kessler 和 Marshall McKusick 于 **20 世纪 80 年代初**在 **UC Berkeley** 开发。它成为标准的 Unix 性能分析器，至今仍是 GNU binutils 的一部分。

# INSTALL

```apt: sudo apt install binutils```

```dnf: sudo dnf install binutils```

```pacman: sudo pacman -S binutils```

```apk: sudo apk add binutils```

```zypper: sudo zypper install binutils```

```brew: brew install binutils```

```nix: nix profile install nixpkgs#binutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perf](/man/perf)(1), [valgrind](/man/valgrind)(1), [gcov](/man/gcov)(1), [gcc](/man/gcc)(1)
