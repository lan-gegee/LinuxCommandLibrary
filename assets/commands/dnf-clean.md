# TAGLINE

清除缓存的 DNF 软件仓库数据

# TLDR

清除**缓存文件**

```dnf clean dbcache```

将元数据标记为**过期**

```dnf clean expire-cache```

清除**软件仓库元数据**

```dnf clean metadata```

清除**缓存的软件包**

```dnf clean packages```

清理**全部** DNF 缓存

```dnf clean all```

# SYNOPSIS

**dnf clean** _type_

# DESCRIPTION

**dnf clean** 清除 DNF 为软件仓库缓存的临时文件，包括元数据、软件包和数据库文件。

可用于释放磁盘空间，或强制 DNF 下次从软件仓库刷新元数据。

# PARAMETERS

**dbcache**
> 清除数据库缓存文件

**expire-cache**
> 将元数据标记为过期

**metadata**
> 清除软件仓库元数据

**packages**
> 清除缓存的软件包

**all**
> 清理全部内容（以上所有）

# CAVEATS

清理缓存后，DNF 在下次使用时必须重新下载元数据。缓存的软件包位于 /var/cache/dnf。"all" 是最彻底的选项。

# SEE ALSO

[dnf](/man/dnf)(8), [yum](/man/yum)(8)
