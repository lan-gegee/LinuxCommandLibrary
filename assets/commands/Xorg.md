# TAGLINE

X Window System 显示服务器

# TLDR

在默认显示上**启动 X 服务器**

```Xorg```

**在指定显示上启动**

```Xorg :1```

**配置并测试**但不启动

```Xorg -configure```

**使用指定的配置文件启动**

```Xorg -config [/path/to/xorg.conf]```

**在指定的虚拟终端上启动**

```Xorg vt7```

查询显示器支持的**显示模式**

```Xorg -query [hostname]```

仅**探测**（不启动服务器）

```Xorg -retro -probeonly```

# SYNOPSIS

**Xorg** [**:**_DISPLAY_] [_OPTIONS_]

# PARAMETERS

**:**_DISPLAY_
> 要使用的显示号（默认：0）。

**-config** _FILE_
> 使用指定的配置文件代替默认文件。

**-configure**
> 探测硬件并生成 xorg.conf。

**-logfile** _FILE_
> 将日志写入指定文件。

**-modulepath** _PATH_
> 可加载模块的搜索路径。

**-retro**
> 以经典 X 点纹背景启动。

**-probeonly**
> 只探测硬件，不启动服务器。

**-query** _HOST_
> 连接到 XDMCP 主机。

**-verbose** [_N_]
> 详细程度（0-7）。

**vt**_N_
> 使用虚拟终端 N。

**-nolisten** _PROTO_
> 禁止在该协议上监听（如 tcp）。

**-novtswitch**
> 启动时不自动切换虚拟终端。

# DESCRIPTION

**Xorg** 是来自 X.Org 基金会的 X Window System 服务器实现。它为类 Unix 系统上的图形用户界面提供基础，管理显示、输入设备和图形硬件。

服务器从 /etc/X11/xorg.conf 或 /etc/X11/xorg.conf.d/ 目录下的文件读取配置。现代系统通常无需显式配置即可运行，依靠自动硬件检测。

Xorg 通常由显示管理器（GDM、SDDM、LightDM）或 **startx** 脚本启动，而不是直接运行。它运行在一个虚拟终端上，并为 X 客户端提供显示连接。

# CAVEATS

运行 Xorg 需要适当的权限（通常是 root 或 video 组成员身份）。许多系统现在改用 Wayland 合成器。配置错误可能导致系统没有图形界面；请保留备份配置或准备回退方案。

# HISTORY

X.Org Server 是 XFree86 的后继者，也是 X Window System 的参考实现。在与 XFree86 发生许可证纠纷后，X.Org 基金会于 **2004 年**成立。Xorg 一直是 Linux 和 BSD 系统上的标准 X 服务器，不过在桌面场景中 Wayland 正日益取代它。

# INSTALL

```apt: sudo apt install xserver-xorg-core```

```pacman: sudo pacman -S xorg-server```

```apk: sudo apk add xorg-server```

```brew: brew install xorg-server```

```nix: nix profile install nixpkgs#xorg-server```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[startx](/man/startx)(1), [xinit](/man/xinit)(1), [xrandr](/man/xrandr)(1)
