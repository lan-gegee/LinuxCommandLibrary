# TAGLINE

使用 Cloud KMS 密钥解密数据

# TLDR

**解密文件**

```gcloud kms decrypt --ciphertext-file=[encrypted.enc] --plaintext-file=[decrypted.txt] --key=[key] --keyring=[keyring] --location=[global]```

**从标准输入解密**

```cat [encrypted.enc] | gcloud kms decrypt --ciphertext-file=- --plaintext-file=[output.txt] --key=[key] --keyring=[keyring] --location=[global]```

**解密到标准输出**

```gcloud kms decrypt --ciphertext-file=[encrypted.enc] --plaintext-file=- --key=[key] --keyring=[keyring] --location=[global]```

# SYNOPSIS

**gcloud kms decrypt** [_options_]

# PARAMETERS

**--ciphertext-file** _FILE_
> 加密的输入文件。

**--plaintext-file** _FILE_
> 解密后的输出文件。

**--key** _KEY_
> 加密密钥名称。

**--keyring** _KEYRING_
> 密钥环名称。

**--location** _LOCATION_
> 密钥位置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gcloud kms decrypt** 使用 Cloud Key Management Service 解密之前用 Cloud KMS 密钥加密的数据。KMS 提供集中式的加密密钥管理，将密钥存储和访问控制与使用它们的应用程序分离开来。

解密操作需要指定加密时使用的确切密钥、密钥环和位置。解密权限由密钥上的 IAM 权限控制，可以精细控制谁有权解密敏感数据。这样可以实现安全的机密信息管理：加密后的数据可以存放在版本控制或配置文件中，而密钥则安全地保存在 KMS 中。

该命令支持从文件或标准输入读取，并写入文件或标准输出，便于集成到管道和脚本中。Cloud KMS 常用于信封加密（envelope encryption），即数据加密密钥本身再由 KMS 密钥加密，从而提供额外的安全层。这是在 Google Cloud 环境中加密应用程序机密、数据库凭据和其他敏感配置数据的标准模式。

# CAVEATS

需要 KMS 权限。密钥必须与加密时使用的密钥一致。位置必须正确。

# HISTORY

gcloud kms decrypt 是 **Google Cloud SDK** 中 Cloud KMS 相关功能的一部分。Cloud KMS 是 Google 提供的托管式加密密钥管理服务。

# SEE ALSO

[gcloud](/man/gcloud)(1)
