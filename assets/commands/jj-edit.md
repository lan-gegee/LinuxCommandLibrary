# TAGLINE

将工作副本设置为特定修订以进行编辑

# TLDR

编辑特定修订

```jj edit [revision]```

编辑当前修订的父修订

```jj edit @-```

# SYNOPSIS

**jj** **edit** _revision_

# DESCRIPTION

**jj edit** 将工作副本设置为特定修订以便编辑。工作副本会成为指定修订的子修订，从而可以修改它。改动会自动记录到正在编辑的修订中。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-new](/man/jj-new)(1), [jj-squash](/man/jj-squash)(1)
