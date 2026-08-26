# TAGLINE

终端接水管益智游戏

# TLDR

**开始游戏**

```nbpipes```

# SYNOPSIS

**nbpipes**

# PREVIEW

```
 .  |  .  .  .  .
 .  +--+  .  .  .
 .  .  |  .  .  .
 .  .  +--+  .  .
 S--+  .  +--+  .
```

# DESCRIPTION

**nbpipes** 是 **nbsdgames** 游戏合集中的终端接水管益智游戏，灵感来自经典的街机游戏 **Pipe Mania**。玩家必须在网格上放置水管段，保持不断流动的污水管道完好无损，防止泄漏。

在水流开始前有一个倒计时，让玩家有时间预先放置水管。一旦水流开始，玩家必须抢在它前面。替换已放置的水管会扣 3 分。用 **f** 开启快速流模式可使得分加倍，但会缩短反应时间。当水流到达死路或分数低于 -1000 时，游戏结束。

操作方式：方向键、hjkl 或 WASD 移动光标，ENTER 放置水管，**p** 暂停，**f** 切换快速流，**g** 跳过倒计时直接开始水流，**q** 退出。也支持鼠标输入。

# CAVEATS

需要支持 ncurses 的终端。属于 nbsdgames 合集。没有命令行选项。

# HISTORY

**nbpipes** 属于 **abakh** 创建的 **nbsdgames**——一个包含 18 款文字终端游戏的软件包。它实现的是经典游戏 **Pipe Mania**，最初于 **1989 年**由 The Assembly Line 发行。

# SEE ALSO

[nbmines](/man/nbmines)(1), [nbfifteen](/man/nbfifteen)(1), [nbsos](/man/nbsos)(1)
