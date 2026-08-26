# TAGLINE

显示时区信息

# TLDR

打印**时区**信息

```zdump [timezone]```

# SYNOPSIS

**zdump** [_OPTIONS_] [_TIMEZONE..._]

# PARAMETERS

**-v**
> 详细输出，包含切换时间

**-V**
> 更详细的输出

**-c** _YEAR_
> 将切换限制在指定的年份范围内

**--help**
> 显示帮助

# DESCRIPTION

**zdump** 打印时区信息，包括当前时间和 UTC 偏移量。它从系统时区数据库读取时区数据。

使用 -v 标志可显示所有时区切换（夏令时变更）。

# CAVEATS

时区名称必须与系统数据库中的条目一致。输出格式因系统版本而异。

# INSTALL

```apt: sudo apt install libc-bin```

```apk: sudo apk add tzdata-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zic](/man/zic)(8), [tzselect](/man/tzselect)(8), [date](/man/date)(1)
