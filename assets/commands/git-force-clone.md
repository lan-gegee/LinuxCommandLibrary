# TAGLINE

强制克隆一个仓库，若目标目录存在则替换之

# TLDR

**强制克隆**到某个目录，先移除其中已有的内容

```git force-clone [url] [directory]```

**强制克隆到指定分支**

```git force-clone -b [branch] [url] [directory]```

**强制克隆并重置到远程 HEAD**，即使该目录已是一个检出结果

```git force-clone [https://github.com/owner/repo.git] [existing-dir]```

# SYNOPSIS

**git force-clone** [**-b** _BRANCH_] _URL_ _DIRECTORY_

# PARAMETERS

_URL_
> 仓库 URL（https、ssh、git 或本地路径）。

_DIRECTORY_
> 目标目录。如果它已存在且是同一仓库的克隆，其内容会被重置为与远程一致；如果它存在但属于另一个仓库（或包含无关文件），则会被移除并重新克隆。

**-b** _BRANCH_
> 克隆后检出 _BRANCH_。

**--help**
> 显示帮助信息。

# DESCRIPTION

来自 **git-extras** 套件的 **git force-clone** 保证目标目录最终成为给定 URL 的全新干净克隆。它是部署脚本中"给我远程上的内容就行"的重锤：

- 如果目录不存在，则正常克隆。
- 如果目录已是同一 URL 的克隆，它会 fetch 并将工作树硬重置为与远程一致，丢弃任何本地改动。
- 如果目录存在但属于另一个仓库（或包含无关文件），则移除该目录并重新克隆。

# CAVEATS

**具有破坏性。** 目标目录中未提交的改动会未经确认直接丢失。如果目录被重新克隆，未推送到远程的本地分支也会被删除。请谨慎使用，尤其是在交互式环境中——如果只需要重新同步并希望保留其他本地状态，建议使用 `git fetch` + `git reset --hard`。

# HISTORY

**git force-clone** 是 **git-extras** 的组成部分，后者是由 **TJ Holowaychuk** 及贡献者长期维护的 git 辅助工具合集。

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

[git-clone](/man/git-clone)(1), [git-reset](/man/git-reset)(1), [git-fetch](/man/git-fetch)(1), [git-extras](/man/git-extras)(1)
