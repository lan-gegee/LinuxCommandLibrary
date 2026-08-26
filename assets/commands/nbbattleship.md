# TAGLINE

终端海战棋（战舰）游戏

# TLDR

**玩战舰游戏**

```nbbattleship```

# SYNOPSIS

**nbbattleship**

# PREVIEW

```
   A B C D E F
 1 ~ ~ X ~ ~ ~
 2 ~ ~ ~ ~ O ~
 3 ~ O ~ ~ ~ ~
 4 ~ ~ ~ ~ ~ ~
```

# DESCRIPTION

**nbbattleship** 是 **nbsdgames** 游戏合集中的一个终端战舰（海战棋）游戏。玩家先在网格上布置舰船，然后轮流猜测对方舰船的位置。击中一艘船的所有部分即可将其击沉；击沉所有船只即获胜。

游戏使用 ncurses 界面。用方向键或 hjkl 移动，按 ENTER 射击，放置阶段按 R 旋转舰船，按 q 退出。也支持鼠标输入。

# CAVEATS

需要支持 ncurses 的终端。属于 nbsdgames 合集。没有命令行选项。

# HISTORY

**nbbattleship** 属于 **abakh** 创建的 **nbsdgames**——一个包含 18 款文字终端游戏的软件包。它实现的是经典桌游 **Battleship**（战舰），一种起源于 **20 世纪 30 年代**铅笔纸面游戏的策略猜谜游戏。

# SEE ALSO

[nbmines](/man/nbmines)(1), [nbsos](/man/nbsos)(1), [nbcheckers](/man/nbcheckers)(1)
