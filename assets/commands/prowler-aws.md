# TAGLINE

AWS 云安全评估

# TLDR

**运行 AWS 安全评估**

```prowler aws```

**运行特定检查项**

```prowler aws -c [iam_password_policy] [s3_bucket_public_access]```

**针对特定服务运行检查**

```prowler aws -s [s3] [iam]```

**按合规框架运行**

```prowler aws --compliance [cis_2.0_aws]```

**按严重性过滤**

```prowler aws --severity [critical] [high]```

**以 JSON 格式输出到文件**

```prowler aws -M json-ocsf -o [results/]```

**列出所有可用检查项**

```prowler aws -l```

# SYNOPSIS

**prowler aws** [_options_]

# PARAMETERS

**-c**, **--checks** _checks_
> 要运行的特定检查项。

**-s**, **--services** _services_
> 要检查的服务（iam、s3、ec2 等）。

**-e**, **--excluded-checks** _checks_
> 从执行中排除特定检查项。

**--excluded-services** _services_
> 从扫描中排除特定服务。

**--compliance** _framework_
> 合规框架（cis、gdpr、hipaa 等）。

**--severity** _levels_
> 按严重性过滤检查项（critical、high、medium、low、informational）。

**-M**, **--output-modes** _format_
> 输出格式（csv、json-asff、json-ocsf、html）。

**-o**, **--output-directory** _dir_
> 输出目录。

**-l**, **--list-checks**
> 列出所有可用检查项。

**--list-services**
> 列出所有可用服务。

**-p**, **--profile** _name_
> AWS 配置文件（profile）。

**-f**, **--filter-region** _region_
> 要扫描的 AWS 区域。

**--security-hub**
> 将结果发送到 AWS Security Hub。

# DESCRIPTION

**prowler aws** 对 AWS 账户执行安全评估。它依据 CIS、NIST 800、PCI-DSS、GDPR、HIPAA 等最佳实践和合规框架检查配置，识别配置错误、漏洞和合规差距。结果可以多种格式输出，并可选发送到 AWS Security Hub。

# INSTALL

```brew: brew install prowler```

```nix: nix profile install nixpkgs#prowler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[prowler](/man/prowler)(1), [aws](/man/aws)(1)
