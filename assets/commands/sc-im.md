# TAGLINE

类 Vim 的终端电子表格计算器

# TLDR

**启动 sc-im** 并新建电子表格

```sc-im```

**打开现有文件**（CSV、TSV、XLSX 或 SC 格式）

```sc-im [path/to/file]```

打开 XLSX 文件中的**指定工作表**

```sc-im --sheet=[2] [file.xlsx]```

从 XLSX **导入公式**而非最终值

```sc-im --xlsx_readformulas [file.xlsx]```

不使用 ncurses 界面，**将结果保存到文件**

```sc-im --nocurses --output=[output.csv] [file.xlsx]```

**运行脚本并在加载后退出**

```sc-im --quit_afterload [script.sc]```

# SYNOPSIS

**sc-im** [_options_] [_file_]

# PARAMETERS

**--sheet=**_SHEET_
> 打开 XLSX 文件中的指定工作表（名称或编号，默认：1）。

**--version**
> 打印版本号和已启用的特性，然后退出。

**--nocurses**
> 不使用 ncurses 界面以交互方式运行。

**--output=**_FILE_
> 将结果保存到指定文件。

**--quit_afterload**
> 加载文件后退出；适合运行脚本。

**--quiet**
> 屏蔽信息、错误和调试消息。

**--autocalc**
> 启用自动重新计算。

**--numeric**
> 数字输入作为数值而非命令倍数。

**--half_page_scroll**
> 使用 Ctrl-f/Ctrl-b 时滚动半页而非整页。

**--newline_action=**_VAL_
> 输入后的光标移动（j 表示向下，l 表示向右）。

**--external_functions**
> 启用外部函数。

**--xlsx_readformulas**
> 从 XLSX 导入公式而不是最终的单元格值。

# DESCRIPTION

**sc-im**（Spreadsheet Calculator Improvised）是一款基于终端的电子表格应用，采用类似 Vim 的按键绑定。它支持最多 65,536 行和 702 列，足以在终端中直接处理大规模数据操作。

程序使用 ncurses 作为界面，支持导入导出 CSV、TSV 和 XLSX 文件。它具备复杂公式支持、宏录制、撤销/重做功能，以及用于绘图的 GNUPlot 集成。单元格支持 256 色着色，还可以应用加粗或下划线等格式。

导航遵循 Vim 惯例：**h**、**j**、**k**、**l** 在单元格间移动，**gg** 跳转到第一个单元格，**G** 到达最后一行，**w**/**b** 移动到下一个/上一个有内容的单元格。配置保存在 **~/.config/sc-im/scimrc** 中。

# CAVEATS

XLSX 导入可能无法保留所有 Excel 特性；复杂的公式或格式可能会丢失。大文件加载可能较慢。对于不熟悉模态编辑器的用户来说，类 Vim 界面有一定学习曲线。

# HISTORY

最初的 **sc**（Spreadsheet Calculator）由 **James Gosling** 和 **Mark Weiser** 于 **1981 年**在卡内基梅隆大学创建。开发在 2002 年前后陷入停滞。**2015 年**，**Andrés Martinelli** 将该项目分叉为 **sc-im**，在保持基于终端的类 Vim 界面的同时，加入了 XLSX 支持、256 色、撤销/重做和 Lua 脚本等现代特性。

# INSTALL

```apt: sudo apt install sc-im```

```dnf: sudo dnf install sc-im```

```apk: sudo apk add sc-im```

```zypper: sudo zypper install sc-im```

```brew: brew install sc-im```

```nix: nix profile install nixpkgs#sc-im```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sc](/man/sc)(1), [vim](/man/vim)(1), [gnuplot](/man/gnuplot)(1), [csvtool](/man/csvtool)(1)
