# TAGLINE

图形化 Git 界面

# TLDR

**启动 Git Cola**

```cola```

**打开指定仓库**

```cola --repo [/path/to/repo]```

**以修正模式打开**

```cola --amend```

# SYNOPSIS

**cola** [_options_] [_repository_]

# PARAMETERS

**--repo** _path_
> 打开指定的 Git 仓库。

**--amend**
> 启动时启用 amend 选项。

**--prompt**
> 提示选择仓库。

# DESCRIPTION

**cola** 启动 Git Cola，这是一个用 Python 和 Qt 构建的强大 Git 图形用户界面。它提供可视化、键盘驱动的界面来暂存更改、创建提交、管理分支、查看历史以及执行其他 Git 操作，无需精通命令行。

界面强调 Git 暂存工作流，三栏视图分别显示未暂存的更改、已暂存的更改和提交信息的编写区域。交互式暂存允许选择单独的行或代码块进行暂存，从而对提交内容进行细粒度控制。diff 查看器支持语法高亮和并排比较模式。

Git Cola 是跨平台的，可在 Linux、macOS 和 Windows 上运行。它与系统编辑器和 diff 工具集成，支持快捷键以实现高效工作流，同时兼顾新手友好和高级用户特性。该工具开源且持续维护，是命令行 Git 和其他 GUI 客户端的替代选择。

# INSTALL

```dnf: sudo dnf install git-cola```

```apk: sudo apk add git-cola```

```zypper: sudo zypper install git-cola```

```brew: brew install git-cola```

```nix: nix profile install nixpkgs#git-cola```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-cola](/man/git-cola)(1), [gitk](/man/gitk)(1), [tig](/man/tig)(1)

# RESOURCES

```[Source code](https://github.com/git-cola/git-cola)```

```[Homepage](https://git-cola.github.io/)```

<!-- verified: 2026-06-22 -->
