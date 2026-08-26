# TAGLINE

Roguelike 地下城探索游戏

# TLDR

**开始新游戏**

```angband```

**加载指定的角色存档**

```angband -u[character]```

**创建全新角色**（跳过加载）

```angband -n```

**以 X11 前端运行**，打开 4 个窗口

```angband -mx11 -- -n4```

**以 SDL 前端运行**

```angband -msdl```

**以向导（调试）模式启动**，会禁用高分榜

```angband -w```

**显示最高分**

```angband -s[10]```

**显示用法信息**

```angband -h```

# SYNOPSIS

**angband** [_options_] [**--** _suboptions_]

# PARAMETERS

**-h**
> 显示用法信息。

**-n**
> 开始新角色（不加载已有存档）。

**-w**
> 启用向导（调试）模式；高分榜被禁用。

**-g**
> 在前端支持时请求图形模式。

**-r**
> 重新平衡怪物。

**-s**_num_
> 显示指定数量的最高分后退出。

**-u**_who_
> 加载角色 _who_ 的存档。

**-m**_sys_
> 选择核心显示系统（curses/控制台用 **gcu**，还有 **x11**、**sdl** 等）。

**-d**_lib_**=**_path_
> 覆盖某个库子目录的路径。有效的 _lib_ 键包括 **help**、**info**、**user**、**save**、**data**、**scores**、**xtra**、**edit** 和 **file**。

**--**
> 将其余参数传递给所选前端（例如 **-n**_N_ 表示打开 _N_ 个 X11 窗口）。

# PREVIEW

```
 ######
 #....#  ####
 #..@.####..#
 #....#  #..#
 ######  ####
```

# DESCRIPTION

**Angband** 是一款经典的单人 Roguelike 地下城探索游戏。玩家创建一个角色，深入 100 层地下城，最终击败黑暗魔君 Morgoth。游戏具有永久死亡、程序化生成关卡和回合制玩法等特色。

角色可从多个种族（人类、精灵、矮人、霍比特人等）和职业（战士、法师、牧师、盗贼等）中选择，每种组合都有不同的能力和玩法。战斗、魔法和装备管理是核心机制，稀有神器能提供强大的加成。

游戏在终端中以 ASCII 字符表现地下城、怪物和物品，不过也有图形贴图可用。每次会话自动保存，默认死亡即永久，存档会被删除。

# GAMEPLAY BASICS

**移动**：使用数字小键盘或 **hjklyubn** 按键
**命令**：**i** 物品栏，**e** 装备，**m** 魔法，**g** 拾取物品，**d** 丢弃，**R** 休息
**楼梯**：**>** 下行，**<** 上行
**目标锁定**：***** 选定目标，**t** 射击
**保存并退出**：**Ctrl-X**

# CONFIGURATION

**~/.angband/Angband/**
> 用户目录，包含存档文件、角色转储和偏好设置。

**~/.angband/Angband/user/pref.prf**
> 用户偏好文件，用于键位映射、颜色和显示设置。

# CAVEATS

永久死亡意味着一次失误就可能失去数小时的进度。学习曲线陡峭，需要记住大量键盘命令。利用存档回档虽然可行，但会破坏预期的游戏体验。某些终端模拟器在显示或按键绑定方面可能有问题。

# HISTORY

Angband 源自 **Moria**（1983 年）的一个变体，而 Moria 本身又受 **Rogue**（1980 年）启发。游戏名称来自托尔金作品中 Morgoth 的要塞。开发始于 **1990** 年，由华威大学的学生发起。它成为最具影响力的 Roguelike 游戏之一，催生了 ZAngband、ToME 和 Sil 等众多变体。该游戏至今仍由社区积极维护。

# INSTALL

```dnf: sudo dnf install angband```

```pacman: sudo pacman -S angband```

```brew: brew install angband```

```nix: nix profile install nixpkgs#angband```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[nethack](/man/nethack)(1), [crawl](/man/crawl)(6), [tome](/man/tome)(6), [moria](/man/moria)(6), [rogue](/man/rogue)(6)
