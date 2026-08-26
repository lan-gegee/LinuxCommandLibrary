# TAGLINE

受经典街机游戏 Pacman 启发的文本界面控制台游戏

# TLDR

从**第 1 关**开始游戏

```pacman4console```

从**指定关卡**开始游戏（共有九个官方关卡）

```pacman4console --level=5```

启动**关卡编辑器**并保存到指定文件

```pacman4consoleedit [path/to/level_file]```

玩一个**自定义关卡**

```pacman4console --level=path/to/level_file```

# SYNOPSIS

**pacman4console** [_options_]

# PARAMETERS

**--level** _level_
> 从指定的关卡编号（1-9）或自定义关卡文件路径开始

# PREVIEW

```
 ##############
 #o....#......#
 #.###.#.####.#
 #.#...........#
 #.#.#.###.#.#.#
 #C..#.....#...#
 ##############
```

# DESCRIPTION

**pacman4console** 是一款受经典街机游戏 Pacman 启发的文本界面控制台游戏。它在终端中运行，用 ASCII 字符渲染迷宫、幽灵和玩家角色。

游戏包含九个官方关卡，并通过 pacman4consoleedit 关卡编辑器支持自定义关卡。

使用方向键或 WASD 在迷宫中移动 Pacman。收集所有豆子即可完成关卡。躲避幽灵，或者吃下能量豆暂时反过来追逐它们。游戏过程中按 **q** 退出。

# CAVEATS

需要支持 ncurses 库的终端。终端尺寸必须足以正常显示游戏迷宫。

# HISTORY

作为经典 Pacman 游戏的终端复刻版而创建，设计目标是能在控制台和嵌入式系统上运行。

# INSTALL

```aur: yay -S pacman4console```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sl](/man/sl)(1), [moon-buggy](/man/moon-buggy)(1), [nsnake](/man/nsnake)(1), [ninvaders](/man/ninvaders)(1), [2048](/man/2048)(1)
