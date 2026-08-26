# TAGLINE

创建修订的副本

# TLDR

复制当前修订

```jj duplicate```

复制特定修订

```jj duplicate [revision]```

复制多个修订

```jj duplicate [rev1] [rev2]```

# SYNOPSIS

**jj** **duplicate** [_revisions_...]

# DESCRIPTION

**jj duplicate** 创建修订的副本。复制出的提交内容完全相同，但拥有新的变更 ID。适合用于创建变体，或在修改前保留提交。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-new](/man/jj-new)(1)
