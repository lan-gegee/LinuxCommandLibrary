# TAGLINE

将本地变更集推送到远程仓库

# TLDR

**推送到默认远程**

```hg push```

**推送到指定 URL**

```hg push [url]```

**推送特定分支**

```hg push -b [branch]```

**推送特定修订版本**

```hg push -r [revision]```

**强制推送**

```hg push -f```

**推送新分支**

```hg push --new-branch```

# SYNOPSIS

**hg push** [_options_] [_dest_]

# PARAMETERS

_DEST_
> 目标仓库。

**-b**, **--branch** _BRANCH_
> 推送特定分支。

**-r**, **--rev** _REV_
> 推送到指定修订版本为止。

**-f**, **--force**
> 强制推送。

**--new-branch**
> 允许推送新分支。

**-B**, **--bookmark** _NAME_
> 推送书签。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hg push** 将本地变更集发送到远程仓库。它传输远程所没有的已提交更改。

该命令会验证推送不会产生多个头（head），除非强制执行。它支持推送特定的分支或修订版本。

# CAVEATS

无法推送未提交的更改。强制推送可能引发问题。远端钩子可能会拒绝推送。

# HISTORY

push 是 **Mercurial** 自 1.0 版本以来用于分布式协作的核心命令。

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

[hg](/man/hg)(1), [hg-pull](/man/hg-pull)(1)
