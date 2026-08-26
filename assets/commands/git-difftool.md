# TAGLINE

使用外部可视化 diff 工具比较改动

# TLDR

**使用外部工具比较**

```git difftool [file]```

**使用指定的工具比较**

```git difftool -t [vimdiff] [file]```

**无需提示地进行比较**

```git difftool -y [file]```

**比较已暂存的改动**

```git difftool --staged```

**比较提交**

```git difftool [commit1] [commit2]```

**目录 diff 模式**

```git difftool -d [commit]```

# SYNOPSIS

**git** **difftool** [_options_] [_commit_] [_--_] [_files_...]

# PARAMETERS

**-t** _tool_, **--tool** _tool_
> 使用指定的 diff 工具，而非配置中的默认工具。

**-y**, **--no-prompt**
> 启动每个 diff 工具实例前不再提示。

**--prompt**
> 每次调用前提示（默认行为；覆盖配置）。

**-d**, **--dir-diff**
> 将修改过的文件复制到临时位置，一次性对整个目录树进行 diff。从不提示。

**-g**, **--gui**
> 使用 **diff.guitool** 中配置的工具，而不是 **diff.tool**。

**--staged**
> 比较已暂存的改动（等同于 **git diff --staged**）。

**--tool-help**
> 列出本系统能识别的可用工具。

**-x** _cmd_, **--extcmd** _cmd_
> 以 `cmd $LOCAL $REMOTE` 的形式运行自定义命令，忽略已配置的工具。

**--no-symlinks**
> 在目录 diff 模式下复制文件而不是用符号链接指向未更改的文件（Windows 上始终如此）。

**--trust-exit-code**
> 以被调用工具的退出码退出，而不是忽略它。

# DESCRIPTION

**git difftool** 启动外部可视化 diff 工具来审查 Git 仓库中的改动。它是 **git diff** 的前端，接受相同的选项和参数，但把实际的比较工作交给图形化或基于终端的 diff 应用程序，而不是打印统一格式的 diff。

该命令支持多种 diff 工具，包括 vimdiff、meld、kdiff3、emerge 和 opendiff；运行 **git difftool --tool-help** 可以查看检测到了哪些。目录 diff 模式（**-d**）对支持同时比较整个目录树的图形化工具尤其有用，因为它会准备两棵树的临时副本，而不是对每个文件都调用一次工具。

# CONFIGURATION

**diff.tool**
> difftool 使用的默认工具（**--gui** 会依次回退到 merge.guitool、diff.tool、merge.tool）。

**difftool.\<tool\>.path**
> 工具可执行文件的显式路径，用于该工具不在 **PATH** 中的情况。

**difftool.\<tool\>.cmd**
> 工具的自定义命令行，其中 **$LOCAL**、**$REMOTE**、**$MERGED** 和 **$BASE** 可用。

**difftool.prompt**
> 是否在启动每个实例之前提示（默认为 true）。

# CAVEATS

除非设置了 **--trust-exit-code**，否则 diff 工具产生的错误会被忽略。目录 diff 模式放弃了针对单个文件的逐个调用方式，对于期望接收单文件输入的工具，行为可能有所不同。

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

[git-diff](/man/git-diff)(1), [git-mergetool](/man/git-mergetool)(1), [git-log](/man/git-log)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-difftool)```

<!-- verified: 2026-07-17 -->
