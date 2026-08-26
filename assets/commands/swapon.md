# TAGLINE

启用交换设备和交换文件

# TLDR

显示**交换空间信息**

```swapon```

**启用**某个交换分区

```sudo swapon /path/to/swapfile```

启用 /etc/fstab 中的**所有**交换分区

```sudo swapon -a```

按**标签**启用交换空间

```sudo swapon -L swap_label```

按 **UUID** 启用交换空间

```sudo swapon -U uuid```

显示交换空间**摘要**

```swapon -s```

# SYNOPSIS

**swapon** [_options_] [_specialfile_...]

# DESCRIPTION

**swapon** 启用用于分页和交换的设备和文件。交换空间可以通过设备路径、标签（-L）或 UUID（-U）指定。该命令通常在系统启动时调用，以便将分页活动分散到多个存储资源上。

# PARAMETERS

**-a, --all**
> 启用 /etc/fstab 中标记的所有交换设备

**-d, --discard[=policy]**
> 启用 trim/discard 操作；策略可以是 'once' 或 'pages'

**-e, --ifexists**
> 静默跳过不存在的设备

**-f, --fixpgsz**
> 当页面大小与内核不匹配时重新初始化交换空间

**-L label**
> 使用具有指定标签的交换分区

**-U uuid**
> 使用具有指定 UUID 的交换分区

**-p, --priority priority**
> 设置交换优先级（-1 到 32767，数值越高越优先使用）

**-s, --summary**
> 显示交换空间使用摘要（已废弃，请改用 --show）

**--show[=column...]**
> 显示可自定义的交换区域表格

**-T, --fstab path**
> 使用替代的 fstab 文件

**-v, --verbose**
> 启用详细输出

# CAVEATS

优先级较高的交换区域会被优先使用。当多个区域的优先级相同时，会以轮转方式使用它们。discard 选项可以提升 SSD 性能，但可能造成延迟。

# HISTORY

**swapon** 是 **util-linux** 软件包的一部分。交换空间管理一直是类 Unix 系统管理虚拟内存的核心组成部分。

# INSTALL

```apt: sudo apt install mount```

```apk: sudo apk add util-linux-misc```

```nix: nix profile install nixpkgs#mount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[swapoff](/man/swapoff)(8), [mkswap](/man/mkswap)(8), [fstab](/man/fstab)(5), [free](/man/free)(1)
