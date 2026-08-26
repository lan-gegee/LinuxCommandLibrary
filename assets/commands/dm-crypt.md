# TAGLINE

Linux 磁盘加密子系统

# TLDR

**创建 LUKS 加密卷**

```sudo cryptsetup luksFormat [/dev/sdX]```

**打开 LUKS 卷**

```sudo cryptsetup open [/dev/sdX] [name]```

**关闭加密卷**

```sudo cryptsetup close [name]```

**显示 LUKS 头信息**

```sudo cryptsetup luksDump [/dev/sdX]```

**向 LUKS 卷添加新密钥**

```sudo cryptsetup luksAddKey [/dev/sdX]```

**创建 plain dm-crypt 卷**

```sudo cryptsetup open --type plain [/dev/sdX] [name]```

**测试加密算法性能**

```cryptsetup benchmark```

# SYNOPSIS

**cryptsetup** _action_ [_options_] _device_ [_name_]

# PARAMETERS

**luksFormat** _device_
> 初始化 LUKS 分区。

**open** _device_ _name_
> 打开并映射加密设备。

**close** _name_
> 关闭已映射的设备。

**luksDump** _device_
> 显示 LUKS 头信息。

**luksAddKey** _device_
> 添加新的口令/密钥文件。

**luksRemoveKey** _device_
> 移除一个口令。

**luksHeaderBackup** _device_
> 备份 LUKS 头。

**luksHeaderRestore** _device_
> 恢复 LUKS 头。

**--type** _type_
> 加密类型：luks、luks2、plain。

**--cipher** _cipher_
> 加密算法（aes-xts-plain64）。

**--key-size** _bits_
> 密钥长度（位）。

**--hash** _hash_
> 用于密钥派生的哈希函数。

**--key-file** _file_
> 使用密钥文件代替口令。

# DESCRIPTION

**dm-crypt** 是 Linux 内核的 device-mapper 加密目标，提供透明磁盘加密。**cryptsetup** 是配置 dm-crypt 的用户空间工具，通常使用 LUKS（Linux Unified Key Setup）格式。

LUKS 提供标准化的磁盘格式，带有多个密钥槽，允许设置多个口令或密钥文件。它将加密元数据存储在头部中，无需重新加密数据即可管理密钥。

Plain dm-crypt 提供无头部的加密方式，可实现合理否认性（plausible deniability），但必须记住确切的参数。两种模式都会在 /dev/mapper/ 中创建映射设备，可像普通文件系统一样操作。

# USAGE WORKFLOW

```bash
# Create encrypted partition
sudo cryptsetup luksFormat /dev/sdb1

# Open and map
sudo cryptsetup open /dev/sdb1 encrypted_data

# Create filesystem
sudo mkfs.ext4 /dev/mapper/encrypted_data

# Mount and use
sudo mount /dev/mapper/encrypted_data /mnt
```

# CAVEATS

LUKS 头损坏可能导致数据无法恢复；务必备份头部。加密有 CPU 开销（AES-NI 可显著缓解）。SSD 可能需要特殊的 TRIM 处理。忘记口令意味着数据永久丢失。

# HISTORY

dm-crypt 于内核 **2.6** 版本（2004 年）合入 Linux 内核。**LUKS** 由 **Clemens Fruhwirth** 于 **2004 年**设计，旨在标准化 Linux 磁盘加密。**2017 年**发布的 LUKS2 引入了现代密钥派生（Argon2）、认证加密和更大的元数据区域。

# SEE ALSO

[cryptsetup](/man/cryptsetup)(8), [crypttab](/man/crypttab)(5)
