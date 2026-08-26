# TAGLINE

将天气预报送到终端

# TLDR

**显示当前天气**

```yr```

**显示 5 天预报**

```yr -f```

**显示明天正午的天气**

```yr -d 1 -h 12```

# SYNOPSIS

**yr** [_options_]

# PARAMETERS

**-f**, **--forecast**
> 显示多日预报而非当前天气。

**-d** _DAYS_
> 距今天的天数偏移（0 = 今天，1 = 明天）。

**-h** _HOUR_
> 预报的小时数（0-23）。

**-l** _LOCATION_
> 本次查询覆盖已配置的位置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**yr** 是一款命令行工具，从 yr.no API（挪威气象局 Meteorologisk institutt）和 OpenStreetMap 的 Nominatim API 获取天气数据。它以 JSON 格式输出预报，并支持通过配置文件查询特定小时和多日预报。

配置文件（通常位于 `~/.config/yr/` 下）保存默认位置、单位和语言设置，因此简单查询无需任何参数。

# CONFIGURATION

**~/.config/yr/config.toml**
> 默认位置、单位与语言设置。

# CAVEATS

需要网络访问以连接 yr.no 和 Nominatim。数据覆盖全球，但精度因位置而异。逐小时预报的范围受上游 API 提供的数据限制。

# HISTORY

**yr** 由 **clux** 创建，以 **Rust** 编写。

# INSTALL

```aur: yay -S yr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1)
