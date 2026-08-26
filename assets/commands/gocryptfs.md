# TAGLINE

基于 FUSE 的加密叠加文件系统

# TLDR

**创建加密目录**

```gocryptfs -init [cipher-dir]```

**挂载加密目录**

```gocryptfs [cipher-dir] [mount-point]```

**卸载**

```fusermount -u [mount-point]```

**修改密码**

```gocryptfs -passwd [cipher-dir]```

**显示信息**

```gocryptfs -info [cipher-dir]```

# SYNOPSIS

**gocryptfs** [_options_] _cipherdir_ [_mountpoint_]

# PARAMETERS

_CIPHERDIR_
> 加密目录。

_MOUNTPOINT_
> 挂载位置。

**-init**
> 初始化新卷。

**-passwd**
> 修改密码。

**-info**
> 显示卷信息。

**-fg**
> 在前台运行。

**-allow_other**
> 允许其他用户访问。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gocryptfs** 是一个用 Go 编写的加密叠加文件系统。它使用 AES-256-GCM 对每个文件单独加密，把密文存储在一个目录中，同时通过 FUSE 挂载呈现明文视图。

该工具提供文件级加密以及加密的文件名，可将加密数据安全地备份到云端。与全盘加密类方案相比，其元数据泄露被降到更低。

# CONFIGURATION

**gocryptfs.conf**
> 保存在密文目录中的每卷配置文件，包含加密参数和加密后的主密钥。

# CAVEATS

需要 FUSE。文件大小对外可见。如果没有备份主密钥，密码将无法恢复。

# HISTORY

gocryptfs 的定位是 EncFS 的现代化、经过安全审计的替代品，采用认证加密并以 Go 编写。

# INSTALL

```apt: sudo apt install gocryptfs```

```dnf: sudo dnf install gocryptfs```

```pacman: sudo pacman -S gocryptfs```

```apk: sudo apk add gocryptfs```

```zypper: sudo zypper install gocryptfs```

```brew: brew install gocryptfs```

```nix: nix profile install nixpkgs#gocryptfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[encfs](/man/encfs)(1), [cryptsetup](/man/cryptsetup)(1), [veracrypt](/man/veracrypt)(1)

# RESOURCES

```[Source code](https://github.com/rfjakob/gocryptfs)```

```[Homepage](https://nuetzlich.net/gocryptfs/)```

<!-- verified: 2026-07-17 -->
