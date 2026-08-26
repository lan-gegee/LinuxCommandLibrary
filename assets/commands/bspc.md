# TAGLINE

控制 bspwm 平铺式窗口管理器

# TLDR

定义**虚拟桌面**

```bspc monitor -d [desktop_name1] [desktop_name2]```

**聚焦**指定桌面

```bspc desktop -f [number]```

**关闭**选中的窗口

```bspc node -c```

将节点**发送**到某个桌面

```bspc node -d [number]```

切换**全屏**模式

```bspc node -t ~fullscreen```

**设置**配置项的值

```bspc config [setting_name] [value]```

# SYNOPSIS

**bspc** _domain_ _command_ [_arguments_]

# DESCRIPTION

**bspc** 是 bspwm（二进制空间分区窗口管理器）的控制程序。它向窗口管理器发送命令，以操作窗口、桌面、显示器以及配置设置。

该工具采用域-命令结构，域包括 node（窗口）、desktop、monitor 和 config。

# DOMAINS

**node**
> 操作窗口节点（聚焦、移动、调整大小、关闭、状态）

**desktop**
> 管理桌面（聚焦、重命名、移除）

**monitor**
> 配置显示器及其桌面

**config**
> 获取或设置配置选项

**rule**
> 管理窗口规则

**query**
> 查询树状态

**subscribe**
> 订阅事件

# PARAMETERS

**-d, --to-desktop** _name_
> 将节点发送到指定桌面

**-f, --focus** _selector_
> 聚焦选中的节点/桌面

**-c, --close**
> 关闭选中的节点

**-t, --state** _state_
> 设置节点状态（tiled、floating、fullscreen）

# INSTALL

```apt: sudo apt install bspwm```

```dnf: sudo dnf install bspwm```

```pacman: sudo pacman -S bspwm```

```apk: sudo apk add bspwm```

```zypper: sudo zypper install bspwm```

```nix: nix profile install nixpkgs#bspwm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bspwm](/man/bspwm)(1), [sxhkd](/man/sxhkd)(1)

# RESOURCES

```[Source code](https://github.com/baskerville/bspwm)```

<!-- verified: 2026-06-22 -->
