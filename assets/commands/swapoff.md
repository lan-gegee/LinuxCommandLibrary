# TAGLINE

禁用交换设备和交换文件

# TLDR

**禁用**某个交换分区

```sudo swapoff /path/to/swapfile```

禁用**所有**交换分区

```sudo swapoff -a```

按**标签**禁用交换空间

```sudo swapoff -L swap_label```

按 **UUID** 禁用交换空间

```sudo swapoff -U uuid```

# SYNOPSIS

**swapoff** [_-va_] [_specialfile_...]

# DESCRIPTION

**swapoff** 禁用在指定设备和文件上的交换。调用 swapoff 时，所有已换出到指定区域的页面会先被换回 RAM，然后才禁用该交换区域。

# PARAMETERS

**-a, --all**
> 禁用 /proc/swaps 中列出的所有交换区域

**-L label**
> 禁用具有指定标签的交换分区

**-U uuid**
> 禁用具有指定 UUID 的交换分区

**-v, --verbose**
> 启用详细输出

**-h, --help**
> 显示帮助文本并退出

**-V, --version**
> 显示版本信息并退出

# CAVEATS

禁用交换需要有足够的 RAM 容纳所有换出的页面。RAM 不足时 swapoff 会失败。在重度使用的交换区域上，这一过程可能耗时较长。

# HISTORY

**swapoff** 是 **util-linux** 软件包的一部分。它是 swapon 的对应工具，用于禁用交换空间。

# INSTALL

```apt: sudo apt install mount```

```apk: sudo apk add util-linux-misc```

```nix: nix profile install nixpkgs#mount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[swapon](/man/swapon)(8), [mkswap](/man/mkswap)(8), [free](/man/free)(1)
