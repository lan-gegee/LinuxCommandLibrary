# TAGLINE

从 Nix store 中移除无引用的 store 路径

# TLDR

**执行垃圾回收**

```nix-collect-garbage```

**删除旧世代**

```nix-collect-garbage -d```

**删除早于指定天数的世代**

```nix-collect-garbage --delete-older-than [30d]```

**试运行**

```nix-collect-garbage --dry-run```

# SYNOPSIS

**nix-collect-garbage** [_options_]

# PARAMETERS

**-d**, **--delete-old**
> 删除旧的 profile 世代。

**--delete-older-than** _period_
> 删除早于该时段的世代。

**--dry-run**
> 显示将要删除的内容。

**--max-freed** _bytes_
> 释放到指定字节数后停止。

# DESCRIPTION

**nix-collect-garbage** 会从 Nix store 中移除没有任何引用的 store 路径，通过删除未关联任何 profile 或垃圾回收根的软件包来释放磁盘空间。

# INSTALL

```apt: sudo apt install nix-bin```

```dnf: sudo dnf install nix```

```pacman: sudo pacman -S nix```

```apk: sudo apk add nix```

```zypper: sudo zypper install nix```

```nix: nix profile install nixpkgs#nix```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix-store](/man/nix-store)(1), [nix-env](/man/nix-env)(1)
