# TAGLINE

初始化带 Git 后端的 Jujutsu 仓库

# TLDR

创建新的 jj/Git 共存仓库（默认）

```jj git init```

在指定路径创建新的 jj 仓库

```jj git init [path]```

使用现有 Git 仓库作为后端存储来初始化 jj

```jj git init --git-repo=[path/to/git-repo]```

# SYNOPSIS

**jj** **git** **init** [_options_] [_path_]

# PARAMETERS

**--colocate**
> 创建 jj/Git 共存（colocated）仓库。除非 `git.colocate` 配置设为 false，否则这是默认行为。

**--git-repo** _path_
> 作为后端存储使用的现有 Git 仓库路径。与 --colocate 互斥。

# DESCRIPTION

**jj git init** 初始化一个带 Git 后端的 Jujutsu 仓库。默认会创建共存仓库，`.jj` 和 `.git` 目录同时存在，使 jj 和 git 命令都能在同一个仓库上工作。在共存模式下，IDE 的 Git 集成可以照常工作。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-git-clone](/man/jj-git-clone)(1), [jj-git-fetch](/man/jj-git-fetch)(1), [git](/man/git)(1)
