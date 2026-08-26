# TAGLINE

显示内核 slab 缓存信息

# TLDR

启动 **slabtop**

```sudo slabtop```

按**缓存大小**排序

```sudo slabtop -s c```

按**对象数量**排序

```sudo slabtop -s o```

按**对象大小**排序

```sudo slabtop -s s```

显示一次后**退出**

```sudo slabtop -o```

将**刷新间隔**设为 5 秒

```sudo slabtop -d 5```

# SYNOPSIS

**slabtop** [_-d delay_] [_-s sortcriteria_] [_-o_]

# DESCRIPTION

**slabtop** 实时显示详细的内核 slab 缓存信息。它按指定排序条件列出排名靠前的缓存，帮助监控内核内存分配。

# PARAMETERS

**-d, --delay=N**
> 每 N 秒刷新一次显示（默认：3）

**-s, --sort=S**
> 按指定的排序条件排列输出

**-o, --once**
> 显示一次输出后退出

**-V, --version**
> 显示版本并退出

**-h, --help**
> 显示用法帮助并退出

# SORT CRITERIA

**a**: 活跃对象数（ACTIVE）
**b**: 每个 slab 的对象数（OBJ/SLAB）
**c**: 缓存大小（CACHE SIZE）
**l**: slab 数量（SLABS）
**o**: 对象数量（OBJS）- 默认
**s**: 对象大小（OBJ SIZE）
**u**: 缓存利用率（USE）

# INTERACTIVE COMMANDS

**Space**: 立即刷新显示
**q**: 退出程序
**s**: 更改排序列

# CAVEATS

读取内核 slab 缓存信息需要 root 权限。排序条件可在运行时通过对应的字母键更改。

# HISTORY

**slabtop** 是 **procps-ng** 软件包的一部分。它提供了洞察内核 slab 分配器的途径，该分配器管理着频繁使用的内核对象的内存。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[top](/man/top)(1), [vmstat](/man/vmstat)(8), [free](/man/free)(1), [ps](/man/ps)(1)
