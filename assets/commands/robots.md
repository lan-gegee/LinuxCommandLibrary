# TAGLINE

在网格追逐游戏中击退邪恶的机器人

# TLDR

**开始一局游戏**

```robots```

**开始时不显示分数**

```robots -s```

**从指定关卡开始**

```robots -j```

# SYNOPSIS

**robots** [_options_]

# PARAMETERS

**-s**
> 退出时不显示分数。

**-j**
> 跳到最高分对应的关卡。

**-t**
> 在小型终端上游戏。

# PREVIEW

```
 . . . . . . . . .
 . + . . . . + . .
 . . . . @ . . . .
 . . + . . . . + .
 . . . . . . . . .
```

# DESCRIPTION

**robots** 是 **bsdgames** 合集中的网格追逐游戏。玩家必须躲避在网格上紧追不舍的机器人。相互碰撞的机器人会被摧毁，留下的废铁堆也会在接触时摧毁其他机器人。

使用 hjklyubn 键移动。按 **t** 传送到随机位置，按 **w** 等待机器人靠近，或按 **s** 进行安全传送（使用次数有限）。策略的核心是引诱机器人相互碰撞并撞上废铁堆。

# CAVEATS

属于 bsdgames 软件包的一部分。基于终端。机器人数量随关卡递增。

# HISTORY

**robots** 源自 **1984 年**的经典游戏 **Chase**，其灵感来自《神秘博士》中的 Daleks。自 **20 世纪 80 年代**起它就是 BSD 游戏合集的一员。

# INSTALL

```dnf: sudo dnf install bsd-games```

```pacman: sudo pacman -S bsd-games```

```apk: sudo apk add bsd-games```

```zypper: sudo zypper install bsd-games```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[worm](/man/worm)(6), [greed](/man/greed)(6), [rogue](/man/rogue)(6)
