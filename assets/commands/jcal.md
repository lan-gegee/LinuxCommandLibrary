# TAGLINE

以 Jalali（波斯历）格式显示日历，类似于 Unix 的 **cal**

# TLDR

**显示当前月份**

```jcal```

**显示三个月**

```jcal -3```

**显示指定年份**

```jcal [1402]```

**显示指定的月份和年份**

```jcal [5] [1402]```

**显示整年**

```jcal -y```

**以波斯数字和名称显示**

```jcal -p```

**以英文星期名称显示**

```jcal -e```

# SYNOPSIS

**jcal** [_options_] [[_month_] _year_]

# PARAMETERS

**-1**
> 显示单个月份（默认）。

**-3**
> 显示上个月、当前月和下个月。

**-y**
> 显示整年。

**-j**
> 显示儒略日（从 Farvardin 1 起编号的天数）。

**-p**
> 以波斯数字和名称显示。

**-P**
> 以 Pahlavi 纪元为基准显示年份。

**-e**
> 星期名称用英文显示。

**-V**
> 显示版本。

# DESCRIPTION

**jcal** 以 Jalali（波斯历）格式显示日历，类似于公历用的 Unix **cal**。Jalali 历是伊朗和阿富汗使用的阳历。是 jcal/libjalali 软件包的一部分。当天会被高亮显示。

单个参数表示年份（1-9999）。两个参数分别表示月份（1-12）和年份。年份必须完整写出："jcal 90" 不会显示 1390 年的日历。

# INSTALL

```apt: sudo apt install jcal```

```dnf: sudo dnf install jcal```

```brew: brew install jcal```

```nix: nix profile install nixpkgs#jcal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cal](/man/cal)(1)
