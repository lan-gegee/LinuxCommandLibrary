# TAGLINE

中土世界背景的 Roguelike 地牢探索游戏

# TLDR

**启动游戏**

```tome```

**以指定的角色存档文件启动**

```tome -u [savefile]```

**以图形模式启动**

```tome -g```

**以文本/ASCII 模式启动**

```tome -m```

**以指定的显示尺寸启动**

```tome -- -geometry [80x50]```

# SYNOPSIS

**tome** [_options_]

# PARAMETERS

**-u** _file_
> 使用指定的存档文件。

**-g**
> 强制图形模式。

**-m**
> 强制单色/ASCII 模式。

**-n**
> 创建一个新角色。

**-r**
> 从存档文件恢复。

**-s**
> 显示高分榜。

**-v**
> 显示版本。

# CONTROLS

**?**: 显示帮助和按键绑定。

**=**：设置游戏选项。

**移动**：方向键或 vi 键（hjklyubn）。

**>**：下楼梯。

**<**：上楼梯。

**i**：查看物品栏。

**d**：丢弃物品。

**e**：进食。

**q**：喝药水。

**r**：阅读卷轴。

**w**：穿戴/装备武器防具。

**Ctrl+S**：保存并退出。

# DESCRIPTION

**tome**（Tales of Middle Earth）是一款以托尔金的中土世界为背景的 Roguelike 地牢探索游戏。玩家在程序生成的地牢中探险、与怪物战斗、收集物品，并通过经验和装备培养角色。

游戏采用永久死亡机制，即角色死亡是永久性的，存档文件会在死亡后被删除。它提供丰富的角色自定义选项，包括多种种族、职业和技能。游戏世界中包含取材自中土设定的主题场景。

ToME 源自 Angband，引入了许多创新，包括地表旅行、多个地牢以及扩展的技能系统。界面将传统的 Roguelike 键盘命令与可选的图形贴图相结合。

# CAVEATS

永久死亡意味着角色死亡后进度即告丢失。一局游戏可能持续数小时。某些版本对终端尺寸有特定要求。对 Roguelike 新手来说学习曲线较为陡峭。角色死亡后存档文件会被删除。

# HISTORY

**ToME** 于 1994 年以 PernAngband 之名起步，历经数次更名后才成为 Tales of Middle Earth。它从 Angband 分叉而来，加入了故事元素和相互连通的世界。2010 年之后更名为 Tales of Maj'Eyal（ToME 4），转向原创奇幻背景，而中土版本则继续独立发展。ToME 曾多次获得 ASCII Dreams 年度 Roguelike 奖。

# SEE ALSO

[angband](/man/angband)(6), [nethack](/man/nethack)(6), [crawl](/man/crawl)(6), [rogue](/man/rogue)(6), [moria](/man/moria)(6)
