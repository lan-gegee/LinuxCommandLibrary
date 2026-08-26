# TAGLINE

ASCII 艺术跳台滑雪游戏

# TLDR

**启动游戏**

```asciijump```

**使用自定义跳台启动**

```asciijump -n [hillname]```

# SYNOPSIS

**asciijump** [_options_]

# PARAMETERS

**-n** _hillname_
> 使用 hills 目录中指定的跳台。

**-h**
> 显示帮助。

# PREVIEW

```
  \O/
   |    /
  / \  /
______/________
   90m  K-point
```

# DESCRIPTION

**asciijump** 是一个基于 ncurses 的 ASCII 艺术跳台滑雪游戏。玩家控制一名跳台滑雪运动员，把握起跳和落地的时机以获得最远距离。游戏包含多个跳台、训练和比赛模式（从游戏内菜单选择），并支持最多 10 名玩家的多人模式。

操作方法：在跳台边缘按空格起跳，落地时再按一次即可平稳着陆。时机的好坏同时影响距离分和姿势分。

# CAVEATS

需要支持 ncurses 的终端。可以自行创建跳台并放入 hills 目录。

# HISTORY

**asciijump** 由 **Fabian Breitkreutz** 创建，是在终端中再现跳台滑雪竞赛的作品。

# INSTALL

```nix: nix profile install nixpkgs#asciijump```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[moon-buggy](/man/moon-buggy)(6), [ninvaders](/man/ninvaders)(6)
