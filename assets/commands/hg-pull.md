# TAGLINE

从远程仓库拉取变更集到本地仓库

# TLDR

**从默认远程拉取**

```hg pull```

**拉取并更新工作目录**

```hg pull -u```

**从指定源拉取**

```hg pull [https://example.com/repo]```

**拉取特定修订版本**

```hg pull -r [revision]```

**拉取特定分支**

```hg pull -b [branch]```

**从源拉取并强制执行（即使仓库无关）**

```hg pull -f [https://example.com/repo]```

# SYNOPSIS

**hg** **pull** [_options_] [_source_]

# PARAMETERS

**-u**, **--update**
> 拉取后更新到新分支头。

**-r**, **--rev** _rev_
> 拉取特定修订版本。

**-b**, **--branch** _branch_
> 拉取特定分支。

**-B**, **--bookmark** _bookmark_
> 从远程仓库拉取特定书签。

**-f**, **--force**
> 即使来自无关仓库也强制拉取。

**--insecure**
> 不验证服务器证书（用于 HTTPS 连接）。

# DESCRIPTION

**hg pull** 从远程仓库获取变更集到本地仓库。与 Git 的 pull 不同，它不会自动更新工作目录。请使用 **-u** 进行更新，或在拉取后单独运行 **hg update**。未指定源时，默认使用本仓库当初克隆自的那个仓库。

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

[hg](/man/hg)(1), [hg-update](/man/hg-update)(1), [hg-push](/man/hg-push)(1), [hg-clone](/man/hg-clone)(1), [hg-log](/man/hg-log)(1)
