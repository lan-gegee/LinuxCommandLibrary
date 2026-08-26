# TAGLINE

基于 XCB 的轻量级状态栏

# TLDR

**启动状态栏并从标准输入读取**

```lemonbar```

**设置状态栏几何参数**

```lemonbar -g [1920x30+0+0]```

**设置背景色与前景色**

```lemonbar -B "[#1d1f21]" -F "[#c5c8c6]"```

**设置字体**

```lemonbar -f "[monospace:size=10]"```

**停靠在底部并带下划线**

```lemonbar -b -u [2]```

**将脚本输出通过管道送入状态栏**

```[./status.sh] | lemonbar```

# SYNOPSIS

**lemonbar** [_options_]

# PARAMETERS

**-g** _geometry_
> 状态栏几何参数（WxH+X+Y）。

**-b**
> 将状态栏停靠在屏幕底部。

**-f** _font_
> 字体规格。

**-B** _color_
> 背景色。

**-F** _color_
> 前景色。

**-u** _pixels_
> 下划线宽度。

**-n** _name_
> WM_NAME 属性。

**-d**
> 强制停靠。

# DESCRIPTION

**lemonbar**（原名 bar）是一个基于 XCB 的轻量级状态栏。它从标准输入读取文本并显示为状态栏，支持颜色、对齐方式和可点击区域。

状态栏使用一套简单的标记格式：%{F#color} 设置前景色，%{B#color} 设置背景色，%{A:command:} 定义可点击区域。

# MARKUP FORMAT

```
%{l}left %{c}center %{r}right
%{F#ff0000}red text%{F-}
%{A:command:}clickable%{A}
```

# CAVEATS

仅支持 X11。动态内容需要借助脚本实现。没有内置的系统监控功能。标记错误可能导致显示问题。

# HISTORY

lemonbar 由 **LemonBoy** 于 **2012 年**前后以 **bar** 为名创建，后来更名为 lemonbar，以避免与其他项目混淆。

# INSTALL

```apt: sudo apt install lemonbar```

```apk: sudo apk add lemonbar```

```zypper: sudo zypper install lemonbar```

```nix: nix profile install nixpkgs#lemonbar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[polybar](/man/polybar)(1), [i3status](/man/i3status)(1)
