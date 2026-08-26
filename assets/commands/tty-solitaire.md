# TAGLINE

基于终端的 Klondike 接龙纸牌游戏

# TLDR

**开始游戏**

```ttysolitaire```

**设置允许翻牌堆的遍数**

```ttysolitaire -p [3]```

**使用指定的牌背颜色**

```ttysolitaire -b [blue]```

# SYNOPSIS

**ttysolitaire** [_options_]

# PARAMETERS

**-p** _NUM_
> 允许翻阅牌堆的遍数（默认：不限）。

**-b** _COLOR_
> 牌背颜色：red、green、blue、cyan、magenta、yellow、white、black。

**-h**
> 显示帮助信息。

**-v**
> 显示版本信息。

# PREVIEW

```
 [Kh] [  ] [  ] [  ]
 [Ac] [2d] [3c]
 [##] [##] [##] [##]
```

# DESCRIPTION

**ttysolitaire** 是一个基于 ncurses 的终端 Klondike 接龙纸牌游戏。经典的接龙玩法，包含七个牌桌列、四个基础堆以及一个发牌堆/弃牌堆。

操作方式：方向键或 hjkl 移动光标，空格键选择/放置纸牌，**m** 从发牌堆抽牌，**q** 退出。在牌桌上纸牌按交替颜色递减排列，在基础堆上按花色递增排列。

# CAVEATS

需要支持 ncurses 和颜色的终端。终端最小尺寸为 80x24。

# HISTORY

**tty-solitaire** 由 **Mats Rauhala** 创建，是一个轻量级的终端接龙实现，让用户在没有图形环境的情况下也能体验经典纸牌游戏。

# INSTALL

```pacman: sudo pacman -S tty-solitaire```

```brew: brew install tty-solitaire```

```nix: nix profile install nixpkgs#tty-solitaire```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[canfield](/man/canfield)(6), [mille](/man/mille)(6), [cribbage](/man/cribbage)(6)
