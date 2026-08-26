# TAGLINE

Vultr API 官方命令行客户端

# TLDR

**列出区域**

```vultr-cli regions```

**列出套餐**

```vultr-cli plans```

**列出实例**

```vultr-cli instance list```

**账户信息**

```vultr-cli account```

**JSON 输出**

```vultr-cli -o json instance list```

**显示版本**

```vultr-cli version```

**查看某个资源的帮助**

```vultr-cli instance --help```

# SYNOPSIS

**vultr-cli** [*flags*] *command*

# DESCRIPTION

**vultr-cli** 是 [Vultr](https://www.vultr.com/) 云服务的官方命令行界面。它覆盖账户与计费、实例、裸金属、块存储和对象存储、DNS、防火墙、Kubernetes、负载均衡器、快照、SSH 密钥、VPC、CDN、数据库等。

可通过 GitHub releases、**go install github.com/vultr/vultr-cli/v3@latest**、发行版软件包（例如 Arch 上的 **pacman -S vultr-cli**）、Homebrew 或 Docker 安装。使用 Vultr API 密钥进行身份验证（配置的环境变量/文件见项目文档）。

# PARAMETERS

全局选项：

**-o**, **--output** text|json|yaml

> 输出格式（默认为 **text**）。

**--config** *path*

> 配置文件的路径。

资源命令（每个都有诸如 **list**、**create**、**delete** 的子命令）：**account**、**apps**、**backups**、**bare-metal**、**billing**、**block-storage**、**cdn**、**container-registry**、**database**、**dns**、**firewall**、**inference**、**instance**、**iso**、**kubernetes**、**load-balancer**、**logs**、**marketplace**、**object-storage**、**os**、**plans**、**regions**、**reserved-ip**、**script**、**snapshot**、**ssh-key**、**user**、**vpc**、**version**、**completion**。

使用 **vultr-cli** *command* **--help** 查看选项和示例。

# CONFIGURATION

需要具有相应权限的 Vultr API 令牌。建议使用环境变量或配置文件存储，而不是 shell 历史。确切的变量名和文件名请查阅你所安装版本的官方文档。

# CAVEATS

破坏性的实例和存储命令不可逆。API 有速率限制。当 Vultr 新增 API 资源时应保持 CLI 更新。

# INSTALL

```dnf: sudo dnf install vultr-cli```

```pacman: sudo pacman -S vultr-cli```

```brew: brew install vultr-cli```

```nix: nix profile install nixpkgs#vultr-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl](/man/doctl)(1), [linode-cli](/man/linode-cli)(1), [hcloud](/man/hcloud)(1), [aws](/man/aws)(1)

# RESOURCES

```[Source code](https://github.com/vultr/vultr-cli)```

<!-- verified: 2026-07-19 -->
