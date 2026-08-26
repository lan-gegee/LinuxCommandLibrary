# TAGLINE

HashiCorp 机密管理工具

# TLDR

**以开发模式启动 Vault 服务器**

```vault server -dev```

**使用令牌登录 Vault**

```vault login [token]```

**向键值存储写入机密**

```vault kv put secret/[path] [key]=[value]```

**读取机密**

```vault kv get secret/[path]```

**列出某路径下的机密**

```vault kv list secret/```

**删除机密**

```vault kv delete secret/[path]```

**启用机密引擎**

```vault secrets enable -path=[path] [engine]```

**查看 Vault 状态**

```vault status```

# SYNOPSIS

**vault** [_global_options_] _command_ [_command_options_] [_arguments_]

# PARAMETERS

**login**
> 向 Vault 进行身份验证并获取令牌。

**kv put**
> 向键值机密引擎写入机密。

**kv get**
> 从键值机密引擎读取机密。

**kv delete**
> 删除键值机密引擎中的机密。

**kv list**
> 列出某路径下的机密键。

**secrets enable**
> 在某路径启用机密引擎。

**secrets disable**
> 禁用机密引擎。

**auth enable**
> 启用一种身份验证方式。

**operator init**
> 初始化新的 Vault 集群。

**operator unseal**
> 解除 Vault 的封锁（unseal）。

**operator seal**
> 封锁 Vault（seal）。

**status**
> 打印 Vault 的当前状态。

**server**
> 启动 Vault 服务器。

**token** _subcommand_
> 管理令牌（capabilities、create、lookup、renew、revoke）。

**policy** _subcommand_
> 管理策略（delete、fmt、list、read、write）。

**audit** _subcommand_
> 管理审计设备（disable、enable、list）。

**lease** _subcommand_
> 管理租约（lookup、renew、revoke）。

**read** _path_
> 从 Vault 读取数据。

**write** _path_ _data_
> 向 Vault 写入数据。

**delete** _path_
> 删除 Vault 中的数据。

**list** _path_
> 列出 Vault 中的数据。

**path-help** _path_
> 显示特定 API 路径的帮助信息。

**-address** _url_
> Vault 服务器地址。

**-token** _token_
> 用于身份验证的 Vault 令牌。

**-format** _format_
> 输出格式：table、json、yaml。

**-help**
> 显示命令的帮助信息。

# DESCRIPTION

HashiCorp 出品的 **Vault** 是一款机密管理工具，可安全存储并控制对令牌、密码、证书、API 密钥等机密的访问。它提供加密即服务、动态机密生成以及详细的审计日志功能。

该 CLI 是 HTTP API 的封装，支持交互式和脚本化使用。配置可通过环境变量设置：**VAULT_ADDR** 指定服务器地址，**VAULT_TOKEN** 用于身份验证，**VAULT_NAMESPACE** 用于企业版命名空间，**VAULT_FORMAT** 指定输出格式（table、json、yaml、jsonx）。

Vault 采用 seal/unseal 机制保障安全。初始化后 Vault 处于封锁状态，需要解封密钥才能投入运行。在开发模式（**vault server -dev**）下，Vault 以未封锁状态启动，便于测试。

# CAVEATS

开发服务器将数据保存在内存中，不可用于生产环境。解封需要达到阈值数量的密钥分片；丢失过多分片可能导致 Vault 无法恢复。令牌管理对安全至关重要；泄露的令牌应立即吊销。

# HISTORY

Vault 由 **HashiCorp** 创建，于 **2015 年 4 月**首次发布。它旨在应对现代基础设施中管理机密的挑战，动态机密、租约和续期等关键特性从一开始就是核心设计。Vault 已发展为支持众多身份验证方式和机密引擎的工具，成为 DevOps 和云原生环境中机密管理的标准工具。

# INSTALL

```pacman: sudo pacman -S vault```

```nix: nix profile install nixpkgs#vault```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[consul](/man/consul)(1), [terraform](/man/terraform)(1), [gpg](/man/gpg)(1), [pass](/man/pass)(1)
