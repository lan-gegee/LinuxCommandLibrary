# TAGLINE

基于终端的间隔重复记忆卡片工具

# TLDR

启动**卡组选择器**界面

```flash```

显示 flash 的**系统信息**

```flash -i```

使用自定义**预览**程序替代 bat

```flash -p [cat]```

打印**版本**

```flash -v```

显示**帮助**

```flash -h```

# SYNOPSIS

**flash** [_-i_] [_-p previewer_] [_-h_] [_-v_]

# PARAMETERS

**-i**
> 显示关于记忆卡系统及卡组位置的信息

**-p** _previewer_
> 更改卡片预览程序（默认：bat，回退：cat）

**-h**
> 显示帮助信息

**-v**
> 显示版本信息

# DESCRIPTION

**Flash**（fla.sh）是一个基于终端的记忆卡片应用，实现了间隔重复和主动回忆的学习原则。它使用纯文本 CSV 文件作为记忆卡组，并以随机顺序呈现卡片进行学习。

卡片以冒号分隔的 CSV 格式存储：**category:question:answer:score**。分数字段用于管理卡片难度——分数越低的卡片出现得越频繁，而被评为 "Easy" 的卡片会获得更高的分数并较少出现。

该工具使用 **fzf** 对卡组进行模糊选择，还可选用 **bat** 来以语法高亮方式显示卡片。卡组存储在 **~/.local/share/flash/** 中，支持嵌套目录组织。

# CAVEATS

需要 **fzf** 作为卡组选择的必备依赖。在 macOS 上，必须通过 Homebrew 安装 GNU coreutils，以便使用随机化所需的 **shuf** 命令。该工具在首次运行时若数据目录不存在则会自动创建。

# HISTORY

Flash 由 **Bryan Jenks**（tallguyjenks）创建，作为图形化记忆卡片应用的轻量级终端替代品。它完全用 **Bash** 编写，灵感来自 Anki 等间隔重复系统，同时保持了 Unix 哲学的简洁性。

# INSTALL

```apt: sudo apt install flash```

```brew: brew install flash```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1), [bat](/man/bat)(1), [cat](/man/cat)(1)

# RESOURCES

```[Source code](https://github.com/tallguyjenks/fla.sh)```

<!-- verified: 2026-07-15 -->
