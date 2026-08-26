# TAGLINE

用 fzf 实现的交互式 git 命令

# TLDR

**交互式** git log 查看器

```forgit log```

**交互式** git diff 查看器

```forgit diff```

**交互式** git add

```forgit add```

**交互式** git stash 查看器

```forgit stash```

# SYNOPSIS

**forgit** [_command_] [_options_]

# PARAMETERS

**log**
> 交互式 git log 浏览器

**diff**
> 交互式 diff 查看器

**add**
> 交互式暂存选择器

**reset**
> 交互式取消暂存选择器

**stash**
> 交互式 stash 查看器

**ignore**
> 交互式 .gitignore 生成器

**clean**
> 交互式清理选择器

**rebase**
> 交互式 rebase 提交选择器

**cherry-pick**
> 交互式 cherry-pick 提交选择器

**checkout**> 交互式分支/检出选择器

**branch**> 交互式分支管理器

**-h, --help**> 显示帮助并退出

**--version**> 显示版本并退出

# DESCRIPTION

**forgit** 为常见的 git 命令封装了交互式 fzf 界面。它为查看日志、diff、暂存文件和管理分支等 git 操作提供模糊查找能力。

该工具需要安装 fzf，让从大量提交、分支或文件中搜索和选择变得容易，从而增强 git 工作流。

# COMMANDS

每个命令都用交互式 fzf 界面封装对应的 git 功能：

```
forgit log      → git log with fuzzy search
forgit diff     → git diff with file selection
forgit add      → git add with file picker
forgit stash    → git stash with list picker
forgit checkout → git checkout with branch picker
```

# CAVEATS

需要安装 fzf。终端必须支持交互式 TUI。大型仓库加载可能较慢。部分命令可能不支持所有 git 标志。

# HISTORY

**forgit** 的诞生是为了把 fzf 的能力与常见 git 操作结合起来，使大型 git 仓库的交互式导航更加容易。

# INSTALL

```brew: brew install forgit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](https://github.com/junegunn/fzf), [git](https://git-scm.com/), [lazygit](https://github.com/jesseduffield/lazygit)
