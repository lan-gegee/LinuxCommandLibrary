# TAGLINE

从另一个修订恢复文件内容

# TLDR

从父修订恢复文件

```jj restore```

恢复特定文件

```jj restore [file1] [file2]```

从特定修订恢复

```jj restore --from [revision]```

恢复到特定修订

```jj restore --to [revision] --from [source]```

恢复匹配某个 revset 的文件

```jj restore -c [revision] [path]```

恢复并将改动保留为新提交

```jj restore --changes-in [revision]```

# SYNOPSIS

**jj** **restore** [_options_] [_paths_...]

# PARAMETERS

**--from** _revision_
> 内容来源修订。

**--to** _revision_
> 要修改的目标修订。

# DESCRIPTION

**jj restore** 从另一个修订恢复文件内容。默认从父修订恢复，相当于丢弃改动。可以恢复特定文件或整个工作副本。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-revert](/man/jj-revert)(1)
