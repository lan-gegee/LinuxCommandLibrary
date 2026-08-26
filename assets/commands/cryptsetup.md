# TAGLINE

dm-crypt 和 LUKS 加密卷管理器

# TLDR

初始化 **LUKS** 卷

```cryptsetup luksFormat /dev/sda1```

**打开** LUKS 卷

```cryptsetup open /dev/sda1 mapping_name```

显示映射**状态**

```cryptsetup status mapping_name```

**关闭**映射

```cryptsetup close mapping_name```

**修改**密码短语

```cryptsetup luksChangeKey /dev/sda1```

# SYNOPSIS

**cryptsetup** _action_ [_OPTIONS_] _device_ [_name_]

# DESCRIPTION

**cryptsetup** 管理 dm-crypt 和 LUKS（Linux 统一密钥设置）加密卷。它为静态数据提供磁盘加密保护，支持多个密钥槽、强加密算法以及头的备份/恢复。

# PARAMETERS

**luksFormat** _device_
> 初始化 LUKS 加密卷（会销毁所有数据）

**open** _device_ _name_
> 打开加密设备并在 /dev/mapper/name 创建映射

**close** _name_
> 移除已有的映射

**status** _name_
> 显示活动映射的信息

**luksChangeKey** _device_
> 更改 LUKS 卷的密码短语

**luksAddKey** _device_
> 向密钥槽添加新的密码短语

**luksRemoveKey** _device_
> 从密钥槽移除密码短语

**luksDump** _device_
> 显示 LUKS 头信息

**luksHeaderBackup** _device_
> 将 LUKS 头备份到文件

**isLuks** _device_
> 检查设备是否为 LUKS 卷

**benchmark**
> 对加密算法进行基准测试

**--type** _type_
> 指定加密类型（luks、luks2、plain）

**--cipher** _cipher_
> 加密算法规范

**--key-size** _bits_
> 加密密钥长度（位）

**--hash** _hash_
> LUKS 头所用的哈希算法

# CONFIGURATION

**/etc/crypttab**
> 定义启动时需要解锁的加密卷。

# CAVEATS

丢失全部密码短语意味着数据永久丢失。务必始终备份 LUKS 头。格式化会销毁所有已有数据。加密设备必须先打开才能挂载。

# HISTORY

**cryptsetup** 由 **Jana Saout**（dm-crypt）和 **Clemens Fruhwirth**（LUKS）创建。LUKS 于 **2004** 年推出，旨在为加密卷提供标准的磁盘格式。LUKS2 于 2017 年加入，改进了头部的灵活性并引入 Argon2 密钥派生。

# INSTALL

```apt: sudo apt install cryptsetup-bin```

```dnf: sudo dnf install cryptsetup```

```pacman: sudo pacman -S cryptsetup```

```apk: sudo apk add cryptsetup```

```zypper: sudo zypper install cryptsetup```

```nix: nix profile install nixpkgs#cryptsetup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmsetup](/man/dmsetup)(8), [losetup](/man/losetup)(8), [mkfs](/man/mkfs)(8)
