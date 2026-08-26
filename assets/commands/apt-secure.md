# TAGLINE

归档认证与信任模型文档。

# TLDR

这是一个**手册页**，介绍 APT 的安全模型，不是命令。

阅读该 man page：

```man apt-secure```

# DESCRIPTION

**apt-secure** 是一个手册页（而非命令），描述 APT 的归档认证系统。它解释了 APT 如何使用加密签名验证软件包完整性，以防范中间人攻击和被入侵的镜像服务器。

该文档涵盖：
- Release 文件如何用 GPG 签名
- Packages 文件如何通过 Release 文件中的校验和进行验证
- 如何添加受信任的密钥用于仓库验证
- 使用不受信任仓库的安全影响
- 从归档维护者到最终用户的信任链

# KEY CONCEPTS

**Release.gpg**
> Release 文件的分离式 GPG 签名

**InRelease**
> 带有内联签名的 Release 文件

**Trusted keys**
> 存储在 /etc/apt/trusted.gpg.d/ 中

**signed-by**
> 指定每个仓库所用密钥的现代方法

# CONFIGURATION

**/etc/apt/trusted.gpg.d/**
> 存放受信任密钥环文件的目录，用于验证仓库签名。

**/etc/apt/sources.list**
> 软件包源列表，支持 signed-by 选项为每个仓库指定密钥。

# CAVEATS

理解 apt-secure 对于安全地添加第三方仓库非常重要。使用 allow-insecure 或 allow-unauthenticated 会绕过安全机制。

# INSTALL

```apt: sudo apt install apt```

```dnf: sudo dnf install apt```

```pacman: sudo pacman -S apt```

```apk: sudo apk add apt```

```brew: brew install apt```

```nix: nix profile install nixpkgs#apt```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apt](/man/apt)(8), [apt-get](/man/apt-get)(8), [apt-key](/man/apt-key)(8), [gpg](/man/gpg)(1)
