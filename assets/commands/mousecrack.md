# TAGLINE

基于深度学习的拟人鼠标移动

# TLDR

**安装**全局 CLI

```npm i -g mousecrack```

将指针**移动**到屏幕坐标

```mousecrack move [x] [y]```

从一个位置到另一位置**生成**步进点序列

```mousecrack steps [x1] [y1] [x2] [y2]```

# SYNOPSIS

**mousecrack** **move** _x_ _y_

**mousecrack** **steps** _x1_ _y1_ _x2_ _y2_

# DESCRIPTION

**mousecrack** 使用混合密度网络合成自然多变、类似人类的鼠标轨迹。该网络作为一个多元时间序列预测器，在位置增量和时间间隔上进行训练。它既可以作为 Node.js SDK（**move**、**steps**）使用，也提供一个面向智能体和自动化场景的小型 CLI。

该项目尚属实验性（v0.x）并被标记为教育用途。输出质量参差不齐，并不能保证绕过机器人检测系统。

可选的智能体技能/插件发布在同一仓库中，支持 Claude Code 和 Codex。

# COMMANDS

**move** _x_ _y_

> 沿生成的路径将系统指针驱动到绝对坐标 (_x_, _y_)。

**steps** _x1_ _y1_ _x2_ _y2_

> 打印从 (_x1_, _y1_) 到 (_x2_, _y2_) 的中间点序列（带时间戳），不一定会实际驱动指针（面向 SDK）。

# CAVEATS

实验性软件。视操作系统而定，GUI 自动化可能需要辅助功能/输入权限。对第三方服务的滥用可能违反其服务条款。

# SEE ALSO

[xdotool](/man/xdotool)(1), [ydotool](/man/ydotool)(1), [cliclick](/man/cliclick)(1)

# RESOURCES

```[Source code](https://github.com/puffinsoft/mousecrack)```

<!-- verified: 2026-07-30 -->
