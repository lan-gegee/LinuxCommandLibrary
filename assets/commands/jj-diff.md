# TAGLINE

显示 Jujutsu 中修订之间的差异

# TLDR

显示工作副本差异

```jj diff```

查看特定修订的差异

```jj diff -r [revision]```

比较修订之间的差异

```jj diff --from [rev1] --to [rev2]```

查看特定文件的差异

```jj diff [file]```

# SYNOPSIS

**jj** **diff** [_options_] [_paths_...]

# PARAMETERS

**-r**, **--revision** _rev_
> 显示修订中的改动。

**--from** _rev_
> 比较的起始修订。

**--to** _rev_
> 比较的结束修订。

**-s**, **--summary**
> 仅显示摘要。

**--stat**
> 显示 diffstat。

# DESCRIPTION

**jj diff** 显示 Jujutsu 中修订之间的差异。默认显示工作副本的改动。使用 **-r** 查看特定修订，或使用 **--from/--to** 进行区间比较。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-status](/man/jj-status)(1)
