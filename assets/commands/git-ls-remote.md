# TAGLINE

列出远程仓库的引用

# TLDR

**列出远程引用**

```git ls-remote [origin]```

**只显示标签**

```git ls-remote --tags [origin]```

**只显示分支**

```git ls-remote --heads [origin]```

**显示特定引用**

```git ls-remote [origin] [refs/heads/main]```

**列出 URL 的引用**

```git ls-remote [https://github.com/owner/repo.git]```

# SYNOPSIS

**git ls-remote** [_options_] [_repository_] [_refs_]

# PARAMETERS

_REPOSITORY_
> 远程名称或 URL。

_REFS_
> 要显示的特定引用。

**--heads**
> 只显示 heads（分支）。

**--tags**
> 只显示标签。

**--refs**
> 仅显示引用，不含剥离后的标签（peeled tags）。

**--get-url**
> 显示远程 URL。

**--exit-code**
> 未找到任何引用时以错误码退出。

**--symref**
> 显示符号引用所指向的底层引用（例如 HEAD 指向什么）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git ls-remote** 在不下载任何对象的情况下列出远程仓库中的引用。它会显示分支、标签及其提交哈希，便于在抓取之前检查远程状态。

该命令直接查询远程，显示查询时刻的最新引用。这可用于检查标签是否存在、验证分支状态，或针对远程仓库状态编写脚本。它既支持具名远程，也支持直接使用 URL。

# CAVEATS

需要网络访问。显示的是查询时刻的引用。大型仓库可能包含大量引用。

# HISTORY

git ls-remote 是 **Git** 用于检查远程引用的核心命令，适用于自动化与校验场景。

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

[git-remote](/man/git-remote)(1), [git-fetch](/man/git-fetch)(1), [git-ls-tree](/man/git-ls-tree)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-ls-remote)```

<!-- verified: 2026-07-17 -->
