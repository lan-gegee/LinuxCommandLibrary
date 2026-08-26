# TAGLINE

初始化仓库并提交所有现存文件

# TLDR

**在当前目录创建新仓库**并完成初始提交

```git setup```

**在指定的**目录中**初始化仓库**

```git setup [path/to/directory]```

# SYNOPSIS

**git setup** [_directory_]

# PARAMETERS

_DIRECTORY_
> 要初始化的目录（默认：当前目录）。

# DESCRIPTION

**git setup** 初始化一个新的 Git 仓库，并将所有现存文件提交为初始提交。它属于 **git-extras** 软件包，把 `git init`、`git add .` 和 `git commit -m "Initial commit"` 合并为一条命令。

适合快速把一个现有的文件目录变成带有干净起始快照的 Git 仓库。

# CAVEATS

属于 **git-extras** 软件包，需单独安装。它会立即提交所有文件，因此请先准备好 **.gitignore** 文件，以免跟踪不想要的文件。

# HISTORY

git setup 是 **git-extras** 的一部分，后者是由 **TJ Holowaychuk** 创建的一组实用 Git 工具。它将新仓库常见的初始化步骤合并到了一起。

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

[git-init](/man/git-init)(1), [git-add](/man/git-add)(1), [git-commit](/man/git-commit)(1), [git-extras](/man/git-extras)(1), [git-ignore](/man/git-ignore)(1)
