# TAGLINE

打开 diff 编辑器，以交互方式修改修订中的改动

# TLDR

在 diff 编辑器中编辑修订

```jj diffedit```

编辑特定修订

```jj diffedit -r [revision]```

编辑修订之间的区间

```jj diffedit --from [rev1] --to [rev2]```

# SYNOPSIS

**jj** **diffedit** [_options_]

# PARAMETERS

**-r**, **--revision** _rev_
> 要编辑的修订。

**--from** _rev_
> 用于比较的基准修订。

**--to** _rev_
> 要修改的目标修订。

# DESCRIPTION

**jj diffedit** 打开一个 diff 编辑器，以交互方式修改修订中的改动。允许在提交中添加、移除或修改代码块（hunk）。编辑器会显示 diff，并将修改保存回该修订。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-diff](/man/jj-diff)(1), [jj-split](/man/jj-split)(1)
