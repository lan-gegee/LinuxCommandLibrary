# TAGLINE

创建一个撤销指定修订改动的新提交

# TLDR

撤销某修订的改动

```jj revert -r [revision]```

撤销多个修订

```jj revert -r [rev1] -r [rev2]```

# SYNOPSIS

**jj** **revert** [_options_]

# PARAMETERS

**-r**, **--revision** _rev_
> 要撤销的修订。

# DESCRIPTION

**jj revert** 创建一个撤销指定修订改动的新提交。原始提交仍保留在历史中。与 restore 不同，revert 通过创建新提交来反转改动。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-restore](/man/jj-restore)(1), [jj-undo](/man/jj-undo)(1)
