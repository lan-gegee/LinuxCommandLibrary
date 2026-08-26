# TAGLINE

经典的 Roguelike 地牢探索游戏

# TLDR

**开始新游戏**

```nethack```

**以指定职业启动**

```nethack -p [Wizard]```

**以指定种族启动**

```nethack -r [Elf]```

**恢复已存档的游戏**

```nethack -u [playername]```

**显示版本**

```nethack --version```

# SYNOPSIS

**nethack** [_options_]

# DESCRIPTION

**nethack** 是一款经典的 Roguelike 地牢探索游戏。玩家需要在程序化生成的地牢中深入探索，面对怪物、陷阱和重重挑战，最终夺回 Yendor 护身符。

游戏具有永久死亡、ASCII 图形，以及极其深邃的玩法系统——物品、怪物与环境之间存在数不清的交互。

# PARAMETERS

**-p** _role_
> 角色的职业/类别。

**-r** _race_
> 角色的种族。

**-u** _name_
> 玩家名称。

**-s**
> 显示高分榜。

**-n**
> 以无条纹模式启动（更简洁的显示）。

**-D**
> 调试/向导模式。

# ROLES

考古学家（Archeologist）、野蛮人（Barbarian）、穴居人（Caveman）、治疗师（Healer）、骑士（Knight）、武僧（Monk）、祭司（Priest）、游侠（Ranger）、盗贼（Rogue）、武士（Samurai）、游客（Tourist）、女武神（Valkyrie）、法师（Wizard）

# KEY COMMANDS

**hjkl/方向键**：移动
**o**：开门
**c**：关门
**s**：搜索
**e**：进食
**q**：饮用
**r**：阅读
**w**：持握
**W**：穿戴
**T**：脱下
**,**：拾取
**d**：丢弃

# CAVEATS

学习曲线陡峭。永久死亡机制要求谨慎行动。ASCII 界面需要适应。机制极其深奥，需要大量学习。

# HISTORY

**NetHack** 源自 **Hack**（1985 年），而 Hack 又衍生自 **Rogue**（1980 年）。NetHack 开发团队自 **1987 年**起一直维护该游戏，使其成为开发周期最长的游戏之一。其开放式开发模式开创了协作式游戏开发的先河。

# INSTALL

```dnf: sudo dnf install nethack```

```pacman: sudo pacman -S nethack```

```apk: sudo apk add nethack```

```zypper: sudo zypper install nethack```

```brew: brew install nethack```

```nix: nix profile install nixpkgs#nethack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rogue](/man/rogue)(6), [angband](/man/angband)(6), [crawl](/man/crawl)(6), [frotz](/man/frotz)(1)
