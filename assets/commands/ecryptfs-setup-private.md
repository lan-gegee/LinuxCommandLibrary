# TAGLINE

加密私有目录设置

# TLDR

**设置加密的私有目录**

```ecryptfs-setup-private```

**使用包装口令设置**

```ecryptfs-setup-private --wrapping```

**不使用包装口令设置**

```ecryptfs-setup-private --noautomount```

**强制设置（覆盖已有配置）**

```ecryptfs-setup-private --force```

# SYNOPSIS

**ecryptfs-setup-private** [_options_]

# PARAMETERS

**--wrapping**
> 使用登录口令进行包装。

**--noautomount**
> 不配置登录时自动挂载。

**--nopwcheck**
> 不校验登录密码。

**--force**
> 覆盖已有的配置。

**-u**, **--username** _name_
> 指定用户名（供 root 使用）。

**-l**, **--loginpass** _pass_
> 登录口令（不安全，仅供脚本使用）。

**-m**, **--mountpass** _pass_
> 挂载口令（不安全，仅供脚本使用）。

# CONFIGURATION

**~/.ecryptfs/**
> 存放加密密钥、包装口令和挂载配置的目录。

**~/.ecryptfs/wrapped-passphrase**
> 用登录密码包装的挂载口令，用于自动解密。

# DESCRIPTION

**ecryptfs-setup-private** 为用户创建一个加密的私有目录。它将 ~/Private 设置为加密文件夹，在用户登录时自动挂载，在登出时卸载。

设置过程会创建必要的加密密钥和包装器并存储到 ~/.ecryptfs 中。挂载口令会用登录密码包装，从而实现登录时自动解密。

# SETUP PROCESS

1. 提示输入登录密码
2. 生成随机的挂载口令
3. 用登录密码包装挂载口令
4. 创建 ~/.Private（加密）和 ~/Private（挂载点）
5. 配置 PAM 以实现自动挂载

# CAVEATS

需要 eCryptfs 内核模块。出于安全考虑应对交换分区加密。修改登录密码后需要重新包装。恢复数据需要未包装的口令。在现代系统上已被 fscrypt 取代。

# HISTORY

该工具是为 Ubuntu 的主目录加密功能开发的。从 **Ubuntu 8.10** 到 **18.04** 被广泛用于按用户加密，之后 fscrypt 成为推荐的解决方案。

# INSTALL

```apt: sudo apt install ecryptfs-utils```

```dnf: sudo dnf install ecryptfs-utils```

```pacman: sudo pacman -S ecryptfs-utils```

```apk: sudo apk add ecryptfs-utils```

```zypper: sudo zypper install ecryptfs-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

