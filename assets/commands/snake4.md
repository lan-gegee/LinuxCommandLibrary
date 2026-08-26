# TAGLINE

基于终端的经典贪吃蛇游戏

# TLDR

**启动**游戏

```snake4```

显示**高分榜**

```snake4 --highscores```

显示**版本**

```snake4 --version```

显示**帮助**

```snake4 --help```

# SYNOPSIS

**snake4** [**-hHV**] [**-M** _file_]

# PARAMETERS

**-h, --help**
> 显示用法信息并退出

**-H, --highscores**
> 显示高分列表并退出

**-V, --version**
> 显示版本信息并退出

**-M, --merge-highscores** _file_
> 将单独的高分文件合并到默认文件（仅限管理员）

# CONTROLS

**方向键**
> 控制蛇的移动（上、下、左、右）

**1-5**
> 选择游戏关卡

**空格键**
> 暂停/继续游戏

**q**
> 退出游戏

# DESCRIPTION

**snake4** 是经典贪吃蛇游戏在 Unix/X11 系统上的终端实现。玩家控制一条蛇，通过吃食物变长，同时避开障碍物、墙壁和自己的尾巴。

游戏包含多个难度级别、一个名为"邪恶摇头者"的敌对角色以及各种道具。细长药丸可以缩短蛇身并奖励额外分数。闪烁的食物表示正在腐烂，吃掉后会中毒。全站共享的高分文件记录前 200 名玩家。

# CAVEATS

高分文件由整个系统共享，每个用户只有一条记录。合并高分需要管理员权限。游戏需要支持方向键的终端。也接受 X11 工具包选项。

# HISTORY

**snake4** 是 BSD 游戏合集的一部分，提供经典的 Unix 娱乐软件。贪吃蛇这一游戏类型可追溯到 **20 世纪 70 年代**的街机游戏，并随着手机上的实现而广为流行。snake4 将这种经典玩法带到了 Unix 终端环境。

# INSTALL

```nix: nix profile install nixpkgs#snake4```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nsnake](/man/nsnake)(6), [bsdgames](/man/bsdgames)(6), [nethack](/man/nethack)(6)
