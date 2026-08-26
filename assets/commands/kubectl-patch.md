# TAGLINE

使用 strategic merge patch、JSON merge 等方式更新资源字段

# TLDR

**用 JSON 补丁更新 deployment**

```kubectl patch deployment [name] -p '{"spec":{"replicas":3}}'```

**使用 strategic merge 补丁**

```kubectl patch deployment [name] --type=merge -p '[patch]'```

**使用 JSON patch**

```kubectl patch deployment [name] --type=json -p '[{"op":"replace","path":"/spec/replicas","value":3}]'```

**从文件打补丁**

```kubectl patch deployment [name] --patch-file=[patch.yaml]```

# SYNOPSIS

**kubectl** **patch** _type_ _name_ [_options_]

# PARAMETERS

**-p**, **--patch** _patch_
> 以 JSON 或 YAML 表示的补丁内容。

**--patch-file** _file_
> 包含补丁的文件。

**--type** _type_
> 补丁类型（strategic、merge、json）。

**-n**, **--namespace** _name_
> Kubernetes 命名空间。

# DESCRIPTION

**kubectl patch** 对 Kubernetes 资源字段应用增量更新，而无需替换整个资源配置。这使它非常适合只需修改特定字段的脚本化和自动化操作，例如调整副本数、更新镜像标签或添加注解。

该命令支持三种补丁策略：strategic merge patch（默认），它根据 Kubernetes schema 知识智能合并列表和映射；JSON merge patch，执行直接的递归合并；JSON patch（RFC 6902），在特定 JSON 路径上使用 add、remove、replace 等显式操作。补丁内容可以通过 -p 标志内联提供，也可以用 --patch-file 从文件读取。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [kubectl-edit](/man/kubectl-edit)(1)
