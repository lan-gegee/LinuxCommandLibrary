# TAGLINE

管理 UEFI 安全启动密钥与签名

# TLDR

查看当前**安全启动状态**

```sbctl status```

**创建**自定义安全启动密钥

```sbctl create-keys```

**注册**密钥并包含微软证书

```sbctl enroll-keys -m```

**列出**签名数据库中的文件

```sbctl list-files```

**签名** EFI 二进制文件并保存到数据库

```sbctl sign -s path/to/efi_binary```

**重新签名**所有已保存的文件

```sbctl sign-all```

**验证**所有 EFI 可执行文件是否已签名

```sbctl verify```

# SYNOPSIS

**sbctl** _command_ [_options_]

# PARAMETERS

**status**
> 显示安全启动状态

**create-keys**
> 生成自定义安全启动密钥

**enroll-keys**
> 将密钥注册到 UEFI 固件

**-m**, **--microsoft**
> 包含微软 UEFI 供应商证书

**sign**
> 签名 EFI 二进制文件

**-s**, **--save**
> 将文件保存到数据库以便重新签名

**sign-all**
> 重新签名所有已保存的文件

**verify**
> 验证 EFI 可执行文件是否已签名

**list-files**
> 列出签名数据库中的文件

**remove-file** _file_
> 从签名数据库中移除文件

**setup**
> 自动完成安全启动设置（创建密钥、签名、注册）

# DESCRIPTION

**sbctl** 是一款易于使用的安全启动密钥管理工具。它简化了自定义安全启动密钥的创建、注册和管理，以及对 EFI 二进制文件的签名。

自定义密钥只允许启动经过签名的内核和引导加载程序，从而增强系统安全性。

# CONFIGURATION

**/usr/share/secureboot/**
> 存放生成的安全启动密钥（PK、KEK、db）以及已签名文件数据库的默认目录。

# CAVEATS

如果不注册微软证书（即不使用 **-m** 标志），某些带有需要微软签名驱动的 Option ROM 的系统可能会无法启动。密钥默认存储在 /usr/share/secureboot 中。所有操作均需 root 权限。

# HISTORY

作为手动安全启动密钥管理工具的易用替代品而开发。

# INSTALL

```pacman: sudo pacman -S sbctl```

```apk: sudo apk add sbctl```

```zypper: sudo zypper install sbctl```

```nix: nix profile install nixpkgs#sbctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mokutil](/man/mokutil)(1), [efibootmgr](/man/efibootmgr)(8)
