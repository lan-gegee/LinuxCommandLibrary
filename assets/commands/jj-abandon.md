# TAGLINE

废弃 Jujutsu 中的修订

# TLDR

废弃当前工作副本变更

```jj abandon```

废弃特定修订

```jj abandon [revision]```

一次废弃多个修订

```jj abandon [rev1] [rev2]```

废弃一个 revset（如 main 的全部后代）

```jj abandon "descendants(main)"```

废弃但不变基后代

```jj abandon --restore-descendants [revision]```

废弃并将书签保留在父修订上

```jj abandon --retain-bookmarks [revision]```

# SYNOPSIS

**jj** **abandon** [_options_] [_revsets_...]

# PARAMETERS

_revsets_
> 要废弃的一个或多个 revset。省略时默认为工作副本提交（`@`）。

**--restore-descendants**
> 不改写被废弃提交的后代。它们的父指针保持不变，内容也得以保留。

**--retain-bookmarks**
> 将指向被废弃提交的书签移动到父修订上，而不是删除它们。

# DESCRIPTION

**jj abandon** 在 Jujutsu 中将修订标记为已废弃。被废弃的提交会从默认日志输出中隐藏，其后代通常会被变基到被废弃提交的父修订上，以保持可见历史呈线性。变更 ID 会保留到垃圾回收之前，因此被废弃的工作仍可通过 `jj op log` 和 `jj op restore` 找回。

如果工作副本提交被废弃，Jujutsu 会自动在其父修订上创建一个新的空工作副本提交，工作区永远不会处于没有当前变更的状态。

# CAVEATS

废弃不会立即删除提交。它们在垃圾回收之前仍可通过操作日志访问到。使用 **--restore-descendants** 时，后代会保留其原始树，但其父链接不会被更新为跳过被废弃的提交，这可能产生重复内容。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-squash](/man/jj-squash)(1), [jj-git-push](/man/jj-git-push)(1)
