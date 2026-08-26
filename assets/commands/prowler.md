# TAGLINE

多云安全评估工具

# TLDR

**运行 AWS 安全审计**

```prowler aws```

**扫描特定服务**

```prowler aws --services [s3] [iam] [ec2]```

**输出到文件**

```prowler aws -M json -o [report.json]```

**使用特定配置文件**

```prowler aws -p [profile_name]```

**扫描 Azure**

```prowler azure```

**扫描 GCP**

```prowler gcp```

**运行特定检查项**

```prowler aws -c [check11] [check12]```

# SYNOPSIS

**prowler** _provider_ [_--services list_] [_-M format_] [_options_]

# PARAMETERS

**aws**
> 审计 AWS 账户。

**azure**
> 审计 Azure 订阅。

**gcp**
> 审计 GCP 项目。

**--services** _LIST_
> 要审计的服务。

**-c**, **--checks** _LIST_
> 特定检查项。

**-p**, **--profile** _NAME_
> AWS 配置文件（profile）。

**-M**, **--output-modes** _FORMAT_
> 输出格式。

**-o**, **--output-filename** _FILE_
> 输出文件。

**--severity** _LEVEL_
> 按严重性过滤。

# DESCRIPTION

**prowler** 通过针对 CIS 基准、合规框架（GDPR、HIPAA、PCI-DSS）以及各云服务商的最佳实践运行数百项检查，对云环境执行自动化安全评估。它支持 AWS、Azure、GCP、Kubernetes、GitHub 和 Microsoft 365，并使检查内容适配各平台的安全模型。

扫描可以定向到特定服务、单个检查项或严重性级别，以便聚焦最关键的发现。输出支持 JSON、CSV 和 HTML 格式，便于集成到安全仪表板和 CI/CD 流水线中。

该工具需要对目标环境具有只读权限的凭据，并使用各服务商的标准身份验证方式（AWS 配置文件、Azure 服务主体、GCP 服务账号）。

# CAVEATS

需要具有只读权限的云凭据。大型账户可能耗时较长。部分检查需要特定权限。

# HISTORY

**Prowler** 由 **Toni de la Fuente** 创建，最初用于 AWS 安全审计，如今已发展为支持多个云服务商和合规框架的工具。

# INSTALL

```brew: brew install prowler```

```nix: nix profile install nixpkgs#prowler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws-cli](/man/aws-cli)(1), [scout](/man/scout)(1), [cloudsploit](/man/cloudsploit)(1)
