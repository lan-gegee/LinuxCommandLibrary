# TAGLINE

在本地构建 Flux 清单以便检查或管道传给 kubectl

# TLDR

**构建 Kustomization** 并打印生成的清单

```flux build kustomization my-app --path ./path/to/local/manifests```

**使用本地的 Flux Kustomization 文件构建**而不改动集群状态

```flux build kustomization my-app --path ./path/to/local/manifests --kustomization-file ./my-app.yaml --dry-run```

**构建后直接应用**

```flux build kustomization my-app --path ./kustomize | kubectl apply -f -```

**将清单打包成 artifact** 压缩包

```flux build artifact --path ./path/to/local/manifests --output ./artifact.tgz```

# SYNOPSIS

**flux** **build** **kustomization** _name_ **--path** _path_ [_options_]

**flux** **build** **artifact** **--path** _path_ [_options_]

# DESCRIPTION

**flux build** 使用与控制器兼容的逻辑在本地渲染 Flux 资源，不会将其应用到集群。支持的子命令有 **kustomization** 和 **artifact**。

**flux build kustomization** 获取（或加载）一个 Flux Kustomization，将其变换应用到 `--path` 处的本地清单，并将生成的多文档 YAML 写到标准输出。适用于预览部署、调试 overlay 或管道传给 `kubectl`。

**flux build artifact** 将目录或单个清单文件打包成适用于 source/OCI 工作流的 `.tgz` artifact。

# PARAMETERS

**kustomization** _name_
> 基于本地清单构建指定的 Flux Kustomization。

**artifact**
> 从本地 Kubernetes 清单打包压缩档。

**-n**, **--namespace** _ns_
> 命名空间范围（默认 `flux-system`）。

**--timeout** _duration_
> 操作超时时间（默认 `5m0s`）。

**--path** _path_ （kustomization 与 artifact）
> 本地清单/kustomization 目录的路径；artifact 构建时为单个文件的路径。

**--kustomization-file** _file_
> 本地 Flux Kustomization YAML 的路径，而不是从集群获取。

**--dry-run**
> 试运行模式，不连接集群。来自 Secret 和 ConfigMap 的变量替换会被跳过。

**--recursive**, **-r**
> 递归构建遇到的 Kustomization。

**--local-sources** _Kind/namespace/name=path,..._
> 将远程源映射到本地路径以进行递归构建（例如 `GitRepository/flux-system/my-repo=./path/to/local/git`）。

**--ignore-paths** _patterns_
> 要排除的 `.gitignore` 风格路径（逗号分隔）。

**--strict-substitute**
> 当声明的变量既没有默认值又不在输入变量中时，构建后的替换失败报错。

**--in-memory-build**
> 构建期间使用内存文件系统（kustomization）。

**-o**, **--output** _file_
> artifact 压缩包的输出路径（默认 `artifact.tgz`）。

**--resolve-symlinks**
> 解析符号链接，将其目标复制进 artifact 中。

# INSTALL

```apk: sudo apk add flux```

```brew: brew install flux```

```nix: nix profile install nixpkgs#flux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flux](/man/flux)(1), [flux-create](/man/flux-create)(1), [kustomize](/man/kustomize)(1)

# RESOURCES

```[Source code](https://github.com/fluxcd/flux2)```

```[Documentation](https://fluxcd.io/flux/cmd/flux_build/)```

<!-- verified: 2026-07-11 -->
