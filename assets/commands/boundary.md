# TAGLINE

基于身份的安全基础设施远程访问工具。

# TLDR

**向 Boundary 认证**

```boundary authenticate```

**连接到目标**

```boundary connect -target-id [ttcp_1234567890]```

**使用 SSH 辅助器连接**

```boundary connect ssh -target-id [ttcp_1234567890]```

**列出可用目标**

```boundary targets list -recursive```

**列出活动会话**

```boundary sessions list -recursive```

**读取目标详情**

```boundary targets read -id [ttcp_1234567890]```

**取消一个会话**

```boundary sessions cancel -id [s_1234567890]```

**启动本地代理**

```boundary connect -target-id [ttcp_1234567890] -listen-port [2222]```

# SYNOPSIS

**boundary** _command_ [_options_]

# COMMANDS

**authenticate**
> 向 Boundary 控制器认证。

**connect** [_helper_]
> 建立与目标的连接。辅助器：ssh、postgres、rdp、http、kube。

**targets** list|read
> 列出或查看目标。

**sessions** list|read|cancel
> 管理活动会话。

**hosts** list|read
> 查看主机目录中的主机。

**host-catalogs** list|read
> 查看主机目录。

**scopes** list|read
> 查看组织作用域。

**accounts** list|read|create|update|delete
> 管理账户。

**auth-methods** list|read
> 查看认证方式。

**roles** list|read
> 查看角色和权限。

**groups** list|read
> 查看组。

**users** list|read
> 查看用户。

**logout**
> 清除存储的凭据。

**version**
> 显示版本信息。

# PARAMETERS

**-target-id** _id_
> 要连接的目标 ID。

**-target-name** _name_
> 目标名称（需要指定作用域）。

**-target-scope-id** _id_
> 包含目标的作用域。

**-target-scope-name** _name_
> 包含目标的作用域名称。

**-listen-port** _port_
> 代理连接使用的本地端口。

**-addr** _address_
> Boundary 控制器地址。

**-token** _token_
> 认证令牌。

**-token-name** _name_
> 用于存储的令牌名称。

**-scope-id** _id_
> 操作所针对的作用域 ID。

**-recursive**
> 递归列出所有作用域中的资源。

**-format** _format_
> 输出格式：table、json。

**-keyring-type** _type_
> 凭据存储使用的密钥环类型。

# DESCRIPTION

**boundary** 是 HashiCorp Boundary 的 CLI。Boundary 是一款基础设施安全远程访问工具，提供基于身份的主机和服务访问，无需暴露网络或直接管理凭据。

**connect** 命令建立与目标的会话。特定协议的辅助器（ssh、postgres、rdp、http、kube）会自动为客户端工具配置正确的凭据。对 SSH 而言，它会生成一个注入了凭据的 ssh 进程；对数据库而言，它会提供连接字符串。

认证方式包括密码、OIDC 和 LDAP。凭据存储在系统密钥环或指定的位置。使用 **authenticate** 登录，使用 **logout** 清除凭据。

Boundary 采用分层作用域模型，包含全局（global）、组织（organization）和项目（project）三级作用域。使用 **-recursive** 可列出所有可访问作用域中的资源。

会话维护客户端与目标之间的连接状态。可以列出并取消活动会话。配置后，会话录制可用于审计与合规。

# CAVEATS

需要能访问 Boundary 控制器。目标必须由具有相应权限的管理员预先配置。连接辅助器要求安装对应的客户端工具（ssh、psql 等）。部分功能需要 Boundary Enterprise 或 HCP Boundary。

# HISTORY

Boundary 由 **HashiCorp** 于 **2020 年 10 月**发布，是与 Vault 并列的安全产品线成员。它面向现代的基于身份的访问模式，用以取代传统 VPN 和堡垒机。0.1 版于 **2020 年 10 月**发布。项目在 **2022 年**达到 1.0 GA 状态。Boundary 与 Vault 集成实现凭据代理和注入，为基础设施提供即时访问能力。

# INSTALL

```nix: nix profile install nixpkgs#boundary```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vault](/man/vault)(1), [ssh](/man/ssh)(1), [tsh](/man/tsh)(1), [kubectl](/man/kubectl)(1)

# RESOURCES

```[Source code](https://github.com/hashicorp/boundary)```

```[Homepage](https://developer.hashicorp.com/boundary)```

```[Documentation](https://developer.hashicorp.com/boundary/docs)```

<!-- verified: 2026-06-19 -->
