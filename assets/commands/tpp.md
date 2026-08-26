# TAGLINE

基于终端的文本演示

# TLDR

**播放演示文稿**

```tpp [presentation.tpp]```

将演示文稿**导出**为 LaTeX

```tpp -l [output.tex] [presentation.tpp]```

# SYNOPSIS

**tpp** [**-l** _output_] [_file.tpp_]

# PARAMETERS

**-l** _output_
> 将演示文稿转换为 LaTeX 格式并写入输出文件

**--help**
> 显示帮助信息

**--version**
> 显示版本号

# DESCRIPTION

**tpp**（Text Presentation Program）是一个基于 ncurses 的工具，用于在终端中创建和展示演示文稿。演示文稿以简单的标记格式编写，可在任何支持 ncurses 的终端上运行。

演示文稿由以 **--newpage** 分隔的页面组成。第一个页面标记之前的文本作为摘要。格式化命令包括用于标题的 **--heading**、居中文本的 **--center**，以及粗体文本的 **--boldon**/**--boldoff**。

特殊功能包括使用 FIGlet 的 **--huge** 大字文本、通过 **--beginshelloutput**/**--endshelloutput** 展示 shell 命令输出，以及用于演示的模拟打字效果。颜色可通过 **--color** 加颜色名称来设置。

该工具支持动画文字效果和实时命令执行，适合直接在终端中进行技术演讲和演示。

# NAVIGATION

**Space**, **Right**, **Down**
> 下一页

**b**, **Left**, **Up**
> 上一页

**j/J**
> 跳转到指定页

**s/S**
> 跳转到开头

**e/E**
> 跳转到结尾

**l/L**
> 重新加载当前文件

**c/C**
> 打开命令行

**q/Q**
> 退出

**?/h**
> 显示帮助

# PRESENTATION FORMAT

```
--author Your Name
--title My Presentation
--date today

--newpage
--heading Introduction
--center Welcome to my talk
This is regular text.

--newpage
--heading Code Example
--beginshelloutput
$ ls -la
--endshelloutput
```

# CAVEATS

tpp 需要支持 ncurses 的终端。**--huge** 功能需要安装 FIGlet。包含大量效果的复杂演示文稿在简陋终端上可能无法正确显示。

# HISTORY

**tpp** 由 **Andreas Krennmair** 和 **Nico Golde** 编写。它的设计目标是直接在终端中进行演示，吸引了偏好文本工具、希望避开图形化演示软件的用户。该工具因技术演讲和演示而在 Linux 社区中广受欢迎。

# INSTALL

```aur: yay -S tpp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(6), [cowsay](/man/cowsay)(1), [slides](/man/slides)(1), [mdp](/man/mdp)(1)
