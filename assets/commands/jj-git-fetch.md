# TAGLINE

从 Git 远程仓库抓取变更到 Jujutsu 仓库

# TLDR

从默认远程抓取

```jj git fetch```

从特定远程抓取

```jj git fetch --remote [origin]```

抓取所有远程

```jj git fetch --all-remotes```

抓取特定分支

```jj git fetch --branch [main]```

# SYNOPSIS

**jj** **git** **fetch** [_options_]

# PARAMETERS

**--remote** _name_
> 要抓取的远程。

**--all-remotes**
> 从所有远程抓取。

**--branch** _name_
> 抓取特定分支。

# DESCRIPTION

**jj git fetch** 从 Git 远程仓库抓取变更到 Jujutsu 仓库。它会更新远程跟踪分支。与 Git 后端协作以同步远程仓库。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-git-push](/man/jj-git-push)(1)
