# TAGLINE

支持颜色和 iCal 的命令行日历

# TLDR

**显示**当前月份

```carl```

**显示**指定的月份和年份

```carl -m [3] -y [2024]```

**显示**整年

```carl -y [2024]```

**显示**周数

```carl -w```

**显示**上月、当月和下月

```carl -3```

**显示**带事件议程的日历

```carl -a```

**显示**儒略日序号

```carl -j```

# SYNOPSIS

**carl** [_options_]

# PARAMETERS

**-m** _MONTH_
> 显示指定月份（1-12）。

**-y** _YEAR_
> 显示指定年份。

**-w**
> 显示 ISO 周数。

**-1, --one**
> 单月输出（默认）。

**-3, --three**
> 显示上月、当月和下月。

**-n, --months** _NUMBER_
> 显示当月及其后的月份。

**-s, --sunday**
> 以星期日为一周的第一天。

**-j, --julian**
> 显示儒略日期（从 1 月 1 日起编号天数）。

**-a, --agenda**
> 在日历下方显示事件议程。

**--theme** _THEME_
> 设置配色主题。

**--themestyletype** _TYPE_
> 使用 "dark" 或 "light" 背景主题样式。

# DESCRIPTION

**carl** 是一个用 Rust 编写的命令行日历工具，可在终端中显示彩色的格式化日历。它试图模仿各种 cal(1) 实现，同时增加了颜色和 iCal 支持等增强功能。与传统的 **cal** 命令相比，其输出使用颜色和排版来提升可读性。

Carl 可以显示单月、多月、整年，并高亮当前日期。iCal 文件通过配置文件（config.toml）中的 `[[ical]]` 部分进行配置，事件日期会在日历视图中高亮显示。`--agenda` 标志会在日历下方列出事件摘要。

# CAVEATS

iCal 支持涵盖基本事件，但可能无法处理所有重复规则或复杂的日历特性。彩色输出需要支持 ANSI 颜色的终端。

# INSTALL

```brew: brew install carl```

```nix: nix profile install nixpkgs#carl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cal](/man/cal)(1), [calcurse](/man/calcurse)(1), [calcure](/man/calcure)(1)
