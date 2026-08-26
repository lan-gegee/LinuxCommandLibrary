# TAGLINE

基于 i3lock 的可自定义锁屏工具

# TLDR

**锁定**屏幕

```betterlockscreen -l```

设置**背景**图片

```betterlockscreen -u path/to/image.png```

以**自定义**文本锁定

```betterlockscreen -l pixel --text "Custom text"```

带**显示器**超时锁定

```betterlockscreen --off 5 -l```

# SYNOPSIS

**betterlockscreen** [_OPTIONS_]

# DESCRIPTION

**betterlockscreen** 是 i3lock-color 的锁屏包装器，通过可自定义的背景效果提供美观的锁屏界面。它支持对壁纸图片应用暗化（dim）、模糊（blur）、暗化模糊（dimblur）和像素化（pixel）效果。

锁定之前，必须先用 **-u** 标志缓存背景图片，它会为每种效果生成处理后的版本。由于效果已预先计算，之后的锁定即可瞬间完成。该工具还可以使用相同的缓存图片设置桌面壁纸。

# PARAMETERS

**-l**, **--lock** [_effect_]
> 锁定屏幕（效果：dim、blur、dimblur、pixel）

**-u**, **--update** _image_
> 缓存锁屏背景图片，预生成所有效果变体

**-t**, **--text** _text_
> 在锁屏界面上显示自定义文本

**--off** _seconds_
> 锁定后经过指定秒数关闭显示器

**-w**, **--wall** [_effect_]
> 使用缓存图片设置桌面壁纸

**--display** _n_
> 设置登录框绘制在哪个显示器上（用于多显示器环境）

**--span**
> 缩放图片使其横跨多个显示器

# CONFIGURATION

**~/.config/betterlockscreenrc**
> 配置文件，用于默认效果、颜色、字体设置和锁屏外观。

# CAVEATS

需要 i3lock-color 和 imagemagick。背景图片会被缓存以加快锁定速度。首次使用需运行 -u 生成缓存图片。

# HISTORY

**betterlockscreen** 最初由 **Pavan Jadhaw** 创建，现由 betterlockscreen GitHub 组织维护。它是一个 Bash 包装脚本，在 i3lock-color 基础上增加模糊、暗化和像素化效果。

# INSTALL

```aur: yay -S betterlockscreen```

```nix: nix profile install nixpkgs#betterlockscreen```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[i3lock](/man/i3lock)(1), [xscreensaver](/man/xscreensaver)(1)
