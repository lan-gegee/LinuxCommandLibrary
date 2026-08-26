# TAGLINE

经典的全局战争策略游戏

# TLDR

**开始新游戏**

```empire```

**以多水域模式开始**（岛屿地图）

```empire -w [90]```

**将消息延迟设为** 500 毫秒

```empire -d [500]```

# SYNOPSIS

**empire** [**-w** _water_] [**-s** _smooth_] [**-d** _delay_] [**-S** _interval_] [**-f** _savefile_]

# PARAMETERS

**-w** _water_
> 地图中水域的百分比（10-90，默认 70）。

**-s** _smooth_
> 地图平滑程度；数值低生成岛屿，数值高生成大陆（默认 5）。

**-d** _delay_
> 信息类消息之后的延迟毫秒数（默认 2000）。

**-S** _interval_
> 自动存档的回合间隔（默认 10）。

**-f** _savefile_
> 指定存档文件名（默认 empsave.dat）。

# PREVIEW

```
 . . + . ~ ~ ~ ~
 . A . . ~ ~ ~ ~
 . . . . . ~ ~ ~
 ~ ~ . . . . ~ ~
 ~ ~ ~ . . . . .
```

# DESCRIPTION

**empire** 是一款经典的全局战争模拟策略游戏。两位皇帝在随机生成的地图上争夺世界霸权，生产军队、战斗机、舰船等单位来探索、征服并守住领土。

游戏在由城市、陆地和海洋组成的网格地图上进行。单位在攻占的城市中生产并可逐一指挥。战争迷雾意味着只有你的单位附近的区域可见。

# CAVEATS

操作复杂，学习曲线陡峭。一局游戏可能耗时很久。终端至少需要 80x24 大小。

# HISTORY

**Empire** 最初由 **Walter Bright** 于 **20 世纪 70 年代**创建，被认为是最早的策略战争游戏之一。Unix 版本由 **Chuck Simmons** 重写，目前由 **Eric S. Raymond** 维护。

# SEE ALSO

[curseofwar](/man/curseofwar)(6), [trek](/man/trek)(6)
