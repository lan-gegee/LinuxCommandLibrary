# TAGLINE

用于 Proxmox VE 集群管理的终端 UI

# TLDR

**启动 Proxmox VE TUI**

```pvetui```

# SYNOPSIS

**pvetui** [_options_]

# DESCRIPTION

**pvetui** 是一个用于管理 Proxmox VE 集群、节点、虚拟机和 LXC 容器的终端用户界面。它支持启动、停止、迁移和监控资源，通过 API 令牌或密码进行安全认证，集成 SSH shell，带有嵌入式 noVNC 客户端的 VNC 控制台访问，多集群配置文件切换，以及插件扩展（包括社区脚本安装器）。

# CAVEATS

需要能够通过网络访问 Proxmox VE 实例，并具备有效的身份验证凭据。

# HISTORY

**pvetui** 由 **devnullvoid** 创建，使用 **Go** 编写。

# INSTALL

```zypper: sudo zypper install pvetui```

```brew: brew install pvetui```

```nix: nix profile install nixpkgs#pvetui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ssh](/man/ssh)(1), [virsh](/man/virsh)(1), [virsh-help](/man/virsh-help)(1)
