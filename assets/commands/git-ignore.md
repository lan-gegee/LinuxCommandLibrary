# TAGLINE

管理 gitignore 条目

# TLDR

**添加到 gitignore**

```git ignore [pattern]```

**添加多个模式**

```git ignore "*.log" "*.tmp"```

**显示当前的忽略规则**

```git ignore```

**添加到全局 gitignore**

```git ignore --global [pattern]```

**添加到私有的 exclude 文件**

```git ignore --private [pattern]```

# SYNOPSIS

**git ignore** [_options_] [_patterns_]

# PARAMETERS

_PATTERNS_
> 要添加到 .gitignore 的模式。

**-l**, **--local**
> 添加到本地 .gitignore（默认）。

**-g**, **--global**
> 添加到全局 gitignore。

**-p**, **--private**
> 添加到私有 exclude 文件（.git/info/exclude）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git ignore** 管理 .gitignore 条目，将模式添加到仓库的 .gitignore 或全局 gitignore 文件中。不带参数运行时，它会显示当前 .gitignore 的内容。

它是 git-extras 套件的组成部分，会处理正确的格式并避免重复。如果文件不存在，它会创建 .gitignore。

# CONFIGURATION

**.gitignore**
> 由该命令管理的仓库级忽略模式。

**.git/info/exclude**
> 使用 --private 时仓库的私有排除模式。

**~/.gitignore_global**
> 使用 --global 时应用于所有仓库的全局忽略模式。

# CAVEATS

属于 git-extras 软件包。若 .gitignore 缺失则创建之。已被跟踪的文件需要手动取消跟踪。

# HISTORY

git ignore 是 **git-extras** 的组成部分，为编辑 gitignore 文件这一常见任务提供命令行界面。

# INSTALL

```brew: brew install git-ignore```

```nix: nix profile install nixpkgs#git-ignore```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-check-ignore](/man/git-check-ignore)(1), [git-extras](/man/git-extras)(1), [gibo](/man/gibo)(1)
