# TAGLINE

命令行天气预报

# TLDR

**当前位置**的当前天气

```weather [city]```

**使用地理定位** / 默认位置

```weather```

**JSON 输出**（如果支持）

```weather -j [city]```

# SYNOPSIS

**weather** [*options*] [*location*]

# DESCRIPTION

**weather**（历史上也曾以 genuinetools 的 **darksky-weather** 名称发布）在终端中打印简洁的天气状况和预报。位置可以是城市名称或坐标，具体取决于版本和后端 API 配置。

许多构建版本需要天气数据提供商的 API 密钥（最初是 Dark Sky；分支可能使用 OpenWeatherMap 或其他提供商）。请查看 **weather --help** 和你的软件包所记载的环境变量。

# PARAMETERS

*location*

> 用于预报的城市或查询字符串。

**-j** / **--json**

> 可用时输出机器可读的格式。

**-h**, **--help**

> 包含单位、预报天数和图标等选项。

# CAVEATS

上游天气 API 变动频繁；密钥、配额和端点的变更可能使旧版本失效。建议使用发行版维护的软件包。与 GNOME Weather 图形界面无关。

# INSTALL

```dnf: sudo dnf install expect```

```pacman: sudo pacman -S expect```

```apk: sudo apk add expect```

```zypper: sudo zypper install expect```

```brew: brew install expect```

```nix: nix profile install nixpkgs#expect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [ansiweather](/man/ansiweather)(1), [wttr](/man/wttr)(1)

# RESOURCES

```[Source code](https://github.com/genuinetools/weather)```

<!-- verified: 2026-07-19 -->
