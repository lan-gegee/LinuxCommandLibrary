# TAGLINE

检查并修复 btrfs 文件系统完整性

# TLDR

**检查** btrfs 文件系统

```sudo btrfs check [path/to/partition]```

检查并**修复** btrfs 文件系统（危险）

```sudo btrfs check --repair [path/to/partition]```

显示检查的**进度**

```sudo btrfs check -p [path/to/partition]```

校验每个数据块的**校验和**

```sudo btrfs check --check-data-csum [path/to/partition]```

使用指定的**超级块**（0、1 或 2）

```sudo btrfs check -s [n] [path/to/partition]```

**重建**校验和树

```sudo btrfs check --repair --init-csum-tree [path/to/partition]```

**重建** extent 树

```sudo btrfs check --repair --init-extent-tree [path/to/partition]```

# SYNOPSIS

**btrfs check** [_options_] _device_

# DESCRIPTION

**btrfs check** 检查 btrfs 文件系统结构的一致性错误，并可选择性地修复某些类型的损坏。它只能对未挂载的文件系统操作。

检查模式是非破坏性的，只报告问题。修复模式会尝试修复，但若使用不当存在数据丢失风险。

# PARAMETERS

**--repair**
> 尝试修复检测到的错误（危险，请先备份）

**-p, --progress**
> 在检查过程中显示进度

**--check-data-csum**
> 校验数据块的校验和

**-s, --super** _num_
> 使用指定的超级块副本（0、1 或 2）

**--init-csum-tree**
> 从头重建校验和树

**--init-extent-tree**
> 从头重建 extent 树

**--readonly**
> 以只读模式运行（默认）

# CAVEATS

文件系统必须处于卸载状态。修复操作很危险，可能导致数据丢失；务必先备份。对已挂载的文件系统运行检查可能报告虚假错误。树重建操作是最后的补救手段。

# INSTALL

```apt: sudo apt install btrfs-progs```

```dnf: sudo dnf install btrfs-progs```

```pacman: sudo pacman -S btrfs-progs```

```apk: sudo apk add btrfs-progs```

```brew: brew install btrfs-progs```

```nix: nix profile install nixpkgs#btrfs-progs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[btrfs](/man/btrfs)(8), [btrfs-rescue](/man/btrfs-rescue)(8), [btrfs-restore](/man/btrfs-restore)(8)

# RESOURCES

```[Source code](https://github.com/kdave/btrfs-progs)```

```[Documentation](https://btrfs.readthedocs.io/)```

<!-- verified: 2026-06-22 -->
