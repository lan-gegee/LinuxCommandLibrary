# TAGLINE

在终端中以 ANSI 颜色显示天气

# TLDR

**获取**某个城市的天气

```ansiweather -l [London,UK]```

显示**预报**

```ansiweather -l [Paris,FR] -f [5]```

使用**摄氏度**

```ansiweather -l [Tokyo,JP] -u metric```

使用**华氏度**

```ansiweather -l [New York,US] -u imperial```

显示**风速和湿度**数据

```ansiweather -l [Berlin,DE] -w true -h true```

显示**五天**预报

```ansiweather -l [Berlin,DE] -F```

显示**紫外线指数**信息

```ansiweather -l [Berlin,DE] -i true```

# SYNOPSIS

**ansiweather** [_-l location_] [_-u units_] [_-f days_] [_options_]

# DESCRIPTION

**ansiweather** 是一个 Shell 脚本，它使用 ANSI 颜色和 Unicode 符号在终端中显示当前天气状况。它从 OpenWeatherMap API 获取数据并格式化为适合终端显示的样式。

该工具让你无需离开命令行即可快速获得彩色的天气概览。

# PARAMETERS

**-l** _location_
> 地点（City,CountryCode 格式）

**-u** _units_
> 单位：metric（摄氏度）或 imperial（华氏度）

**-f** _days_
> 预报天数（1-5）

**-F**
> 开启未来五天的预报模式。

**-a** _bool_
> 开关 ANSI 颜色显示（true/false）。

**-s** _bool_
> 开关 Unicode 符号显示（true/false）。

**-k** _key_
> 指定 OpenWeatherMap API 密钥。

**-d** _bool_
> 开关日照数据显示：日出/日落（true/false）。

**-w** _bool_
> 开关风速数据显示（true/false）。

**-p** _bool_
> 开关气压数据显示（true/false）。

**-h** _bool_
> 开关湿度数据显示（true/false）。

**-i** _bool_
> 开关紫外线指数显示（true/false）。

**-v**
> 显示版本信息。

# CONFIGURATION

**~/.ansiweatherrc**
> 用户配置文件，用于设置默认地点、单位、API 密钥和显示选项。

# CAVEATS

部分功能需要 OpenWeatherMap API 密钥。免费 API 有速率限制。地点匹配可能不够精确；请使用国家代码以确保准确。

# HISTORY

**ansiweather** 是一款简单而多彩的终端天气工具，利用 OpenWeatherMap 的免费 API 层级获取天气数据。

# INSTALL

```aur: yay -S ansiweather```

```brew: brew install ansiweather```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[curl](/man/curl)(1), [wttr.in](/man/wttr.in)(1)
