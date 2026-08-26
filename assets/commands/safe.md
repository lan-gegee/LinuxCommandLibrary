# TAGLINE

简化的 HashiCorp Vault 命令行工具

# TLDR

**写入机密**

```safe set [secret/path] [key]=[value]```

**读取机密**

```safe get [secret/path]```

以树状结构**列出所有机密路径**

```safe tree```

**删除机密**

```safe rm [secret/path]```

**指定 Vault 服务器**

```safe target [https://vault-url] [alias]```

对当前 Vault 进行**身份验证**

```safe auth [ldap|token|github]```

**将机密复制到新路径**

```safe cp [secret/old/path] [secret/new/path]```

**生成随机密码**

```safe gen [secret/path] [key]```

# SYNOPSIS

**safe** _command_ [_options_] [_args_]

# PARAMETERS

**set**（别名：**write**）
> 在指定路径写入或更新机密。

**get**（别名：**read**）
> 读取并显示机密。

**rm**（别名：**delete**）
> 删除一个或多个机密路径。

**tree**
> 以树状列表打印所有可达的键。

**paths**
> 以平铺列表打印所有可达的键。

**target**
> 设置或列出 Vault 目标。

**auth**
> 对当前指定的 Vault 进行身份验证。

**export**
> 将机密导出到备份文件。

**import**
> 从备份文件导入机密。

**cp**（别名：**copy**）
> 将机密从一个路径复制到另一个路径。

**mv**（别名：**move**）
> 将机密从一个路径移动到另一个路径。

**gen**
> 生成随机机密。

**ssh**
> 生成新的 SSH RSA 密钥对。

**rsa**
> 生成新的 RSA 密钥对。

# DESCRIPTION

**safe** 是一款面向 HashiCorp Vault 的易用命令行界面，简化了常见的机密管理操作。它用直观的命令封装了 Vault API，无需掌握完整的 Vault CLI 语法即可读取、写入和组织机密。

该工具支持多种认证方式，包括 LDAP、GitHub token 和直接的 token 认证。在指定并认证某个 Vault 服务器后，即可使用 **set**、**get**、**rm** 等简单命令管理机密。**tree** 命令提供所有机密路径的层级视图，便于浏览。

机密可以导出和导入，用于备份或在 Vault 实例之间迁移。**target** 命令管理与多个 Vault 服务器的连接，可在不同环境间快速切换。

# CAVEATS

需要 Vault 访问权限。需要认证。权限因配置而异。

# HISTORY

**safe** 由 Stark & Wayne 开发，是 HashiCorp Vault 的易用命令行工具，用于简化机密管理操作。

# INSTALL

```nix: nix profile install nixpkgs#safe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vault](/man/vault)(1), [pass](/man/pass)(1), [aws](/man/aws)(1)
