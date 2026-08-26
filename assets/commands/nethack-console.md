# TAGLINE

经典 Roguelike 地牢探索游戏，你需要深入迷宫夺回护身符

# TLDR

**启动 NetHack**

```nethack```

**以指定用户名启动**

```nethack -u [playername]```

**以发现模式启动**（不计分的探索）

```nethack -X```

**显示高分榜**后退出

```nethack -s```

**以指定游戏目录启动**

```nethack -d [path/to/directory]```

**显示版本信息**

```nethack --version```

**显示配置文件路径**

```nethack --showpaths```

# SYNOPSIS

**nethack** [_-d directory_] [_-n_] [_-u playername_] [_-X_]

**nethack** -s [_-v_] [_-p profession_] [_names_...]

# PARAMETERS

**-u** _NAME_
> 以指定的玩家名称开始游戏

**-d** _DIR_
> 使用替代的游戏目录

**-D**
> 以调试/向导模式启动（仅限管理员）

**-X**
> 以发现模式启动（不计分）

**-n**
> 不显示游戏管理员的消息

**-s**
> 显示高分榜并退出

**-v**
> 显示版本信息

**-p** _PROFESSION_
> 按职业/角色过滤分数

**--version**
> 打印版本并退出

**--showpaths**
> 显示预期的配置文件位置

# ENVIRONMENT

**NETHACKOPTIONS**
> 游戏选项与设置

**NETHACKDIR**, **HACKDIR**
> 游戏目录位置

**HOME**
> 用于存放配置文件的用户主目录

**TERM**
> 显示所用的终端类型

# PREVIEW

```
 ------       -----
 |....|  ###  +...|
 |..@.|###   #|.>.|
 |.<..|      #|...|
 ------       -----
```

# DESCRIPTION

**nethack** 是一款经典的 Roguelike 地牢探索游戏，玩家需要深入"凶险迷宫"（Mazes of Menace）夺回 Yendor 护身符。控制台版本使用 ASCII 字符表示游戏世界，因此可以在任何终端上运行。

玩家角色（**@**）在程序化生成的地牢中探索，与怪物战斗、收集物品并躲避陷阱。游戏采用永久死亡机制——角色死亡后游戏即结束，必须从头开始。这种设计理念强调谨慎行动并从失败中学习。

游戏选项通过 **~/.nethackrc** 或 **NETHACKOPTIONS** 环境变量配置。在游戏中，按 **?** 获取帮助，按 **O** 查看和修改选项。移动使用 **hjklyubn** 键（vi 风格），或在启用 **number_pad** 选项后使用数字小键盘。

# CAVEATS

NetHack 学习曲线陡峭，包含数百种命令和交互机制。游戏不会手把手引导你——需要在实验和死亡中不断摸索。存档在死亡时会被删除（永久死亡）。不同发行版的二进制名称可能略有差异（nethack、nethack-console、nethack-tty）。

# HISTORY

NetHack 源自 **Hack**（1982 年），而 Hack 又脱胎于最早的 Roguelike 游戏 **Rogue**（1980 年）。开发始于 **1987 年**，由 NetHack 开发团队负责，其名称反映了它作为早期互联网协作项目的起源。它是计算机游戏史上最具影响力的游戏之一，启发了无数 Roguelike 及整个"roguelike"游戏类型。该游戏至今仍在活跃开发，3.6 版本在间隔 12 年后于 **2015 年**发布。

# INSTALL

```dnf: sudo dnf install nethack```

```pacman: sudo pacman -S nethack```

```apk: sudo apk add nethack```

```zypper: sudo zypper install nethack```

```brew: brew install nethack```

```nix: nix profile install nixpkgs#nethack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rogue](/man/rogue)(6), [angband](/man/angband)(6), [crawl](/man/crawl)(6)
