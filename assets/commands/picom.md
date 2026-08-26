# TAGLINE

独立的 X11 合成器，提供阴影、透明、模糊和淡入淡出效果

# TLDR

以默认设置**在前台运行**

```picom```

**作为守护进程运行**（后台）

```picom -b```

**使用指定配置文件**

```picom --config [~/.config/picom/picom.conf]```

**选择渲染后端**

```picom --backend [glx]```

**启用实验性的重写后端**（旧版本）

```picom --experimental-backends --backend [glx]```

**禁用窗口阴影**

```picom --no-shadow```

**设置非活动窗口的默认不透明度**

```picom -i [0.9]```

**启用垂直同步**

```picom --vsync```

**记录日志到文件**而非 stderr

```picom --log-file [~/.picom.log]```

# SYNOPSIS

**picom** [_options_]

# PARAMETERS

**-b**, **--daemon**
> 作为守护进程运行（分叉到后台）。

**--config** _FILE_
> 配置文件的路径（默认 `~/.config/picom/picom.conf`）。

**--backend** _TYPE_
> 渲染后端：`glx`、`xrender` 或 `xr_glx_hybrid`（遗留）。某些构建的现代 picom 还支持 Vulkan 后端。

**--experimental-backends**
> 使用重写后的后端实现。旧版本上需要该选项才能使用 `dual_kawase` 模糊等特性。picom ≥ 10 无需此选项，新后端已是默认值。

**--shadow** / **--no-shadow**
> 启用或禁用投影阴影。

**--fading** / **--no-fading-openclose**
> 在窗口打开/关闭时启用淡入淡出，或专门针对打开/关闭禁用。

**--fade-in-step** _N_ / **--fade-out-step** _N_
> 淡入淡出时每帧的不透明度步长（0.001–1.0）。

**-i** _OPACITY_, **--inactive-opacity** _OPACITY_
> 非活动窗口的默认不透明度（0.0–1.0）。

**-e** _OPACITY_, **--frame-opacity** _OPACITY_
> 窗口边框的不透明度。

**--active-opacity** _OPACITY_
> 聚焦窗口的不透明度。

**--blur-method** _METHOD_
> 模糊算法：`none`、`gaussian`、`box`、`kernel`、`dual_kawase`。

**--blur-background**
> 模糊透明窗口背后的背景。

**--vsync**
> 为所选后端使用合适的方式启用垂直同步。

**--use-damage** / **--no-use-damage**
> 只渲染发生变化的区域（更快，默认开启）。

**--unredir-if-possible**
> 取消重定向全屏窗口（如全屏视频/游戏）以提升性能。

**--corner-radius** _N_
> 用半径 _N_ 像素圆化窗口角落（picom ≥ 10）。

**--shadow-radius** _N_ / **--shadow-offset-x** _N_ / **--shadow-offset-y** _N_ / **--shadow-opacity** _O_
> 投影阴影的形状、偏移和不透明度。

**--log-level** _LEVEL_
> `trace`、`debug`、`info`、`warn`、`error`、`fatal`。

**--log-file** _FILE_
> 将日志写入 _FILE_ 而不是 stderr。

**-v**, **--version**
> 显示版本。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**picom** 是一个轻量级的独立 X11 合成器——它把绘制到屏幕外像素图中的窗口内容合成为你最终看到的图像，因此能添加窗口管理器本身不会渲染的效果：阴影、淡入淡出、透明背景模糊、圆角（v10+）和动画。它通常与非自身带合成器的平铺/浮动窗口管理器（i3、bspwm、Openbox、awesome、Xmonad）一同启动。

大多数实际配置位于 `picom.conf` 中。命令行标志会覆盖配置值，便于测试。

# CAVEATS

只能在 X11 下工作（Wayland 合成器自行渲染）。`glx` 后端需要 GLX 正常工作的 GPU 驱动；VirtualBox/VMware 虚拟机通常需要 `xrender`。与其他合成器冲突（包括 KWin 和 Mutter）——请先停用它们。特效在老旧硬件上资源消耗大；如果 CPU/GPU 跟不上，请禁用模糊和阴影。

# HISTORY

**picom** 是 **compton** 的活跃维护分支，而 compton 本身又是 **xcompmgr-dana**/**xcompmgr** 的分支。在 compton 停止维护后由 **yshui** 接手维护，picom 如今是平铺 WM 社区的标准合成器。

# INSTALL

```apt: sudo apt install picom```

```dnf: sudo dnf install picom```

```pacman: sudo pacman -S picom```

```apk: sudo apk add picom```

```zypper: sudo zypper install picom```

```nix: nix profile install nixpkgs#picom```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xcompmgr](/man/xcompmgr)(1), [compton](/man/compton)(1), [i3](/man/i3)(1), [bspwm](/man/bspwm)(1)
