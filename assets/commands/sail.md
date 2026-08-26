# TAGLINE

大航海时代的海战模拟游戏

# TLDR

**开始游戏**

```sail```

**列出可用场景**

```sail -l```

**玩指定场景**

```sail -s [1]```

# SYNOPSIS

**sail** [_options_]

# PARAMETERS

**-l**
> 列出可用场景。

**-s** _NUM_
> 选择场景编号。

**-x**
> 继续玩之前保存的游戏。

# PREVIEW

```
 ~~~~~~~~  Wind: NE
 ~~A~~~~~
 ~~~~B~~~~
 ~~~~~~~~~
 ~~~~C~~~~
 A: Constitution
```

# DESCRIPTION

**sail** 是 **bsdgames** 合集中的海战模拟游戏，背景设定在"木船铁人"的大航海时代。玩家在历史海战中指挥战舰，管理帆装、船员和火炮射击。

通过命令控制舰船航向、帆索调整和炮击。游戏模拟风力影响、船体损伤、船员伤亡以及接舷战斗。

# CAVEATS

属于 bsdgames 软件包。操作复杂，有一定学习曲线。支持在同一系统上进行多人游戏。

# HISTORY

**sail** 由 **David Riggle** 和 **Ed Wang** 编写，基于 **Avalon Hill** 的桌面游戏 "Wooden Ships and Iron Men"。自 **20 世纪 80 年代**起它就是 BSD 游戏合集的一部分。

# INSTALL

```dnf: sudo dnf install bsd-games```

```pacman: sudo pacman -S bsd-games```

```apk: sudo apk add bsd-games```

```zypper: sudo zypper install bsd-games```

```brew: brew install sail```

```nix: nix profile install nixpkgs#sail```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trek](/man/trek)(6), [atc](/man/atc)(6), [battlestar](/man/battlestar)(6)
