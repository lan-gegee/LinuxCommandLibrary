# TAGLINE

堆叠式加密文件系统

# TLDR

**挂载加密目录**

```sudo mount -t ecryptfs [/encrypted] [/mnt/decrypted]```

**设置加密私有目录**

```ecryptfs-setup-private```

**挂载用户私有目录**

```ecryptfs-mount-private```

**卸载私有目录**

```ecryptfs-umount-private```

**将口令加入密钥环**

```ecryptfs-add-passphrase```

**恢复加密目录**

```ecryptfs-recover-private```

# SYNOPSIS

**mount -t ecryptfs** _source_ _dest_ [**-o** _options_]

# PARAMETERS

**ecryptfs_cipher** _cipher_
> 加密算法（aes、blowfish、des3_ede）。

**ecryptfs_key_bytes** _bytes_
> 密钥长度（字节）（16、24、32）。

**ecryptfs_passthrough** _yes|no_
> 允许未加密的文件。

**ecryptfs_enable_filename_crypto** _yes|no_
> 加密文件名。

**ecryptfs_sig** _sig_
> 密钥的挂载签名。

**ecryptfs_fnek_sig** _sig_
> 文件名加密密钥签名。

**no_sig_cache**
> 不缓存签名。

# DESCRIPTION

**eCryptfs** 是 Linux 上的堆叠式加密文件系统。它在文件系统层面加密文件：加密后的数据存放在下层目录中，同时通过挂载点呈现解密后的文件。

与块级加密不同，eCryptfs 对单个文件加密，允许加密文件与未加密文件共存。元数据存储在文件头部，使备份和恢复变得简单直接。

# SETUP EXAMPLE

```bash
# Create directories
mkdir /encrypted /decrypted

# Mount with interactive setup
sudo mount -t ecryptfs /encrypted /decrypted

# Answer prompts for cipher, key size, plaintext passthrough
```

# CAVEATS

文件名加密需要额外设置。与块级加密相比存在性能开销。密钥管理需要理解内核密钥环。对 ext4 而言已被 fscrypt 取代。不建议用于新部署。

# HISTORY

eCryptfs 由 **IBM** 开发，于 **2006 年**首次进入 Linux 内核。Ubuntu 曾用它实现主目录加密。该项目已在很大程度上被 **fscrypt**（原生 ext4/F2FS 加密）取代，但仍可用于遗留场景。

# SEE ALSO

[cryptsetup](/man/cryptsetup)(8), [fscrypt](/man/fscrypt)(8), [mount](/man/mount)(8), [keyctl](/man/keyctl)(1), [ecryptfs-setup-private](/man/ecryptfs-setup-private)(1), [ecryptfs-setup-swap](/man/ecryptfs-setup-swap)(1)

# RESOURCES

```[Source code](https://launchpad.net/ecryptfs)```

```[Homepage](https://www.ecryptfs.org/)```

<!-- verified: 2026-07-14 -->
