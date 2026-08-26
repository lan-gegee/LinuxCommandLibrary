# TAGLINE

Git 脚本通用的 Shell 库

# TLDR

**在 git 脚本中引入**

```. "$(git --exec-path)/git-sh-setup"```

# SYNOPSIS

**git-sh-setup**

# DESCRIPTION

**git-sh-setup** 是一个内部 shell 库，为 Git 脚本提供常用函数。其中包含用于仓库校验、目录跳转、彩色输出和错误处理的工具函数。

关键函数包括 `require_work_tree`、`cd_to_toplevel`、`die` 和 `git_pager`。脚本引入该库后即可在各 Git shell 命令之间保持一致的行为。

# CAVEATS

内部库，不是命令。必须被引入（source），不能直接执行。由 git 的 shell 脚本使用。

# HISTORY

git-sh-setup 是 **Git** 内部基础设施的一部分，为基于 shell 的 git 命令和钩子提供共享功能。

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

[git-sh-i18n](/man/git-sh-i18n)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-sh-setup)```

<!-- verified: 2026-07-17 -->
