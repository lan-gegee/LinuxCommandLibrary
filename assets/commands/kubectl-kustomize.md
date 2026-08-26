# TAGLINE

从目录或 URL 构建 kustomization 目标

# TLDR

**从当前目录构建 kustomization**

```kubectl kustomize```

**从目录构建 kustomization**

```kubectl kustomize [directory]```

**构建并输出到文件**

```kubectl kustomize [directory] -o [output.yaml]```

**启用 Helm chart 支持构建**

```kubectl kustomize --enable-helm [directory]```

**从远程 URL 构建**

```kubectl kustomize [https://github.com/user/repo/config]```

**直接应用 kustomization**

```kubectl apply -k [directory]```

# SYNOPSIS

**kubectl** **kustomize** [_directory_] [_options_]

# PARAMETERS

**--enable-helm**
> 启用 Helm chart 渲染。

**--helm-command** _STRING_
> Helm 命令路径（默认："helm"）。

**--load-restrictor** _STRING_
> 控制资源加载限制（默认：LoadRestrictionsRootOnly）。设为 LoadRestrictionsNone 可允许从根目录之外加载。

**--reorder** _STRING_
> 输出前重新排序资源："legacy" 或 "none"（默认："legacy"）。

**-o**, **--output** _STRING_
> 将输出写入此文件路径。

**--enable-alpha-plugins**
> 启用 kustomize 插件。

# DESCRIPTION

**kubectl kustomize** 从包含 kustomization.yaml 文件的目录，或从带路径后缀的 git 仓库 URL 构建一组 KRM（Kubernetes Resource Model）资源。如果省略目录参数，则假定使用当前目录。无需模板即可处理补丁、overlay 和资源修改。输出可以通过管道传给 kubectl apply。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-apply](/man/kubectl-apply)(1)
