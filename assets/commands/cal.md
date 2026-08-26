# TAGLINE

在终端中显示日历

# TLDR

显示**当前月份**的日历

```cal```

显示跨越当前日期的 **3 个月**

```cal -3```

显示**整年**日历

```cal -y```

显示**接下来的 12 个月**

```cal -Y```

以**周一**作为每周第一天

```cal -m```

显示**指定年份**的日历

```cal [year]```

显示**指定月份和年份**的日历

```cal [month] [year]```

# SYNOPSIS

**cal** [_options_] [[_month_] _year_]

# DESCRIPTION

**cal** 在终端中显示日历，并高亮当天。它可以显示单个月、多个月或整年。

默认以周日作为每周第一天。使用 **-m** 可改为以周一开始。

# PARAMETERS

**-3, --three**
> 显示上个月、当前月和下个月

**-y, --year**
> 显示当前年份的日历

**-Y, --twelve**
> 显示接下来的 12 个月

**-m, --monday**
> 以周一作为每周第一天

**-s, --sunday**
> 以周日作为每周第一天（默认）

**-j, --julian**
> 显示儒略日（一年中的第几天）

**-n** _num_
> 从当前月开始显示 _num_ 个月的日历

# INSTALL

```apt: sudo apt install ncal```

```apk: sudo apk add util-linux-misc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ncal](/man/ncal)(1), [date](/man/date)(1), [calcurse](/man/calcurse)(1)

# RESOURCES

```[Source code](https://github.com/util-linux/util-linux)```

<!-- verified: 2026-06-22 -->
