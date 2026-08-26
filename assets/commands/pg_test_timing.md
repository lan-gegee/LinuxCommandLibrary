# TAGLINE

测量系统上的计时开销

# TLDR

以默认的 **3 秒**时长**测试计时开销**

```pg_test_timing```

以**秒**为单位**指定测试时长**

```pg_test_timing -d [seconds]```

**显示版本**信息

```pg_test_timing -V```

# SYNOPSIS

**pg_test_timing** [_option_...]

# PARAMETERS

**-d** _duration_, **--duration=**_duration_
> 指定测试时长（秒）。更长的时长精度稍高，也更容易发现系统时钟倒退的问题。默认为 3 秒。

**-V**, **--version**
> 打印 pg_test_timing 版本并退出。

**-?**, **--help**
> 显示关于 pg_test_timing 命令行参数的帮助并退出。

# DESCRIPTION

**pg_test_timing** 是一个测量系统计时开销的工具，并可确认系统时间从不倒退。它会反复调用系统时钟计时函数，报告每次调用的平均开销，以及调用时长的直方图。

收集计时数据较慢的系统会导致 **EXPLAIN ANALYZE** 结果不够准确。良好的结果是大多数（>90%）单次计时调用耗时低于一微秒，且每循环平均开销低于 100 纳秒。低开销使得启用 **track_io_timing** 不会带来显著的性能影响。

# INSTALL

```dnf: sudo dnf install postgresql17```

```apk: sudo apk add postgresql17```

```zypper: sudo zypper install postgresql17```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pg_test_fsync](/man/pg_test_fsync)(1), [postgres](/man/postgres)(1)
