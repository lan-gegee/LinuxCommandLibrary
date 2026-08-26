# TAGLINE

跟踪多个 Git 仓库的状态

# TLDR

**显示**当前目录下所有仓库的状态

```gfold```

**显示**所有仓库（递归）

```gfold -r```

只显示有未提交更改的仓库

```gfold --dirty```

以 JSON 格式显示

```gfold --json```

# SYNOPSIS

**gfold** [_options_] [_path_]

# PARAMETERS

**-r, --recursive**
> 递归搜索仓库

**--dirty**
> 只显示有未提交更改的仓库

**--json**
> 以 JSON 格式输出

**-p, --path** _PATH_
> 搜索仓库的路径（默认：当前目录）

**-v, --version**
> 显示版本后退出

**-h, --help**
> 显示帮助后退出

# DESCRIPTION

**gfold** 是一个跟踪多个 Git 仓库状态的命令行工具。它扫描目录中的 Git 仓库，并以清晰、有条理的格式展示它们的状态。

该工具会显示各仓库是干净的、有未提交更改、领先/落后于远程，还是有未跟踪文件。对于同时维护许多仓库、希望快速总览所有项目状态的开发者来说非常实用。

# OUTPUT FORMAT

输出按类别组织：
- **Clean**：仓库是最新的
- **Unclean**：有未提交的更改
- **Unpushed**：有尚未推送的提交
- **Untracked**：有未跟踪的文件

# CAVEATS

扫描大型目录树可能耗时较长。需要对仓库目录的读取权限。不执行 fetch 的情况下，状态可能不反映上游变更。

# HISTORY

**gfold** 的诞生是为了替代手动逐一检查多个 Git 仓库的做法，提供跨项目的仓库状态统一视图。

# INSTALL

```pacman: sudo pacman -S gfold```

```apk: sudo apk add gfold```

```brew: brew install gfold```

```nix: nix profile install nixpkgs#gfold```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [ghq](/man/ghq)(1)
