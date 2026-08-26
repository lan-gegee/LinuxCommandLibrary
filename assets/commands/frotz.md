# TAGLINE

Z-machine 文字冒险游戏解释器

# TLDR

**运行 Z-machine 游戏**

```frotz [game.z5]```

**设置屏幕宽高**

```frotz -w [80] -h [24] [game.z5]```

以哑终端模式游玩

```dfrotz [game.z5]```

**启动时加载存档**

```frotz -L [savefile] [game.z5]```

**限制文件访问范围到一个目录**

```frotz -R [/path/to/directory] [game.z5]```

开启缩写展开并忽略错误进行游戏

```frotz -x -i [game.z5]```

# SYNOPSIS

**frotz** [_options_] _story-file_

# PREVIEW

```
West of House
You are in an open
field west of a house.

>
```

# DESCRIPTION

**frotz** 是 Infocom 风格文字冒险游戏（Z-machine 游戏）的解释器。它可以运行 Z3 到 Z8 各格式的文字冒险游戏，包括经典作品和现代 IF 作品。

该工具提供终端和图形界面来运行这些游戏，支持保存/恢复、记录文本（transcript）和输入录制。

# PARAMETERS

**-a**
> 监视属性设置。

**-A**
> 监视属性测试。

**-b** _color_
> 背景色。

**-c** _n_
> 滚动时保留的上下文行数。

**-d**
> 禁用彩色输出。

**-e**
> 启用音效。

**-f** _color_
> 前景色。

**-F**
> 即使配置中禁用也强制启用颜色模式。

**-h** _rows_
> 屏幕高度（行数）。

**-i**
> 忽略致命的 Z-machine 错误。

**-I** _n_
> 报告给游戏的解释器编号。

**-l** _n_
> 左边距（字符数）。

**-L** _file_
> 启动时加载存档文件。

**-m**
> 启用鼠标支持。

**-o**
> 监视对象移动。

**-O**
> 监视对象定位。

**-p**
> 仅输出纯 ASCII（不带重音字符）。

**-P**
> 修改盗版检测 opcode。

**-q**
> 安静模式（禁用音效）。

**-r** _n_
> 右边距（字符数）。

**-R** _directory_
> 将文件读写限制在指定目录内。

**-s** _n_
> 随机数种子值。

**-S** _n_
> 设置记录宽度（0 表示禁用换行拆分）。

**-t**
> 设置 Tandy 位。

**-u** _n_
> 撤销槽位数量。

**-v**
> 显示版本信息。

**-w** _columns_
> 屏幕宽度（列数）。

**-x**
> 将缩写 "g"、"x"、"z" 展开为 "again"、"examine"、"wait"。

**-Z** _n_
> 错误检查模式（0=不检查，1=首个错误，2=全部，3=出错即退出；默认 1）。

# CAVEATS

部分游戏需要特定的 Z-machine 版本。颜色支持取决于终端能力。存档格式在不同解释器之间未必通用。共有三个变体：**frotz**（curses）、**dfrotz**（哑终端）和 **sfrotz**（SDL 图形界面）。

# HISTORY

**Frotz** 由 **Stefan Jokisch** 于 **20 世纪 90 年代中期**编写，是一个可移植的 Z-machine 解释器。它成为运行 Infocom 游戏和现代文字冒险游戏最受欢迎的解释器之一。其名字来自 Zork 中的一个咒语。

# INSTALL

```dnf: sudo dnf install frotz```

```apk: sudo apk add frotz```

```brew: brew install frotz```

```nix: nix profile install nixpkgs#frotz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nethack](/man/nethack)(6)
