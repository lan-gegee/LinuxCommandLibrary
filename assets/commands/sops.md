# TAGLINE

在结构化配置文件中加密机密信息

# TLDR

**加密文件**

```sops -e [secrets.yaml] > [secrets.enc.yaml]```

**解密文件**

```sops -d [secrets.enc.yaml]```

**编辑加密文件**

```sops [secrets.enc.yaml]```

**使用指定密钥加密**

```sops -e --age [age-public-key] [file.yaml]```

**轮换密钥**

```sops -r [secrets.enc.yaml]```

**添加 KMS 密钥**

```sops --add-kms [arn:aws:kms:...] [file.yaml]```

# SYNOPSIS

**sops** [_options_] _file_

# DESCRIPTION

**sops**（Secrets OPerationS）在加密文件的同时保持其格式不变。它只加密值而保留键的可读性，使 diff 和代码审查变得切实可行。

该工具支持多种密钥来源，包括 AWS KMS、GCP KMS、Azure Key Vault、age 和 PGP。

# PARAMETERS

**-e**, **--encrypt**
> 加密文件。

**-d**, **--decrypt**
> 解密文件。

**-r**, **--rotate**
> 轮换数据密钥。

**-i**, **--in-place**
> 原地修改文件。

**--age** _key_
> age 公钥。

**--pgp** _key_
> PGP 指纹。

**--kms** _arn_
> AWS KMS 密钥 ARN。

**--gcp-kms** _resource_
> GCP KMS 密钥。

**--azure-kv** _url_
> Azure Key Vault 密钥。

**--input-type** _type_
> 输入格式。

**--output-type** _type_
> 输出格式。

# CONFIGURATION

**.sops.yaml**
> 项目级配置文件，定义默认加密密钥，以及将匹配的文件映射到特定密钥集的规则。

**SOPS_AGE_KEY_FILE**
> 用于解密的 age 私钥文件路径（默认：~/.config/sops/age/keys.txt）。

**SOPS_AGE_KEY**
> 直接通过环境变量提供的 age 私钥。

# CAVEATS

解密需要密钥访问权限。建议使用多个密钥以保证冗余。应定期轮换密钥。某些格式存在限制。

# HISTORY

**sops** 由 **Mozilla** 创建，用于管理配置文件中的机密信息。它源于 Mozilla 的实际需求，现已在 GitOps 工作流中被广泛用于机密管理。

# INSTALL

```pacman: sudo pacman -S sops```

```apk: sudo apk add sops```

```zypper: sudo zypper install sops```

```brew: brew install sops```

```nix: nix profile install nixpkgs#sops```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[age](/man/age)(1), [gpg](/man/gpg)(1), [vault](/man/vault)(1)
