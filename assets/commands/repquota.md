# TAGLINE

报告文件系统磁盘配额使用情况

# TLDR

**报告**所有已启用配额的统计信息

```sudo repquota -a```

**报告**所有用户的配额统计，即使未使用任何配额的用户也包括在内

```sudo repquota -v [filesystem]```

仅**报告**用户配额

```repquota -u [filesystem]```

仅**报告**组配额

```sudo repquota -g [filesystem]```

以人类可读格式**报告**已用配额和限制

```sudo repquota -s [filesystem]```

以人类可读格式**报告**用户和组的所有配额

```sudo repquota -augs```

# SYNOPSIS

**repquota** [_options_] [_filesystem_...]

# PARAMETERS

**-a, --all**
> 报告所有启用了配额的文件系统

**-u, --user**
> 报告用户配额（默认）

**-g, --group**
> 报告组配额

**-v, --verbose**
> 包含未使用存储的用户/组

**-s, --human-readable**
> 以人类可读格式显示大小（KB、MB、GB）

**-p, --raw-grace**
> 以自纪元起的秒数报告宽限期

**-n, --no-names**
> 显示数字 UID/GID 而不是名称

**-c, --batch-translation**
> 缓存名称查找以提高性能

# DESCRIPTION

**repquota** 显示指定文件系统的磁盘配额摘要。它展示用户和/或组的当前用量、软限制、硬限制以及宽限期状态。

输出包含已用空间、软/硬限制、已用文件数（inode）以及用户是否超出配额等列。宽限期表示用户可以在软限制之上继续使用多长时间。

# CAVEATS

需要文件系统支持配额并安装 quota 工具。通常必须以 root 运行才能查看所有用户的配额。必须在文件系统上启用配额才能得到有意义的输出。

# INSTALL

```apt: sudo apt install quota```

```dnf: sudo dnf install quota```

```pacman: sudo pacman -S quota-tools```

```apk: sudo apk add quota-tools```

```zypper: sudo zypper install quota```

```nix: nix profile install nixpkgs#quota```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[quota](/man/quota)(1), [quotacheck](/man/quotacheck)(8), [quotaon](/man/quotaon)(8), [edquota](/man/edquota)(8), [setquota](/man/setquota)(8)
