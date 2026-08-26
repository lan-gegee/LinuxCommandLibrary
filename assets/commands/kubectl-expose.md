# TAGLINE

为资源创建 service

# TLDR

**暴露 deployment**

```kubectl expose deployment [name] --port=[80]```

**以指定类型暴露**

```kubectl expose deployment [name] --port=[80] --type=[LoadBalancer]```

**暴露 Pod**

```kubectl expose pod [pod-name] --port=[8080] --target-port=[80]```

**以指定名称暴露**

```kubectl expose deployment [name] --port=[80] --name=[service-name]```

**暴露 NodePort**

```kubectl expose deployment [name] --port=[80] --type=[NodePort]```

# SYNOPSIS

**kubectl expose** [_options_] _resource_ _name_

# PARAMETERS

_RESOURCE_
> 要暴露的资源类型。

_NAME_
> 资源名称。

**--port** _PORT_
> Service 端口。

**--target-port** _PORT_
> 容器端口。

**--type** _TYPE_
> Service 类型（ClusterIP、NodePort、LoadBalancer）。

**--name** _NAME_
> Service 名称。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl expose** 创建一个 Kubernetes Service，为一组由 deployment、replica set、Pod 或其他资源管理的 Pod 提供稳定的网络访问。它通过检查目标资源的标签和端口定义自动生成 service 配置，创建基于选择器的 service，无需手动编写清单。

该命令支持四种 service 类型：ClusterIP（默认）用于集群内部访问；NodePort 用于在每个节点的 IP 上以静态端口暴露服务；LoadBalancer 用于通过云服务商配置外部负载均衡器；ExternalName 用于映射到 DNS 名称。`--port` 标志设置 service 的监听端口，而 `--target-port` 指定要转发流量的容器端口。

这种方式便于在开发或原型设计期间快速创建 service。在生产环境中，建议在清单文件中以声明式方式与工作负载定义一起定义 service，以获得更好的可复现性和版本控制。

# CAVEATS

kubectl 的子命令。Service 类型影响可访问性。考虑使用清单文件。

# HISTORY

kubectl expose 为 **Kubernetes** 工作负载网络提供快速的 service 创建能力。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-create](/man/kubectl-create)(1), [kubectl-run](/man/kubectl-run)(1)
