# TAGLINE

加密 Kubernetes 密钥以便安全存储

# TLDR

**加密 secret**

```kubeseal < [secret.yaml] > [sealed-secret.yaml]```

**指定控制器名称加密**

```kubeseal --controller-name=[sealed-secrets] < [secret.yaml]```

**加密特定命名空间**

```kubeseal --namespace=[namespace] < [secret.yaml]```

**获取证书**

```kubeseal --fetch-cert > [cert.pem]```

**从字面值加密**

```kubectl create secret generic [name] --dry-run=client -o yaml | kubeseal```

# SYNOPSIS

**kubeseal** [_options_]

# PARAMETERS

**--controller-name** _NAME_
> Sealed Secrets 控制器的名称。

**--controller-namespace** _NS_
> 控制器所在的命名空间。

**--namespace** _NS_
> 目标命名空间。

**--fetch-cert**
> 获取公钥证书。

**--format** _FMT_
> 输出格式（yaml、json）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubeseal** 是一个客户端工具，用于将 Kubernetes Secret 资源加密为可安全存入版本控制的 SealedSecret 对象。它使用非对称加密，公钥取自集群中运行的 Sealed Secrets 控制器，从而确保只有该控制器能把数据解密回可用的 Secret。

该工具从 stdin 或文件读取标准的 Kubernetes Secret，对其进行加密，并输出 YAML 或 JSON 格式的 SealedSecret 自定义资源。这使得 GitOps 工作流成为可能：包括密钥在内的所有集群配置都可以提交到 Git 仓库，而不暴露敏感值。每个 SealedSecret 默认限定于特定的命名空间和集群，防止加密数据跨环境复用。

# CAVEATS

需要 Sealed Secrets 控制器。加密与特定集群绑定。请谨慎备份密钥。

# HISTORY

kubeseal 是 Bitnami 的 **Sealed Secrets** 项目的组成部分，用于 GitOps 工作流中的安全密钥管理。

# INSTALL

```pacman: sudo pacman -S kubeseal```

```zypper: sudo zypper install kubeseal```

```brew: brew install kubeseal```

```nix: nix profile install nixpkgs#kubeseal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [sops](/man/sops)(1), [vault](/man/vault)(1)
