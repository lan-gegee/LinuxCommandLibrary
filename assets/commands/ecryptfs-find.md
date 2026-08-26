# TAGLINE

将 eCryptfs 加密文件名与其解密后的名称互相匹配

# TLDR

**查找某个解密后文件名对应的加密形式**

```ecryptfs-find [cleartext-filename]```

**查找某个加密文件名对应的解密形式**

```ecryptfs-find [ECRYPTFS_FNEK_ENCRYPTED.fwBGx...]```

# SYNOPSIS

**ecryptfs-find** _filename_

# PARAMETERS

_FILENAME_
> 要查询的明文或 eCryptfs 加密文件名。该工具通过 inode 号解析对应的另一侧名称。

# DESCRIPTION

**ecryptfs-find** 使用 inode 号将加密文件名与解密后的名称互相匹配。它先调用 **ls**(1) 确定 inode，再用 **find**(1) 在文件系统上定位该 inode。

命令要正常工作必须已挂载 eCryptfs 文件系统，因为匹配需要同时访问目录的加密视图和解密视图。

它主要是一个诊断工具，用于在 eCryptfs 部署中排查文件名映射关系。

# CAVEATS

运行此命令前必须已挂载 eCryptfs 文件系统。该工具不解密文件内容，只处理文件名的映射关系。需要对被搜索目录拥有读取权限。

# HISTORY

ecryptfs-find 是 **ecryptfs-utils** 软件包的一部分。eCryptfs 是一个符合 POSIX 标准的堆叠式加密文件系统，自 Linux 内核 **2.6.19**（**2006 年**发布）起被纳入内核。

# INSTALL

```apt: sudo apt install ecryptfs-utils```

```dnf: sudo dnf install ecryptfs-utils```

```pacman: sudo pacman -S ecryptfs-utils```

```apk: sudo apk add ecryptfs-utils```

```zypper: sudo zypper install ecryptfs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ecryptfs-setup-private](/man/ecryptfs-setup-private)(1), [ecryptfs-verify](/man/ecryptfs-verify)(1), [ecryptfs](/man/ecryptfs)(1), [encfs](/man/encfs)(1), [fscrypt](/man/fscrypt)(1)
