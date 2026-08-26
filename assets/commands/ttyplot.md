# TAGLINE

从标准输入实时绘制终端图表

# TLDR

从 stdin**绘制**数值

```printf "1\n2\n3\n" | ttyplot```

设置**标题和单位**

```printf "10\n20\n30\n" | ttyplot -t "Title" -u "ms"```

**持续**绘制随机值

```while true; do echo $RANDOM; sleep 1; done | ttyplot```

**绘制 ping** 延迟

```ping 8.8.8.8 | sed -u 's/^.*time=//g; s/ ms//g' | ttyplot -t "Ping" -u ms```

实时**监控 CPU 使用率**

```while true; do grep 'cpu ' /proc/stat | awk '{u=$2+$4; t=$2+$4+$5; printf "%.1f\n", u/t*100}'; sleep 1; done | ttyplot -t "CPU %" -u "%"```

绘制**两个数值**（双图模式）

```command | ttyplot -2```

# SYNOPSIS

**ttyplot** [_options_]

# DESCRIPTION

**ttyplot** 是一个实时终端绘图工具，它从 stdin 读取数值并在终端中显示为滚动图形。适用于可视化流式数据，如网络延迟、CPU 使用率或传感器读数。

# PARAMETERS

**-t TITLE**
> 设置图表标题

**-u UNIT**
> 设置数值的单位标签

**-s SCALE**
> 设置垂直刻度（最大值）

**-m MIN**
> 设置最小值

**-2**
> 启用双值/双线绘图模式

**-c COLOR**
> 设置绘图颜色

**-e**
> 在 stdin 关闭时退出

**-r**
> 速率模式（每秒数值）

**-w WIDTH**
> 以字符数设置图表宽度

# CAVEATS

输入必须是数值，每行一个。可用 sed 或 awk 从命令输出中提取数值。图表会随终端尺寸变化自动调整大小。

# HISTORY

**ttyplot** 的诞生是为了提供一种无需图形环境即可在终端中直接可视化流式数值数据的简单方式。

# INSTALL

```apt: sudo apt install ttyplot```

```dnf: sudo dnf install ttyplot```

```apk: sudo apk add ttyplot```

```zypper: sudo zypper install ttyplot```

```brew: brew install ttyplot```

```nix: nix profile install nixpkgs#ttyplot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gnuplot](/man/gnuplot)(1), [termgraph](/man/termgraph)(1), [sed](/man/sed)(1), [awk](/man/awk)(1)
