# TAGLINE

基于文本的科幻冒险游戏

# TLDR

**开始新的 Battlestar 游戏**

```battlestar```

**从文件恢复存档**

```battlestar -r [savefile]```

# SYNOPSIS

**battlestar** [_-r_] [_file_]

# PREVIEW

```
You are in the cockpit.
Strewn about are pieces
of broken instrumentation.

> look
```

# DESCRIPTION

**battlestar** 是 BSD games 合集中的文字冒险游戏。故事发生在一艘刚经历惨烈太空战的战斗之星飞船上，玩家必须探索残骸、寻找关键物品，并在穿越热带岛屿等不同地点的过程中在各种遭遇中存活下来。

游戏采用解析器式的输入系统，玩家输入自然语言命令与环境交互。导航使用罗盘方位（携带罗盘时）或相对方向（右、左、前方、后方）。

# PARAMETERS

**-r**
> 恢复之前保存的游戏。

_file_
> 要恢复的存档文件名。

# COMMANDS

- **take/drop** - 管理物品
- **wear/draw** - 装备物品
- **inven** - 显示物品栏
- **score** - 显示当前游戏状态
- **save** - 保存游戏
- **!** - 转义到 Shell
- **N/S/E/W** - 罗盘方位（需要罗盘）
- **R/L/A/B** - 右、左、前方、后方

# CAVEATS

纯文本界面。需要了解冒险游戏的惯例。解析器对措辞可能比较挑剔。属于 bsd-games 软件包，默认可能未安装。

# HISTORY

**battlestar** 由 **David Riggle** 于 **1979** 年编写，最初是一次 C 语言的编程实验。此后一直是 BSD games 发行版的一部分。

# INSTALL

```dnf: sudo dnf install bsd-games```

```pacman: sudo pacman -S bsd-games```

```apk: sudo apk add bsd-games```

```zypper: sudo zypper install bsd-games```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[adventure](/man/adventure)(6), [nethack-console](/man/nethack-console)(6)
