# TAGLINE

安装开发者工具和 Kubernetes 应用的应用市场 CLI

# TLDR

将常用 CLI **下载**到 PATH

```arkade get [kubectl] [kind] [terraform]```

**列出**可用的 CLI 软件包

```arkade get --help```

**安装** Kubernetes 应用（以 OpenFaaS 为例）

```arkade install [openfaas]```

**安装**系统软件包（如 Go）

```arkade system install [go]```

**安装**来自 OCI 镜像的二进制文件

```arkade oci install [ghcr.io/org/tool]```

# SYNOPSIS

**arkade** *command* [*args*]

# DESCRIPTION

**arkade** 用简单的命令安装固定版本的常见开发者 CLI 和 Kubernetes 应用。**arkade get** 下载静态二进制文件（kubectl、helm、terraform、jq 等），无需等待包管理器；**arkade install** 将 chart/应用部署到集群；**arkade system** 和 **arkade oci** 则覆盖主机软件包和镜像打包的工具。由 Alex Ellis / OpenFaaS 社区维护。

# PARAMETERS

**get** *tool*[@version]...

> 将 CLI 二进制文件下载到 arkade 的 bin 目录（通常为 **$HOME/.arkade/bin**）。

**install** *app*

> 以合理的默认值和标志安装 Kubernetes 应用。

**uninstall** *app*

> 移除先前安装的应用。

**system install** *package*

> 安装主机级工具（Go、containerd 等）。

**oci install** *image* [*path*]

> 从 OCI 容器镜像中提取/安装。

**info** / **chart** / **version**

> 内省辅助命令——参见 **arkade --help**。

# CAVEATS

从互联网下载二进制文件需要信任上游发布产物。Kubernetes 安装需要可用的 kubeconfig。请确保 **$HOME/.arkade/bin** 在 PATH 中。

# INSTALL

```zypper: sudo zypper install arkade```

```brew: brew install arkade```

```nix: nix profile install nixpkgs#arkade```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[kubectl](/man/kubectl)(1), [helm](/man/helm)(1), [kind](/man/kind)(1)

# RESOURCES

```[Source code](https://github.com/alexellis/arkade)```

```[Homepage](https://arkade.dev)```

<!-- verified: 2026-07-19 -->
