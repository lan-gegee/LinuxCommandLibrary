# TAGLINE

Scaleway 云基础设施 CLI

# TLDR

**登录** / 配置 profile

```scw init```

**列出**实例

```scw instance server list```

**创建**小型实例

```scw instance server create type=[DEV1-S] image=[ubuntu_noble] zone=[fr-par-1]```

**Kubernetes** 集群助手

```scw k8s cluster list```

# SYNOPSIS

**scw** *product* *resource* *command* [*args*]

# DESCRIPTION

**scw** 是 Scaleway 官方 CLI（v2），用于在终端管理云资源——实例、对象存储、Kubernetes（Kapsule）、网络等。层级化的命令结构对应 Scaleway API。文档：https://cli.scaleway.com/

# PARAMETERS

**init**

> 交互式配置访问密钥以及默认 zone/region。

*product* *resource* *verb*

> 例如 **instance server list**、**object list**。

**-o** *json*|*yaml*|*human*

> 输出格式（常用的全局选项）。

**--help**

> 在任意命令层级显示上下文相关的帮助。

# CAVEATS

需要 Scaleway API 密钥；请安全保存。资源名称和 SKU 可能变化——请查阅当前产品文档。创建付费资源会产生云服务费用。

# INSTALL

```pacman: sudo pacman -S scaleway-cli```

```apk: sudo apk add scaleway-cli```

```brew: brew install scw```

```nix: nix profile install nixpkgs#scaleway-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [doctl](/man/doctl)(1), [kubectl](/man/kubectl)(1)

# RESOURCES

```[Source code](https://github.com/scaleway/scaleway-cli)```

```[Documentation](https://cli.scaleway.com/)```

<!-- verified: 2026-07-19 -->
