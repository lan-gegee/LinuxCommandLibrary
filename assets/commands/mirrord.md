# TAGLINE

在 Kubernetes 集群的上下文中运行本地代码

# TLDR

**以某个特定 Pod 的身份运行本地二进制**

```mirrord exec --target pod/[pod_name] -- [command] [arguments]```

**以指定命名空间中的部署为目标**

```mirrord exec --target deployment/[deployment_name] --target-namespace [namespace] -- [command]```

**使用配置文件运行**

```mirrord exec --config-file [path/to/mirrord.json] -- [command]```

**将远程端口转发**到本地可达的主机

```mirrord port-forward --target pod/[pod_name] --port-mapping [local_port]:[remote_port]```

**转储目标端口的入站流量**

```mirrord dump --target pod/[pod_name] --ports [8080]```

**交互式生成配置**

```mirrord wizard```

**检查配置与连通性**

```mirrord diagnose```

# SYNOPSIS

**mirrord** _command_ [_options_] [**--** _binary_ [_args_]]

# DESCRIPTION

**mirrord** 让运行在你自己机器上的进程表现得像是在远程 Kubernetes 集群内部运行。它将本地进程连接到选定的目标（Pod 或部署），并透明地中继该目标的网络流量、环境变量、DNS 解析和文件系统，使本地代码观察到与真实工作负载相同的上下文，而无需构建镜像、推送并部署。

其工作原理是在与目标相同的节点上启动一个临时 agent Pod。目标的入站流量可以采用**镜像**方式（副本发送给本地进程，集群继续正常服务）或**窃取**方式（流量被重定向到本地进程）。出站流量、DNS 和文件读取通过 agent 隧道传输，从而按集群的视角解析。本地进程退出时，agent 会被清理，集群恢复到之前的状态。

mirrord 最常通过 **exec** 子命令使用，它可以包装任意命令，但它也提供 VS Code 和 IntelliJ 的编辑器集成，驱动同一引擎。通常在 Shell 中用上游安装脚本安装（`curl -fsSL https://raw.githubusercontent.com/metalbear-co/mirrord/main/scripts/install.sh | bash`），或通过 Homebrew 安装。

# COMMANDS

**exec**

> 在目标上下文中运行本地二进制。**--** 之后的所有内容都是命令及其参数。

**port-forward**

> 将一个或多个集群端口转发到本地机器可访问的主机。

**dump**

> 捕获并打印目标端口看到的入站流量，不运行本地二进制。

**container**

> 在集群上下文中于本地运行容器，相当于 **exec** 对普通二进制的作用。

**operator**

> 管理可选的 mirrord Operator，启用团队功能如队列拆分和共享目标。

**wizard**

> 交互式构建 mirrord 配置文件。

**diagnose**

> 对集群执行连通性和延迟检查，验证设置。

# PARAMETERS

以下参数适用于 **exec**（以及大多数接受目标的子命令）。

**-t**, **--target** _path_

> 要模拟的目标，例如 `pod/my-pod`、`deployment/my-deploy` 或 `pod/my-pod/container/sidecar`。

**-n**, **--target-namespace** _namespace_

> 目标所在命名空间。默认为当前 kubectl 上下文的命名空间。

**-f**, **--config-file** _file_

> 从 JSON、TOML 或 YAML 配置文件加载选项，而非命令行标志。

**-a**, **--agent-namespace** _namespace_

> 创建临时 mirrord agent Pod 的命名空间。

**--steal**

> 重定向（窃取）目标的入站流量到本地进程，而不是镜像副本。

**--fs-mode** _mode_

> 控制文件系统访问的处理方式（例如从远程读取、从本地读取，或两者兼有）。

**-h**, **--help**

> 显示 mirrord 或特定子命令的帮助信息。

# CAVEATS

mirrord 需要访问 Kubernetes 集群并有创建临时 agent Pod 的权限，因此适用于 `kubectl exec` 的注意事项同样适用于此。使用 **--steal** 窃取流量会将真实请求从集群工作负载转移走，可能干扰共享环境；因此镜像方式更安全。文件和网络行为可能与真正的集群内部部署存在细微差异，所以它是暂存测试的补充而非替代。

# HISTORY

mirrord 由 **MetalBear** 开发，以 **MIT** 许可证发布。它主要用 **Rust** 编写，源自移除云原生开发中缓慢的构建-推送-部署循环的想法，让开发者可以从本地机器对实时集群进行调试。项目引用的使用者包括 monday.com、SurveyMonkey 和 Cadence。

# INSTALL

```nix: nix profile install nixpkgs#mirrord```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [docker](/man/docker)(1), [skaffold](/man/skaffold)(1), [helm](/man/helm)(1)

# RESOURCES

```[Source code](https://github.com/metalbear-co/mirrord)```

```[Homepage](https://metalbear.com/mirrord)```

```[Documentation](https://metalbear.com/mirrord/docs)```

<!-- verified: 2026-06-27 -->
