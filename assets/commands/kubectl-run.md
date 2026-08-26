# TAGLINE

创建并运行 Pod

# TLDR

**运行 Pod**

```kubectl run [pod-name] --image=[nginx]```

**运行交互式 Pod**

```kubectl run [pod-name] --image=[busybox] -it --rm -- [/bin/sh]```

**带端口运行**

```kubectl run [pod-name] --image=[nginx] --port=[80]```

**带环境变量运行**

```kubectl run [pod-name] --image=[nginx] --env="[KEY=value]"```

**试运行输出**

```kubectl run [pod-name] --image=[nginx] --dry-run=client -o yaml```

**带命令运行**

```kubectl run [pod-name] --image=[busybox] -- [echo hello]```

# SYNOPSIS

**kubectl run** [_options_] _name_ **--image=**_image_

# PARAMETERS

_NAME_
> Pod 名称。

**--image** _IMAGE_
> 容器镜像。

**-it**
> 交互式 TTY。

**--rm**
> 会话结束后删除 Pod。

**--port** _PORT_
> 容器端口。

**--env** _VAR=VALUE_
> 环境变量。

**--dry-run** _MODE_
> `none`、`client` 或 `server` — `client` 不联系 API 直接打印清单；`server` 针对集群进行校验。

**--restart** _POLICY_
> `Always`（默认）、`OnFailure` 或 `Never`。`Never` 生成裸 Pod；其他值会相应调整生成的 PodSpec。

**--command**
> 将 `--` 之后的额外参数视为容器的 `command`（入口点），而不是镜像入口点的参数。

**--labels**, **-l** _KEY=VALUE,..._
> 以逗号分隔的标签，设置在 Pod 上。

**-o** _FORMAT_
> 输出格式：yaml、json、name、jsonpath 等。与 `--dry-run=client -o yaml` 结合可生成清单模板。

**--image-pull-policy** _POLICY_
> `Always`、`IfNotPresent` 或 `Never`。

**--overrides** _JSON_
> 应用于生成的 PodSpec 的 JSON merge patch，用于设置未以标志形式暴露的字段。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl run** 从指定的容器镜像在集群中创建并启动单个 Pod。它专为快速、临时的 Pod 创建而设计，常用于调试、运行一次性任务以及在不编写完整清单文件的情况下测试容器镜像。

该命令支持使用 `-it` 的交互模式，将终端会话直接连接到容器，适合用 busybox 或 curl 等工具启动临时排查用的 Pod。配合 `--rm` 使用时，Pod 会在会话结束后自动删除。`--dry-run=client -o yaml` 模式经常用于生成 Pod 清单模板，之后可以自定义并单独应用。

在较早的 Kubernetes 版本中，`kubectl run` 可以创建 deployment 和其他资源类型，但现在只创建独立的 Pod。对于生产工作负载，请改用 deployment、statefulset 或 job，以获得副本、滚动更新和自愈能力。

# CAVEATS

kubectl 的子命令。现在只能创建 Pod。生产环境请使用 deployment。

# HISTORY

kubectl run 为 **Kubernetes** 测试和调试提供快速的 Pod 创建能力。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-create](/man/kubectl-create)(1), [kubectl-exec](/man/kubectl-exec)(1)
