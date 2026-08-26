# TAGLINE

Linux 原生文件系统加密管理工具

# TLDR

为使用 fscrypt 准备**根文件系统**

```sudo fscrypt setup```

为使用 fscrypt 准备**特定挂载点**

```fscrypt setup [path/to/directory]```

为目录**启用加密**

```fscrypt encrypt [path/to/directory]```

**解锁**已加密的目录

```fscrypt unlock [path/to/encrypted_directory]```

**锁定**已加密的目录

```fscrypt lock [path/to/encrypted_directory]```

# SYNOPSIS

**fscrypt** _command_ [_arguments_]

# PARAMETERS

**setup**
> 在文件系统或挂载点上初始化 fscrypt。

**encrypt**
> 为目录启用加密。

**unlock**
> 使用保护器（protector）解锁已加密的目录。

**lock**
> 锁定已加密的目录，使内容不可访问。

**purge**
> 从内核密钥环中移除某个挂载点的密钥。

**status**
> 显示文件或目录的加密状态。

**metadata**
> 管理加密元数据和策略。

# CONFIGURATION

**/.fscrypt**
> 在每个启用的挂载点上存储加密元数据。

**~/.config/fscrypt/fscrypt.conf**
> 全局 fscrypt 配置设置和保护器定义。

# DESCRIPTION

**fscrypt** 是管理 Linux 原生文件系统加密（fscrypt）的高级工具。它为内核的文件系统加密能力提供友好的界面，支持 ext4、F2FS 和 UBIFS 文件系统。

fscrypt 使用 "保护器"（密码、PAM 集成或原始密钥）来保护加密密钥。一个目录可以有多个保护器，从而支持共享访问或恢复选项。解锁之后，加密对用户是透明的。

初始化需要内核支持（CONFIG_FS_ENCRYPTION）和相应的文件系统配置。该工具把元数据存储在每个启用挂载点的 **/.fscrypt** 中。

# CAVEATS

只加密文件内容和文件名，不加密文件大小或时间戳等元数据。交换空间和临时目录可能泄露数据。文件系统必须以支持加密的方式挂载。加密之前创建的文件不会被自动加密。

# HISTORY

fscrypt 由 Google 开发，于 **2017** 年首次发布，是管理 Linux 内核原生文件系统加密（fscrypt）的用户空间工具。该内核功能在 4.1 中面向 ext4 引入，随后扩展到其他文件系统。

# INSTALL

```apt: sudo apt install fscrypt```

```dnf: sudo dnf install fscrypt```

```pacman: sudo pacman -S fscrypt```

```apk: sudo apk add fscrypt```

```zypper: sudo zypper install fscrypt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cryptsetup](/man/cryptsetup)(8), [ecryptfs](/man/ecryptfs)(7), [gpg](/man/gpg)(1)

# RESOURCES

```[Source code](https://github.com/google/fscrypt)```

<!-- verified: 2026-07-15 -->
