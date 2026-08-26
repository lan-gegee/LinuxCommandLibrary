# TAGLINE

管理系统信任策略证书存储

# TLDR

列出信任策略存储中的条目

```trust list```

列出信任策略存储中特定条目的信息

```trust list --filter=[blocklist|ca-anchors|certificates|trust-policy]```

向信任策略存储添加信任锚

```trust anchor [path/to/certificate.crt]```

从信任策略存储移除锚点

```trust anchor --remove [path/to/certificate.crt]```

将信任策略提取到目录

```trust extract --format=x509-directory --filter=ca-anchors [path/to/directory]```

显示子命令的帮助信息

```trust [subcommand] --help```

# SYNOPSIS

**trust** _command_ [_options_]

# PARAMETERS

**list**
> 列出信任策略存储中的条目

**anchor** _file_
> 向存储添加信任锚

**anchor** **--remove** _file_
> 移除信任锚

**extract** **--format=**_format_ _path_
> 以指定格式提取信任锚。

**extract-compat**
> 以与系统原生工具兼容的格式提取信任策略。

**--filter=**_type_
> 按类型过滤 (ca-anchors, blocklist, certificates, trust-policy)。

**--format=**_format_
> 输出格式 (x509-file, x509-directory, pem-file, pem-bundle, java-cacerts, openssl-bundle, openssl-directory 等)。

**--purpose=**_purpose_
> 按用途过滤 (server-auth, client-auth, email, code-signing)。

# DESCRIPTION

**trust** 管理共享的系统信任策略存储，其中包含受信任的 CA 证书、被列入黑名单的证书以及信任策略。它让管理员能够添加、移除和提取用于全系统 TLS/SSL 验证的信任锚。

用 trust 所做的更改会影响所有使用 p11-kit 信任模块的应用程序，从而提供一种统一管理证书的方式，无需逐个配置每个应用。

# CAVEATS

如果没有用户专属的存储可用，修改系统信任存储可能需要 root 权限。更改后可能需要重启应用才能生效。存储格式和位置因发行版而异。

# HISTORY

属于 **p11-kit** 的一部分，作为 FreeDesktop.org 项目的一部分开发，旨在提供跨 Linux 发行版管理信任锚的标准方式。取代 update-ca-certificates 等各发行版专有的方法。

# INSTALL

```apt: sudo apt install p11-kit```

```dnf: sudo dnf install p11-kit```

```pacman: sudo pacman -S p11-kit```

```apk: sudo apk add p11-kit-trust```

```zypper: sudo zypper install p11-kit```

```brew: brew install p11-kit```

```nix: nix profile install nixpkgs#p11-kit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[update-ca-trust](/man/update-ca-trust)(8), [update-ca-certificates](/man/update-ca-certificates)(8), [openssl](/man/openssl)(1), [p11-kit](/man/p11-kit)(8)
