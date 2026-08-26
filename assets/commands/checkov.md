# TAGLINE

基础设施即代码的静态分析工具

# TLDR

**扫描目录中的 IaC 错误配置**

```checkov -d [path/to/directory]```

**扫描特定文件**

```checkov -f [path/to/file.tf]```

**使用特定框架扫描**

```checkov -d [path/to/directory] --framework [terraform|kubernetes|cloudformation]```

**仅运行特定检查项**

```checkov -d [path/to/directory] --check [CKV_AWS_1,CKV_AWS_2]```

**跳过特定检查项**

```checkov -d [path/to/directory] --skip-check [CKV_AWS_1]```

**以 JSON 格式输出结果**

```checkov -d [path/to/directory] --output json```

**扫描 Terraform plan 文件**

```checkov -f [tfplan.json] --framework terraform_plan```

# SYNOPSIS

**checkov** [**-d** _directory_] [**-f** _file_] [**--framework** _framework_] [**--check** _checks_] [**--skip-check** _checks_] [**--output** _format_] [_options..._]

# DESCRIPTION

**Checkov** 是一个面向基础设施即代码（IaC）的静态代码分析工具，用于检测安全与合规方面的错误配置。它支持 Terraform、CloudFormation、Kubernetes、Helm、Dockerfile、ARM 模板等多种框架。

该工具内置超过 750 条策略，涵盖 CIS Benchmarks、PCI 和 HIPAA 等行业标准。它使用基于图的扫描来分析资源依赖关系并检测复杂的配置问题。

Checkov 还能执行软件组成分析（SCA），并通过正则表达式、关键字和基于熵的检测来发现密钥泄露。

# PARAMETERS

**-d, --directory** _path_
> 要扫描的目录

**-f, --file** _path_
> 要扫描的具体文件

**--framework** _framework_
> IaC 框架：terraform、cloudformation、kubernetes、helm、dockerfile 等

**--check** _ids_
> 仅按 ID 运行特定检查项

**--skip-check** _ids_
> 按 ID 跳过特定检查项

**--output** _format_
> 输出格式：cli、json、junitxml、sarif

**--compact**
> 只显示未通过的检查项

**--list**
> 列出所有可用的检查项

# CONFIGURATION

**.checkov.yaml**
> 项目级配置，用于默认框架、跳过规则和输出设置。

# CAVEATS

自定义策略可用 Python 或 YAML 编写。为获得准确的 Terraform 扫描结果，建议扫描 plan 输出（**terraform plan -out=tfplan && terraform show -json tfplan > tfplan.json**），而不仅是源文件。

# HISTORY

**Checkov** 最初由 **Bridgecrew.io** 开发，后被 **Palo Alto Networks** 收购，成为其 Prisma Cloud 平台的一部分。它仍然是开源项目，并在 GitHub 上持续维护。

# INSTALL

```brew: brew install checkov```

```nix: nix profile install nixpkgs#checkov```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [kubectl](/man/kubectl)(1), [tfsec](/man/tfsec)(1)

# RESOURCES

```[Source code](https://github.com/bridgecrewio/checkov)```

```[Documentation](https://www.checkov.io/)```

<!-- verified: 2026-06-22 -->
