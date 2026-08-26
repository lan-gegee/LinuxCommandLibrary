# TAGLINE

在 Jujutsu 中将提交移动到新的基点

# TLDR

将当前变更变基到目标位置

```jj rebase -d [destination]```

变基特定修订

```jj rebase -r [revision] -d [destination]```

将当前分支变基到 main 上

```jj rebase -b @ -d main```

在目标之后插入修订

```jj rebase -r [revision] -A [destination]```

# SYNOPSIS

**jj** **rebase** [_options_]

# PARAMETERS

**-r**, **--revisions** _rev_
> 仅变基指定的修订，通过将其后代变基到它们的父修订来填补空缺。

**-s**, **--source** _rev_
> 将该修订及其所有后代作为一个子树进行变基。

**-b**, **--branch** _rev_
> 变基整个分支，包括与目标不共享的祖先。

**-d**, **--destination** _rev_
> 变基的目标位置。

**-A**, **--insert-after** _rev_
> 在目标之后插入被变基的修订，并将目标的后代变基到它们之上。

**-B**, **--insert-before** _rev_
> 通过变基到目标的父修订，将被变基的修订插入到目标之前。

# DESCRIPTION

**jj rebase** 在 Jujutsu 中将提交移动到新的基点。如果未指定 **-b**、**-s** 或 **-r** 中的任何一个，默认为 **-b @**（变基当前分支）。冲突会被记录在提交中，可稍后解决。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-squash](/man/jj-squash)(1)
