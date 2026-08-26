# TAGLINE

带 Vim 按键绑定的终端电子表格

# TLDR

**打开电子表格**

```scim [file.sc]```

**打开 CSV 文件**

```scim --txtdelim="," [file.csv]```

**启动时加载文件**

```scim [file.xlsx]```

**只读模式**

```scim -R [file.sc]```

# SYNOPSIS

**scim** [_--txtdelim delim_] [_-R_] [_options_] [_file_]

# PARAMETERS

**--txtdelim** _DELIM_
> 文本分隔符。

**-R**
> 只读模式。

**--nocurses**
> 不使用 ncurses 模式。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**scim**（sc-im）是一款基于终端的电子表格计算器，采用类 Vim 的按键绑定和模态化界面。它是图形化电子表格应用的轻量替代品，完全运行在 ncurses 终端界面中，实现快速、纯键盘驱动的操作。

该电子表格支持公式、数学函数、单元格引用和范围，与传统电子表格软件类似。文件可以从 CSV、TSV 和 Excel 格式导入导出，实现与其他工具的互操作。原生 **.sc** 格式会保留所有公式和格式。

导航和编辑遵循 Vim 惯例：**h/j/k/l** 移动、**i** 进入插入模式、**=** 输入公式、**:** 执行保存和退出等命令。这种模态方式让高效的纯键盘工作流成为可能，无需碰鼠标。

# KEY BINDINGS

- **h/j/k/l** - 导航
- **i** - 插入模式
- **=** - 输入公式
- **:w** - 保存
- **:q** - 退出

# CAVEATS

学习曲线陡峭。Excel 兼容性有限。仅限控制台。

# HISTORY

**sc-im** 是基于 **sc** 的电子表格计算器，具有类 Vim 界面和现代化改进。

# INSTALL

```apt: sudo apt install scim```

```dnf: sudo dnf install scim```

```pacman: sudo pacman -S scim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sc](/man/sc)(1), [gnumeric](/man/gnumeric)(1), [calc](/man/calc)(1)
