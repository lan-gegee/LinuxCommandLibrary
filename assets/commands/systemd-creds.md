# TAGLINE

管理加密的服务凭证

# TLDR

**加密**文件并指定名称

```systemd-creds encrypt --name [name] [input] [output]```

**解密**文件

```systemd-creds decrypt [input] [output]```

从 **stdin** 加密

```echo -n [text] | systemd-creds encrypt --name [name] - [output]```

以适合单元文件的 **pretty** 格式加密

```echo -n [text] | systemd-creds encrypt --name [name] --pretty - - >> [unit.service]```

创建带**过期时间**的凭证

```systemd-creds encrypt --not-after "[timestamp]" [input] [output]```

# SYNOPSIS

**systemd-creds** [_OPTIONS_] _COMMAND_

# COMMANDS

**encrypt** _INPUT_ _OUTPUT_
> 加密一个凭证

**decrypt** _INPUT_ _OUTPUT_
> 解密一个凭证

**list**
> 列出可用的凭证

**cat** _CREDENTIAL_
> 显示凭证内容

# PARAMETERS

**--name=** _NAME_
> 设置凭证名称

**--pretty**
> 以适合单元文件的格式输出

**--not-after=** _TIMESTAMP_
> 设置凭证的过期时间

**--with-key=** _TYPE_
> 加密密钥来源（host、tpm2 等）

# DESCRIPTION

**systemd-creds** 管理 systemd 服务的加密凭证。凭证是经过加密的秘密信息，可通过 `$CREDENTIALS_DIRECTORY` 机制安全地传递给服务。

凭证可以使用主机密钥、TPM2 或两者同时加密。它们支持基于时间的过期机制，并且可以用 `--pretty` 格式直接嵌入单元文件。

# CAVEATS

使用主机密钥加密的凭证绑定到特定机器。TPM2 加密的凭证需要 TPM 硬件。凭证必须由 systemd 解密，服务无法直接手动访问。

# HISTORY

**systemd-creds** 的加入为服务提供了安全的秘密管理方式，取代了以往用于存储敏感配置的环境变量和全局可读文件。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1)
