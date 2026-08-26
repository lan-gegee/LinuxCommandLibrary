# TAGLINE

用二分查找定位引入 bug 的提交

# TLDR

**开始**一次 bisect 会话

```git bisect start```

预先给出坏提交和好提交来**开始**

```git bisect start [HEAD] [v1.0]```

将当前提交**标记**为有问题

```git bisect bad```

将某个提交**标记**为正常

```git bisect good [commit]```

**跳过**无法测试的提交

```git bisect skip```

用测试脚本**自动化**搜索

```git bisect run [./test.sh]```

用内联测试命令**自动化**

```git bisect run [make test]```

**显示**目前为止的标记记录

```git bisect log```

**结束**会话并回到起点

```git bisect reset```

# SYNOPSIS

**git bisect** _subcommand_ [_options_]

# PARAMETERS

**start** [_bad_ [_good_...]] [**--**] [_paths_...]
> 开始一次会话。可选地立即给出坏提交和好提交，并把搜索限制在 _paths_ 内。

**bad** [_commit_]
> 标记一个提交包含 bug。默认为当前提交。

**good** [_commit_...]
> 将一个或多个提交标记为不含 bug。

**new** [_commit_], **old** [_commit_]
> **bad** 和 **good** 的别名，用于追查任何行为变化而不只是 bug。

**terms** **--term-old**=_term_ **--term-new**=_term_
> 使用你自己的措辞，例如 **--term-old=fast --term-new=slow**。

**skip** [_commit_...]
> 跳过无法测试的提交，例如无法构建的那些。

**run** _cmd_ [_args_...]
> 在每一步运行 _cmd_，并根据其退出状态自动标记。

**reset** [_commit_]
> 结束会话并回到原来的分支，或回到 _commit_。

**log**
> 打印已做标记的日志。

**replay** _logfile_
> 重放一份 bisect 日志，恢复之前的会话。

**visualize**, **view**
> 在 gitk 或 **git log** 中显示剩余的候选提交。

**--first-parent**
> 只跟随合并提交的第一父提交。

**--no-checkout**
> 不检出树；只更新 **BISECT_HEAD**。当检出代价高昂时有用。

# DESCRIPTION

**git bisect** 通过二分查找定位引入问题的提交。你告诉它一个存在 bug 的提交和一个不存在的提交，它检出中间的那个，你测试并报告结果，然后它把剩余范围对半缩小。搜索是对数级的：约 **10** 次测试足以覆盖 **1000** 个提交，一百万个也只需 **20** 次。

**good**/**bad** 这套词汇假定你在追查 bug，但机制是通用的：任何在某个时点发生变化的属性都可以被二分。**old**/**new** 以及自定义的 **--term-old**/**--term-new** 就是为追查性能退化、行为变化甚至修复了某个问题的提交而存在的。

**git bisect run** 是这个命令赢得声誉的地方。给定一个以 **0** 表示好、非零表示坏的脚本，git 就能无人值守地驱动整个搜索。特殊的退出码 **125** 表示"无法测试此提交"，效果等同 **skip**；**126** 到 **255** 之间的任何退出码都会中止会话。由于 **run** 接受的是命令行而非只能是文件，**git bisect run make test** 可以直接使用。

搜索结束时，git 会报告第一个坏提交并把你停在那里。**git bisect reset** 让你回到原处。

# CAVEATS

退出码 **1** 表示坏，但大多数失败也是如此，包括编译错误或依赖缺失。一个无法区分"bug 存在"和"此提交无法构建"的测试脚本会冤枉错误的提交。对不可测试的提交请返回 **125**。

避免在测试脚本中使用退出码 **255**：它会中止 bisect。**grep** 找不到内容时返回 **1**，这很方便，但以裸 **grep** 结尾的脚本会反转你可能想要的意思，所以请明确处理退出状态。

Bisect 会检出任意的历史提交，因此脏的工作树可能阻碍检出或悄悄污染测试结果。先提交或储藏（stash）。构建产物和生成文件也会跨检出残留，可能掩盖真实结果：请在测试脚本中清理它们。

**skip** 缩小范围的效果不如真实的回答，跳过整片区域可能让 git 无法锁定单一的罪魁祸首，转而报告一段候选范围。

结果只是你的测试第一次失败的提交，未必就是造成问题的提交。bug 可能以潜伏形式引入，之后才被无关更改暴露出来。

如果历史中包含合并，第一个坏提交可能是合并本身，而实际更改在被合并的分支上。**--first-parent** 把搜索限制在主线上，对于采用特性分支合并的仓库来说这往往正是你想要的。

# HISTORY

**git bisect** 由 **Linus Torvalds** 于 **2005 年**（git 诞生的第一年）加入，最初是一个 shell 脚本。**git bisect run** 随后不久由 **Christian Couder** 贡献，他还在 git **2.7**（**2015 年**）中加入了 **old**/**new** 术语，用于对非 bug 类的变化进行二分。实现则在后续版本中被逐步重写为 C。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-log](/man/git-log)(1), [git-blame](/man/git-blame)(1), [git-annotate](/man/git-annotate)(1), [git-stash](/man/git-stash)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-bisect)```

<!-- verified: 2026-07-16 -->
