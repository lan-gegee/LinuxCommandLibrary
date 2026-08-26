# TAGLINE

在终端中显示实时天体图

# TLDR

**以彩色并显示星座**方式启动

```astroterm --color --constellations```

**按城市名称设置观测位置**

```astroterm --city "[Boston]"```

**按经纬度设置观测位置**

```astroterm --latitude [42.36] --longitude [-71.06]```

**显示指定的 UTC 日期和时间**

```astroterm --datetime [1969-07-16T13:32:00]```

以自定义 FPS **高速动画**播放

```astroterm --color --constellations --speed [10000] --fps [64]```

**绘制方位网格并使用 Unicode 字符**

```astroterm --grid --unicode --metadata```

# SYNOPSIS

**astroterm** [_options_]

# PARAMETERS

**-a**, **--latitude** _degrees_
> 观测者纬度 [-90, 90]（默认：0.0）。

**-o**, **--longitude** _degrees_
> 观测者经度 [-180, 180]（默认：0.0）。

**-i**, **--city** _name_
> 使用指定城市的经纬度。

**-d**, **--datetime** _yyyy-mm-ddThh:mm:ss_
> UTC 时间下的观测日期时间（默认：系统时间）。

**-t**, **--threshold** _float_
> 只渲染亮于该星等的恒星（默认：5.0）。

**-l**, **--label-thresh** _float_
> 为亮于该星等的恒星添加标签（默认：0.25）。

**-f**, **--fps** _int_
> 每秒帧数（默认：24）。

**-s**, **--speed** _float_
> 动画速度倍率（默认：1.0）。

**-c**, **--color**
> 启用终端彩色输出。

**-C**, **--constellations**
> 绘制星座连线图。

**-g**, **--grid**
> 绘制方位网格叠加层。

**-u**, **--unicode**
> 使用 Unicode 字符进行渲染。

**-m**, **--metadata**
> 显示元数据信息。

**-r**, **--aspect-ratio** _float_
> 覆盖自动计算的终端单元格纵横比。

**-q**, **--quit-on-any**
> 按任意键退出（默认：仅按 'q' 或 ESC 退出）。

**-h**, **--help**
> 打印帮助消息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**astroterm** 是一款用 C 编写的基于终端的天象仪，可直接在控制台中渲染恒星、行星、星座及其他天体的实时位置。它根据观测者的位置和时间计算天体坐标，无需图形桌面环境即可提供交互式星图。按 **q** 或 **ESC** 退出（若启用 **--quit-on-any** 则按任意键退出）。

# CAVEATS

彩色输出需要 **--color** 标志以及支持 256 色或真彩色的终端。显示效果取决于终端大小和字体。若未提供 **--latitude**/**--longitude** 或 **--city**，观测位置默认为 0,0（几内亚湾）。

# INSTALL

```dnf: sudo dnf install astroterm```

```pacman: sudo pacman -S astroterm```

```apk: sudo apk add astroterm```

```zypper: sudo zypper install astroterm```

```brew: brew install astroterm```

```nix: nix profile install nixpkgs#astroterm```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[cal](/man/cal)(1), [date](/man/date)(1)
