# TAGLINE

图形化 Git 仓库浏览器

# TLDR

**启动 gitk**

```gitk```

**显示所有分支**

```gitk --all```

**查看特定文件的历史**

```gitk [file.txt]```

**查看特定范围**

```gitk [v1.0..v2.0]```

**显示指定日期之后的记录**

```gitk --since="[2 weeks ago]"```

**加载时选中特定提交**

```gitk --select-commit=[HEAD]```

**追踪某个函数的历史**

```gitk -L:[function_name]:[file.c]```

# SYNOPSIS

**gitk** [_options_] [_revision-range_] [_--_] [_path_...]

# PARAMETERS

_REVISION-RANGE_
> 要显示的提交范围（例如 `v1.0..v2.0`）。

_PATH_...
> 只限于触及给定路径的提交。

**--all**
> 显示所有引用（分支、标签等），如同它们都在命令行上列出一样。

**--branches**[=_PATTERN_]
> 显示所有分支，可用 glob 模式加以限定。

**--tags**[=_PATTERN_]
> 显示所有标签，可用 glob 模式加以限定。

**--remotes**[=_PATTERN_]
> 显示所有远程跟踪分支，可用 glob 模式加以限定。

**--since** _DATE_
> 显示晚于给定日期的提交。

**--until** _DATE_
> 显示早于给定日期的提交。

**--date-order**
> 按日期而非拓扑顺序对提交排序。

**--merge**
> 在发生合并冲突后，显示双方分支上都修改了冲突文件的提交。

**--left-right**
> 用 `<` 或 `>` 标记提交，表明其来自对称差异的哪一侧。

**--full-history**
> 按路径过滤时不裁剪历史。

**--simplify-merges**
> 与 **--full-history** 配合使用，从结果中去掉不必要的合并。

**-L** _start_,_end_:_file_ / **-L**:_funcname_:_file_
> 追踪文件中某行范围或某函数的演变过程。

**--argscmd** _COMMAND_
> 每次 gitk 刷新修订范围时都会运行的命令；其输出列出要额外显示的修订。

**--select-commit** _REF_
> 加载图形后选中给定的提交（默认 `HEAD`）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gitk** 是 Git 的图形化仓库浏览器。它在 GUI 窗口中以可视化图形展示提交历史，呈现分支、合并及提交详情。

界面显示提交图、文件变更和 diff 内容。它支持搜索、过滤以及直观地探索仓库历史。

# CAVEATS

需要 Tcl/Tk。界面较为陈旧。可能未随系统默认安装。

# HISTORY

gitk 由 **Paul Mackerras** 编写，是最早的 **Git** 图形工具之一，自 Git 诞生初期就提供可视化的历史浏览功能。

# INSTALL

```dnf: sudo dnf install gitk```

```apk: sudo apk add git-gitk```

```zypper: sudo zypper install gitk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-gui](/man/git-gui)(1), [tig](/man/tig)(1), [git-log](/man/git-log)(1)

# RESOURCES

```[Documentation](https://git-scm.com/docs/gitk)```

<!-- verified: 2026-07-17 -->
