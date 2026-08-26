# TAGLINE

撤销最近的提交同时保留改动

# TLDR

**撤销最近一次提交**

```git undo```

**撤销 N 个提交**

```git undo [3]```

**撤销并将改动保留在暂存区**

```git undo --soft```

**撤销并丢弃改动**

```git undo --hard```

# SYNOPSIS

**git undo** [_count_] [_options_]

# PARAMETERS

_COUNT_
> 要撤销的提交数量（默认：1）。

**--soft**
> 将改动保留在暂存区。

**--hard**
> 丢弃所有改动。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git undo** 移除最近的提交，同时把改动保留在工作目录中（未暂存状态）。它是 `git reset` 的便捷封装，默认执行混合重置，不会丢失任何工作成果。

不带参数时会撤销最近一次提交；传入数字可撤销多个提交。用 **--soft** 可让改动保留在暂存区，用 **--hard** 则将其完全丢弃。

# CAVEATS

属于 **git-extras** 软件包，需单独安装。只影响尚未推送的本地提交。**--hard** 会永久丢弃改动，难以恢复。

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

[git-reset](/man/git-reset)(1), [git-revert](/man/git-revert)(1), [git-extras](/man/git-extras)(1)
