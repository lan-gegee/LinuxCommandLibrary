# TAGLINE

用于测试的系统时间篡改工具

# TLDR

把时间伪装成**今晚**

```faketime '[today 23:30]' [date]```

以**昨天**为当前日期打开 shell

```faketime '[yesterday]' [bash]```

模拟程序在**下周五**的表现

```faketime '[next Friday 1 am]' [path/to/program]```

# SYNOPSIS

**faketime** [_options_] _timestamp_ _command_

# DESCRIPTION

**faketime** 通过拦截时间相关的系统调用，以伪造的系统时间运行命令。它利用 LD_PRELOAD 包装 time()、gettimeofday() 和 clock_gettime() 等函数，返回用户指定的时间而不是真实的系统时间。

这对测试依赖时间的软件、调试与日期相关的缺陷、模拟未来或过去的条件以及测试过期或调度逻辑非常有用。时间戳既接受绝对日期（"YYYY-MM-DD hh:mm:ss"），也接受经 GNU date 解析的自然语言和相对描述。

给出绝对时间戳会把时钟冻结在该时刻：重复查询时间返回相同的值。高级格式（**-f**）则允许时间继续流动、加速或减速，或在每次调用时步进。

# PARAMETERS

_timestamp_
> 时间规格（绝对日期、自然语言，或配合 -f 使用的高级偏移/速度规格）。

_command_
> 以伪造时间运行的命令。

**-f**
> 使用高级时间戳格式（偏移量、每次调用递增量、时钟速度倍率）。

**-m**
> 使用 libfaketime 的多线程变体。

**--exclude-monotonic**
> 不伪造 CLOCK_MONOTONIC 查询。

**--date-prog** _path_
> 使用另一个兼容 GNU date 的程序来解析时间戳。

# CAVEATS

使用 LD_PRELOAD 实现，因此对静态链接的二进制或 setuid 程序可能无效。要冻结时间请给出绝对时间戳；要让时间流动或缩放请使用 -f 高级格式。

# INSTALL

```apt: sudo apt install faketime```

```dnf: sudo dnf install libfaketime```

```pacman: sudo pacman -S libfaketime```

```apk: sudo apk add libfaketime```

```zypper: sudo zypper install libfaketime```

```brew: brew install libfaketime```

```nix: nix profile install nixpkgs#libfaketime```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[date](/man/date)(1), [timedatectl](/man/timedatectl)(1)

# RESOURCES

```[Source code](https://github.com/wolfcw/libfaketime)```

<!-- verified: 2026-07-15 -->
