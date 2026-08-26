# TAGLINE

图形化的 Git 客户端 GUI

# TLDR

**启动 Git Cola**

```git cola```

**打开指定仓库**

```git cola [path/to/repo]```

**以修改模式打开**

```git cola --amend```

**打开特定对话框**

```git cola stash```

# SYNOPSIS

**git** **cola** [_options_] [_path_]

# PARAMETERS

**--amend**
> 以修改模式启动。

**--version**
> 显示版本。

**--prompt**
> 提示输入仓库。

# DESCRIPTION

**git cola** 是一个用 Python 和 Qt 构建的功能丰富的图形化 Git 客户端。它为常见 Git 操作提供友好的可视化界面，包括暂存代码块、提交更改、查看差异、管理分支以及浏览仓库历史。

该工具具有文件浏览器、带语法高亮的差异查看器、支持拼写检查的提交信息编辑器，以及允许选择特定行或代码块进行暂存的交互式暂存功能。Git Cola 还包含 stash、分支、合并及其他高级操作的专用对话框。

与更简单的 Git 图形工具不同，Git Cola 面向希望获得可视化工具又不牺牲控制力的进阶用户。它可以配合命令行工作流使用，支持 Linux、macOS 和 Windows。界面高度可定制，可配置快捷键绑定、主题和布局选项。

# CONFIGURATION

**~/.config/git-cola/**
> 用户设置，包括窗口布局、主题偏好和快捷键绑定。

# INSTALL

```dnf: sudo dnf install git-cola```

```apk: sudo apk add git-cola```

```zypper: sudo zypper install git-cola```

```brew: brew install git-cola```

```nix: nix profile install nixpkgs#git-cola```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gitk](/man/gitk)(1), [git-gui](/man/git-gui)(1), [tig](/man/tig)(1), [lazygit](/man/lazygit)(1)
