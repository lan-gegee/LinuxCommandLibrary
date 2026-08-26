# TAGLINE

以纽约市为背景的交易策略游戏

# TLDR

**以文本模式开始游戏**

```dopewars -t```

使用指定的玩家名称**开始游戏**

```dopewars -t -n [name]```

# SYNOPSIS

**dopewars** [_options_]

# PARAMETERS

**-t**
> 文本模式（curses）界面。

**-n** _NAME_
> 设置玩家名称。

**-s**
> 作为多人游戏服务器运行。

**-c**
> 连接到多人游戏服务器。

**-h**
> 显示帮助。

# PREVIEW

```
 Bronx -> Manhattan
 Cocaine:  $15000
 Heroin:    $6300
 Cash: $2000  Debt: $5500
 Day 1 of 30
```

# DESCRIPTION

**dopewars** 是一款策略游戏：玩家要在 30 天内穿梭于纽约各处买卖货物。目标是还清高利贷，同时利用街区间价格的差异尽可能多赚钱。

遭遇警察、市场波动等随机事件为游戏增添不可预测性。游戏还提供多人模式，可以通过网络与其他玩家对抗。

# CAVEATS

终端模式需使用 **-t** 标志。多人游戏需要一台正在运行的服务器。游戏的题材可能被认为存在争议。

# HISTORY

**dopewars** 基于 **Drug Wars**——由 **John E. Dell** 于 **1984 年**为 TI-83 计算器编写的游戏。Unix 版本由 **Ben Webb** 创建，自 **20 世纪 90 年代末**以来一直处于活跃维护状态。

# INSTALL

```pacman: sudo pacman -S dopewars```

```brew: brew install dopewars```

```nix: nix profile install nixpkgs#dopewars```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trek](/man/trek)(6), [adventure](/man/adventure)(6)
