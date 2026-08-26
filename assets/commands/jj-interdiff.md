# TAGLINE

显示两个修订所引入改动之间的差异

# TLDR

显示两个修订改动之间的差异

```jj interdiff --from [rev1] --to [rev2]```

带上下文显示 interdiff

```jj interdiff --from [rev1] --to [rev2] --context [5]```

# SYNOPSIS

**jj** **interdiff** [_options_]

# PARAMETERS

**--from** _revision_
> 第一个要比较的修订。

**--to** _revision_
> 第二个要比较的修订。

**--context** _lines_
> 上下文行数。

# DESCRIPTION

**jj interdiff** 显示两个修订各自引入的改动之间的差异。普通 diff 比较的是文件内容，而 interdiff 比较的是每个修订相对于其父修订所做的更改。适合比较同一改动的不同实现方式。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-diff](/man/jj-diff)(1)
