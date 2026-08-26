# TAGLINE

带行内批注的 diff 审查 TUI

# TLDR

**审查当前仓库中未提交的更改**

```revdiff```

**审查相对于特定分支的更改**

```revdiff [main]```

仅**审查已暂存的**更改

```revdiff --staged```

**审查最近一次提交**

```revdiff HEAD~1```

**浏览项目中所有** git 跟踪的文件

```revdiff --all-files```

**审查两个引用之间**的更改

```revdiff [main] [feature]```

仅**包含**匹配路径前缀的文件

```revdiff --include [src/api/]```

**审查从 stdin 管道传入的内容**

```echo "[text]" | revdiff --stdin```

# SYNOPSIS

**revdiff** [_options_] [_base_] [_against_]

# PARAMETERS

**--staged**
> 只显示已暂存的更改

**-A, --all-files**
> 浏览所有 git 跟踪的文件，而不只是已更改的文件

**--stdin**
> 将 stdin 内容作为临时缓冲区进行审查

**--stdin-name** _name_
> stdin 内容使用的合成文件名（默认：scratch-buffer）

**-I, --include** _prefix_
> 只包含匹配路径前缀的文件

**-X, --exclude** _prefix_
> 排除匹配路径前缀的文件

**-F, --only** _path_
> 按路径只显示特定文件

**-o, --output** _file_
> 将批注写入文件而不是 stdout

**--tree-width** _n_
> 文件树面板宽度，取值 1-10（默认：2）

**--tab-width** _n_
> 每个制表符对应的空格数（默认：4）

**--wrap**
> 在 diff 视图中启用自动换行

**--collapsed**
> 启动时折叠 diff

**--line-numbers**
> 在边栏中显示行号

**--blame**
> 启动时显示 blame 边栏

**--word-diff**
> 高亮行内的单词级变更

**--cross-file-hunks**
> 允许跨文件边界导航

**--no-colors**
> 禁用所有颜色和语法高亮

**--no-status-bar**
> 隐藏状态栏

**--no-confirm-discard**
> 丢弃批注时跳过确认

**--chroma-style** _theme_
> 语法高亮主题（默认：catppuccin-macchiato）

**--theme** _name_
> 从配置目录加载颜色主题

**--config** _path_
> 配置文件路径（默认：~/.config/revdiff/config）

**--keys** _path_
> 键位绑定文件路径

**-V, --version**
> 显示版本信息

# DESCRIPTION

**revdiff** 是一个用于审查 diff、文件和文档并添加行内批注的终端用户界面。它提供双面板布局，左侧为文件树，右侧为彩色 diff 视口，支持导航、批注和语法高亮。

批注可以放在 diff 中的任何一行——新增行、删除行或上下文行——也可以添加文件级备注。退出时，批注以结构化文本输出到 stdout（或使用 **-o** 输出到文件），便于将结果通过管道传给 AI 智能体、脚本或其他工具。

revdiff 会自动检测版本控制系统，同时支持 **Git** 和 **Mercurial** 仓库。它在两种后端上都支持 diff、blame 和未跟踪文件列表。当 diff 恰好只包含一个文件时，树状面板会自动隐藏。

# CONFIGURATION

配置保存在 **~/.config/revdiff/config** 中，使用 INI 格式。键位绑定在 **~/.config/revdiff/keybindings** 中配置。环境变量和 CLI 标志会覆盖配置值。审查历史会自动保存到 **~/.config/revdiff/history/**。

# CAVEATS

除非使用 **--only** 或 **--stdin** 模式，否则需要 **git** 或 **hg** 来生成 diff。用于 AI 智能体集成的终端覆盖功能依赖终端复用器支持（tmux、Zellij、kitty、wezterm）。用 **Q** 丢弃批注不会保存审查历史。

# HISTORY

revdiff 由 **Umputun** 创建，使用 **Go** 编写。它是一个 TUI 代码审查工具，设计为与 Claude Code、Codex 和 OpenCode 等 AI 编程智能体集成，输出可供智能体程序化处理的结构化批注。

# INSTALL

```aur: yay -S revdiff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [git](/man/git)(1), [tig](/man/tig)(1), [delta](/man/delta)(1)
