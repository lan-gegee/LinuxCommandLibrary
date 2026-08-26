# TAGLINE

在本地和远程重命名 Git 标签

# TLDR

**重命名标签**

```git rename-tag [old_name] [new_name]```

# SYNOPSIS

**git** **rename-tag** _old_name_ _new_name_

# DESCRIPTION

**git rename-tag** 在本地和远程同时重命名标签。它是 git-extras 的一部分：先创建指向旧标签所在提交的新标签，删除本地的旧标签，然后将新标签和旧标签的删除操作推送到 `origin`。

# CAVEATS

总是推送到名为 `origin` 的远程；不支持通过参数指定其他远程。

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

[git-tag](/man/git-tag)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-rename-tag)```

<!-- verified: 2026-07-17 -->
