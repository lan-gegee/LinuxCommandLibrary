# TAGLINE

Git 的 Tcl/Tk 图形界面

# TLDR

**启动 git gui**

```git gui```

**打开 blame 查看器**

```git gui blame [file.txt]```

**在指定行打开 blame**

```git gui blame --line=[100] [file.txt]```

**浏览分支处的仓库树**

```git gui browser [branch]```

**打开用于单次提交的 citool**

```git gui citool```

**用 citool 修正上一次提交**

```git gui citool --amend```

# SYNOPSIS

**git gui** [_command_] [_arguments_]

# PARAMETERS

**blame** _FILE_
> 打开文件的 blame 查看器。

**browser** _REVISION_
> 浏览指定修订版本处的树。

**citool**
> 启动 git gui，完成恰好一次提交后退出。

**version**
> 显示当前运行的 git gui 版本。

**--line=**_NUMBER_
> （blame）滚动 blame 视图使行 NUMBER 居中。

**--amend**
> （citool）自动进入 Amend Last Commit（修正上次提交）模式。

**--nocommit**
> （citool）不做提交，以零状态退出。

# DESCRIPTION

**git gui** 是 Git 的 Tcl/Tk 图形界面。它提供用于提交、浏览历史和查看 blame 注记的可视化工具。

该界面会显示已暂存和未暂存的改动，支持选择性暂存和撰写提交信息。blame 查看器逐行展示归属信息，并可在提交历史中交互式导航。

# CAVEATS

需要安装 Tcl/Tk。与现代 GUI 工具相比界面较为陈旧。可能未随默认安装提供。

# HISTORY

git gui 由 **Shawn O. Pearce** 创建，是 Git 官方的 Tcl/Tk 图形界面，自 Git 早期就提供图形化操作。

# INSTALL

```dnf: sudo dnf install git-gui```

```zypper: sudo zypper install git-gui```

```brew: brew install git-gui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-commit](/man/git-commit)(1), [git-blame](/man/git-blame)(1), [gitk](/man/gitk)(1), [tig](/man/tig)(1)
