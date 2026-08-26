# TAGLINE

收集 LVM2 子系统的诊断信息用于故障排查

# TLDR

收集**标准的 LVM 诊断转储**（tarball）

```lvmdump```

包含**高级**数据（元数据、锁、守护进程信息）

```lvmdump -a -l -m```

将转储文件写入**目录**（而非 tarball）

```lvmdump -d [path/to/directory]```

显示**帮助**

```lvmdump -h```

# SYNOPSIS

**lvmdump** [_options_]

# PARAMETERS

**-a**
> 包含高级诊断信息

**-l**
> 包含 lvmetad 缓存状态（如果正在运行）

**-m**
> 包含来自所有卷组的 LVM 元数据

**-d _directory_**
> 输出到目录而非压缩 tarball

**-h**
> 显示帮助信息

# DESCRIPTION

**lvmdump** 收集 LVM2（逻辑卷管理器）子系统的诊断信息，用于故障排查。默认情况下，它会在主目录中创建一个压缩的 tar 归档，其中包含系统信息、LVM 配置和状态数据。

转储内容包括 **pvs**、**vgs**、**lvs** 等命令的输出、配置文件、dmsetup 信息以及相关的系统信息。配合 **-m** 标志使用时，还会捕获所有卷组的原始元数据。

该工具主要用于向开发者或支持团队报告 LVM 问题时提供诊断所需的全部上下文。

# CAVEATS

转储可能包含有关存储配置的敏感信息。对外分享前请先检查内容。**-m** 选项会生成包含卷组元数据的较大转储。需要 root 权限。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2-extra```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [pvs](/man/pvs)(8), [vgs](/man/vgs)(8), [lvs](/man/lvs)(8), [dmsetup](/man/dmsetup)(8)
