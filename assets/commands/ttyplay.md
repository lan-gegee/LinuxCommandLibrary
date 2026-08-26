# TAGLINE

回放 ttyrec 录制的终端会话

# TLDR

**播放录制的会话**

```ttyplay [recording.tty]```

**以两倍速播放**

```ttyplay -s [2] [recording.tty]```

**以半速播放**

```ttyplay -s [0.5] [recording.tty]```

**不按时间延迟播放**

```ttyplay -n [recording.tty]```

在录制进行的同时**窥看录像**（实时跟随）

```ttyplay -p [/path/to/recording.tty]```

# SYNOPSIS

**ttyplay** [_options_] _file_

# PARAMETERS

**-s** _speed_
> 按指定倍数调整播放速度（默认 1）。

**-n**
> 不等待模式；忽略时间信息。

**-p**
> 窥看模式；持续跟随不断增长的录像文件，让观看者可以实时查看仍在录制中的 ttyrec 会话。

# PLAYBACK CONTROLS

**+** 或 **f**：加倍播放速度。

**-** 或 **s**：减半播放速度。

**0**：暂停播放。

**1**：恢复正常速度。

**空格**或任意键：跳到下一个输入事件。

# DESCRIPTION

**ttyplay** 回放由 ttyrec 录制的终端会话。它会按照原始时序重现输出，展示录制时的命令、输出和用户交互。

播放器以微秒精度保留时间信息，适合用于演示、教程以及分享终端工作流。速度控制让你可以快速回顾或放慢检查复杂操作序列。

窥看模式可以实时查看正在进行的录制，功能类似于只读的终端共享系统。适合实时监控或演示终端会话。

# CAVEATS

终端尺寸应与原始录制一致才能正确显示。播放假定终端能力兼容。除非调整速度，否则原会话中很长的停顿也会原样保留。颜色取决于终端设置。

# HISTORY

**ttyplay** 与 ttyrec 一同开发，是 BSD script 命令的衍生版本，具有更高的计时精度。它曾在 NetHack 和 Roguelike 游戏社区流行，用于分享游戏过程，精确的时序为观看体验增色不少。

# INSTALL

```apt: sudo apt install ttyrec```

```brew: brew install ttyrec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ttyrec](/man/ttyrec)(1), [ttytime](/man/ttytime)(1), [script](/man/script)(1), [asciinema](/man/asciinema)(1)
