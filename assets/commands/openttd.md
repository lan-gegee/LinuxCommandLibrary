# TAGLINE

运输模拟游戏

# TLDR

**启动游戏**

```openttd```

**使用指定配置文件启动**

```openttd -c [config.cfg]```

**启动专用服务器**

```openttd -D```

**在启动时加载存档**

```openttd -g [savegame.sav]```

**以指定的地图生成器种子开始新游戏**

```openttd -G [12345]```

**连接到网络游戏**

```openttd -n [host:3979]```

**从特定年份开始**

```openttd -t [1970]```

**以固定分辨率运行**

```openttd -r [1280x720]```

# SYNOPSIS

**openttd** [_options_]

# PARAMETERS

**-c** _FILE_
> 使用指定的配置文件而非 openttd.cfg。

**-D** [_host_[_:port_]]
> 以专用服务器模式运行（无图形客户端）。

**-f**
> 转入后台运行（在类 Unix 系统上与 **-D** 搭配使用）。

**-g** [_FILE_]
> 加载存档启动；不带参数时立即开始新游戏。

**-G** _SEED_
> 设置用于生成地图的随机种子。

**-n** _HOST_[_:PORT_][_#PLAYER_]
> 加入运行于 _HOST_ 的网络游戏。

**-p** _PASSWORD_
> 专用服务器的口令（与 **-D** 搭配使用）。

**-t** _YEAR_
> 新游戏的起始年份。

**-r** _WIDTHxHEIGHT_
> 设置屏幕分辨率。

**-b** _BLITTER_
> 选择 blitter（图形渲染器）。

**-v** _DRIVER_
> 选择视频驱动。

**-s** _DRIVER_
> 选择声音驱动。

**-m** _DRIVER_
> 选择音乐驱动。

**-I** _SET_, **-S** _SET_, **-M** _SET_
> 分别选择基础图形集、声音集和音乐集。

**-e**
> 以场景编辑器模式启动。

**-q** _FILE_
> 将存档信息写入 stdout 后退出。

**-d** [_LEVEL_]
> 以给定的详细级别启用调试输出。

**-x**
> 退出时不自动保存配置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**openttd** 是 OpenTTD 运输模拟游戏。开源版的 Transport Tycoon Deluxe（运输大亨豪华版）。

游戏模拟运输公司的经营管理，支持多人联机。

# CAVEATS

需要基础图形集。可使用 NewGRF 模组。支持多人网络对战。

# HISTORY

OpenTTD 作为 Transport Tycoon Deluxe 的**开源重制版**而诞生。

# INSTALL

```dnf: sudo dnf install openttd```

```pacman: sudo pacman -S openttd```

```apk: sudo apk add openttd```

```zypper: sudo zypper install openttd```

```nix: nix profile install nixpkgs#openttd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[simutrans](/man/simutrans)(1)
