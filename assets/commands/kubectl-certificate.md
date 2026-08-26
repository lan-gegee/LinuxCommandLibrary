# TAGLINE

管理 Kubernetes 中的证书签名请求

# TLDR

**批准证书签名请求**

```kubectl certificate approve [csr-name]```

**拒绝证书签名请求**

```kubectl certificate deny [csr-name]```

**批准所有待处理的证书签名请求**

```kubectl get csr -o name | xargs kubectl certificate approve```

**以指定原因拒绝 CSR**

```kubectl certificate deny [csr-name] --reason="[Expired certificate]"```

**列出证书签名请求**

```kubectl get csr```

# SYNOPSIS

**kubectl** **certificate** _subcommand_ [_options_]

# PARAMETERS

**approve** _name_
> 批准证书签名请求。

**deny** _name_
> 拒绝证书签名请求。

**--reason** _string_
> 批准或拒绝 CSR 的原因，存储在状态条件中。

**--force**
> 即使 CSR 已被批准或拒绝也进行更新。

**--allow-missing-template-keys**
> 如果为 true，当字段或映射键缺失时忽略模板中的错误。默认为 true。

**-o, --output** _format_
> 输出格式。可选：json、yaml、name、go-template、go-template-file、template、templatefile、jsonpath、jsonpath-as-json、jsonpath-file。

# DESCRIPTION

**kubectl certificate** 管理 Kubernetes 中的证书签名请求（CSR）。用于批准或拒绝 kubelet 客户端证书及其他 TLS 证书的 CSR，是集群 PKI 管理的一部分。当新节点加入集群时，它会生成一个 CSR，必须先获得批准节点才能与 API 服务器通信。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-get](/man/kubectl-get)(1), [kubectl-auth](/man/kubectl-auth)(1), [kubectl-config](/man/kubectl-config)(1)
