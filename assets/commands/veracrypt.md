# TAGLINE

开源磁盘加密软件

# TLDR

**创建**新卷

```veracrypt -t -c --random-source=/dev/urandom```

以交互方式**挂载**卷

```veracrypt -t [path/to/volume] [path/to/mount_point]```

使用**密钥文件**挂载

```veracrypt -k [path/to/keyfile] [/dev/sdXN] [path/to/mount_point]```

**卸载**卷

```veracrypt -d [path/to/mounted_point]```

# SYNOPSIS

**veracrypt** [_OPTIONS_] [_VOLUME_] [_MOUNT_POINT_]

# PARAMETERS

**-t, --text**
> 使用文本用户界面

**-c, --create**
> 创建新卷

**-k, --keyfiles** _FILE_
> 使用密钥文件解密

**-d, --dismount**
> 卸载卷

**--random-source** _FILE_
> 创建卷时的随机数据来源

**-p, --password** _PASSWORD_
> 指定密码（安全性较低）

# DESCRIPTION

**veracrypt** 是免费的开源磁盘加密软件。它可以创建加密容器（基于文件的卷），或加密整个分区或磁盘，提供即时（on-the-fly）加密。

VeraCrypt 支持多种加密算法，并可创建隐藏卷以实现合理否认。

# CAVEATS

忘记密码或丢失密钥文件将导致数据永久丢失。创建卷可能较慢。某些功能需要 root 权限。

# HISTORY

**VeraCrypt** 是已停止维护的 TrueCrypt 项目的分支，在继续开发的同时进行了安全改进并添加了新特性。

# INSTALL

```pacman: sudo pacman -S veracrypt```

```nix: nix profile install nixpkgs#veracrypt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cryptsetup](/man/cryptsetup)(8)
