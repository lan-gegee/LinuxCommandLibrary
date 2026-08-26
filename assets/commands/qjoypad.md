# TAGLINE

将游戏手柄输入映射到键盘和鼠标

# TLDR

**启动** QJoyPad

```qjoypad```

指定**设备目录**

```qjoypad --device=[path/to/directory]```

启动时**不用托盘**图标

```qjoypad --notray```

**强制**显示托盘图标

```qjoypad --force-tray```

**更新**设备列表

```qjoypad --update```

加载指定**布局**

```qjoypad "[layout_name]"```

# SYNOPSIS

**qjoypad** [**--device** _path_] [**--notray**] [**--force-tray**] [**--update**] [_layout_]

# PARAMETERS

**--device _path_**
> 查找设备的目录

**--notray**
> 不显示系统托盘图标

**--force-tray**
> 强制窗口管理器使用托盘图标

**--update**
> 更新正在运行的实例的设备列表

**layout**
> 要加载的布局名称

# DESCRIPTION

**qjoypad** 将游戏手柄和摇杆输入映射为键盘按键和鼠标操作。它让你能在不原生支持手柄的应用程序中使用游戏手柄。

该工具提供图形界面来创建和管理输入映射。布局可以保存和加载，以便用于不同的游戏或应用程序。

# CAVEATS

需要 evdev 或 joystick 输入设备。某些游戏可能与重新映射冲突。布局按用户存储。访问设备可能需要 udev 规则。

# HISTORY

**qjoypad** 的诞生是为了让缺乏原生手柄支持的 Linux 应用程序能够使用游戏手柄。对于仅支持键盘输入的模拟器和游戏尤其有用。

# INSTALL

```apt: sudo apt install qjoypad```

```nix: nix profile install nixpkgs#qjoypad```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[antimicrox](/man/antimicrox)(1), [xboxdrv](/man/xboxdrv)(1), [jstest](/man/jstest)(1)
