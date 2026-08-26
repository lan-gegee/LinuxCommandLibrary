# TAGLINE

经典单人地下城探索游戏

# TLDR

**启动 Moria**

```moria```

**使用指定存档文件启动**

```moria -s [savefile]```

**以向导模式启动**

```moria -w```

# SYNOPSIS

**moria** [_options_]

# PARAMETERS

**-s** _file_
> 要使用的存档文件。

**-w**
> 向导模式（调试用）。

**-r**
> 恢复已保存的游戏。

# DESCRIPTION

**Moria** 是一款经典的单人地下城探索游戏（roguelike）。玩家在不断危险的地下城中逐层深入，与怪物战斗并收集宝藏，最终目标是击败 Balrog（炎魔）。

Moria 具有永久死亡、随机生成地下城和 ASCII 图形等特性。

# CONTROLS

```
hjkl or arrows  - Movement
i               - Inventory
e               - Equipment
c               - Cast spell
f               - Fire ranged
>               - Go down stairs
<               - Go up stairs
?               - Help
```

# CHARACTER CLASSES

```
Warrior, Mage, Priest, Rogue
Ranger, Paladin
```

# CAVEATS

永久死亡（角色死亡不可恢复）。ASCII 图形。键盘操作复杂。角色死亡后存档会被删除。

# HISTORY

Moria 由 **Robert Alan Koeneke** 自 **1983 年**起在俄克拉何马大学开发，灵感来自 Rogue。它成为 Angband 及许多其他 roguelike 游戏的鼻祖。

# SEE ALSO

[angband](/man/angband)(1), [nethack](/man/nethack)(1), [rogue](/man/rogue)(1), [crawl](/man/crawl)(1)
