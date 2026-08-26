# TAGLINE

设置 X11 窗口透明度

# TLDR

**通过点击设置窗口透明度**

```transset [0.8]```

**为特定窗口 ID 设置透明度**

```transset -i [0x1400003] [0.75]```

**切换被点击窗口的透明状态**

```transset -t```

**增加被点击窗口的透明度**

```transset --inc [0.1]```

**降低被点击窗口的透明度**

```transset --dec [0.1]```

**应用到所有窗口**

```transset -a [0.9]```

# SYNOPSIS

**transset** [_options_] [_opacity_]

# PARAMETERS

**-i**, **--id** _id_
> 按 X 窗口 ID 选择窗口。

**-n**, **--name** _name_
> 按名称选择窗口。

**-t**, **--toggle**
> 在当前不透明度和完全不透明之间切换。

**--inc** _value_
> 将不透明度增加指定数值。

**--dec** _value_
> 将不透明度降低指定数值。

**-a**, **--all**
> 应用到所有窗口。

**-p**, **--point**
> 选择指针下的窗口（默认行为）。

**-v**, **--verbose**
> 输出详细日志。

**--version**
> 显示版本。

# DESCRIPTION

**transset** 通过修改窗口的 _NET_WM_WINDOW_OPACITY 属性来设置 X11 窗口透明度。不透明度取值范围为 0（完全透明）到 1（完全不透明），默认值为 0.75。

该工具需要合成窗口管理器（如 picom、xcompmgr、KWin 或 Mutter）才能真正渲染透明效果。若没有合成器，属性虽然会被设置，但不会产生任何视觉效果。

默认情况下，transset 进入交互模式，点击某个窗口即可设置其透明度。窗口 ID 或名称选项则支持非交互式的脚本化使用。

# CAVEATS

需要正在运行的合成管理器才能看到效果。仅支持 X11；在 Wayland 上无法使用。某些应用程序可能不理会透明度设置。窗口 ID 在不同会话之间会变化。

# HISTORY

**transset** 作为 X.Org 项目的一部分开发，用于演示和使用 COMPOSITE 扩展。Daniel Forchheimer 开发的 transset-df 变体增加了命令行选项，无需交互式点击即可在脚本中使用。

# INSTALL

```apt: sudo apt install x11-apps```

```zypper: sudo zypper install transset```

```nix: nix profile install nixpkgs#transset```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xwininfo](/man/xwininfo)(1), [picom](/man/picom)(1), [xcompmgr](/man/xcompmgr)(1), [xprop](/man/xprop)(1)
