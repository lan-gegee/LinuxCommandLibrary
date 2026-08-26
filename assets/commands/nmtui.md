# TAGLINE

基于 curses 的 NetworkManager 文本界面（TUI）

# TLDR

打开**用户界面**

```nmtui```

**列出可用连接**，并可选择激活或停用它们

```nmtui connect```

**连接**到给定网络

```nmtui connect [name|uuid|device|SSID]```

**编辑/添加/删除**给定网络

```nmtui edit [name|id]```

设置**系统主机名**

```nmtui hostname```

# SYNOPSIS

**nmtui** [_command_] [_argument_]

# PARAMETERS

**connect**
> 列出连接并允许激活/停用

**edit**
> 添加、修改或删除网络连接

**hostname**
> 修改系统主机名

# DESCRIPTION

**nmtui**（NetworkManager Text User Interface）提供一个基于 curses 的界面，用于配置 NetworkManager 管理的网络连接。对于喜欢可视化导航的用户来说，它是比 **nmcli** 更友好的替代方案。

使用方向键浏览菜单，Enter 选择条目，Escape 返回或取消。该界面可以配置 NetworkManager 支持的以太网、Wi-Fi、VPN 及其他连接类型。

不带参数时，nmtui 会显示一个主菜单，提供编辑连接、激活连接或设置主机名的选项。使用子命令可以直接跳转到特定功能。

# CAVEATS

需要 NetworkManager 作为网络管理守护进程。终端必须支持 curses（大多数都支持）。nmcli 或图形工具中的某些高级选项可能未在 nmtui 中提供。保存后更改立即生效。修改连接需要 root 或相应的 polkit 权限。

# HISTORY

**nmtui** 于 **2014 年**随 **NetworkManager 0.9.10** 推出，为 GNOME 网络设置 GUI 和 nmcli 命令行工具提供了一个轻量的文本模式替代方案。

# INSTALL

```apt: sudo apt install network-manager```

```apk: sudo apk add networkmanager-tui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nmcli](/man/nmcli)(1), [nm-online](/man/nm-online)(1), [NetworkManager](/man/NetworkManager)(8), [nm-connection-editor](/man/nm-connection-editor)(1)
