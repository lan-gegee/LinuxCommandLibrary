# TAGLINE

使用通用编程语言进行基础设施即代码管理

# TLDR

**创建新项目**

```pulumi new [template]```

**预览变更**

```pulumi preview```

**部署堆栈**

```pulumi up```

**销毁资源**

```pulumi destroy```

**列出堆栈**

```pulumi stack ls```

**选择堆栈**

```pulumi stack select [stack-name]```

**显示堆栈输出**

```pulumi stack output```

# SYNOPSIS

**pulumi** [_options_] _command_ [_args_]

# DESCRIPTION

**pulumi** 是一个支持多种编程语言的基础设施即代码工具。它使用 TypeScript、Python、Go、C#、Java 和 YAML 来管理云资源。

该工具使用熟悉的编程结构在 AWS、Azure、GCP、Kubernetes 以及许多其他提供商上预置资源。

# PARAMETERS

**new**
> 创建新项目。

**up**
> 部署变更。

**preview**
> 预览变更。

**destroy**
> 删除资源。

**stack**
> 管理堆栈。

**config**
> 管理配置。

**logs**
> 查看日志。

**-s** _stack_
> 目标堆栈。

**-y**, **--yes**
> 跳过确认。

**--diff**
> 显示详细差异。

# CONFIGURATION

**Pulumi.yaml**
> 项目定义文件，指定项目名称、运行时语言和描述。

**Pulumi.<stack>.yaml**
> 每个堆栈的配置文件，包含配置值和加密的机密。

**PULUMI_ACCESS_TOKEN**
> 环境变量，用于无需交互登录即可向 Pulumi Cloud 后端进行身份验证。

# CAVEATS

需要 Pulumi 账户或自托管后端。状态管理很重要。provider 插件在首次使用时下载。编程方式有一定的学习曲线。

# HISTORY

**Pulumi** 由 **Joe Duffy** 和 **Eric Rudder** 于 **2017 年**创立。它将通用编程语言引入基础设施管理，与 Terraform 的 HCL 等领域专用语言形成差异化。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [aws](/man/aws)(1), [kubectl](/man/kubectl)(1), [cdktf](/man/cdktf)(1)
