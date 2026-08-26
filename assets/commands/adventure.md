# TAGLINE

原版巨洞冒险（Colossal Cave）文字冒险游戏

# TLDR

**启动**冒险游戏

```adventure```

**从存档恢复**游戏

```adventure -r```

# SYNOPSIS

**adventure** [_-r_]

# PREVIEW

```
You are inside a building.
There are some keys on the
ground here.

> get keys
OK
```

# DESCRIPTION

**adventure**（也称为 Colossal Cave Adventure 或 ADVENT）是最早的文字冒险游戏。玩家探索一个完全用文字描述的洞穴系统，使用简单的“动词 + 名词”命令与环境互动，例如 “GO NORTH”、“GET LAMP” 或 “KILL DRAGON”。

游戏包含寻宝、解谜以及对一个奇幻地下世界的探索，那里居住着矮人、海盗和一条龙。命令通常是两个词（动词 + 名词），移动则用单个词。

# PARAMETERS

**-r**
> 恢复之前保存的游戏

# CAVEATS

游戏使用简单的双词解析器，可能无法识别复杂句子。请经常保存进度，因为游戏中有许多导致死亡或陷入困境的方式。

# HISTORY

**adventure** 由 Will Crowther 于 **1976** 年根据他在肯塔基州猛犸洞穴探洞的经历创作。Don Woods 在 **1977** 年对其加以扩展，加入了奇幻元素。它被公认为第一款文字冒险游戏，影响了包括 Zork 在内的整个冒险游戏类型及无数后来者。

# INSTALL

```dnf: sudo dnf install bsd-games```

```pacman: sudo pacman -S bsd-games```

```apk: sudo apk add bsd-games```

```zypper: sudo zypper install bsd-games```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[frotz](/man/frotz)(1), [nethack](/man/nethack)(6)
