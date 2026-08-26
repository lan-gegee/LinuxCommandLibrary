# TAGLINE

Kubernetes 的 cert-manager CLI

# TLDR

**检查 cert-manager 状态**

```cmctl check api```

**查看证书状态**

```cmctl status certificate [cert-name]```

**续期证书**

```cmctl renew [cert-name]```

**批准证书请求**

```cmctl approve [request-name]```

**拒绝证书请求**

```cmctl deny [request-name]```

**检查证书**

```cmctl inspect secret [secret-name]```

**显示版本**

```cmctl version```

# SYNOPSIS

**cmctl** _command_ [_options_]

# DESCRIPTION

**cmctl** 是与 cert-manager（Kubernetes 证书管理控制器）交互的官方命令行工具。它提供用于检查 API 就绪状态、查看证书状态、触发续期以及批准或拒绝证书请求的命令。

该工具还可以作为 kubectl 插件安装，从而以 **kubectl cert-manager** 的形式使用。它简化了那些原本需要用 kubectl 手动创建或编辑 Kubernetes 资源的常见 cert-manager 操作。

cmctl 对调试证书问题尤其有用，因为 **status** 和 **inspect** 命令能提供有关证书链、到期日期和签发条件的详细信息，而这些信息通过标准 kubectl 输出并不容易看到。

# COMMANDS

**check** api
> 验证 cert-manager API 是否就绪

**status** certificate _name_
> 显示证书状态

**renew** _name_
> 将证书标记为待续期

**approve** _name_
> 批准 CertificateRequest

**deny** _name_
> 拒绝 CertificateRequest

**inspect** secret _name_
> 显示证书详情

**create** certificaterequest
> 创建证书请求

**convert**
> 在 API 版本之间转换

**upgrade**
> 升级辅助工具

**version**
> 显示版本

# PARAMETERS

**-n**, **--namespace** _ns_
> Kubernetes 命名空间

**--context** _ctx_
> Kubernetes context

**--kubeconfig** _file_
> kubeconfig 文件路径

# INSTALLATION

```
go install github.com/cert-manager/cmctl/v2@latest
```

或从 GitHub releases 下载。

# CAVEATS

需要在集群中安装 cert-manager。支持 Tab 自动补全。建议优先使用独立工具而非 kubectl 插件，以获得更好的体验。

# INSTALL

```pacman: sudo pacman -S cmctl```

```apk: sudo apk add cmctl```

```zypper: sudo zypper install cmctl```

```brew: brew install cmctl```

```nix: nix profile install nixpkgs#cmctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [openssl](/man/openssl)(1)

# RESOURCES

```[Source code](https://github.com/cert-manager/cmctl)```

```[Documentation](https://cert-manager.io/docs/reference/cmctl/)```

<!-- verified: 2026-06-22 -->
