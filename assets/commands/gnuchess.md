# TAGLINE

GNU Chess 国际象棋引擎

# TLDR

**开始交互式国际象棋对局**

```gnuchess```

以**双人模式**对弈（用户对用户）

```gnuchess -u```

以**简单模式**对弈（不进行后台思考）

```gnuchess -e```

**从 PGN 文件加载对局**

```gnuchess -l [game.pgn]```

**设置搜索深度级别**

```gnuchess -S [5]```

**作为 UCI 引擎运行**

```gnuchess --uci```

**作为 XBoard 引擎运行**

```gnuchess --xboard```

# SYNOPSIS

**gnuchess** [_options_]

# PARAMETERS

**-h**, **--help**
> 显示用法帮助。

**-v**, **--version**
> 显示版本信息。

**-u**
> 双人模式（用户对用户）。

**-e**
> 简单模式。引擎在对手回合期间不思考。

**-l** _PGNFILE_, **--load** _PGNFILE_
> 从 PGN 文件加载对局。

**-S** _LEVEL_, **--setlevel** _LEVEL_
> 设置搜索深度级别（1-10）。

**--xboard**, **-x**
> XBoard/WinBoard 引擎协议模式。

**--uci**
> UCI 引擎协议模式。

**--post**, **-p**
> 显示引擎的思考过程输出。

**--manual**, **-m**
> 手动模式。引擎在被指示之前不会行棋。

**-M** _SIZE_, **--memory** _SIZE_
> 设置哈希表内存大小（MB）。

# PREVIEW

```
 r n b q k b n r
 p p p p p p p p
 . . . . . . . .
 . . . . . . . .
 P P P P P P P P
 R N B Q K B N R
```

# DESCRIPTION

**gnuchess** 是一个自由的国际象棋程序，既可以作为独立的交互式对弈游戏，也可以作为 **XBoard** 或 **GNOME Chess** 等图形棋类前端的引擎后端。它同时支持 **XBoard** 和 **UCI** 通信协议。

在交互模式下，以代数记法输入着法（如 e2e4、Nf3）。输入 **help** 可查看命令列表。该引擎内置开局库，使用带迭代加深的 alpha-beta 搜索。

# CAVEATS

默认开局库未必在所有系统上都已安装。棋力取决于搜索深度和可用于哈希表的内存大小。

# HISTORY

GNU Chess 由 **Stuart Cracraft** 于 **1984** 年首次编写，是 GNU 计划中最早的程序之一。几十年来由众多贡献者维护，至今仍是最著名的自由软件象棋引擎之一。

# INSTALL

```dnf: sudo dnf install gnuchess```

```pacman: sudo pacman -S gnuchess```

```apk: sudo apk add gnuchess```

```zypper: sudo zypper install gnuchess```

```nix: nix profile install nixpkgs#gnuchess```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nbcheckers](/man/nbcheckers)(1), [gnugo](/man/gnugo)(1)
