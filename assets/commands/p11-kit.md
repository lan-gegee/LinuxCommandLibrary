# TAGLINE

管理 PKCS#11 模块

# TLDR

**列出模块**

```p11-kit list-modules```

**列出 token**

```p11-kit list-tokens```

**显示对象信息**

```p11-kit list-objects```

**提取 CA 证书为 PEM 包**

```p11-kit extract --format=pem-bundle --filter=ca-anchors [path/to/output.pem]```

**在 Unix 套接字上运行 PKCS#11 服务器**

```p11-kit server --provider [module.so] [pkcs11:token-uri]```

**在 token 上生成密钥对**

```p11-kit generate-keypair --type=rsa [pkcs11:token-uri]```

# SYNOPSIS

**p11-kit** [_command_] [_options_]

# PARAMETERS

**list-modules**
> 列出 PKCS#11 模块。

**list-tokens**
> 列出 token。

**list-objects**
> 列出对象。

**extract**
> 从共享信任存储中提取证书和信任策略。

**server**
> 运行 PKCS#11 服务器，通过本地套接字暴露 token。

**remote**
> 通过 stdin/stdout 远程暴露 PKCS#11 模块。

**generate-keypair**
> 在 token 上生成密钥对（rsa、ecdsa、eddsa）。

**add-profile**
> 在 token 上创建新的 profile 对象。

**delete-profile**
> 从 token 上删除 profile 对象。

**--format** _FORMAT_
> extract 的输出格式（例如 pem-bundle、x509-directory）。

**--filter** _FILTER_
> extract 的证书过滤器（例如 ca-anchors、trust-policy、blocklist、certificates）。

**-v, --verbose**
> 以详细模式运行并输出调试信息。

**-q, --quiet**
> 以安静模式运行，不输出警告。

# DESCRIPTION

**p11-kit** 提供了一种加载和枚举系统中 PKCS#11 模块的方式。它充当代理，让应用程序使用单一的 PKCS#11 模块即可访问所有已注册的 token（智能卡、HSM、软件 token）。

**extract** 命令常用于将信任存储中的 CA 证书导出为 PEM 包或其他格式，供 Web 服务器和 curl 等应用程序使用。

# CAVEATS

模块配置是系统级的，位于 /etc/pkcs11/modules/。修改系统信任存储需要 root 权限。使用 GnuTLS 或 NSS 的应用通常依赖 p11-kit 进行证书信任管理。

# HISTORY

p11-kit 的创建目的是在各个应用之间**统一 PKCS#11 模块**的管理。

# INSTALL

```apt: sudo apt install p11-kit```

```dnf: sudo dnf install p11-kit```

```pacman: sudo pacman -S p11-kit```

```apk: sudo apk add p11-kit```

```zypper: sudo zypper install p11-kit```

```brew: brew install p11-kit```

```nix: nix profile install nixpkgs#p11-kit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trust](/man/trust)(1), [pkcs11-tool](/man/pkcs11-tool)(1), [openssl](/man/openssl)(1)
