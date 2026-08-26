# TAGLINE

面向 git 命令的终端用户界面，简化常见的 git 工作流

# TLDR

在当前仓库中**打开 lazygit**

```lazygit```

在指定仓库中打开

```lazygit -p [/path/to/repo]```

使用指定的工作树打开

```lazygit -w [/path/to/worktree]```

会话结束后**打开日志文件**

```lazygit -d```

**打印默认配置**

```lazygit -c```

**检查版本**

```lazygit -v```

# SYNOPSIS

**lazygit** [_options_]

# DESCRIPTION

**lazygit** 是一个面向 Git 的终端用户界面（TUI），用可视化、键盘驱动的面板取代了一连串手工输入的命令。它的分栏布局将 Status、Files、Branches、Commits 和 Stash 并排呈现，让你只需按一个键就能暂存单个文件或代码块（hunk）、就地查看差异，并在不离开界面的情况下完成提交。

除了日常的暂存与提交之外，lazygit 还让 Git 更高级的操作变得平易近人。交互式变基通过可视化的提交列表完成，列表中的条目可以重新排序、压缩（squash）或就地编辑。Cherry-pick 只需给提交打上标记，再把它们粘贴到另一个分支即可。解决合并冲突时会展示冲突区块，每一侧都能一键选定。分支管理、远程操作（push、pull、fetch）和 stash 操作都可以在各自的面板中完成，上下文菜单会列出当前可用的动作。通过可自定义的配置文件，还能定义自己的按键绑定和自定义命令快捷方式。

# PARAMETERS

**-p** _path_, **--path** _path_
> 要打开的仓库路径。

**-f** _path_, **--filter** _path_
> 在状态面板中按路径过滤文件。

**-g** _path_, **--git-dir** _path_
> 自定义 git 目录。

**-w** _path_, **--work-tree** _path_
> 自定义工作树。

**-c**, **--config**
> 打印默认配置。

**-d**, **--debug**
> 以调试日志模式运行。

**-v**, **--version**
> 打印版本。

# KEYBOARD SHORTCUTS

**Space**: 暂存/取消暂存文件或代码块
**c**: 提交已暂存的更改
**P**: 推送到远程
**p**: 从远程拉取
**b**: 创建分支
**m**: 合并分支
**r**: 变基
**s**: 将更改存入 stash
**Tab**: 切换面板
**?**: 显示所有按键绑定
**q**: 退出

# CAVEATS

需要先安装 git。部分操作会改写 git 历史，务必谨慎使用。配置文件的位置因操作系统而异（Linux 上为 ~/.config/lazygit/config.yml）。

# HISTORY

**lazygit** 由 **Jesse Duffield** 于 **2018 年**创建，目的是提供一种更轻松的方式在终端里操作 git。它用 Go 编写，迅速受到那些偏好终端工作流却又嫌原生 git 命令繁琐的开发者欢迎。项目至今仍在活跃开发，陆续加入了 worktree 支持和自定义命令等特性。

# INSTALL

```apt: sudo apt install lazygit```

```pacman: sudo pacman -S lazygit```

```apk: sudo apk add lazygit```

```zypper: sudo zypper install lazygit```

```brew: brew install lazygit```

```nix: nix profile install nixpkgs#lazygit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [tig](/man/tig)(1), [gitk](/man/gitk)(1), [gitui](/man/gitui)(1)
