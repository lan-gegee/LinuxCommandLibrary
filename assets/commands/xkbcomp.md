# TAGLINE

编译 XKB 键盘描述

# TLDR

**为当前显示器编译键盘映射**

```xkbcomp [keymap.xkb] $DISPLAY```

**将当前键盘映射提取到文件**

```xkbcomp $DISPLAY [output.xkb]```

**编译为二进制键盘映射文件**

```xkbcomp -xkm [keymap.xkb] -o [keymap.xkm]```

**从键盘映射生成 C 头文件**

```xkbcomp -C [keymap.xkb] -o [keymap.h]```

**使用额外的包含路径编译**

```xkbcomp -I[/usr/share/X11/xkb] [keymap.xkb] $DISPLAY```

**详细模式编译**

```xkbcomp -v 10 [keymap.xkb] $DISPLAY```

# SYNOPSIS

**xkbcomp** [_options_] _source_ [_destination_]

# PARAMETERS

**-xkb**
> 输出 XKB 源格式。

**-xkm**
> 输出编译后的二进制格式。

**-C**
> 输出 C 头文件。

**-I** _dir_
> 将目录添加到包含搜索路径。

**-o** _file_
> 指定输出文件名。

**-v** _level_
> 设置详细程度（0-10）。

**-w** _level_
> 设置警告级别。

**-dflts**
> 为缺失的组件计算默认值。

# DESCRIPTION

**xkbcomp** 将 XKB（X Keyboard Extension）键盘描述编译为二进制格式，或直接上传到 X server。它是自定义键盘布局的核心工具，功能超出 setxkbmap 所能提供的范围。

该工具可以从运行中的 X server 提取当前键盘映射，修改后再上传更改。输出格式包括 XKB 源文件（.xkb）、编译后的二进制文件（.xkm）以及用于嵌入应用程序的 C 头文件。

XKB 提供高级键盘特性，包括多布局、死键、组合键序列、修饰键处理和无障碍选项，这些是 xmodmap 等较简单工具无法实现的。

# CAVEATS

语法复杂，需要理解 XKB 架构。没有 $DISPLAY 时只会创建文件而不会加载。出错可能使键盘处于不可用状态；请保留可用的备份布局。

# HISTORY

**xkbcomp** 是 X Keyboard Extension（XKB）的一部分，XKB 在 X11R6 中引入，用于取代早期 X 版本有限的键盘处理能力。XKB 为键盘配置提供了全面的框架，支持国际化和无障碍特性。

# INSTALL

```apt: sudo apt install x11-xkb-utils```

```dnf: sudo dnf install xkbcomp```

```apk: sudo apk add xkbcomp```

```zypper: sudo zypper install xkbcomp```

```brew: brew install xkbcomp```

```nix: nix profile install nixpkgs#xkbcomp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setxkbmap](/man/setxkbmap)(1), [xmodmap](/man/xmodmap)(1), [xev](/man/xev)(1)
