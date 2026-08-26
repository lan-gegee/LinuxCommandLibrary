# TAGLINE

设置并控制将普通文件呈现为块设备的回环设备

# TLDR

**列出**所有回环设备

```losetup -a```

将文件**挂接**到回环设备

```sudo losetup /dev/loop0 /path/to/file```

挂接到**空闲**设备并扫描分区

```sudo losetup --show -P -f /path/to/file```

以**只读**方式挂接

```sudo losetup -r /dev/loop0 /path/to/file```

**卸下**所有回环设备

```sudo losetup -D```

**卸下**指定回环设备

```sudo losetup -d /dev/loop0```

# SYNOPSIS

**losetup** [_OPTIONS_] [_loopdev_] [_file_]

# DESCRIPTION

**losetup** 用于设置和控制回环设备（loop device），使普通文件可以像块设备一样被访问。常用于挂载磁盘镜像、ISO 文件或加密容器。

# PARAMETERS

**-a, --all**
> 显示所有已挂接回环设备的状态。

**-f, --find**
> 查找第一个未使用的回环设备。不带其他参数时打印其名称；给定后备文件时将该文件挂接到该设备。

**-P, --partscan**
> 强制内核扫描新建回环设备上的分区表。

**-r, --read-only**
> 设置只读回环设备。

**-d, --detach** _loopdev_
> 卸下指定的回环设备。

**-D, --detach-all**
> 卸下当前所有已挂接的回环设备。

**-j, --associated** _file_
> 显示与 _file_ 关联的回环设备。

**--show**
> 打印分配到的设备名（与 **-f** 搭配使用很有用）。

**-o, --offset** _bytes_
> 从后备文件的 _bytes_ 偏移处开始建立回环设备。

**--sizelimit** _bytes_
> 将回环设备的大小限制为从偏移处起的 _bytes_ 字节。

**-b, --sector-size** _bytes_
> 设置逻辑扇区大小（512、1024、2048 或 4096）。

**--direct-io**[=**on**|**off**]
> 启用或禁用内核对后备文件的直接 I/O。

**-c, --set-capacity** _loopdev_
> 强制内核重新读取后备文件的大小。

**-L, --nooverlap**
> 若已有回环设备覆盖后备文件的相同字节范围则失败。

**-O, --output** _columns_
> 指定要打印的列（可用 `--list --output list` 查看可用列）。

**-l, --list**
> 使用类似 `losetup -a` 的列表格式，但包含更多列。

**-J, --json**
> 以 JSON 输出（配合 --list 使用）。

**--help**
> 显示帮助信息。

# CAVEATS

创建和卸下回环设备需要 root 权限。内核可用的回环设备数量有限（可配置）。使用完毕后务必卸下回环设备以释放资源。

# HISTORY

**losetup** 属于 **util-linux** 软件包，负责 Linux 系统上的回环设备管理。

# INSTALL

```apt: sudo apt install mount```

```apk: sudo apk add losetup```

```nix: nix profile install nixpkgs#mount```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mount](/man/mount)(8), [cryptsetup](/man/cryptsetup)(8), [dd](/man/dd)(1)
