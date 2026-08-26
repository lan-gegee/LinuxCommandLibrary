# TAGLINE

基于终端的俄罗斯方块游戏

# TLDR

**开始游戏**

```vitetris```

**不显示菜单启动**（直接进入游戏）

```vitetris -nomenu```

**在某个端口监听网络对战**

```vitetris listen [34034]```

**连接到网络对战**

```vitetris connect [hostname:34034]```

**显示高分榜**

```vitetris -hiscores```

为网络对战**设置玩家名称**

```vitetris -name [name] listen [port]```

# SYNOPSIS

**vitetris** [**-nomenu**] [**-hiscores**] [**listen** _port_] [**connect** _host:port_]

# PARAMETERS

**-nomenu**
> 跳过菜单，立即开始游戏。

**-hiscores**
> 打印高分列表后退出。

**-hiscores** _FILE_
> 从 FILE 读取并添加高分记录。

**listen** _port_
> 在指定端口监听传入的网络连接。

**connect** _host:port_
> 连接到远程玩家进行网络对战。主机可以是 IP 地址或主机名。使用 **connect** _port_ 可连接到本机。

**-help**
> 打印帮助后退出。使用 **-help game** 查看游戏选项，使用 **-help term** 查看终端选项。

**-js0** _device_, **-js1** _device_
> 为玩家 1 或玩家 2 指定摇杆设备。

**-name** _NAME_
> 设置网络对战的玩家名称。

# PREVIEW

```
    []
    [][]
      []

  [][][]
    [][]
  [][][][]
  [][][][]
```

# DESCRIPTION

**vitetris** 是一个基于终端的俄罗斯方块克隆，玩法类似早期的任天堂俄罗斯方块游戏。它具有可自定义的按键、高分表、带垃圾行的双人模式、网络对战以及 Linux 上的摇杆支持。

游戏完全在终端中以字符图形运行，因此可以通过 SSH 或在无图形环境的系统上游玩。按键可以通过游戏内选项菜单完全自定义。

网络对战允许两名玩家通过互联网比拼，每位玩家都可以选择自己的难度和起始高度。一方在某个端口上监听，另一方连接到该地址即可。

游戏的依赖极少，只需要 libc，并已在 Linux 和 BSD 上测试通过，还被移植到 Windows 和 DOS。

# CAVEATS

终端尺寸至少应为 80x24 才能正常显示。网络对战需要配置防火墙以允许所选端口的连接。某些终端模拟器可能存在输入延迟，影响游戏体验。

# HISTORY

**vitetris** 由 **Victor Geraldsson** 创建，于 **2000 年代初期**首次发布。它的设计目标是一个轻量的、基于终端且支持网络对战的俄罗斯方块实现。该项目至今仍在维护，可在主流 Linux 发行版的软件仓库中获取。

# INSTALL

```zypper: sudo zypper install vitetris```

```brew: brew install vitetris```

```nix: nix profile install nixpkgs#vitetris```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bastet](/man/bastet)(6), [tint](/man/tint)(6), [ninvaders](/man/ninvaders)(6)
