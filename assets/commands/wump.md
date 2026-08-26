# TAGLINE

Hunt the Wumpus 洞穴探险游戏

# TLDR

**开始游戏**

```wump```

# SYNOPSIS

**wump** [**-h**] [**-a** _arrows_] [**-b** _bats_] [**-p** _pits_] [**-r** _rooms_] [**-t** _tunnels_]

# PARAMETERS

**-a** _arrows_
> 箭的数量（默认：5）。

**-b** _bats_
> 蝙蝠房间的数量（默认：2）。

**-p** _pits_
> 陷阱房间的数量（默认：2）。

**-r** _rooms_
> 房间数量（默认：20）。

**-t** _tunnels_
> 每个房间的通道数量（默认：3）。

# PREVIEW

```
 You are in room 12.
 I smell a Wumpus!
 Tunnels lead to
 3, 14, 15.

 Move or shoot? (m-s)
```

# DESCRIPTION

**wump** 是 **bsdgames** 合集中的经典游戏 **Hunt the Wumpus**（猎杀 Wumpus）。玩家在一个由通道连接的洞穴房间网络中穿行，猎杀可怕的 Wumpus，同时避开无底陷阱和超级蝙蝠。

线索会提示附近的危险："I smell a Wumpus!"（闻到 Wumpus 的气味）、"I feel a draft"（附近有陷阱）或 "Bats nearby!"（附近有蝙蝠）。玩家可以移动到相邻房间，也可以射出最多可穿过 5 个房间的弯箭。杀死 Wumpus 即获胜；但若射偏，它可能会移动。

# CAVEATS

属于 bsdgames 软件包。通过文本输入房间号进行操作。箭用完即判负，Wumpus 获胜。

# HISTORY

**Hunt the Wumpus** 由 **Gregory Yob** 于 **1973 年**创作，作为对网格类游戏的回应而诞生。它是最早的非网格计算机游戏之一，后来被广泛移植和重新演绎。

# INSTALL

```dnf: sudo dnf install bsd-games```

```pacman: sudo pacman -S bsd-games```

```apk: sudo apk add bsd-games```

```zypper: sudo zypper install bsd-games```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[adventure](/man/adventure)(6), [rogue](/man/rogue)(6), [battlestar](/man/battlestar)(6)
