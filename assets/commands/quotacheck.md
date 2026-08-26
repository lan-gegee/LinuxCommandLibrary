# TAGLINE

扫描文件系统并生成配额文件

# TLDR

检查**所有**文件系统的配额

```sudo quotacheck --all```

**强制**检查（可能损坏配额文件）

```sudo quotacheck --force [mountpoint]```

以**调试**模式检查

```sudo quotacheck --debug [mountpoint]```

以**详细输出**进行检查

```sudo quotacheck --verbose [mountpoint]```

检查**用户**配额

```sudo quotacheck --user [user] [mountpoint]```

检查**组**配额

```sudo quotacheck --group [group] [mountpoint]```

# SYNOPSIS

**quotacheck** [**-a**] [**-f**] [**-v**] [**-u** _user_] [**-g** _group_] [_mountpoint_]

# PARAMETERS

**-a, --all**
> 检查所有已挂载的非 NFS 文件系统

**-f, --force**
> 即使配额已启用也强制检查

**-v, --verbose**
> 显示进度信息

**-d, --debug**
> 启用调试模式

**-u, --user _user_**
> 仅检查用户配额

**-g, --group _group_**
> 仅检查组配额

**-c**
> 配额文件缺失时创建它们

# DESCRIPTION

**quotacheck** 扫描文件系统的磁盘使用情况，并创建或校验配额文件。它会检查每个文件，以确定每个用户和组占用了多少空间。

在配额启用状态下运行 quotacheck 可能损坏配额文件，因此通常应先关闭配额。该工具会创建 aquota.user 和 aquota.group 文件。

# CAVEATS

最好在关闭配额的状态下运行。强制标志可能导致数据丢失。大型文件系统上可能耗时较长。需要 root 权限。

# HISTORY

**quotacheck** 是 Linux 磁盘配额系统的一部分，源自 BSD Unix 的配额机制。它对初始化和维护磁盘配额执行至关重要。

# INSTALL

```apt: sudo apt install quota```

```dnf: sudo dnf install quota```

```pacman: sudo pacman -S quota-tools```

```apk: sudo apk add quota-tools```

```zypper: sudo zypper install quota```

```nix: nix profile install nixpkgs#quota```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[quota](/man/quota)(1), [quotaon](/man/quotaon)(8), [edquota](/man/edquota)(8), [repquota](/man/repquota)(8)
