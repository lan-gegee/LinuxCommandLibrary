# TAGLINE

加密块设备配置文件

# TLDR

**查看当前 crypttab**

```cat /etc/crypttab```

**基本的加密分区条目**

```luks_root UUID=[device-uuid] none luks```

**带密钥文件的条目**

```luks_data UUID=[device-uuid] /root/keyfile luks```

**支持 discard/TRIM 的条目**

```luks_ssd UUID=[device-uuid] none luks,discard```

**用于 swap 加密的条目**

```cryptswap /dev/sdX /dev/urandom swap,cipher=aes-xts-plain64,size=256```

# SYNOPSIS

**/etc/crypttab**

# FORMAT

```
name  device  keyfile  options
```

**name**：映射后的设备名（/dev/mapper/name）
**device**：块设备、UUID=xxx 或 PARTUUID=xxx
**keyfile**：密钥路径；"none" 表示提示输入密码
**options**：逗号分隔的挂载选项

# OPTIONS

**luks**
> 设备是 LUKS 加密的（通常可自动检测）。

**plain**
> 普通 dm-crypt（无 LUKS 头）。

**swap**
> 格式化为加密交换空间（会销毁数据）。

**discard**
> 允许 TRIM/discard 命令透传（SSD 优化）。

**noauto**
> 启动时不解锁。

**nofail**
> 设备不可用时不要导致启动失败。

**tries=N**
> 失败前允许的密码尝试次数。

**timeout=N**
> 等待设备的秒数。

**cipher=**_cipher_
> 加密算法（适用于 plain 模式）。

**size=**_bits_
> 密钥长度（位）。

**keyfile-offset=**_bytes_
> 密钥文件中的偏移量。

**keyfile-size=**_bytes_
> 从密钥文件读取的字节数。

# DESCRIPTION

**/etc/crypttab** 定义了要在启动时由 systemd-cryptsetup 或 cryptsetup 解锁的加密块设备。每一行描述一个加密设备：其映射名称、源设备、密钥材料和选项。

该文件与 **/etc/fstab** 配合工作：crypttab 负责解锁加密设备，fstab 随后挂载生成的映射设备。对于 LUKS 设备，除非指定了密钥文件，否则系统会在启动时提示输入密码。

建议使用基于 UUID 的设备标识而不是设备路径，以便在硬件变化时保持可靠。

# EXAMPLE

```
# LUKS root partition, password prompt
luks-root UUID=12345678-1234-1234-1234-123456789abc none luks

# Data partition with keyfile
luks-data UUID=abcdefab-cdef-abcd-efab-cdefabcdefab /root/data.key luks

# SSD with TRIM support
luks-ssd UUID=87654321-4321-4321-4321-210987654321 none luks,discard

# Encrypted swap (random key each boot)
cryptswap /dev/sda2 /dev/urandom swap,cipher=aes-xts-plain64,size=256
```

# CAVEATS

密钥文件应仅限 root 可读，且最好放在已加密的根分区上。**discard** 选项可能泄露文件系统使用情况的信息。使用随机密钥的加密交换空间在重启后会丢失其中的内容。修改 crypttab 后务必仔细测试，避免系统无法启动。

# HISTORY

crypttab 格式起源于 Debian，后来被 systemd 和其他发行版采纳。它的设计目的是将 dm-crypt/LUKS 加密集成到启动流程中。文件格式不断演进，现已支持 LUKS、普通 dm-crypt 以及各种用于密钥管理和性能调优的选项。

# SEE ALSO

[cryptsetup](/man/cryptsetup)(8), [fstab](/man/fstab)(5), [systemd-cryptsetup](/man/systemd-cryptsetup)(8)

# RESOURCES

```[Source code](https://github.com/systemd/systemd)```

```[Documentation](https://www.freedesktop.org/software/systemd/man/crypttab.html)```

<!-- verified: 2026-06-26 -->
