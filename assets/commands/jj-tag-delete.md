# TAGLINE

从仓库中移除标签

# TLDR

删除标签

```jj tag delete [tagname]```

删除多个标签

```jj tag delete [tag1] [tag2]```

# SYNOPSIS

**jj** **tag** **delete** _name_...

# DESCRIPTION

**jj tag delete** 从仓库中移除标签。标签是指向特定提交的轻量级引用。删除标签不会影响底层的提交。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-tag](/man/jj-tag)(1), [jj-tag-list](/man/jj-tag-list)(1)
