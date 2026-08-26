# TAGLINE

在多个仓库中执行 Git 命令

# TLDR

**在配置键列出的每个仓库中运行 git 命令**

```git for-each-repo --config=[maintenance.repo] [fetch]```

**对所有已注册的仓库执行维护**

```git for-each-repo --config=[maintenance.repo] maintenance run```

**失败后继续执行**

```git for-each-repo --config=[maintenance.repo] --keep-going [gc]```

# SYNOPSIS

**git** **for-each-repo** **--config**=_key_ [**--keep-going**] [--] _command_ [_args_]

# PARAMETERS

**--config** _key_
> 列出各仓库绝对路径的多值配置键。

**--keep-going**
> 命令在某个仓库上失败时继续处理其余仓库。退出码仍会指示失败。

# DESCRIPTION

**git for-each-repo** 在由 Git 配置值定义的多个仓库中执行指定的 Git 命令。该命令读取一个多值配置键，其中每个值都是一个 Git 仓库的绝对路径，然后在每个仓库中运行所提供的命令。

它的主要用例是 git-maintenance，后者利用 for-each-repo 按计划在所有已注册的仓库上运行 gc、fetch 或 repack 等维护任务。配置值从系统、全局和本地 Git 配置中加载。如果在 Git 仓库之外运行，则只使用系统和全局配置。

# CONFIGURATION

**~/.gitconfig**
> 包含列出仓库路径以供批量操作使用的多值配置键。

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

[git-maintenance](/man/git-maintenance)(1), [git-config](/man/git-config)(1)
