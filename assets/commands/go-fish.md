# TAGLINE

与计算机对战经典的 Go Fish 纸牌游戏

# TLDR

**开始一局游戏**

```go-fish```

**以"专业"模式游玩**（随机决定谁先要牌）

```go-fish -p```

# SYNOPSIS

**go-fish** [**-p**]

# PARAMETERS

**-p**
> 专业模式：随机决定谁先要牌，而不是总让玩家先开始。

# PREVIEW

```
Your hand: 3 3 7 9 K
Got any 7s? y
I had a 7? Here!
Books won: 1
```

# DESCRIPTION

**go-fish** 是传统儿童纸牌游戏的文本界面版本，属于 **bsd-games** 游戏合集。玩家和计算机各发七张牌，双方轮流互相索要某个点数的牌，以收集"成套牌"（books，即该点数的全部四张牌）。

你只能索要自己手中至少持有一张的那个点数。如果对方没有这种牌，你会收到"Go Fish!"（去钓鱼）的提示，必须从剩余的牌堆中摸一张牌；若恰好摸到所请求的点数，还可以继续行动。收集完成的成套牌会被放到一旁，该点数此后不可再被索要。当任一方手牌出完时游戏结束，收集成套牌最多的一方获胜。

# CAVEATS

本命令属于 bsd-games 软件包，因此是否可用取决于你的发行版是否安装了该软件包。计算机对手很少虚张声势，基本按规则诚实出牌。

# HISTORY

**go-fish** 源自 **BSD Games** 游戏合集，该合集最初汇编于 20 世纪 80 至 90 年代，后来以 **bsd-games**/**bsdgames** 软件包的形式提供给各 Linux 发行版。

# SEE ALSO

[hangman](/man/hangman)(6), [cribbage](/man/cribbage)(6)

# RESOURCES

```[Source code](https://github.com/jsm28/bsd-games)```

```[Documentation](https://packages.debian.org/stable/bsdgames)```

<!-- verified: 2026-07-17 -->
