# TAGLINE

同时删除本地与远程标签

# TLDR

**删除本地和远程标签**

```git delete-tag [tag_name]```

**一次删除多个标签**

```git delete-tag [tag1] [tag2]```

# SYNOPSIS

**git** **delete-tag** _tag_ [_tag_...]

# DESCRIPTION

**git delete-tag** 在一次操作中同时删除本地和远程的标签。它是 git-extras 工具集的组成部分，将原本需要分别执行 git tag -d 和 git push origin --delete 的过程合并为一步，简化了标签删除操作。

标签通常用于标记发布节点或重要提交，但有时也会因失误、版本变更或发布回滚而需要删除。该命令确保本地与远程仓库保持同步，避免删除本地标签后从远程拉取时该标签仍然出现的情形。

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

[git-tag](/man/git-tag)(1), [git-extras](/man/git-extras)(1), [git-push](/man/git-push)(1), [git-delete-branch](/man/git-delete-branch)(1)
