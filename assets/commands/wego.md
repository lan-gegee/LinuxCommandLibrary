# TAGLINE

带 ASCII 艺术的终端天气预报

# TLDR

**显示当前位置的 3 天预报**

```wego```

**显示指定城市的预报**

```wego [London]```

**显示 5 天预报**

```wego -d [5]```

**显示指定城市指定天数的预报**

```wego [Paris] [4]```

**使用 emoji 前端**

```wego -f emoji```

**输出 JSON**

```wego -f json```

# SYNOPSIS

**wego** [_options_] [_location_] [_days_]

# PARAMETERS

**-d**, **--days** _num_
> 预报天数（1-7，默认 3）。

**-f**, **--frontend** _type_
> 输出前端：ascii-art-table、emoji 或 json。

**-u**, **--units** _system_
> 单位制：metric 或 imperial。

**-b**, **--backend** _name_
> 天气数据源。

**-l**, **--location** _place_
> 设置预报位置。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**wego** 是一款以 ASCII 艺术显示预报的终端天气客户端。它使用 Go 编写，可显示温度、风速与风向、能见度和降水概率。

该工具支持多种天气数据后端，包括 OpenWeatherMap。使用前你需要注册获取 API 密钥并在 ~/.wegorc 中配置。

有三种输出前端可选：ascii-art-table（经典终端外观）、emoji（现代图标）和 json（便于脚本处理）。显示效果需要支持 UTF-8 和 256 色的终端。

# CONFIGURATION

配置文件：~/.wegorc

必需：天气后端的 API 密钥。可选：默认位置、单位制和前端偏好。

# CAVEATS

需要天气服务的 API 密钥。部分后端已不再提供免费密钥。ASCII 艺术显示需要支持 UTF-8 和 256 色的终端以及合适的字体。

# HISTORY

**wego** 最初是一个趣味性的终端天气应用。它启发了 wttr.in——一个封装 wego 并通过 curl 提供天气查询的网络服务，让终端查天气简单到只需 `curl wttr.in`。

# INSTALL

```apt: sudo apt install wego```

```apk: sudo apk add wego```

```brew: brew install wego```

```nix: nix profile install nixpkgs#wego```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [finger](/man/finger)(1)
