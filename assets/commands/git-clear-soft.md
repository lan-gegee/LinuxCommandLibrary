# TAGLINE

重置并清理工作目录，但保留被忽略的文件

# TLDR

**清空工作目录**（会提示确认）

```git clear-soft```

# SYNOPSIS

**git** **clear-soft**

# DESCRIPTION

**git clear-soft** 是一个 **git-extras** 命令，用于丢弃所有未提交的工作：它会移除未跟踪的文件和目录，并将已跟踪的文件重置回 **HEAD**。它是 **git-clear** 的温和版本，因为被 **.gitignore** 匹配的文件会被保留，而不会被一并删除。

它在询问 **"Sure? - This command may delete files that cannot be recovered. Files and directories in .gitignore will be preserved [y/N]:"** 之后，依次执行 **git clean -d -f** 和 **git reset --hard**。与 **git-clear** 不同，它没有 **-f**/**--force** 选项，因此无法跳过确认提示，也无法以非交互方式使用。

# CAVEATS

对未跟踪且未被忽略的文件具有破坏性且不可逆：这些文件会被直接删除，而不是暂存（stash）。仅在安装了 **git-extras** 时可用；它不属于核心 Git。

# HISTORY

git clear-soft 被加入社区维护的 Git 实用脚本合集 **git-extras**，作为 **git-clear** 的低破坏性替代，可以保留被忽略的文件。

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

[git-clear](/man/git-clear)(1), [git-reset](/man/git-reset)(1), [git-clean](/man/git-clean)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-clear-soft)```

<!-- verified: 2026-07-17 -->
