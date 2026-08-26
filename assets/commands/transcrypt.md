# TAGLINE

透明的 Git 文件加密

# TLDR

**初始化加密**

```transcrypt```

使用指定密码算法

```transcrypt -c [aes-256-cbc]```

**显示凭据**

```transcrypt -d```

**清除凭据**

```transcrypt -f```

**为仓库重新生成密钥**

```transcrypt -r```

**卸载**

```transcrypt -u```

# SYNOPSIS

**transcrypt** [_-c cipher_] [_-d_] [_-f_] [_-r_] [_options_]

# PARAMETERS

**-c** _CIPHER_
> 加密密码算法。

**-d**
> 显示凭据。

**-f**
> 清除凭据。

**-r**
> 为仓库重新生成密钥。

**-u**
> 卸载。

**-p** _PASSWORD_
> 设置密码。

# DESCRIPTION

**transcrypt** 使用 OpenSSL 对称密码为 Git 仓库中的文件提供透明加密。它利用 Git 内置的 clean 和 smudge 过滤器机制，在文件暂存时自动加密、在检出时自动解密，让这一过程在日常开发工作流中无缝进行。

该工具会在推送时加密敏感文件，使其以加密形式存储在远程仓库中，并在拉取时自动解密供本地使用。它支持 OpenSSL 提供的任何密码算法，默认为 AES-256-CBC。凭据通过 Git 的凭据辅助（credential helper）系统管理；如果需要更改密码，可以为仓库重新生成密钥。

仓库的每个克隆都需要使用正确的密码进行初始化才能访问加密文件。加密配置保存在 `.gitattributes` 中，由其指定哪些文件应被加密。

# CAVEATS

每个克隆都需要单独设置。需管理密码。仅适用于 Git。

# HISTORY

**transcrypt** 的设计目标是使用 OpenSSL 对 Git 仓库中的文件进行透明加密。

# INSTALL

```brew: brew install transcrypt```

```nix: nix profile install nixpkgs#transcrypt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-crypt](/man/git-crypt)(1), [age](/man/age)(1), [gpg](/man/gpg)(1)
