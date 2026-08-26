# TAGLINE

加密交换分区配置

# TLDR

**设置加密交换分区**

```ecryptfs-setup-swap```

**指定**交换分区进行设置

```ecryptfs-setup-swap [/dev/sda2]```

# SYNOPSIS

**ecryptfs-setup-swap** [**-f**|**--force**] [_device_]

# PARAMETERS

_DEVICE_
> 要加密的交换分区。省略时使用所有处于活动状态的交换设备。

**-f**, **--force**
> 即使设备看起来已经加密也照样设置加密交换。

# DESCRIPTION

**ecryptfs-setup-swap** 使用 dm-crypt 和随机密钥配置加密交换空间。这能防止敏感数据在关机后仍可从交换分区中被恢复。

该脚本会修改 /etc/fstab 和 /etc/crypttab，以便在启动时启用加密交换。每次启动都会生成新的随机密钥，因此重启后交换分区中的内容无法恢复。

在使用加密主目录时，加密交换尤为重要，因为未加密的交换空间可能泄露已解密的数据。

# CAVEATS

会禁用休眠功能（交换内容无法恢复）。需要 root 权限。现有的交换分区将被重新格式化。必须在系统未使用交换分区时运行。

# HISTORY

ecryptfs-setup-swap 是 **eCryptfs** 工具集的一部分，用于解决加密文件系统数据可能泄露到未加密交换空间的安全缺口。

# INSTALL

```apt: sudo apt install ecryptfs-utils```

```dnf: sudo dnf install ecryptfs-utils```

```pacman: sudo pacman -S ecryptfs-utils```

```apk: sudo apk add ecryptfs-utils```

```zypper: sudo zypper install ecryptfs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ecryptfs-setup-private](/man/ecryptfs-setup-private)(1), [ecryptfs](/man/ecryptfs)(7), [cryptsetup](/man/cryptsetup)(8), [swapon](/man/swapon)(8)

# RESOURCES

```[Source code](https://launchpad.net/ecryptfs)```

```[Homepage](https://www.ecryptfs.org/)```

<!-- verified: 2026-07-14 -->
