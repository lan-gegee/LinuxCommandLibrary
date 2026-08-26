# TAGLINE

修改 X11 按键和指针映射

# TLDR

**交换**指针的左键和右键

```xmodmap -e 'pointer = 3 2 1'```

将键盘上的某个按键**重新分配**为另一个键

```xmodmap -e 'keycode [keycode] = [keyname]'```

**禁用**键盘上的某个按键

```xmodmap -e 'keycode [keycode] ='```

**执行**文件中的所有表达式

```xmodmap [path/to/file]```

# SYNOPSIS

**xmodmap** [_options_] [_filename_]

# PARAMETERS

**-e _expression_**
> 执行给定的表达式

**-pm**
> 打印当前修饰键映射

**-pk**
> 打印当前键盘映射表

**-pp**
> 打印当前指针映射

**-grammar**
> 打印表达式语法

**-verbose**
> 详细输出

**-n**
> 只显示将要执行的操作而不应用

# DESCRIPTION

**xmodmap** 修改 X Window System 中的键盘映射和指针按钮映射。它可以重映射按键、交换修饰键以及更改鼠标按钮行为。

常见用途包括交换 Caps Lock 和 Control、重新映射特殊按键，或配置多按钮鼠标。更改保存在内存中，直到 X 会话结束。

# CAVEATS

更改不会在 X server 重启后保留。要永久生效，请将 xmodmap 命令添加到 **~/.xinitrc** 或 **~/.xprofile**。可使用 **xev** 查找键码。现代系统配置键盘时可能更推荐使用 **setxkbmap**。

# INSTALL

```apt: sudo apt install x11-xserver-utils```

```dnf: sudo dnf install xmodmap```

```apk: sudo apk add xmodmap```

```zypper: sudo zypper install xmodmap```

```brew: brew install xmodmap```

```nix: nix profile install nixpkgs#xmodmap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xev](/man/xev)(1), [setxkbmap](/man/setxkbmap)(1), [xkbcomp](/man/xkbcomp)(1)
