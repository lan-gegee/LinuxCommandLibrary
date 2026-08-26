# TAGLINE

基于终端的 ncurses 数独游戏

# TLDR

**开始新一局数独游戏**

```nudoku```

**以指定难度开始**

```nudoku -d [hard]```

**显示帮助**

```nudoku -h```

# SYNOPSIS

**nudoku** [_options_]

# PARAMETERS

**-d** _DIFFICULTY_
> 设置难度级别（easy、normal、hard）

**-c**
> 使用黑白模式（无颜色）

**-h**
> 显示帮助信息

**-v**
> 显示版本信息

# IN-GAME CONTROLS

**h j k l** 或 **方向键**
> 移动光标（vi 风格或方向键）

**1-9**
> 在当前格子中填入数字

**0** 或 **Backspace**
> 清除当前格子

**H**
> 获取提示（填充一个格子）

**N**
> 开始新一局游戏

**C**
> 让计算机解开谜题

**Q**
> 退出游戏

**?**
> 显示帮助

# DESCRIPTION

**nudoku** 是一款使用 ncurses 库构建的终端数独游戏。它提供交互式界面，让你可以直接在终端里玩经典的数字谜题。

游戏会生成各种难度级别的随机数独谜题。玩家需要填写 9x9 网格，使每一行、每一列和每个 3x3 宫都包含 1 到 9 的所有数字。预先填好的格子不能修改。

界面采用 vi 风格的移动键（h、j、k、l）进行导航，对 vim 用户来说非常熟悉。偏好方向键的用户也可以使用方向键。游戏可以通过 **C** 命令自动解谜。

# CAVEATS

nudoku 可能未在所有发行版中默认安装。软件包名称各不相同——可能是 **nudoku**，图形版本则可能是 **gnome-sudoku**。终端必须支持 ncurses 才能正常显示。某些终端可能无法正确渲染颜色；可使用 **-c** 启用黑白模式。

# HISTORY

nudoku 由 **Michael Vetter**（jubalh）创建，是一款简单轻量的终端数独游戏。其名字由 "ncurses" 和 "sudoku" 组合而成。该项目是基于 GPL v3 许可证的开源软件。数独本身起源于 20 世纪 80 年代的日本，由更早的数字谜题演变而来，并在 2000 年代风靡全球。

# SEE ALSO

[gnome-sudoku](/man/gnome-sudoku)(6), [nethack](/man/nethack)(6), [rogue](/man/rogue)(6)
