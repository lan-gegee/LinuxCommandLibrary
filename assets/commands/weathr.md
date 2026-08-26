# TAGLINE

带 ASCII 动画的终端天气应用

# TLDR

**显示你所在位置的当前天气**（通过 IP 自动检测）

```weathr```

**使用英制单位**（华氏度、mph、英寸）

```weathr --imperial```

**模拟特定的天气状况**

```weathr --simulate [rain|snow|thunderstorm|fog|clear|...]```

**模拟夜间**天气

```weathr --simulate [condition] --night```

**隐藏状态 HUD**，只显示动画

```weathr --hide-hud```

**添加落叶**效果

```weathr --leaves```

# SYNOPSIS

**weathr** [**--imperial** | **--metric**] [**--simulate** _condition_] [**--night**] [**--leaves**] [**--auto-location**] [**--hide-location**] [**--hide-hud**] [**--silent**]

# PARAMETERS

**--simulate** _condition_
> 模拟某种天气状况而不是使用真实数据。可选状况：**clear**、**partly-cloudy**、**cloudy**、**overcast**、**fog**、**drizzle**、**rain**、**freezing-rain**、**rain-showers**、**snow**、**snow-grains**、**snow-showers**、**thunderstorm**、**thunderstorm-hail**

**--night**
> 模拟夜间画面（月亮、星星、萤火虫）

**--leaves**
> 添加落叶动画（秋季效果）

**--imperial**
> 使用英制单位：华氏度、mph、英寸

**--metric**
> 使用公制单位：摄氏度、km/h、mm（默认）

**--auto-location**
> 通过 IP 地理定位自动检测位置（ipinfo.io）

**--hide-location**
> 在显示中隐藏位置坐标

**--hide-hud**
> 隐藏状态 HUD，只显示 ASCII 动画

**--silent**
> 不显示非错误消息

**-h**, **--help**
> 打印帮助信息

**-V**, **--version**
> 打印版本信息

# DESCRIPTION

**weathr** 是一款终端天气应用，以动画 ASCII 艺术展示实时天气数据。它从 **Open-Meteo** API 获取当前天气状况，并渲染成多彩的终端动画，包括雨、雪、雷暴、飞过的飞机、飘动的云和飞鸟。

显示效果随一天中的时间变化：白天显示太阳、滑翔的云朵、V 字形飞鸟和明亮的色彩；夜晚则有月亮、闪烁的星星、滑翔的云朵、萤火虫和流星。状态 HUD 显示天气类别、温度、风速和降水量。

**weathr** 支持在 Linux、macOS、Windows 和 NixOS 上跨平台使用。它遵循 **NO_COLOR** 环境变量以提升无障碍性。

# CONFIGURATION

配置保存在 TOML 文件中：
> **Linux**：```~/.config/weathr/config.toml```
> **macOS**：```~/Library/Application Support/weathr/config.toml```
> **Windows**：```~/AppData/Roaming/weathr/config.toml```

配置示例：

```
hide_hud = false
silent = false

[location]
latitude = 40.7128
longitude = -74.0060
auto = false
hide = false

[units]
temperature = "celsius"
wind_speed = "kmh"
precipitation = "mm"
```

**temperature**：```celsius``` 或 ```fahrenheit```
**wind_speed**：```kmh```、```ms```、```mph``` 或 ```kn```（节）
**precipitation**：```mm``` 或 ```inch```

将 **[location]** 下的 **auto** 设为 true 会使用基于 IP 的地理定位。显式提供 **latitude** 和 **longitude** 可以避免调用外部 API，保护隐私。

# CAVEATS

位置自动检测依赖 **ipinfo.io** 的 IP 地理定位，在 VPN 或代理环境下可能不准确。天气数据来自 **Open-Meteo**，免费但在偏远地区精度可能降低。应用需要支持真彩色（truecolor）的终端才能获得最佳视觉效果；当 **COLORTERM** 未设置为 "truecolor" 或 "24bit" 时，会回退到基础颜色。

# HISTORY

**weathr** 由 **Veirt** 创建，使用 **Rust** 编写。项目托管在 GitHub 上，采用 **GPL-3.0-or-later** 许可证。天气数据来自 **Open-Meteo.com**（CC BY 4.0 许可）。最新版本为 2026 年 2 月发布的 **v1.3.0**。

# INSTALL

```nix: nix profile install nixpkgs#weathr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ansiweather](/man/ansiweather)(1), [wego](/man/wego)(1), [curl](/man/curl)(1)
