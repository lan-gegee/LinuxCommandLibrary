# TAGLINE

Wayland 键盘输入模拟器

# TLDR

**输入**文本

```wtype "[Hello World]"```

输入特定**按键**

```wtype -k [Left]```

**按下并释放**指定名称的按键

```wtype -P [Left] -p [Left]```

**按下**修饰键

```wtype -M [shift|ctrl]```

**释放**修饰键

```wtype -m [ctrl]```

按键之间加入**延迟**

```wtype -d [500] "[text]"```

从**标准输入**读取

```echo "[text]" | wtype -```

# SYNOPSIS

**wtype** [_OPTIONS_] [_TEXT_]

# PARAMETERS

**-k** _KEY_
> 按名称输入特定按键

**-M** _MOD_
> 按下修饰键

**-m** _MOD_
> 释放修饰键

**-P** _KEY_
> 按下指定名称的按键

**-p** _KEY_
> 释放指定名称的按键

**-d** _MS_
> 按键之间的延迟（毫秒）

**-s** _MS_
> 在处理下一个选项前休眠（用于复杂序列）

**-**
> 从标准输入读取文本

# DESCRIPTION

**wtype** 在 Wayland 合成器上模拟键盘输入，类似于 X11 上的 xdotool type。它可以输入文本、按下特定按键并管理修饰键状态。

该工具适用于 Wayland 系统上的自动化、测试和脚本编写。

# CAVEATS

仅支持 Wayland。输入模拟需要相应的权限。由于安全限制，某些应用程序可能无法接收模拟输入。

# INSTALL

```apt: sudo apt install wtype```

```dnf: sudo dnf install wtype```

```pacman: sudo pacman -S wtype```

```apk: sudo apk add wtype```

```zypper: sudo zypper install wtype```

```brew: brew install wtype```

```nix: nix profile install nixpkgs#wtype```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ydotool](/man/ydotool)(1), [xdotool](/man/xdotool)(1)
