# TAGLINE

ASCII/文本艺术时钟、计时器与模式时间管理器

# TLDR

**启动** arttime（艺术 + 时钟）

```arttime```

**计时器模式** / 模式计时

```arttime -t [25m]```

**交互式选择**艺术样式

```arttime```

# SYNOPSIS

**arttime** [*options*]

# DESCRIPTION

**arttime** 将循环播放的文本/ASCII 艺术与终端中的时钟、计时器和基于模式的时间管理融为一体。它的目标是带来愉悦的专注时段，而非做一款极简秒表。可通过上游安装脚本或代码仓库中记录的软件包安装。

# PARAMETERS

**-t** *duration*

> 计时器相关模式（模式语法见 **arttime -h**）。

运行期间，交互式按键可切换艺术样式、切换视图并控制计时器。完整选项列表见 **arttime --help**。

# CAVEATS

需要支持 UTF-8 且尺寸足以容纳艺术的终端。它不是调度守护进程——进程必须保持运行。

# INSTALL

```brew: brew install arttime```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[pomodoro](/man/pomodoro)(1), [tty-clock](/man/tty-clock)(1), [peaclock](/man/peaclock)(1)

# RESOURCES

```[Source code](https://github.com/poetaman/arttime)```

<!-- verified: 2026-07-19 -->
