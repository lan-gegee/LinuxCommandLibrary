# TAGLINE

Vim 交互式教程

# TLDR

**启动 vim 教程**

```vimtutor```

**以指定语言启动**

```vimtutor [de]```

**启动第 2 章**（仅 **en** 和 **fr** 可用）

```vimtutor -c 2```

**在 Vim 的 GUI 版本中启动教程**

```vimtutor -g```

**列出所有支持的语言**

```vimtutor --list```

# SYNOPSIS

**vimtutor** [_-g_] [_-c chapter_] [_language_]

# PARAMETERS

_LANGUAGE_
> ISO-639 语言代码（例如 **en**、**de**、**fr**、**ja**）。

**-l**, **--language** _CODE_
> 显式选择教程语言。也接受紧连形式 **-l**_code_ / **--language**_code_。

**-c**, **--chapter** _N_
> 加载第 _N_ 章（1 或 2）。第 2 章仅随 **en** 和 **fr** 提供。

**-g**, **--gui**
> 启动 GUI 版本的 Vim（**gvim**）而不是终端版本。

**--list**
> 列出可用的语言代码并退出。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**vimtutor** 通过动手练习教授 vim 基础。它会创建教程文件的副本并在 vim 中打开，供你练习。

整个教程大约 30 分钟即可学完核心操作。每一课都配有可立即上手的练习来介绍命令。

主题包括导航、编辑、删除、撤销、复制/粘贴、搜索以及文件操作。这些是高效使用 vim 的基础。

使用副本意味着操作失误不会影响原文件。你可以随时用全新副本重新开始。

可用语言包括英语、德语、法语、西班牙语、中文等许多其他语言。教程会根据系统区域设置自适应。

完成 vimtutor 后即可掌握基本编辑所需的知识。高级功能还需要进一步学习。

# LESSONS

**Lesson 1**
> 光标移动、删除、插入、ESC。

**Lesson 2**
> 删除、操作符与动作、撤销。

**Lesson 3**
> 粘贴、替换、修改操作符。

**Lesson 4**
> 定位、搜索、匹配、替换。

**Lesson 5**
> 外部命令、文件操作。

**Lesson 6**
> 打开、追加、替换、复制、设置选项。

**Lesson 7**
> 帮助、vimrc、补全。

# CAVEATS

仅涵盖基础知识。要熟练掌握 vim 需要大量练习。部分课程假设使用美式键盘布局。

# HISTORY

**vimtutor** 自早期版本起就随 **vim** 一同发布，由 **Bram Moolenaar**（vim 作者）创建。它基于 Michael C. Pierce 和 Robert K. Ware 编写的原始 vi 教程。

# INSTALL

```apk: sudo apk add vim-tutor```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1), [vi](/man/vi)(1), [nvim](/man/nvim)(1), [vimdiff](/man/vimdiff)(1)
