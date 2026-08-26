# TAGLINE

多人终端俄罗斯方块游戏

# TLDR

**连接到服务器**

```tetrinet [nickname] [server.example.com]```

**以华丽图形连接**

```tetrinet -fancy [nickname] [server]```

**以 tetrifast 模式连接**

```tetrinet -fast [nickname] [server]```

**使用自定义窗口大小**

```tetrinet -log [logfile] [nickname] [server]```

**启用投影预览**

```tetrinet -shadow [nickname] [server]```

# SYNOPSIS

**tetrinet** [_options_] _nickname_ _server_

# PARAMETERS

**-fancy**
> 使用带制表符的华丽 TTY 图形。

**-fast**
> 以 tetrifast 模式连接（更快的游戏节奏）。

**-log** _file_
> 将聊天频道消息记录到文件。

**-shadow**
> 启用方块落点投影显示。

**-slide**
> 启用方块落地后的滑动。

**-noshadow**
> 禁用方块投影。

**-noslide**
> 禁用方块滑动。

**-windows**
> 模拟 Windows 客户端行为。

# CONTROLS

**Left/Right arrows**: 水平移动方块。

**Up arrow**: 顺时针旋转方块。

**Down arrow**: 软降。

**Space**: 硬降。

**d**: 丢弃特殊块。

**1-6**: 对玩家场地使用特殊块。

**t**: 在聊天频道发言。

# DESCRIPTION

**tetrinet** 是一款最多支持六名玩家的多人俄罗斯方块游戏，运行在文本终端中。它连接 TetriNET 服务器，既支持合作组队也支持对抗比赛。

游戏特色是特殊块：当消掉包含它们的行时会出现。特殊块包括加行、消行、清空场地、方块炸弹、重力等，可用于攻击对手或帮助队友。

终端客户端使用 ncurses 进行显示，要求终端至少有 50 行。它与原始的 Windows TetriNET 服务器兼容，并支持速度更快的 tetrifast 变体。

# CAVEATS

需要至少 50 行的终端。服务器可用性不一；公共服务器的在线时间可能有限。-fancy 选项要求终端支持 Unicode。网络延迟会影响对战体验。

# HISTORY

**TetriNET** 由 St0rmCat 于 1997 年创建，是面向 Windows 的多人俄罗斯方块变体。Linux 客户端的开发目的是让 Unix 系统也能兼容访问。该游戏在 1990 年代末和 2000 年代初流行一时，其独特的特殊块机制为多人俄罗斯方块增添了策略深度。

# INSTALL

```pacman: sudo pacman -S tetrinet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tint](/man/tint)(1), [bastet](/man/bastet)(1), [vitetris](/man/vitetris)(1), [netris](/man/netris)(1)
