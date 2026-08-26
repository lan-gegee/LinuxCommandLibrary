# TAGLINE

ZFS 存储池调试与诊断工具

# TLDR

**显示存储池配置**

```sudo zdb -C [pool]```

**显示详细的 vdev 信息**

```sudo zdb -l [/dev/disk]```

**转储存储池元数据**

```sudo zdb -d [pool]```

**显示对象集内容**

```sudo zdb -dd [pool/dataset]```

**检查存储池完整性而不修改数据**

```sudo zdb -c [pool]```

**显示块统计信息**

```sudo zdb -b [pool]```

# SYNOPSIS

**zdb** [**-AbcdDFGhiLMPsvXY**] [**-e** [**-V**] [**-p** _path_]...] [**-I** _inflight_] [**-x** _dumpdir_] [**-t** _txg_] [**-U** _cache_] [**-K** _key_] [_poolname_|_dataset_|_objset_...]

# PARAMETERS

**-b**
> 显示块分配统计信息

**-c**
> 校验存储池完整性（对全部数据做校验和）

**-C**
> 从缓存文件显示存储池配置

**-d**
> 转储指定数据集的元数据

**-D**
> 显示去重统计信息

**-e**
> 操作已导出的存储池（用 -p 指定设备）

**-l**
> 读取并显示 vdev 标签内容

**-L**
> 禁用泄漏跟踪

**-m**
> 显示 metaslab 信息

**-p** _path_
> vdev 的路径（与 -e 搭配使用）

**-R**
> 读取并显示原始数据

**-s**
> 显示空间映射直方图

**-v**
> 详细输出

# DESCRIPTION

**zdb** 是 ZFS 调试器，用于显示 ZFS 存储池、数据集和 vdev 的详细内部信息。它主要面向 ZFS 管理员和开发者的诊断与调试。

该工具可以检查存储池结构、显示块分配图、校验数据校验和，以及转储原始 ZFS 元数据。它以只读方式运行，不会修改存储池数据。

常见用途包括诊断存储池损坏、在磁盘故障后查看 vdev 标签，以及理解 ZFS 内部机制。

# CAVEATS

zdb 需要 root 权限才能访问原始磁盘设备和 ZFS 内部结构。

这是一个面向专家的调试工具。误读输出可能导致对存储池健康状况的错误结论。

随着内部结构的演进，输出格式可能随 ZFS 版本而变化。

常规的存储池诊断请改用 **zpool status**。

# INSTALL

```apt: sudo apt install zfs-fuse```

```apk: sudo apk add zfs```

```nix: nix profile install nixpkgs#zfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zfs](/man/zfs)(8), [zpool](/man/zpool)(8), [zpool-status](/man/zpool-status)(8)
