# TAGLINE

为任意文本流添加交互式过滤

# TLDR

**对 stdin 做交互式过滤**

```[command] | percol```

**从 Shell 历史中挑选一行**

```history | percol```

**交互式搜索文件**

```find . | percol```

**启动时预置查询词**

```percol --query [pattern] [file]```

**在底部显示提示符**

```percol --prompt-bottom --result-bottom-up```

**交互式检出 git 分支**

```git checkout $(git branch | percol)```

**从 ps 输出中挑选进程并终止**

```ps aux | percol | awk '{print $2}' | xargs kill```

# SYNOPSIS

**percol** [_options_] [_file_]

# PARAMETERS

**--tty** _TTY_
> 要使用的终端设备文件（默认 `/dev/tty`）。

**--rcfile** _FILE_
> percol 初始化/配置文件的路径（默认 `~/.percol.d/rc.py`）。

**--output-encoding** _ENC_, **--input-encoding** _ENC_
> 强制指定输出/输入的字符编码。

**--query** _STRING_
> 初始查询字符串。

**--eager**
> 立即显示所有候选（不进行增量搜索）。

**--reverse**
> 反转输入行的顺序。

**--auto-match**
> 只有一个匹配项时自动选中。

**--auto-fail**
> 若没有任何行匹配查询，则以非零状态退出。

**--match-method** _METHOD_
> 匹配方法：`string`（默认）、`regex` 或 `migemo`（日语罗马字）。

**--case-sensitive** / **--caseless-match-regex-if-lowercase**
> 控制查询是否区分大小写。

**--prompt** _STRING_
> 自定义提示符格式（支持 Python 风格的格式化）。

**--prompt-top** / **--prompt-bottom**
> 在屏幕顶部（默认）或底部显示提示符。

**--result-top-down** / **--result-bottom-up**
> 控制结果列表在屏幕上的排列方向。

**--query-multiline**
> 允许查询输入跨越多行。

**-h**, **--help**
> 显示帮助。

# KEYBINDINGS

- `Ctrl-n` / `Ctrl-p` —— 向下 / 向上移动候选列表
- `Ctrl-i`（Tab）—— 切换选中状态（多选）
- `Ctrl-m`（回车）—— 结束并打印选中的行
- `Ctrl-g` —— 中止且不打印
- `Ctrl-a` / `Ctrl-e` —— 移到查询行行首 / 行尾
- `Ctrl-h` / `Ctrl-?` —— 向前 / 向后删除字符
- `Ctrl-u` / `Ctrl-k` —— 剪切至行首 / 行尾
- `Ctrl-y` —— 粘贴被剪切的文本

# DESCRIPTION

**percol** 是一款交互式的 grep 加选择工具，灵感来自 Emacs 的 `anything`/`helm`。它从 stdin 或文件读取候选行，在 curses 界面中展示，并随输入逐步缩小范围。按下回车会把选中的行打印到 stdout，因此可以直接嵌入 Shell 管道中使用。

配置（提示符、颜色、键位映射、匹配方法）以 Python 形式保存在 `~/.percol.d/rc.py` 中——percol 本身就用 Python 编写，所以 rc 文件可以完全访问 percol 的 API。

# CAVEATS

使用 Python 编写，面对超大输入（数十万行）时明显慢于 `fzf` 或 `peco`。上游开发时断时续；GitHub 上有若干分支版本。

# HISTORY

**percol** 由 **mooz** 创建，使用 **Python** 编写。其界面受 Emacs 的 `anything.el` 启发。它比 `fzf` 和 `peco` 出现得更早，并推广了"交互式过滤管道"这一模式。

# INSTALL

```brew: brew install percol```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1), [peco](/man/peco)(1), [sk](/man/sk)(1), [grep](/man/grep)(1), [rofi](/man/rofi)(1)
