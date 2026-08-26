# TAGLINE

Git 的文本模式界面

# TLDR

**打开仓库浏览器**（主视图）

```tig```

**显示提交日志**视图

```tig log```

**显示工作目录状态**

```tig status```

对文件**显示 blame（行级追溯）**

```tig blame [path/to/file]```

**显示 stash** 视图

```tig stash```

**浏览特定文件的提交**

```tig [path/to/file]```

**浏览某范围内的提交**

```tig [commit1]..[commit2]```

作为 git 输出的**分页器**使用

```git log --pretty=raw | tig --pretty=raw```

# SYNOPSIS

**tig** [_options_] [_revisions_] [**--**] [_paths_]

# SUBCOMMANDS

**log**
> 在日志视图中启动，显示 git log 输出

**show**
> 使用 git show 选项打开 diff 视图

**blame** _file_
> 显示附带提交信息的文件标注

**grep**
> 打开 grep 视图；支持 git grep 的选项

**refs**
> 在 refs 视图中启动，显示分支和标签

**reflog**
> 在 reflog 视图中启动

**stash**
> 在 stash 视图中启动

**status**
> 在状态视图中启动，显示工作目录状态

# PARAMETERS

**+**_number_
> 首个视图打开时选中指定的行。

**-C** _path_
> 就像在 _path_ 中而不是当前目录启动 tig 一样运行。

**--all**
> 相当于把所有引用都写在命令行上（显示每个分支）。

**--stdin**
> 从标准输入读取提交 ID 或 git 输出（分页器模式）。

**--pretty=raw**
> 处理格式化为 `git log --pretty=raw` 输出的 stdin。

**-v**, **--version**
> 显示版本后退出。

**-h**, **--help**
> 显示帮助信息后退出。

# DESCRIPTION

**tig** 是基于 ncurses 的 Git 文本界面。它可作为仓库浏览器，用于查看提交历史、浏览 diff 以及管理暂存。它还可以充当 git 命令输出的分页器。

主视图显示包含作者、日期和说明的提交历史。按 **Enter** 可打开所选提交的 diff 视图。用 **j/k** 或方向键导航，**/** 搜索，**q** 退出或返回。

在状态视图中，你可以按文件或代码块（hunk）级别暂存更改。按 **u** 暂存/取消暂存文件，进入文件内部可以逐块暂存。这为 **git add -p** 提供了可视化替代方案。

配置从 **~/.config/tig/config** 或 **~/.tigrc** 读取。颜色、快捷键和视图均可自定义。在 tig 中按 **h** 可显示包含所有快捷键的帮助菜单。

# KEY BINDINGS

**j/k** 或方向键
> 向上/向下导航

**Enter**
> 打开选中项

**q**
> 退出或关闭当前视图

**/**
> 向前搜索

**n/N**
> 下一个/上一个搜索结果

**u**
> 暂存/取消暂存文件或代码块（在状态视图中）

**h**
> 显示帮助

# CAVEATS

tig 接受大多数 git-log 和 git-diff 选项，但一些复杂的 git 命令可能无法按预期显示。提交数量庞大的仓库导航速度可能较慢。自定义配色需要终端支持。

# HISTORY

**tig** 由 **Jonas Fonseca** 创建，首次发布于 **2006 年**。名字是"git"的倒序拼写。它使用 C 语言和 ncurses 编写，设计目标是提供一个不离开终端即可使用的 Git 可视化界面，其灵感来自 gitk 等工具，但面向文本模式环境。

# INSTALL

```apt: sudo apt install tig```

```dnf: sudo dnf install tig```

```pacman: sudo pacman -S tig```

```apk: sudo apk add tig```

```zypper: sudo zypper install tig```

```brew: brew install tig```

```nix: nix profile install nixpkgs#tig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-log](/man/git-log)(1), [git-diff](/man/git-diff)(1), [gitk](/man/gitk)(1), [lazygit](/man/lazygit)(1)
