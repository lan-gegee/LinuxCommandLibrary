# TAGLINE

从既有云基础设施生成 Terraform 配置

# TLDR

将 AWS 资源**导入** Terraform 文件

```terraformer import aws --resources=[vpc,subnet] --regions=[us-east-1]```

**导入** GCP 项目资源

```terraformer import google --resources=[gcs,forwardingRules] --projects=[my-project]```

**列出**某 provider 支持的资源

```terraformer import [provider] list```

输出 **JSON** 而非 HCL

```terraformer import [provider] --resources=[...] -O json```

# SYNOPSIS

**terraformer** **import** *provider* [*flags*]

# DESCRIPTION

**terraformer** 是一个"反向 Terraform"CLI：它通过 Terraform provider 读取在线基础设施，写出 **.tf**/**.json** 配置及状态文件，从而把既有云资源纳入 Terraform 管理。支持众多 provider（AWS、GCP、Azure、Kubernetes、GitHub 等）。

**重要：** 自 2026-03-16 起上游仓库已**归档且不再维护**。新项目建议选用仍在维护的替代品；本页面记录的是仍存在于许多环境中的这一历史工具。

# PARAMETERS

**import** *provider*

> 导入资源。各 provider 特有的标志不尽相同；常见的包括：

**-r**, **--resources** *list*

> 要导入的资源类型（名称因 provider 而异）。

**--regions** / **--projects** / ...

> 云账号范围（参见仓库 **docs/** 目录下各 provider 文档）。

**-O**, **--output** *hcl*|*json*

> 输出格式（默认 **hcl**）。

**-o**, **--path-output** *dir*

> 输出目录（默认 **generated**）。

**-x**, **--excludes** *list*

> 要跳过的资源类型。

**-f**, **--filter** *rules*

> 过滤特定的资源 ID。

**-c**, **--connect**

> 用远程状态引用连接各资源（默认 true）。

**list**（import 下的子命令）

> 列出某 provider 支持的资源类型。

# CAVEATS

**已弃用 / 上游已归档**——没有安全修复。生成的代码通常需要手动清理后才能 **terraform apply**。必须先配置云服务商凭据和 Terraform provider 插件。Cloudflare 及部分其他 provider 已知存在问题。

# INSTALL

```brew: brew install terraformer```

```nix: nix profile install nixpkgs#terraformer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [pulumi](/man/pulumi)(1)

# RESOURCES

```[Source code](https://github.com/GoogleCloudPlatform/terraformer)```

<!-- verified: 2026-07-19 -->
