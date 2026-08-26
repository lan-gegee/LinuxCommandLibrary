# TAGLINE

管理 Azure 中的 SSH 公钥资源

# TLDR

**创建 SSH 密钥资源**（自动生成密钥对）

```az sshkey create --name [MySSHKey] --resource-group [MyResourceGroup]```

**从现有公钥创建 SSH 密钥**

```az sshkey create --name [MySSHKey] --resource-group [MyResourceGroup] --public-key "@[~/.ssh/id_rsa.pub]"```

**创建 Ed25519 SSH 密钥资源**

```az sshkey create --name [MySSHKey] --resource-group [MyResourceGroup] --encryption-type [Ed25519]```

**列出所有 SSH 密钥资源**

```az sshkey list --resource-group [MyResourceGroup]```

**显示 SSH 密钥详情**

```az sshkey show --name [MySSHKey] --resource-group [MyResourceGroup]```

**删除 SSH 密钥资源**

```az sshkey delete --name [MySSHKey] --resource-group [MyResourceGroup]```

# SYNOPSIS

**az** **sshkey** _subcommand_ [_options_]

# SUBCOMMANDS

**create**
> 创建新的 SSH 公钥资源。

**delete**
> 删除 SSH 公钥资源。

**list**
> 列出 SSH 公钥资源。

**show**
> 获取 SSH 公钥资源的信息。

**update**
> 更新 SSH 公钥资源。

# PARAMETERS

**--name** **--ssh-public-key-name** **-n**
> SSH 公钥资源的名称。

**--resource-group** **-g**
> 资源组的名称。

**--public-key**
> SSH 公钥内容，或用 `@filename` 表示从文件读取。创建时若省略此参数，将自动生成密钥对。提供的密钥必须至少为 2048 位且采用 ssh-rsa 格式。

**--encryption-type**
> 生成密钥时使用的算法。接受 **RSA**（默认）或 **Ed25519**。

**--location** **-l**
> 资源所在的 Azure 区域。

# DESCRIPTION

**az sshkey** 管理 Azure 的 SSH 公钥资源。这类资源将 SSH 公钥存储在 Azure 中，以便创建 VM 时重复使用。通过引用已存储的密钥而不必每次都提供密钥，可以简化部署。

在 **create** 时若省略 **--public-key**，Azure 会生成新的密钥对，并在命令输出中返回私钥。请立即保存该私钥，因为之后无法再获取。

# CAVEATS

需要已安装并完成身份验证的 Azure CLI；这是核心命令，无需额外扩展。Azure 中只存储公钥。自动生成密钥时，请立即保存返回的私钥。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[azure-cli](/man/azure-cli)(1), [az-vm](/man/az-vm)(1), [ssh-keygen](/man/ssh-keygen)(1)

# RESOURCES

```[Source code](https://github.com/Azure/azure-cli)```

```[Documentation](https://learn.microsoft.com/en-us/cli/azure/sshkey)```

```[Homepage](https://learn.microsoft.com/en-us/cli/azure/)```

<!-- verified: 2026-06-19 -->
