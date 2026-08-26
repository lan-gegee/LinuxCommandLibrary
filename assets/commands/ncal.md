# TAGLINE

以纵向格式显示日历，周自上而下排列

# TLDR

此命令是 **cal** 的别名，采用纵向日历布局。

显示**当前月份**的日历

```ncal```

显示**指定月份和年份**的日历

```ncal [month] [year]```

显示**整年**的日历

```ncal -y [year]```

# SYNOPSIS

**ncal** [**-y**] [**-3**] [**-1**] [**-A** _months_] [**-B** _months_] [[_month_] _year_]

# PARAMETERS

**-y**
> 显示整年。

**-3**
> 显示上月、当月和下月。

**-1**
> 仅显示当前月份。

**-A** _months_
> 显示当前月份之后的若干月。

**-B** _months_
> 显示当前月份之前的若干月。

**-h**
> 关闭今天的高亮显示。

**-M**
> 每周从周一开始。

**-S**
> 每周从周日开始。

**-b**
> 使用横向布局（类似 cal）。

# DESCRIPTION

**ncal** 以纵向格式显示日历，周自上而下排列。它是 **cal** 命令的另一种界面，后者以横向方式显示日历。

纵向格式适用于宽度有限的终端，或者需要跨周比较日期的场景。在大多数系统上，ncal 和 cal 通常由同一个软件包提供。

# CAVEATS

在源自 BSD 的系统上可用。某些 Linux 发行版可能不包含 ncal，或将其别名为 cal。**-b** 选项可切换回传统的横向 cal 布局。

# INSTALL

```apt: sudo apt install ncal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cal](/man/cal)(1)
