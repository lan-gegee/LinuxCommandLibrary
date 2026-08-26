# TAGLINE

为网络设备配置初始化版本控制

# TLDR

**为所有已定义的 RANCID 组初始化 CVS 仓库**

```rancid-cvs```

**向 CVS 仓库添加新组**（先添加到 rancid.conf）

```rancid-cvs```

# SYNOPSIS

**rancid-cvs**

# DESCRIPTION

**rancid-cvs** 为 RANCID（Really Awesome New Cisco Config Differ）初始化并维护版本控制仓库结构。它为 RANCID 配置中定义的每个设备组创建必要的目录和 CVS/Subversion 仓库。

RANCID 是一个网络设备配置管理工具，可自动备份路由器、交换机和防火墙（Cisco、Juniper、HP 等）的配置，在版本控制中跟踪变更，并在配置变化时发送邮件通知。

该命令从 **/etc/rancid/rancid.conf** 读取 LIST_OF_GROUPS 变量，并在 RANCID 主目录（通常为 /var/lib/rancid）下创建相应的目录结构。每个组都有自己的子目录和 CVS 工作目录。

在初次安装 RANCID 后以及每次向配置添加新设备组时运行此命令。重新运行时不会覆盖已有的组。

# CONFIGURATION

**/etc/rancid/rancid.conf**
> RANCID 主配置文件，定义 LIST_OF_GROUPS、RCSSYS（cvs 或 svn）、邮件别名和工作目录路径。

**router.db**
> 每个组的设备清单文件，列出设备主机名、类型和状态（up/down），用于配置采集。

**RCSSYS**
> rancid.conf 中的变量，用于选择版本控制后端（cvs 或 svn）。

# CAVEATS

必须以 **rancid** 用户身份运行，而不是 root。该命令要求对 RANCID 目录和 CVS 仓库具有正确的权限。

需要安装并配置 CVS 或 Subversion。仓库类型由 rancid.conf 中的 RCSSYS 变量决定。

该命令不配置设备或凭据。设备定义必须单独添加到各组的 **router.db** 文件中。

# HISTORY

RANCID 最初由 Henry Kilmer 和 John Heasley 在 **Shrubbery Networks** 开发。"Really Awesome New Cisco Config Differ" 这个名字反映了它最初专注于 Cisco 的定位，不过现在已支持众多网络设备厂商。开发始于 20 世纪 90 年代末，当时各组织需要自动化的配置备份和变更跟踪。

# INSTALL

```apt: sudo apt install rancid```

```dnf: sudo dnf install rancid```

```apk: sudo apk add rancid```

```brew: brew install rancid```

```nix: nix profile install nixpkgs#rancid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rancid-run](/man/rancid-run)(1), [cvs](/man/cvs)(1), [svn](/man/svn)(1), [clogin](/man/clogin)(1)
