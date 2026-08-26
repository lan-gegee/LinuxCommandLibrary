# TAGLINE

开源云安全态势管理扫描器

# TLDR

**以默认设置运行扫描**

```cloudsploit scan```

**扫描特定的云提供商**

```cloudsploit scan --cloud [aws]```

**按特定合规框架扫描**

```cloudsploit scan --compliance [hipaa]```

**以 JSON 格式输出结果**

```cloudsploit scan --json [output.json]```

**仅运行特定插件**

```cloudsploit scan --plugin [pluginName]```

**使用自定义配置文件扫描**

```cloudsploit scan --config [config.js]```

**以 CSV 格式输出结果**

```cloudsploit scan --csv [output.csv]```

# SYNOPSIS

**cloudsploit** _command_ [_options_]

# PARAMETERS

**scan**
> 对云基础设施执行安全扫描。

**--cloud** _provider_
> 目标云提供商：aws、azure、gcp、oracle。

**--compliance** _framework_
> 依据合规框架进行检查（hipaa、pci、cis）。CIS 会同时运行 Level 1 和 Level 2 控制项。

**--plugin** _name_
> 仅运行指定的插件。

**--json** _file_
> 以 JSON 格式将结果输出到指定文件。

**--csv** _file_
> 以 CSV 格式将结果输出到指定文件。

**--junit** _file_
> 以 JUnit XML 格式输出结果。

**--config** _file_
> 使用自定义配置文件提供凭证和设置。

**--suppress** _plugins_
> 在结果中屏蔽特定插件。

**--remediate** _plugins_
> 尝试对指定插件进行自动修复。接受逗号分隔的插件名列表。

# DESCRIPTION

**CloudSploit** 是一款开源云安全扫描器，用于检测 AWS、Azure、GCP、Oracle Cloud 和 GitHub 上的安全风险与配置错误。它可检查数百种安全问题，包括公开的 S3 存储桶、过于宽松的 IAM 策略、未加密的数据库以及暴露的服务。

该工具分两个阶段工作：收集阶段查询云 API 以获取基础设施元数据；扫描阶段分析这些数据以识别配置错误和安全风险。结果按严重程度分类（OK、WARN、FAIL、UNKNOWN），并附带描述和修复指导。

CloudSploit 支持映射到 CIS Benchmarks、PCI-DSS 和 HIPAA 等合规框架，帮助组织满足监管要求。它还可以集成到 CI/CD 流水线中，实现持续安全监控。

# CAVEATS

需要在 config.js 或环境变量中配置具有读取权限的相应云凭证。扫描大型环境可能耗时较长并产生 API 费用。某些检查需要受限账户中可能不具备的特定权限。自动修复应先在非生产环境中测试。

# HISTORY

CloudSploit 最初由 **CloudSploit Inc.** 创建，该公司于 **2019 年**被 **Aqua Security** 收购。它于 **2015 年**前后首次发布，逐步支持多家云提供商，并成为云安全态势管理（CSPM）领域的基础性开源工具之一。Aqua 持续维护其开源版本，同时提供商业 SaaS 平台。

# SEE ALSO

[prowler](/man/prowler)(1)
