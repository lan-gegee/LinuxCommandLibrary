# TAGLINE

通用命令行模糊查找器

# TLDR

**交互式文件查找器**

```find . -type f | fzf```

**带预览的选择**

```fzf --preview 'cat {}'```

**多选**

```fzf -m```

**过滤命令历史**

```history | fzf```

**模糊查找并**编辑

```vim $(fzf)```

**精确匹配**模式

```fzf -e```

**非交互式过滤**（模糊 grep）

```fzf -f "[query]"```

**唯一匹配时自动选中**

```fzf --select-1 -q "[query]"```

# SYNOPSIS

**fzf** [_options_]

# PARAMETERS

**-m**, **--multi**
> 启用多选。

**--preview** _CMD_
> 预览命令。

**-q** _QUERY_, **--query** _QUERY_
> 初始搜索查询词。

**--height** _HEIGHT_
> 显示高度（行数或百分比）。

**--reverse**
> 自顶向下的布局。

**--border**
> 绘制边框。

**-e**, **--exact**
> 启用精确匹配模式而非模糊匹配。

**-f** _QUERY_, **--filter** _QUERY_
> 非交互式过滤模式（模糊 grep）。

**-1**, **--select-1**
> 仅有一个匹配时自动选中。

**-0**, **--exit-0**
> 无匹配时立即退出。

**--ansi**
> 启用 ANSI 颜色代码处理。

**-d** _DELIM_, **--delimiter** _DELIM_
> 供 --nth 使用的字段分隔正则。

**-n** _N_, **--nth** _N_
> 将搜索范围限定到指定字段。

**--layout** _LAYOUT_
> 显示布局：default、reverse、reverse-list。

**--info** _STYLE_
> 信息栏样式：default、right、hidden、inline。

**--header** _STR_
> 显示固定的页眉字符串。

**--bind** _KEYS_
> 自定义按键绑定。

**--tac**
> 反转输入顺序。

**--no-sort**
> 保持输入的原有顺序。

**--cycle**
> 启用循环滚动。

**--print-query**
> 将查询词作为输出的第一行打印。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fzf** 是一个通用的模糊查找器，可对任何列表进行交互式过滤。它从 stdin 接收输入并输出选中的条目，从而构建强大的 shell 工作流。

该工具在键入时即时反馈，模糊匹配可以容忍拼写错误，预览窗口则提供上下文。Shell 集成还为历史、文件和目录添加了快捷键。

fzf 为文件、进程、git 分支等带来交互式选择，彻底改变了命令行工作流。

# SHELL INTEGRATION

**CTRL-T**: 将选中的文件路径粘贴到命令行
**CTRL-R**: 搜索命令历史
**ALT-C**: cd 进入选中的目录

# ENVIRONMENT VARIABLES

**FZF_DEFAULT_COMMAND**
> 输入为终端时要运行的命令（替代默认的 find）。

**FZF_DEFAULT_OPTS**
> 应用于每次 fzf 调用的默认选项。

# CAVEATS

需要支持完整功能的终端。Shell 集成需要 source fzf 的设置脚本。大量输入可能较慢。

# HISTORY

fzf 由 **Junegunn Choi** 于 2013 年创建。它以 Go 编写以追求性能，成为命令行生产力的重要工具，催生了遍布 shell、编辑器和各种工具的集成。

# INSTALL

```apt: sudo apt install fzf```

```dnf: sudo dnf install fzf```

```pacman: sudo pacman -S fzf```

```apk: sudo apk add fzf```

```zypper: sudo zypper install fzf```

```brew: brew install fzf```

```nix: nix profile install nixpkgs#fzf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sk](/man/sk)(1), [peco](/man/peco)(1), [fd](/man/fd)(1)
