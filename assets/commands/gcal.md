# TAGLINE

支持节日计算的高级日历

# TLDR

**显示当前月份**

```gcal```

**显示指定月份**

```gcal [3] [2024]```

**显示全年**

```gcal [2024]```

**显示周数**

```gcal -K```

**显示节日**

```gcal -q [US]```

显示以当前月为中心的 3 个月

```gcal .```

# SYNOPSIS

**gcal** [_options_] [_date_]

# PARAMETERS

**-K**
> 显示周数。

**-q** _country_
> 显示国家节日。

**-b** _number_
> 当前月之前的月份数。

**-a** _number_
> 当前月之后的月份数。

**-s** _day_
> 一周起始日（0=周日）。

**--today**
> 高亮今天。

# DESCRIPTION

**gcal** 是一款功能丰富的日历程序，远不止简单的日期显示。与标准的 cal 工具不同，gcal 支持大量自定义功能，包括周数显示、可配置的一周起始日以及多月显示。

gcal 最强大的特性之一是节日计算能力，可显示多个国家和宗教传统的节日。该程序还支持天文数据、永久节日列表以及多种国际历法系统。

gcal 高度可脚本化，可用于复杂的日期计算，无论交互使用还是需要精细日历运算的自动化任务都十分适用。

# INSTALL

```apt: sudo apt install gcal```

```dnf: sudo dnf install gcal```

```zypper: sudo zypper install gcal```

```nix: nix profile install nixpkgs#gcal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cal](/man/cal)(1), [ncal](/man/ncal)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/gcal/)```

```[Documentation](https://www.gnu.org/software/gcal/manual/)```

<!-- verified: 2026-07-15 -->
