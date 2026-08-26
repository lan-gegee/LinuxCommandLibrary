# TAGLINE

加密的命令行 TOTP/HOTP 认证器

# TLDR

**启动**交互式 OTP 面板

```cotp```

**添加**新的 TOTP 码

```cotp add --label [myaccount@gmail.com] --issuer [Google]```

**添加**自定义设置的 HOTP 码

```cotp add --label [example] --type hotp --algorithm SHA256 --digits 8 --counter 10```

以 JSON 格式**列出**所有验证码

```cotp list --json```

按 issuer **提取**验证码并复制到剪贴板

```cotp extract --issuer [Google] --copy-clipboard```

从加密的 Aegis 备份**导入**

```cotp import --path [my_backup.json] --aegis-encrypted```

**导出**数据库

```cotp export```

# SYNOPSIS

**cotp** [_OPTIONS_] [_SUBCOMMAND_]

# PARAMETERS

**--database-path** _PATH_
> 使用自定义的数据库文件路径。

**--password-stdin**
> 从 stdin 读取数据库密码。

**--help**
> 显示命令或子命令的帮助信息。

# SUBCOMMANDS

**add**
> 添加新的 TOTP 或 HOTP 码。选项：**--label**、**--issuer**、**--type**（totp/hotp）、**--algorithm**（SHA1/SHA256/SHA512）、**--digits**、**--counter**。

**edit**
> 编辑已有的 OTP 条目。选项：**--index**、**--digits**。

**list**
> 列出所有验证码。使用 **--json** 以 JSON 输出。

**extract**
> 提取特定的 OTP 码。选项：**--issuer**、**--copy-clipboard**。

**import**
> 从其他认证器应用导入验证码。支持：**--andotp**、**--aegis**、**--aegis-encrypted**、**--authy**、**--authy-exported**、**--cotp**、**--freeotp**、**--freeotp-plus**、**--google-authenticator**、**--microsoft-authenticator**、**--otp-uri**。

**export**
> 导出/备份数据库。

# DESCRIPTION

**cotp** 是一个值得信赖的加密命令行 TOTP/HOTP 认证器，用 Rust 编写。它同时生成 TOTP（基于时间的一次性密码，RFC 6238）和 HOTP（基于 HMAC 的一次性密码，RFC 4226）验证码，还支持 Steam、Yandex 和 MOTP 验证码生成。

所有数据保存在单个加密数据库文件中，采用 **XChaCha20Poly1305** 认证加密和 **Argon2id** 密钥派生。默认位置为 **$HOME/.cotp/db.cotp**，可通过 **COTP_DB_PATH** 环境变量配置。交互式 TUI 面板支持模糊搜索显示所有 OTP 码，且在 SSH 下也能复制到剪贴板。

# CAVEATS

某些导入格式（Authy XML、FreeOTP XML、Google Authenticator、Microsoft Authenticator）需要先从手机提取数据，再运行 **converters/** 目录下的 Python 转换脚本。在基于 Debian 的系统上，从源码构建还需要额外的 X11 开发库。

# HISTORY

**cotp** 由 **replydev** 创建，首次发布于 **2020 年 12 月底**。以 Rust 编写，采用 GPL-3.0 许可证。最新版本为 v1.9.7（2025 年 9 月），共发布 45 个版本。可用于 Arch Linux、Debian、Ubuntu、NixOS，也可通过 Homebrew 和 Cargo 获取。

# INSTALL

```apt: sudo apt install cotp```

```pacman: sudo pacman -S cotp```

```brew: brew install cotp```

```nix: nix profile install nixpkgs#cotp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[oathtool](/man/oathtool)(1), [pass](/man/pass)(1)
