# TAGLINE

与计算机对战的经典克里比奇纸牌游戏

# TLDR

**开始一局游戏**

```cribbage```

**解释计分错误**

```cribbage -e```

**使用更简短的（安静）提示**

```cribbage -q```

**让计算机切牌**（跳过切牌提示）

```cribbage -r```

# SYNOPSIS

**cribbage** [**-eqr**]

# PARAMETERS

**-e**
> 每当玩家在为手牌或底牌计分时出错，就解释正确的得分。

**-q**
> 安静模式：打印更简短的提示和消息。

**-r**
> 由程序随机切牌，而不是提示玩家来切。

# PREVIEW

```
 Your hand:
 [5h] [5d] [Jc] [Kd]
 Starter: [5s]
 Points: 12
```

# DESCRIPTION

**cribbage** 是 **bsdgames** 合集中经典克里比奇（Cribbage）纸牌游戏的文本版实现。玩家与计算机对战，通过对局过程和记分阶段组成各类牌型组合来赢得分数。

先为底牌（crib）选牌，随后双方交替出牌，设法组出对子、顺子并凑出 15 或 31。率先达到 121 分的一方获胜。

# CAVEATS

属于 bsdgames 软件包。熟悉克里比奇规则会更有帮助。可以使用 **-e** 边玩边学计分。

# HISTORY

Cribbage 由 **Sir John Suckling** 在 **17 世纪**早期发明。这个 BSD 实现由 **Bill Joy** 编写，自 **1980 年代**起便成为 BSD 游戏的一部分。

# INSTALL

```dnf: sudo dnf install bsd-games```

```pacman: sudo pacman -S bsd-games```

```apk: sudo apk add bsd-games```

```zypper: sudo zypper install bsd-games```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[canfield](/man/canfield)(6), [mille](/man/mille)(6), [backgammon](/man/backgammon)(6)
