# TAGLINE

将工作目录更新到指定修订版本

# TLDR

**更新到 tip**

```hg update```

**更新到特定修订版本**

```hg update -r [revision]```

**更新到某个分支**

```hg update [branch-name]```

**更新到某个标签**

```hg update [tag-name]```

**丢弃更改进行强制更新**

```hg update -C```

**先检查是否存在未提交的更改**

```hg update -c [revision]```

# SYNOPSIS

**hg** **update** [_options_] [_rev_]

# PARAMETERS

**-r**, **--rev** _rev_
> 要更新到的修订版本。

**-C**, **--clean**
> 丢弃未提交的更改。

**-c**, **--check**
> 存在未提交的更改时中止。

**-m**, **--merge**
> 合并未提交的更改。

**-d**, **--date** _date_
> 匹配日期的最新（tipmost）修订版本。

# DESCRIPTION

**hg update**（别名：**up**、**checkout**、**co**）将工作目录更新到指定修订版本。不带参数时，更新到当前分支的 tip。可以更新到修订版本、分支、标签或书签。使用 **-C** 丢弃本地更改，或使用 **-c** 在存在更改时中止。

# INSTALL

```apt: sudo apt install mercurial```

```dnf: sudo dnf install mercurial```

```pacman: sudo pacman -S mercurial```

```apk: sudo apk add mercurial```

```zypper: sudo zypper install mercurial```

```brew: brew install mercurial```

```nix: nix profile install nixpkgs#mercurial```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hg](/man/hg)(1), [hg-pull](/man/hg-pull)(1), [hg-commit](/man/hg-commit)(1), [hg-status](/man/hg-status)(1)
