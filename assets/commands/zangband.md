# TAGLINE

Roguelike 地牢探索游戏

# TLDR

**开始新游戏**

```zangband```

**使用指定的存档文件开始**

```zangband -u [savefile]```

**以向导模式（调试）开始**

```zangband -w```

# SYNOPSIS

**zangband** [**-n** _num_] [**-u** _name_] [**-w**] [**-v**]

# PARAMETERS

**-n** _num_
> 以指定的服务器编号启动

**-u** _name_
> 使用指定的存档文件名

**-w**
> 以向导（调试）模式启动

**-v**
> 启用详细模式

**--**
> 忽略其余选项

# PREVIEW

```
 ##.##
 #...#  ####
 #.@.####..#
 #...#  #.>#
 #####  ####
```

# DESCRIPTION

**ZAngband** 是一款单人 roguelike 地牢探索游戏，是 Angband 的变体，而 Angband 又源自 Moria，最终可追溯至 Rogue。目标是深入越来越危险的地下城层级，获取经验和装备，最终击败强大的终极首领。

ZAngband 在 Angband 基础上增加了许多特性，包括城镇之间的荒野区域、更多种族和职业、新怪物以及扩展的魔法系统。该游戏具有永久死亡机制——角色一旦死亡就永远消失。

界面基于文本，使用 ASCII 字符表示地牢、怪物和物品。移动和操作通过键盘命令完成。

存档文件默认存储在 **~/.angband/ZAngband/save/** 中。

# CAVEATS

ZAngband 是一款复杂且学习曲线陡峭的游戏。在游戏中按 **?** 可查看详尽的帮助文档。

游戏采用永久死亡机制。请经常存档，但操纵存档文件（save-scumming）会破坏游戏设计的挑战性。

ZAngband 的开发已在很大程度上被 ToME、Sil 和 FAangband 等 Angband 变体取代。

# INSTALL

```apk: sudo apk add zangband```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[angband](/man/angband)(6), [nethack](/man/nethack)(6), [crawl](/man/crawl)(6), [tome](/man/tome)(6)
