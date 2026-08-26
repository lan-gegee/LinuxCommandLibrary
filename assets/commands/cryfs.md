# TAGLINE

面向云存储的加密文件系统

# TLDR

**创建并挂载**加密文件系统

```cryfs [path/to/cipher_dir] [path/to/mount_point]```

使用指定的配置文件**挂载**

```cryfs --config [cryfs.config] [cipher_dir] [mount_point]```

**卸载**加密文件系统

```cryfs-unmount [path/to/mount_point]```

**修改加密密码**

```cryfs-change-password [path/to/cipher_dir]```

**显示文件系统信息**

```cryfs --show-ciphers```

以前台模式**挂载**以便调试

```cryfs -f [cipher_dir] [mount_point]```

# SYNOPSIS

**cryfs** [_options_] _cipher_dir_ _mount_point_

# PARAMETERS

_CIPHER_DIR_
> 存放加密数据的目录。

_MOUNT_POINT_
> 解密后文件系统的挂载点目录。

**-c** _FILE_, **--config** _FILE_
> 使用指定的配置文件。

**-f**, **--foreground**
> 以前台运行而不是转为守护进程。

**--allow-filesystem-upgrade**
> 允许升级文件系统格式。

**--show-ciphers**
> 显示可用的加密算法选项。

**--unmount-idle** _MINUTES_
> 空闲指定时间后自动卸载。

**--logfile** _FILE_
> 将日志写入指定文件。

# DESCRIPTION

**CryFS** 是专为 Dropbox、Google Drive 或 OneDrive 等云存储服务设计的加密文件系统。与其他加密文件系统不同，CryFS 不仅加密文件内容，还加密文件大小、元数据和目录结构。

文件会被拆分为固定大小的块，逐块独立加密并以随机名称存储。这可以防止云服务商和攻击者获知任何有关你数据的信息，包括哪些文件发生了变化以及它们的大小。

加密数据存放在 cipher 目录中，该目录可与云服务同步。挂载点显示的则是解密后的文件视图。CryFS 默认使用带认证的加密算法 AES-256-GCM。

# CONFIGURATION

**~/.cryfs/config**
> 存储文件系统配置和加密算法设置。

# CAVEATS

由于加密开销和基于块的存储方式，性能低于未加密的文件系统。应同步的是 cipher 目录而不是挂载点。忘记密码意味着数据永久丢失。系统必须支持 FUSE。

# HISTORY

CryFS 由 Sebastian Messmer 作为其硕士论文项目开发，首个版本于 **2015** 年发布。它的设计初衷是解决云存储带来的隐私问题，比 EncFS 等传统加密文件系统提供更强的机密性保证。

# INSTALL

```apt: sudo apt install cryfs```

```dnf: sudo dnf install cryfs```

```pacman: sudo pacman -S cryfs```

```zypper: sudo zypper install cryfs```

```brew: brew install cryfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[encfs](/man/encfs)(1), [gocryptfs](/man/gocryptfs)(1), [veracrypt](/man/veracrypt)(1), [fusermount](/man/fusermount)(1)

# RESOURCES

```[Source code](https://github.com/cryfs/cryfs)```

```[Homepage](https://www.cryfs.org)```

<!-- verified: 2026-06-26 -->
