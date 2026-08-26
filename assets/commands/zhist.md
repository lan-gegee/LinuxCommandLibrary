# TAGLINE

带目录和退出状态上下文的 Zsh 历史记录存储

# TLDR

**将 zhist 挂接进 zsh**（添加到 `.zshrc`）

```eval "$(zhist init)"```

**一次性导入**现有的 zsh 历史文件

```zhist import ~/.zsh_history```

**列出**存储的命令供 fzf 选择器使用（最新在前，已去重）

```zhist list```

**只列出**在当前目录记录的命令

```zhist list -dir "$PWD"```

**打印**某个条目的完整命令文本

```zhist get -id [id]```

**删除**单个存储条目

```zhist delete -id [id]```

**删除所有**具有相同命令文本的条目

```zhist delete -id [id] -all```

从标准输入**记录**一条命令，附带目录和退出状态

```print -r -- "[command]" | zhist add -dir "$PWD" -exit 0```

# SYNOPSIS

**zhist** **init**

**zhist** **add** **-dir** _dir_ **-exit** _n_ [**-ts** _unix_]

**zhist** **list** [**-dir** _dir_]

**zhist** **get** **-id** _id_

**zhist** **delete** **-id** _id_ [**-all**]

**zhist** **import** _file_

# DESCRIPTION

**zhist** 是一个仅支持 zsh 的 Shell 历史工具，用 Go 编写。它取代 zsh 历史文件作为持久化存储，并为每条命令记录其工作目录和退出状态。原生 zsh 历史只保存命令和时间戳；zhist 额外保存这些上下文，使选择器能够高亮失败的命令，并在全局历史与当前目录之间切换。

交互式界面是 **fzf**，而非自定义 TUI。`eval "$(zhist init)"` 会输出调用 **zhist** 二进制程序的 zsh 钩子和按键绑定：一对 **preexec**/**precmd** 钩子通过 **zhist add** 追加每条命令，而 **ctrl-r**（以及空行上的裸上/下方向键）会在 fzf 中打开 **zhist list**。失败的命令以红色渲染。**ctrl-g** 可在全局历史与目录范围历史之间切换。

条目以 JSON 行的形式追加到 **~/.local/share/zhist/history.jsonl**（权限 **0600**），或追加到 **ZHIST_FILE** 指定的路径。导入的 zsh **EXTENDED_HISTORY** 行没有目录或退出状态信息；它们的目录显示为空，且永远不会渲染为红色。

# PARAMETERS

**init**
> 打印 zsh 集成脚本（钩子、fzf 选择器和按键绑定）。用于 `eval "$(zhist init)"`。

**add** **-dir** _dir_ **-exit** _n_ [**-ts** _unix_]
> 追加一个条目。命令文本从标准输入读取。**-ts** 默认为当前 Unix 时间。

**list** [**-dir** _dir_]
> 为 fzf 打印条目：最新在前，每行一条唯一命令，以制表符分隔 id / 相对时间 / 命令。**-dir** 只保留在该目录下记录的条目。

**get** **-id** _id_
> 打印某条目的完整命令（包括内嵌换行符）。

**delete** **-id** _id_ [**-all**]
> 删除具有该 id 的条目。**-all** 还会删除所有其他具有相同命令文本的条目。

**import** _file_
> 导入 zsh **EXTENDED_HISTORY** 文件（`: timestamp:elapsed;command` 格式的行）。输出 `imported N entries`。

# KEY BINDINGS

这些绑定由 **zhist init** 安装：

**ctrl-r**
> 打开历史选择器。

**up** / **down**
> 当输入行不为空时逐步浏览原生行历史。

**ctrl-g**
> 在全局历史与当前目录历史之间切换。

**ctrl-d**
> 删除选中的条目。

**ctrl-x**
> 删除所有具有相同命令的条目。

**tab**
> 接受并将命令留在输入行上。

**ctrl-/**
> 切换命令预览窗格。可见性状态保存在 **${XDG_STATE_HOME:-$HOME/.local/state}/zhist/preview-hidden** 中。

# CONFIGURATION

添加到 **~/.zshrc** 中任何绑定 **ctrl-r** 或方向键的插件之后（后绑定的生效）：

```
eval "$(zhist init)"
```

通过 **HIST_EXCLUDE** 数组按首词跳过记录。匹配仅在首词上精确且区分大小写（`ls` 会跳过 `ls -la`，但不会跳过 `lsd`）。以空格开头的命令也会被跳过，与 **HIST_IGNORE_SPACE** 一致。

```
HIST_EXCLUDE=(cd ls clear pwd exit)
```

**ZHIST_FILE**
> 覆盖 JSONL 存储路径（默认 **~/.local/share/zhist/history.jsonl**）。

由于持久化由 zhist 负责，请将原生 zsh 历史保持在仅内存模式：

```
unset HISTFILE
HISTSIZE=100000
SAVEHIST=0
```

不要设置 **SHARE_HISTORY**、**INC_APPEND_HISTORY** 或 **EXTENDED_HISTORY**；它们只影响 zhist 所取代的历史文件。

# CAVEATS

仅支持 zsh；没有 bash 或 fish 集成。选择器需要 **fzf** 0.45 或更新版本。`eval "$(zhist init)"` 必须在 atuin、zsh-history-substring-search 或其他绑定相同按键的 widget 之后运行。通过 **go install** 从源码构建需要模块声明的 Go 版本。导入的历史没有目录或退出状态。记录钩子会将自身置于 **precmd_functions** 最前面并透传 **$?**，以便后续的提示符钩子仍能看到真实的退出状态。

# HISTORY

**zhist** 由 **overflowy** 于 **2026 年 8 月**创建。它使用 Go 编写，以 MIT 许可证发布。存储格式为 JSON Lines；搜索界面委托给 fzf。

# SEE ALSO

[atuin](/man/atuin)(1), [mcfly](/man/mcfly)(1), [hishtory](/man/hishtory)(1), [hstr](/man/hstr)(1), [fzf](/man/fzf)(1), [history](/man/history)(1), [zsh](/man/zsh)(1)

# RESOURCES

```[Source code](https://github.com/overflowy/zhist)```

<!-- verified: 2026-08-12 -->
