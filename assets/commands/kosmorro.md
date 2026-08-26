# TAGLINE

计算天文星历，包括月相和行星可见性

# TLDR

**显示今日星历**

```kosmorro```

**显示指定日期的星历**

```kosmorro --date [2024-01-15]```

**设置观测位置以获得升落时间**

```kosmorro --latitude [48.8566] --longitude [2.3522]```

**将星历导出为 PDF**

```kosmorro --format pdf --output [sky.pdf]```

**以指定时区显示**

```kosmorro --timezone [Europe/Paris]```

# SYNOPSIS

**kosmorro** [_options_]

# PARAMETERS

**--date** _date_
> 要计算的日期（YYYY-MM-DD）。

**--latitude** _degrees_
> 观测者纬度。

**--longitude** _degrees_
> 观测者经度。

**--timezone** _tz_
> 显示所用时区。

**--format** _format_
> 输出格式（text、json、pdf）。

**--output** _file_
> 输出文件路径。

# DESCRIPTION

**kosmorro** 计算天文星历，包括月相、行星可见性和天象事件。它显示给定地点的日出、日落和天文晨昏蒙影时间。首次运行时，它会下载必要的计算文件到 `~/.kosmorro-cache`。对天文爱好者和摄影师很有用。

# CAVEATS

首次运行需要联网以下载星历数据文件。要计算升落时间必须提供位置坐标。PDF 输出需要安装 LaTeX。


# INSTALL

```aur: yay -S kosmorro```

<!-- packages: 2026-07-22 -->
