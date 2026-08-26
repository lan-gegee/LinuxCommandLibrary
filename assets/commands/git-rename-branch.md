# TAGLINE

在本地和远程重命名 Git 分支

# TLDR

**重命名当前分支**

```git rename-branch [new_name]```

**重命名特定分支**

```git rename-branch [old_name] [new_name]```

# SYNOPSIS

**git** **rename-branch** [_old_name_] _new_name_

# DESCRIPTION

**git rename-branch** 在本地和远程同时重命名分支。它是 git-extras 的一部分，用一条命令完成本地重命名、将新分支名推送到远程、删除旧远程分支以及更新上游跟踪引用。

没有这个工具时，重命名远程分支需要多个步骤：`git branch -m`、`git push origin new_name`、`git push origin --delete old_name`，以及 `git branch -u origin/new_name`。

# PARAMETERS

**old_name**
> 要重命名的分支的当前名称。若省略，则使用当前分支。

**new_name**
> 分支的新名称。

# CAVEATS

需要安装 git-extras。其他协作者在重命名后必须更新他们的本地引用。指向旧分支名的 pull request 或 merge request 可能需要手动更新。

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

[git-branch](/man/git-branch)(1), [git-extras](/man/git-extras)(1)
