# TAGLINE

通过二分查找提交历史，定位引入问题的提交

# TLDR

开始 bisect 会话

```jj bisect start```

将当前修订标记为好（good）

```jj bisect good```

将当前修订标记为坏（bad）

```jj bisect bad```

重置 bisect 会话

```jj bisect reset```

# SYNOPSIS

**jj** **bisect** _subcommand_ [_options_]

# PARAMETERS

**start**
> 开始 bisect 会话。

**good** [_revision_]
> 将修订标记为好。

**bad** [_revision_]
> 将修订标记为坏。

**reset**
> 结束 bisect 会话。

**skip**
> 跳过当前修订。

# DESCRIPTION

**jj bisect** 通过二分查找提交历史来定位引入 bug 的提交。通过将提交标记为好或坏来缩小问题改动的范围。类似于 git bisect，但与 Jujutsu 的修订模型集成在一起。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-log](/man/jj-log)(1)
