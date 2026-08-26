# TAGLINE

Proxmox VE 订阅密钥管理器

# TLDR

**显示**当前订阅信息

```pvesubscription get```

**设置**订阅密钥

```pvesubscription set pveXc-xxxxxxxxxx```

从服务器**更新**订阅信息

```pvesubscription update```

即使本地缓存仍然有效也强制刷新

```pvesubscription update --force```

从此节点上**删除**订阅密钥

```pvesubscription delete```

# SYNOPSIS

**pvesubscription** _COMMAND_ [_ARGS_] [_OPTIONS_]

# PARAMETERS

**get**
> 读取此节点的订阅信息

**set** _key_
> 设置 Proxmox VE 订阅密钥

**update**
> 从许可证服务器刷新订阅信息

**--force**
> 与 **update** 搭配使用：即使本地缓存仍然有效也始终联系服务器

**delete**
> 从此节点移除订阅密钥

**help**
> 显示 pvesubscription 或某个子命令的帮助

# DESCRIPTION

**pvesubscription** 管理节点上的 Proxmox VE 订阅密钥。有效的订阅可以访问企业软件仓库和官方支持渠道。没有订阅时，节点通常改用免费的 no-subscription 软件仓库。

该工具可以安装或移除密钥、显示当前状态，以及从 Proxmox 服务器刷新验证数据。离线密钥处理仅限内部使用；对于离线环境，Proxmox 另有专门的离线镜像工具文档。

# CAVEATS

订阅密钥与特定节点绑定，不应在无关的机器之间共享。移除密钥或在无订阅状态下运行不会卸载 Proxmox VE 本身，但企业仓库访问权限和支持权益会发生变化。更改订阅状态后务必检查软件仓库配置。

# HISTORY

**pvesubscription** 是 **Proxmox VE** 管理 CLI 套件的一部分，用于管理商业订阅许可证。

# SEE ALSO

[pvenode-config](/man/pvenode-config)(1), [pveversion](/man/pveversion)(1), [apt](/man/apt)(8)

# RESOURCES

```[Documentation](https://pve.proxmox.com/pve-docs/pvesubscription.1.html)```

```[Homepage](https://www.proxmox.com)```

<!-- verified: 2026-07-16 -->
