# TAGLINE

管理 Azure Cache for Redis 实例

# TLDR

**创建 Redis 缓存**

```az redis create --name [MyCache] --resource-group [MyResourceGroup] --location [eastus] --sku [Basic] --vm-size [c0]```

**列出资源组中的所有 Redis 缓存**

```az redis list --resource-group [MyResourceGroup]```

**显示**某个 Redis 缓存的**详情**

```az redis show --name [MyCache] --resource-group [MyResourceGroup]```

**列出访问密钥**

```az redis list-keys --name [MyCache] --resource-group [MyResourceGroup]```

**重新生成访问密钥**

```az redis regenerate-keys --name [MyCache] --resource-group [MyResourceGroup] --key-type [Primary]```

**更新缓存设置**

```az redis update --name [MyCache] --resource-group [MyResourceGroup] --set redisConfiguration.maxmemory-policy=allkeys-lru```

**强制重启**指定的 Redis 节点

```az redis force-reboot --name [MyCache] --resource-group [MyResourceGroup] --reboot-type [AllNodes]```

清空 Redis 缓存中的**所有键**

```az redis flush --name [MyCache] --resource-group [MyResourceGroup] --yes```

**删除 Redis 缓存**

```az redis delete --name [MyCache] --resource-group [MyResourceGroup] --yes```

# SYNOPSIS

**az** **redis** _subcommand_ [_options_]

# SUBCOMMANDS

**create**
> 创建 Redis 缓存。

**delete**
> 删除 Redis 缓存。

**list**
> 列出 Redis 缓存。

**show**
> 获取 Redis 缓存的详情。

**update**
> 更新 Redis 缓存。

**list-keys**
> 检索访问密钥。

**regenerate-keys**
> 重新生成访问密钥。

**flush**
> 删除 Redis 缓存中的所有键。

**force-reboot**
> 重启指定的 Redis 节点。

**import**
> 向 Redis 缓存导入数据。

**export**
> 从 Redis 缓存导出数据。

**firewall-rules**
> 管理防火墙规则。

**patch-schedule**
> 管理修补计划。

**server-link**
> 管理 Redis 服务器链接（需要 Premium SKU）。

**identity**
> 管理分配给 Azure Cache for Redis 的标识。

**access-policy**
> 管理 Redis 缓存的访问策略。

**access-policy-assignment**
> 管理访问策略分配（Redis 用户）。

# PARAMETERS

**--name** **-n**
> Redis 缓存的名称。

**--resource-group** **-g**
> 资源组的名称。

**--sku**
> SKU 层级：Basic、Standard 或 Premium。

**--vm-size**
> 要部署的 Redis 缓存大小。Basic 和 Standard 大小以 c 开头（c0-c6）。Premium 大小以 p 开头（p1-p5）。

**--location** **-l**
> 缓存的位置。

**--minimum-tls-version**
> 指定客户端连接缓存所需的 TLS 版本（1.0、1.1、1.2）。

**--redis-version**
> Redis 版本，格式为 'major[.minor]' 或 'latest'。默认值为 'latest'。

**--yes** **-y**
> 不提示确认（与 delete 和 flush 一起使用）。

# DESCRIPTION

**az redis** 管理 Azure Cache for Redis，这是一种基于 Redis 的完全托管内存数据存储。它为应用程序提供低延迟、高吞吐量的缓存。

可用的 SKU 有 Basic（单节点）、Standard（带副本）和 Premium（支持群集、持久化、虚拟网络）。

# CAVEATS

需要安装 Azure CLI 并已完成身份验证。缓存创建可能需要几分钟。群集和异地复制等 Premium 功能需要 Premium SKU。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [redis-cli](/man/redis-cli)(1)
