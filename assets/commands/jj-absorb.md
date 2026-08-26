# TAGLINE

自动将改动移入合适的祖先提交

# TLDR

将工作副本的改动吸收进祖先提交

```jj absorb```

仅吸收特定文件路径的改动

```jj absorb [file1] [file2]```

从特定源修订吸收

```jj absorb --from [revision]```

吸收进一组特定的目标修订

```jj absorb --into [revset]```

# SYNOPSIS

**jj** **absorb** [_options_] [_filesets_...]

# PARAMETERS

**-f**, **--from** _REVSET_
> 吸收来源修订（默认：@）。

**-t**, **--into** _REVSETS_
> 吸收目标修订（默认：mutable()）。仅考虑源修订的祖先。

**-R**, **--repository** _PATH_
> 要操作的仓库路径。

**--ignore-working-copy**
> 不对工作副本做快照或更新。

**--ignore-immutable**
> 允许改写不可变提交。

# DESCRIPTION

**jj absorb** 将源修订中的改动拆分，并把每处改动移动到对应行最后一次修改所在的最近可变祖先中。这适合在不手动变基的情况下修正一系列提交。

如果某处改动无法明确判定目标修订，该改动会留在源修订中。当所有改动都被吸收且源修订没有描述时，它会被废弃。

absorb 所做的修改可以通过 `jj op show -p` 审查。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-squash](/man/jj-squash)(1), [git-absorb](/man/git-absorb)(1)
