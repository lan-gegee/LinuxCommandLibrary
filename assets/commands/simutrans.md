# TAGLINE

开源交通运输模拟游戏

# TLDR

正常**启动 Simutrans**

```simutrans```

以全屏模式**启动**

```simutrans -fullscreen```

**设置指定的屏幕尺寸**

```simutrans -screensize [1920] [1080]```

**加载指定 pakset**

```simutrans -objects [pak128/]```

**读取存档**

```simutrans -load [savegame.sve]```

以自由模式（freeplay）**启动**（不会破产）

```simutrans -freeplay```

不加载声音**启动**（对声音驱动问题有用）

```simutrans -nosound -nomidi```

**启动多人游戏服务器**

```simutrans -server [13353]```

# SYNOPSIS

**simutrans** [_options_]

# PARAMETERS

**-screensize** _WIDTH_ _HEIGHT_
> 将屏幕尺寸设置为 WIDTHxHEIGHT 像素。宽度不是 16 的倍数可能出问题。

**-fullscreen**
> 以全屏模式运行。

**-fps** _n_
> 每秒刷新显示 n 次。

**-nosound**
> 禁用音效。

**-nomidi**
> 禁用音乐。也有助于避免 64 位 Linux 上有问题的声音驱动导致崩溃。

**-freeplay**
> 启用自由模式，此模式下不会破产。

**-timeline** _0|1_
> 0 = 所有车辆从一开始就可用，1 = 按真实时间线解锁。

**-startyear** _year_
> 设置游戏的起始年份。

**-load** _savefile_
> 直接读取存档，不显示初始菜单。

**-pause**
> 以暂停状态开始已载入的游戏。

**-lang** _code_
> 使用 ISO 代码设置语言（如 en、de、fr）。

**-objects** _folder/_
> 从给定文件夹加载特定 pakset。末尾斜杠不可省略。

**-singleuser**
> 不在主目录中查找文件；只使用数据目录。

**-use_workdir**
> 使用当前工作目录作为 Simutrans 环境。

**-log** _1_
> 将全部日志输出写入 "simu.log" 文件。

**-debug** _1-4_
> 设置调试输出的详细级别（1-4）。

**-server** [_port_]
> 作为多人游戏服务器在指定端口启动（默认：13353）。

**-server_name** _"name"_
> 设置多人模式的服务器名称。

# DESCRIPTION

**Simutrans** 是一款开源交通运输模拟游戏，玩家需要建设和管理包括火车、公共汽车、卡车、船舶和飞机在内的交通网络。玩家在城市、工业区和旅游景点之间开辟路线来赚钱，同时与 AI 公司竞争。

游戏通过 "pakset" 支持大量模组，pakset 定义了车辆、建筑和游戏规则。流行的 pakset 包括 pak64、pak128 和 pak192.comic，各自提供不同的视觉风格和玩法复杂度。

配置文件在 Linux 上保存在 **~/.simutrans**。游戏可以单人游玩、自由模式游玩，也可以作为多人服务器运行，让多名玩家在同一地图上协作或竞争。

# CONFIGURATION

**~/.simutrans/**
> 用户数据目录，包含存档、设置、截图和已安装的 pakset。

**~/.simutrans/simuconf.tab**
> 主配置文件，包含显示、网络和玩法设置。

# CAVEATS

部分命令行选项（如 **-async** 和 **-net**）仅在 Linux/X-Windows 上可用。屏幕宽度不能被 16 整除时可能出现显示问题。在声音驱动有问题的系统上建议使用 **-nomidi** 选项，尤其是 64 位 Linux。Pakset 需要单独从基础游戏之外下载。

# HISTORY

**Simutrans** 由 Hansjörg Malthaner 创建，于 **1999 年**首次发布。名字是 "simulation" 和 "transport" 的合成词。Malthaner 停止活跃开发后，项目以开源形式延续，由国际开发者社区维护。这款游戏常被拿来与 Transport Tycoon 比较，但发展出了独特的特性和丰富的模组支持。开发持续活跃，定期发布新版本。

# INSTALL

```pacman: sudo pacman -S simutrans```

```zypper: sudo zypper install simutrans```

```brew: brew install simutrans```

```nix: nix profile install nixpkgs#simutrans```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openttd](/man/openttd)(6)
