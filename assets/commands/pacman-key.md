# TAGLINE

GnuPG 的封装工具，用于管理 pacman 验证软件包签名所需的密钥环

# TLDR

**初始化** pacman 密钥环

```sudo pacman-key --init```

添加**默认的 Arch Linux 密钥**

```sudo pacman-key --populate```

从公钥环中**列出密钥**

```pacman-key -l```

**添加**指定的密钥

```sudo pacman-key -a [path/to/keyfile.gpg]```

从密钥服务器**接收密钥**

```sudo pacman-key -r "[uid|name|email]"```

打印特定密钥的**指纹**

```pacman-key -f "[uid|name|email]"```

在本地**签署**导入的密钥

```sudo pacman-key --lsign-key "[uid|name|email]"```

**移除**特定密钥

```sudo pacman-key -d "[uid|name|email]"```

# SYNOPSIS

**pacman-key** [_options_] [_operation_]

# PARAMETERS

**--init**
> 初始化 pacman 密钥环

**--populate**
> 从 archlinux-keyring 软件包重新加载默认密钥

**-l, --list-keys**
> 列出公钥环中的密钥

**-a, --add _file_**
> 从文件添加密钥

**-r, --recv-keys _keyid_**
> 从密钥服务器获取密钥

**-f, --finger _keyid_**
> 显示密钥指纹

**--lsign-key _keyid_**
> 在本地签署密钥（信任它）

**-d, --delete _keyid_**
> 从密钥环中移除密钥

**--refresh-keys**
> 从密钥服务器更新密钥

# DESCRIPTION

**pacman-key** 是 GnuPG 的封装工具，用于管理 pacman 验证软件包签名所用的密钥环。它负责密钥初始化、导入、签署和信任管理。

在新装的 Arch Linux 系统上，先运行 **--init** 创建密钥环，再运行 **--populate** 添加官方的 Arch Linux 打包者密钥。对于第三方仓库（如 AUR 助手或自定义仓库），需手动添加并签署它们的密钥。

密钥签署（**--lsign-key**）会将密钥标记为受信任，使 pacman 安装由该密钥签名的软件包时不出现警告。

# CAVEATS

大多数操作需要 root 权限。密钥初始化需要足够的熵；如果卡住，可以制造一些系统活动（磁盘 I/O、网络访问、敲击键盘）。密钥环存储在 **/etc/pacman.d/gnupg/**。损坏的密钥环可以通过删除该目录并重新初始化来重置。

# HISTORY

随 2011 年发布的 pacman 4.0 引入以支持软件包签名，通过密码学方式验证软件包的完整性和真实性来增强安全性。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [gpg](/man/gpg)(1), [makepkg](/man/makepkg)(8)
