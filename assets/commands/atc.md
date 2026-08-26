# TAGLINE

文本界面空中交通管制模拟游戏

# TLDR

**启动**空中交通管制游戏

```atc```

以**指定关卡**启动

```atc -g [game]```

**列出**可用的关卡

```atc -l```

显示**高分榜**

```atc -s```

# SYNOPSIS

**atc** [_-u?lstp_] [_-gf game_] [_-r seed_]

# PREVIEW

```
 .  .  .  *  .  .
 .  A2 .  .  .  .
 .  .  .  .  B1 .
 .  .  .  .  .  .
 .  .  C3 .  .  .
```

# DESCRIPTION

**atc** 是 BSD games 合集中的经典文本界面空中交通管制模拟游戏。玩家引导喷气机和螺旋桨飞机经由出口和机场抵达目的地，同时避免碰撞，并需要同时管理多架飞机。

喷气机每个更新周期移动一次，而螺旋桨飞机每两个周期移动一次。飞机在 7000 英尺高度进入空域，必须在 9000 英尺经出口离开或降落在机场。若两架飞机靠得过近，游戏结束。得分取决于安全处置的飞机数量。

# PARAMETERS

**-g** _game_, **-f** _game_
> 选择要玩的指定关卡/机场布局

**-l**
> 列出可用的关卡文件

**-s**, **-t**
> 显示高分排名

**-r** _seed_
> 设置随机种子，以获得可复现的游戏

**-p**
> 打印游戏私有文件目录的路径

**-u**, **-?**
> 显示用法信息

# CONTROLS

命令以序列方式输入：
- 字母用于选择飞机
- 数字和字母控制动作（高度、转弯、方向）
- 机场/信标字母作为导航目标

# CAVEATS

需要基于字符显示的终端。学习曲线较陡。若飞机相撞或靠得太近则游戏结束。在大多数系统上是 bsd-games 软件包的一部分。

# HISTORY

**atc** 由加州大学伯克利分校的 **Ed James** 编写，自 **1980 年代**起就被收入 BSD games 合集。

# INSTALL

```dnf: sudo dnf install bsd-games```

```pacman: sudo pacman -S bsd-games```

```apk: sudo apk add bsd-games```

```zypper: sudo zypper install bsd-games```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[nethack-console](/man/nethack-console)(6), [adventure](/man/adventure)(6)
