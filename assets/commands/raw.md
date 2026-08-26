# TAGLINE

将原始字符设备绑定到块设备

# TLDR

**将**原始字符设备**绑定到**块设备

```raw /dev/raw/raw1 /dev/block_device```

**查询**已有的绑定

```raw /dev/raw/raw1```

**查询所有**已绑定的原始设备

```raw -qa```

# SYNOPSIS

**raw** _/dev/raw/rawN_ _major_ _minor_

**raw** _/dev/raw/rawN_ _/dev/blockdev_

**raw** **-q** [**-a**] [_rawN_]

# PARAMETERS

**/dev/raw/raw**_N_
> 要绑定或查询的原始设备节点

**-q**, **--query**
> 查询指定原始设备的绑定

**-a**, **--all**
> 查询所有原始设备（配合 -q）

_major_ _minor_
> 通过主/次设备号指定的块设备

_/dev/blockdev_
> 要绑定到原始设备的块设备路径

# DESCRIPTION

**raw** 将 Linux 原始字符设备绑定到块设备，允许对底层存储进行直接（无缓冲）I/O 访问。原始设备绕过内核的缓冲区缓存，为自行管理缓存的应用程序（如数据库）提供对块设备的直接访问。

将原始设备绑定到块设备后，对原始设备的读写会以同步、直接 I/O 的方式访问底层存储，而不经过内核缓冲。

# CAVEATS

原始设备在很大程度上已被**弃用**，取而代之的是普通文件 I/O 上的 O_DIRECT 标志。需要先加载 raw 驱动（modprobe raw）。绑定前原始设备节点必须已存在于 /dev/raw/ 中。只有 root 才能绑定原始设备。

# HISTORY

原始设备在 **Linux 2.4** 中引入，用于支持 Oracle 等需要无缓冲 I/O 的数据库。后续内核加入的 O_DIRECT 标志提供了类似功能而无需专用原始设备，使该接口基本过时。

# SEE ALSO

[losetup](/man/losetup)(8), [dd](/man/dd)(1), [blockdev](/man/blockdev)(8)
