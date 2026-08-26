# TAGLINE

基于终端的电子表格计算器

# TLDR

**启动 sc** 并新建电子表格

```sc```

**打开现有电子表格文件**

```sc [file.sc]```

**启动 sc-im**（改进版）

```sc-im```

在 sc-im 中**打开 CSV 文件**

```sc-im [file.csv]```

在 sc-im 中**打开 Excel 文件**

```sc-im [file.xlsx]```

# SYNOPSIS

**sc** [_-rxnCqS_] [_file_]

# PARAMETERS

**-r**
> 只读模式

**-x**
> 禁用 X11 功能

**-n**
> 不提示输入命令

**-C**
> 启动时禁用颜色

**-q**
> 安静模式

# KEYBOARD COMMANDS

**h, j, k, l**
> 向左、下、上、右移动（vi 风格）

**g** _cell_
> 跳转到指定单元格（例如 gA1、gD3）

**e**
> 进入当前单元格的编辑模式

**=**
> 输入公式

**x**
> 删除当前单元格内容

**dd**
> 删除整行

**yy**
> 复制（yank）行

**p**
> 粘贴已复制的内容

**ZZ**
> 保存并退出

**ZQ**
> 不保存直接退出

# DESCRIPTION

**sc** 是一款基于终端的电子表格计算器，采用 vi 风格的按键绑定。它完全运行在文本模式下，支持公式、宏和外部函数。电子表格以人类可读的命令脚本形式保存。

现代后继者 **sc-im**（Spreadsheet Calculator Improvised）为 sc 扩展了撤销/重做、65,536 行和 702 列的支持、CSV/XLSX 导入导出以及 Lua 脚本功能。两者共享相似的类 vi 导航和编辑命令。

电子表格文件可以导出为纯文本、LaTeX 或 CSV 格式，供其他应用程序使用。

# CAVEATS

sc 使用独特的文件格式（.sc），将电子表格存储为命令序列。原版 sc 的开发于 2002 年停滞；sc-im 是面向现代系统、仍在积极维护的分叉版本。

# HISTORY

sc 的开发始于 **1981 年**，由 James Gosling 和 Mark Weiser 编写，是最古老的开源电子表格应用之一。Chuck Martin 后来对其进行了修改。**2015 年**，开发以 **sc-im** 之名恢复，并带来了大量增强。

# INSTALL

```apt: sudo apt install sc```

```dnf: sudo dnf install sc```

```apk: sudo apk add sc```

```nix: nix profile install nixpkgs#sc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sc-im](/man/sc-im)(1), [gnumeric](/man/gnumeric)(1), [bc](/man/bc)(1), [vi](/man/vi)(1)
