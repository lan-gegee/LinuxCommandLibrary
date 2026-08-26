# TAGLINE

面向单一应用的 Wayland kiosk 合成器

# TLDR

以 kiosk 模式**运行**应用

```cage application```

带**参数**运行

```cage -- application arguments```

**隐藏**窗口装饰

```cage -d application```

允许**切换终端**

```cage -s application```

显示**帮助**

```cage -h```

# SYNOPSIS

**cage** [_options_] [**--**] _application_ [_arguments_]

# DESCRIPTION

**cage** 是一个 Wayland kiosk 合成器，以全屏模式运行单个应用。它专为 kiosk 部署、数字标牌或任何只需运行单个应用而无需完整桌面环境的场景设计。

# PARAMETERS

**-d**
> 禁用窗口装饰（可能导致你无法进入终端）

**-s**
> 允许用 Ctrl+Alt+F2 等快捷键切换虚拟终端

**-r**
> 旋转输出画面（0、90、180、270 度）

**-h**
> 显示帮助信息

**-v**
> 显示版本信息

**--**
> 应用参数的分隔符

# CAVEATS

不使用 -s 选项时，无法切换到其他虚拟终端。使用 -d 又没有退出应用的途径时，可能会把自己锁在外面。Cage 需要可用的 Wayland 环境。

# HISTORY

**cage** 是为 Wayland 开发的轻量级 kiosk 合成器，得名于 kiosk 模式部署中“笼中显示屏”的概念。

# INSTALL

```apt: sudo apt install cage```

```dnf: sudo dnf install cage```

```pacman: sudo pacman -S cage```

```apk: sudo apk add cage```

```zypper: sudo zypper install cage```

```nix: nix profile install nixpkgs#cage```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[weston](/man/weston)(1), [sway](/man/sway)(1), [gamescope](/man/gamescope)(1)

# RESOURCES

```[Source code](https://github.com/cage-kiosk/cage)```

<!-- verified: 2026-06-22 -->
