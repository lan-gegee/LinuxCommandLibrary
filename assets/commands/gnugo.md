# TAGLINE

与计算机对弈围棋

# TLDR

**以 ASCII 显示开始对局**

```gnugo --mode gtp```

**用指定的棋盘尺寸对弈**

```gnugo --boardsize [9]```

**设置 AI 难度等级**

```gnugo --level [10]```

**在 ASCII 模式下交互对弈**

```gnugo --mode ascii```

**回放 SGF 棋谱文件**

```gnugo -l [game.sgf] --mode ascii```

**为已结束的对局计分**

```gnugo -l [game.sgf] --score finish```

# SYNOPSIS

**gnugo** [_options_]

# PARAMETERS

**--mode** _MODE_
> 界面模式：ascii、gtp 或 gmp。

**--boardsize** _N_
> 棋盘尺寸（默认：19）。常见尺寸：9、13、19。

**--level** _N_
> AI 思考等级（0-10，默认：10）。

**--handicap** _N_
> 让子数量。

**--color** _COLOR_
> 选择颜色：black 或 white。

**--komi** _N_
> 设置贴目数（补偿点数，默认：5.5）。

**-l**, **--infile** _FILE_
> 加载 SGF 棋谱文件用于分析或回放。

**-L**, **--until** _MOVE_
> 在指定着法落下之前停止加载 SGF 文件。

**-o**, **--outfile** _FILE_
> 将对局保存为 SGF 文件。

**--score** _MODE_
> 估算或确定已加载对局的得分（_estimate_、_finish_、_aftermath_）。

**--printboard**
> 每步之后打印棋盘。

**--quiet**
> 抑制提示性消息。

# PREVIEW

```
    A B C D E F G
 7  . . . . . . .
 6  . . X . . . .
 5  . X O X . . .
 4  . . X O . . .
 3  . . . . . . .
```

# DESCRIPTION

**gnugo** 是一个与用户对弈围棋的程序。它支持多种棋盘尺寸、可调节的 AI 棋力，并能通过 Go Text Protocol（GTP）通信以便与图形前端集成。

在 ASCII 模式下，以坐标形式输入着法（如 "C4"）。AI 使用模式匹配和向前推演来分析盘面。输入 **pass** 虚着一手，输入 **quit** 退出。

# CAVEATS

ASCII 模式不需要特殊的终端支持。其 AI 具有中等棋力，但无法与 KataGo 等现代围棋引擎抗衡。GTP 模式供图形前端使用。

# HISTORY

**GNU Go** 自 **1989** 年起由 **自由软件基金会（Free Software Foundation）** 开发。在神经网络引擎出现之前，它曾是最强的开源围棋程序之一。

# INSTALL

```apt: sudo apt install gnugo```

```dnf: sudo dnf install gnugo```

```pacman: sudo pacman -S gnugo```

```zypper: sudo zypper install gnugo```

```nix: nix profile install nixpkgs#gnugo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gomoku](/man/gomoku)(6), [gnuchess](/man/gnuchess)(6)
