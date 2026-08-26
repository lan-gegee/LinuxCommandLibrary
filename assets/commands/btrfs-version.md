# TAGLINE

显示 btrfs-progs 版本信息

# TLDR

显示 **btrfs-progs 版本**

```btrfs version```

显示该子命令的**帮助**

```btrfs version --help```

等效的**全局标志**

```btrfs --version```

# SYNOPSIS

**btrfs** **version**

# DESCRIPTION

**btrfs version** 打印提供 `btrfs` 命令的用户态 **btrfs-progs** 软件包的版本。内核模块版本是独立的，可通过 `/sys/module/btrfs/version` 或 `modinfo btrfs` 查看。

该输出在报告 bug、对照变更日志比较功能特性，或在脚本中进行功能探测时很有用。较新的发行版（6.x）还通过 `mkfs.btrfs --version`、`btrfs-convert --version` 以及类似的各工具专属标志暴露内置功能。

# CAVEATS

只报告用户态工具版本，而非运行中内核的 btrfs 实现。用户态与内核版本不一致是受支持的，但某些磁盘格式特性可能不可用。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8)
