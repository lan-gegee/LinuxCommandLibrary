# TAGLINE

充满惊喜的类俄罗斯方块益智游戏

# TLDR

开始新游戏

```cuyo```

以全屏模式启动

```cuyo -f```

设置自定义窗口分辨率

```cuyo -g [800x600]```

启用调试模式

```cuyo -d```

加载自定义关卡描述文件

```cuyo [level.ld]```

显示帮助信息

```cuyo -h```

# SYNOPSIS

**cuyo** [**-d**] [**-f**] [**-g** _width_**x**_height_] [**-h**|**-?**] [**--version** _versions_] [_ld-file_]

# PARAMETERS

**-d**
> 启用调试模式。

**-f**
> 以全屏模式运行。

**-g** _WxH_
> 设置窗口大小（例如 **-g 1024x768**）。

**-h**
> 打印简短帮助信息并以状态码 0 退出。

**-?**
> 打印简短帮助信息并以状态码 1 退出。

**--version** _versions_
> 通过逗号分隔的说明符列表激活特殊的关卡版本（难度、玩家人数、eco、geek 模式等）。

_ld-file_
> 要加载的关卡描述文件路径，可用于测试自定义关卡。

# DESCRIPTION

**cuyo** 是一款支持单人或双人游玩的 Puyo Puyo / 俄罗斯方块风格益智游戏。方块从游戏区域顶部落下，玩家需要将相同颜色的团块连接起来；当足够多的相同团块相互接触时就会爆炸消除。消除引发的连锁反应会摧毁草丛等障碍物，这通常是关卡真正的目标。

众多内置关卡各有自己的规则、图形和音乐，游戏还自带关卡描述语言，玩家可以通过 _ld-file_ 参数创建并加载自己的关卡。在双人模式下，一方的连锁反应会向对方场地投放干扰块。

# KEYBINDINGS

**a**, **Left Arrow**
> 向左移动方块。

**d**, **Right Arrow**
> 向右移动方块。

**w**, **Up Arrow**
> 旋转方块。

**s**, **Down Arrow**
> 加速下落（硬降）。

**Esc**
> 暂停游戏/打开菜单。

# CAVEATS

图形和声音需要 SDL。各关卡在规则、目标和视觉风格上差异巨大，因此在一个关卡中学到的策略很难直接套用到下一个。该项目多年来基本无人维护，但大多数主流发行版仍有打包。

# HISTORY

**cuyo** 由 **Mark Weyer** 编写，约 **2001 年**首次发布，最初是向 Puyo Puyo 致敬的自由软件，但很快通过引入逐关规则变化和关卡描述语言而自成一格。它在 Debian 和 Ubuntu 中以 **cuyo** 软件包的形式提供。

# INSTALL

```pacman: sudo pacman -S cuyo```

```nix: nix profile install nixpkgs#cuyo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tetris](/man/tetris)(6), [bastet](/man/bastet)(6)
