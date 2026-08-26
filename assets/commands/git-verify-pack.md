# TAGLINE

校验 Git 打包归档文件

# TLDR

**校验**一个 pack 索引文件

```git verify-pack .git/objects/pack/pack-hash.idx```

校验并**列出包内所有对象**

```git verify-pack -v .git/objects/pack/pack-hash.idx```

只显示 **delta 链统计信息**而不进行校验

```git verify-pack -s .git/objects/pack/pack-hash.idx```

# SYNOPSIS

**git** **verify-pack** [**-v** | **--verbose**] [**-s** | **--stat-only**] [**--**] _pack_.idx...

# PARAMETERS

**-v**, **--verbose**
> 校验 pack 后，显示包中包含的对象列表以及 delta 链长度的直方图

**-s**, **--stat-only**
> 不校验 pack 内容；只显示 delta 链长度的直方图。配合 **--verbose** 时还会显示对象列表

**--**
> 不再把后续参数解释为选项

# DESCRIPTION

**git verify-pack** 读取每个给定的 idx 文件并校验对应的 pack 文件及其索引。它会报告发现的任何损坏或不一致。

使用 **-v** 时，对于非 delta 化的对象会显示：对象名、类型、大小、在 pack 文件中的大小、在 pack 文件中的偏移量。对于 delta 化的对象还会额外显示：深度和基础对象名。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-repack](/man/git-repack)(1), [git-fsck](/man/git-fsck)(1)
