# TAGLINE

报告仓库对象的数量和大小

# TLDR

**统计对象数量**

```git count-objects```

**详细统计**

```git count-objects -v```

**人类可读的大小**

```git count-objects -vH```

# SYNOPSIS

**git count-objects** [_options_]

# PARAMETERS

**-v**, **--verbose**
> 显示详细的分类统计。

**-H**, **--human-readable**
> 以人类可读格式显示大小。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git count-objects** 报告未打包对象文件的数量及其磁盘占用，帮助判断何时适合重新打包。

详细模式（**-v**）显示细目：count（松散对象数量）、size（松散对象的磁盘占用，单位 KiB）、in-pack（打包对象数量）、packs（pack 文件数量）、size-pack（pack 的磁盘占用，单位 KiB）、prune-packable（同时存在于 pack 中的松散对象）以及 garbage（对象目录中既非有效松散对象也非有效 pack 的文件）。

**-H** 标志以人类可读格式（KiB、MiB、GiB）呈现大小，无需手动换算单位即可一目了然地评估存储占用。

# CAVEATS

核心 git 命令。未打包对象较多说明近期活动频繁。数量过大可能意味着需要执行 gc。

# HISTORY

git count-objects 是 **Git** 用于仓库维护的核心命令，帮助管理员了解存储使用情况。

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

[git-gc](/man/git-gc)(1), [git-prune](/man/git-prune)(1), [git-fsck](/man/git-fsck)(1)
