# TAGLINE

为 picom 合成器设置窗口透明度

# TLDR

**设置窗口透明度**

```picom-trans -w [window_id] [75]```

**点击选择窗口设置**

```picom-trans -c [75]```

**按窗口名称设置**

```picom-trans -n [firefox] [90]```

**重置透明度**

```picom-trans -w [window_id] -d```

**切换透明度**

```picom-trans -c -t```

**设置不透明度 (0-100)**

```picom-trans -c [50]```

# SYNOPSIS

**picom-trans** [_-w id_] [_-n name_] [_-c_] [_-t_] [_-d_] _opacity_

# PARAMETERS

**-w** _ID_
> 窗口 ID。

**-n** _NAME_
> 窗口名称/类名。

**-c**
> 点击选择窗口。

**-t**
> 切换透明度。

**-d**
> 删除/重置透明度。

**-o** _OPACITY_
> 设置不透明度 (0-100)。

**-s**
> 选择当前聚焦的窗口。

# DESCRIPTION

**picom-trans** 为 picom 合成器设置窗口透明度。它可调整单个窗口的不透明度。

点击选择窗口支持交互式使用。点击任意窗口即可修改其透明度。

不透明度取值范围为 0（不可见）到 100（完全不透明）。75 这类数值可产生轻微的透明效果。

切换模式在透明和不透明之间转换，适合临时改变可见性。

重置操作会移除自定义透明度，窗口恢复为合成器默认设置。

# CAVEATS

需要 picom 合成器正在运行。某些窗口可能不支持透明度。需要 GPU 合成。

# HISTORY

**picom-trans** 是 **picom** 的一部分，后者是从 compton 分叉而来的合成器。它为 X11 桌面提供命令行方式的窗口透明度控制。

# INSTALL

```apt: sudo apt install picom```

```dnf: sudo dnf install picom```

```pacman: sudo pacman -S picom```

```apk: sudo apk add picom```

```zypper: sudo zypper install picom```

```nix: nix profile install nixpkgs#picom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[picom](/man/picom)(1), [xdotool](/man/xdotool)(1), [xwininfo](/man/xwininfo)(1)
