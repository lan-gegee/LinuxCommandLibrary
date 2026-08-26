# TAGLINE

批量更新用户密码

# TLDR

更改**特定用户**的密码

```printf "[username]:[new_password]" | sudo chpasswd```

为**多个用户**更改密码

```printf "[username_1]:[password_1]\n[username_2]:[password_2]" | sudo chpasswd```

使用**加密形式**的密码更改密码

```printf "[username]:[encrypted_password]" | sudo chpasswd -e```

以**指定的加密方式**更改密码

```printf "[username]:[new_password]" | sudo chpasswd -c [SHA512]```

# SYNOPSIS

**chpasswd** [_options_]

# DESCRIPTION

**chpasswd** 从标准输入读取 username:password 对并批量更新用户密码。它适用于需要一次性更改多个用户密码的系统管理任务，例如初始账户开通或自动化密码轮换。

输入格式为每行一个用户，形如 **username:password**，冒号两侧不能有空格。除非指定了其他加密方式，否则密码将使用系统默认方法（通常为 SHA-512）加密。也可以通过 **-e** 参数提供已加密的密码。

# PARAMETERS

**-e, --encrypted**
> 提供的密码已是加密形式

**-c, --crypt-method** _method_
> 指定加密方式（NONE、DES、MD5、SHA256、SHA512）

**-m, --md5**
> 使用 MD5 加密

**-s, --sha-rounds** _rounds_
> SHA 加密的轮数

# CONFIGURATION

**/etc/login.defs**
> 控制默认加密方式（ENCRYPT_METHOD）、SHA 轮数（SHA_CRYPT_MIN_ROUNDS、SHA_CRYPT_MAX_ROUNDS）以及 chpasswd 使用的其他密码策略设置。

# CAVEATS

需要 root 权限。通过命令行传递的密码可能出现在进程列表中。在脚本中建议使用已加密的密码或安全的输入方式。DES 加密已被认为不安全。

# HISTORY

**chpasswd** 是 **shadow-utils** 软件包的一部分，用于批量密码管理。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[passwd](/man/passwd)(1), [usermod](/man/usermod)(8), [useradd](/man/useradd)(8)
