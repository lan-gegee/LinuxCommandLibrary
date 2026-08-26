# TAGLINE

极简的 neofetch 风格天气 CLI

# TLDR

**显示当前位置的天气**

```stormy```

**以英制单位显示指定城市的天气**

```stormy --city "[New York]" --units imperial```

**以紧凑模式显示天气**

```stormy --compact```

# SYNOPSIS

**stormy** [**--city** _name_] [**--units** _metric_|_imperial_|_standard_] [**--compact**]

# DESCRIPTION

**stormy** 是一个极简、可定制的天气 CLI，它以 neofetch 式的布局配合彩色 ASCII 艺术图显示当前天气状况。它支持多个天气数据源，包括 Open-Meteo（无需 API 密钥）和 OpenWeatherMap，可配置单位并具有紧凑显示模式。

# HISTORY

**stormy** 由 **Ashish Kumar**（ashish0kumar）创建，使用 **Go** 编写。

# INSTALL

```brew: brew install stormy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rustormy](/man/rustormy)(1), [starlit](/man/starlit)(1), [curl](/man/curl)(1)
