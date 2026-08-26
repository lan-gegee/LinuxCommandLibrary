# TAGLINE

Roguelike 地牢探索游戏

# TLDR

**启动 Dungeon Crawl Stone Soup**

```crawl```

**以指定角色启动**

```crawl -name [CharacterName]```

**使用种子启动以获得可复现的地牢**

```crawl -seed [12345]```

**以控制台模式游玩**

```crawl -console```

**以图形（tiles）模式游玩**

```crawl -tiles```

**以指定的种族和背景启动**

```crawl -species [Minotaur] -background [Berserker]```

# SYNOPSIS

**crawl** [_options_]

# PARAMETERS

**-name** _name_
> 设置角色名称。

**-species** _species_
> 选择起始种族。

**-background** _background_
> 选择起始背景（职业）。

**-seed** _n_
> 设置地牢生成种子。

**-console**
> 强制控制台（ASCII）模式。

**-tiles**
> 强制图形（tiles）模式。

**-sprint**
> 以 Sprint 模式开始。

**-tutorial**
> 开始教学关卡。

**-morgue** _dir_
> morgue 文件所在的目录。

**-version**
> 显示版本。

# PREVIEW

```
 ####
 #..####
 #..@..#
 #.....#
 ########
```

# DESCRIPTION

**Dungeon Crawl Stone Soup**（简称 DCSS 或 Crawl）是一款专注于战斗、策略和细致资源管理的 Roguelike 地牢探索游戏。玩家要深入程序生成的地牢，取回 Zot 之球并活着逃出去。

游戏特色包括永久死亡（角色死亡不可撤销）、回合制玩法、数十种拥有独特能力的种族与背景、供奉各路神祇的宗教系统、庞大而丰富的魔法与物品体系，以及讲求战术的深度战斗。

DCSS 以精简的设计哲学著称：去除 Roguelike 中常见的繁琐元素，同时保持深度。既有控制台（ASCII）版本，也有图形 tiles 版本。

# GAMEPLAY BASICS

**移动**：方向键或数字小键盘
**命令**：**o** 自动探索，**g** 拾取物品，**i** 物品栏
**战斗**：朝敌人移动即可攻击
**休息**：按 **5** 或 **.** 休息/等待
**楼梯**：**>** 下行，**<** 上行
**保存**：**Ctrl-S**（或直接退出，会自动保存）

# CONFIGURATION

**~/.crawlrc**
> 用户级配置文件，包括键位绑定、自动拾取规则、显示选项和游戏偏好。

# CAVEATS

学习曲线陡峭；入门阶段要做好屡屡阵亡的心理准备。没有手动存档——死亡是永久的。一局游戏可能耗时数小时。控制台模式需要支持 Unicode 或 CP437 图形的终端。

# HISTORY

Dungeon Crawl Stone Soup 于 **2006 年**从 **Linley's Dungeon Crawl** 分叉而来，当时原作的开发已陷入停滞。DCSS 得名于"石头汤"式的开发理念（众人协作改进），由志愿者社区持续开发至今。它被公认为最优秀的现代 Roguelike 之一，因既易于上手又不失挑战性而广受好评。

# INSTALL

```dnf: sudo dnf install crawl```

```nix: nix profile install nixpkgs#crawl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nethack](/man/nethack)(6), [angband](/man/angband)(6), [tome](/man/tome)(6)
