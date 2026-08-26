# TAGLINE

按作者分组汇总 git log 输出

# TLDR

**按作者汇总提交**

```git shortlog```

**显示提交数量**

```git shortlog -sn```

**显示邮箱地址**

```git shortlog -sne```

**某个范围的 shortlog**

```git shortlog [v1.0..v2.0]```

**按提交者分组**

```git shortlog -c```

# SYNOPSIS

**git shortlog** [_options_] [_revision-range_]

# PARAMETERS

_REVISION-RANGE_
> 要汇总的提交。

**-s**, **--summary**
> 仅显示数量。

**-n**, **--numbered**
> 按数量排序。

**-e**, **--email**
> 显示邮箱地址。

**-c**, **--committer**
> 按提交者分组。

**--group** _FIELD_
> 按指定字段分组。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git shortlog** 将提交按作者归组，从而对 `git log` 的输出做汇总。它常用于生成发布说明和贡献者致谢名单。

该命令可以显示每位作者的提交数量、按贡献量排序，并利用 mailmap 在不同的姓名/邮箱变体之间做身份归一。

# CONFIGURATION

**.mailmap**
> 将作者身份映射到规范的姓名和邮箱，git shortlog 用它来做去重。

# CAVEATS

从 stdin 或修订范围读取。使用 mailmap 合并同一身份。与 git log --oneline 不同。

# HISTORY

git shortlog 是用于生成贡献者汇总的核心 **Git** 命令，常见于发布说明和致谢名单中。

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

[git-log](/man/git-log)(1), [git-authors](/man/git-authors)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-shortlog)```

<!-- verified: 2026-07-17 -->
