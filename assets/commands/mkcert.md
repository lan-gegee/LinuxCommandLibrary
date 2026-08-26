# TAGLINE

创建本地受信任的证书

# TLDR

**安装本地 CA**

```mkcert -install```

**生成证书**

```mkcert [localhost]```

**多个域名**

```mkcert [localhost] [127.0.0.1] [::1]```

**通配符证书**

```mkcert [*.local.dev]```

**指定输出名称**

```mkcert -key-file [key.pem] -cert-file [cert.pem] [localhost]```

**生成 PKCS#12 打包**

```mkcert -pkcs12 [example.test]```

**显示 CA 根目录**

```mkcert -CAROOT```

**卸载 CA**

```mkcert -uninstall```

# SYNOPSIS

**mkcert** [_options_] [_domains_]

# PARAMETERS

_DOMAINS_
> 用于证书的域名。

**-install**
> 安装本地 CA。

**-uninstall**
> 卸载本地 CA。

**-key-file** _FILE_
> 密钥输出文件。

**-cert-file** _FILE_
> 证书输出文件。

**-p12-file** _FILE_
> PKCS#12 输出文件（配合 **-pkcs12** 使用）。

**-pkcs12**
> 生成包含证书和密钥的 ".p12"/".pfx" 文件（用于 Java/旧式工具）。

**-client**
> 生成用于客户端认证的证书。

**-ecdsa**
> 使用 ECDSA 密钥而非 RSA。

**-csr** _CSR_
> 基于提供的 CSR 生成证书。

**-CAROOT**
> 打印 CA 证书和密钥的存储位置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mkcert** 创建本地受信任的证书。它简化了开发环境的 HTTPS 配置。

该工具安装本地 CA 并生成受信任的证书。不再出现浏览器警告。

# CAVEATS

仅用于开发。妥善保管根 CA。不要分享 CA 密钥。

# HISTORY

mkcert 由 **Filippo Valsorda** 创建，旨在用受信任的证书简化本地 HTTPS 开发。

# INSTALL

```apt: sudo apt install mkcert```

```dnf: sudo dnf install mkcert```

```pacman: sudo pacman -S mkcert```

```zypper: sudo zypper install mkcert```

```brew: brew install mkcert```

```nix: nix profile install nixpkgs#mkcert```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl](/man/openssl)(1), [certbot](/man/certbot)(1)
