# TAGLINE

受 Neofetch 启发、带 ASCII 艺术图的天气 CLI

# TLDR

**显示当前位置的天气**

```rustormy```

**显示特定城市的天气**

```rustormy -c [London]```

**以英制单位彩色显示天气**

```rustormy -c [Austin] --colors -u imperial```

**以 JSON 格式输出天气数据**

```rustormy -c [Tokyo] -o json```

# SYNOPSIS

**rustormy** [_options_]

# PARAMETERS

**-c**, **--city** _CITY_
> 指定城市名称。

**-u**, **--units** _UNITS_
> 单位制：metric 或 imperial。

**-o**, **--format** _FORMAT_
> 输出格式：text 或 json。

**-m**, **--text-mode** _MODE_
> 显示模式：full、compact 或 one_line。

**-l**, **--live**
> 启用定期更新的实时模式。

**--colors**
> 启用 ANSI 彩色输出。

# DESCRIPTION

**rustormy** 是一个轻量级天气 CLI 工具，以 ASCII 艺术天气图标显示当前天气状况，包括温度、风速、湿度、降水、气压和紫外线指数。它支持多个天气数据源（默认 Open-Meteo，无需 API key）、多种输出格式，以及在达到 API 限制时自动切换备用数据源。

# HISTORY

**rustormy** 由 **Tairesh** 创建，使用 **Rust** 编写。

# SEE ALSO

[stormy](/man/stormy)(1), [curl](/man/curl)(1), [zeitfetch](/man/zeitfetch)(1)
