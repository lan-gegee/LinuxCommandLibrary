# TAGLINE

检查 Flux 的前置条件和已安装控制器的健康状况

# TLDR

在引导安装 Flux 之前**检查前置条件**

```flux check --pre```

**检查集群上 Flux 安装的状态**

```flux check```

仅**检查特定组件**

```flux check --components=source-controller,kustomize-controller```

**包含额外组件**（例如镜像自动化）

```flux check --components-extra=image-reflector-controller,image-automation-controller```

# SYNOPSIS

**flux** **check** [_options_]

# DESCRIPTION

**flux check** 验证当前机器是否满足运行 Flux 的前置条件，以及（在连接到集群时）Flux 控制器是否健康就绪。

`--pre` 执行客户端侧检查（kubectl、权限、网络等），通常在 `flux bootstrap` 之前运行。

不带 `--pre` 时会连接集群并报告已安装的 Flux 组件状态。

# PARAMETERS

**--pre**
> 仅执行预安装检查（大多数检查不需要连接集群）。

**--components** _list_
> 要检查的组件列表（逗号分隔）（默认 `source-controller,kustomize-controller,helm-controller,notification-controller`）。

**--components-extra** _list_
> 在指定或默认组件之外额外检查的组件（逗号分隔）。

**--poll-interval** _duration_
> 健康检查器轮询集群资源状态的频率（默认 `5s`）。

**--timeout** _duration_
> 操作超时时间（默认 `5m0s`）。

**-n**, **--namespace** _ns_
> CLI 请求的命名空间范围（默认 `flux-system`）。

# INSTALL

```apk: sudo apk add flux```

```brew: brew install flux```

```nix: nix profile install nixpkgs#flux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flux](/man/flux)(1), [flux-bootstrap](/man/flux-bootstrap)(1)

# RESOURCES

```[Source code](https://github.com/fluxcd/flux2)```

```[Documentation](https://fluxcd.io/flux/cmd/flux_check/)```

<!-- verified: 2026-07-11 -->
