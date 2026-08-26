# TAGLINE

分析和校验 IAM 策略的安全风险

# TLDR

**列出**当前区域的所有访问分析器

```aws accessanalyzer list-analyzers```

**创建**外部访问分析器

```aws accessanalyzer create-analyzer --analyzer-name [name] --type ACCOUNT```

**列出**某个分析器生成的发现结果

```aws accessanalyzer list-findings --analyzer-arn [arn]```

**获取**特定发现结果的详细信息

```aws accessanalyzer get-finding --analyzer-arn [arn] --id [finding_id]```

**创建**用于归档（屏蔽）发现结果的归档规则

```aws accessanalyzer create-archive-rule --analyzer-name [name] --rule-name [rule] --filter '[filter_json]'```

在部署前**校验** IAM 策略

```aws accessanalyzer validate-policy --policy-document [file://policy.json] --policy-type IDENTITY_POLICY```

# SYNOPSIS

**aws accessanalyzer** _command_ [_options_]

# DESCRIPTION

**AWS IAM Access Analyzer** 提供一整套管理 AWS 中身份和资源访问的能力，帮助你设置、验证和完善 IAM 策略。它使用自动化推理和基于逻辑的分析来识别潜在安全风险和未使用的访问权限。

该服务提供三种主要类型的分析器：

> **外部访问分析器** - 识别可从你的 AWS 账户或组织之外访问的资源，包括公网访问和跨账户访问。这些分析器使用基于逻辑的推理来分析基于资源的策略，在部署前识别意外的外部访问。

> **内部访问分析器** - 识别组织或账户内哪些主体可以访问特定资源。这有助于确保资源只对预期的内部主体开放，从而实现最小权限原则。

> **未使用访问分析器** - 通过检测未使用的资源来识别身份访问风险，例如近期未被使用的 IAM 角色、访问密钥、控制台密码以及服务级或操作级权限。

该工具还提供**策略验证**，检查 IAM 策略中的语法错误并核对是否符合 AWS 最佳实践；此外还有**策略生成**功能，根据 CloudTrail 日志中记录的实际访问活动自动创建细粒度策略。

# AVAILABLE COMMANDS

**apply-archive-rule**
> 将现有的归档规则应用到发现结果

**cancel-policy-generation**
> 取消进行中的策略生成请求

**check-access-not-granted**
> 检查策略未授予对指定操作的访问权限

**check-no-new-access**
> 检查新策略未授予额外的访问权限

**check-no-public-access**
> 检查策略不允许公开访问

**create-access-preview**
> 在部署前创建资源访问预览

**create-analyzer**
> 创建新的分析器（ACCOUNT、ORGANIZATION、ACCOUNT_UNUSED_ACCESS）

**create-archive-rule**
> 创建自动归档发现结果的规则

**delete-analyzer**
> 删除分析器及其发现结果

**get-finding**
> 检索特定发现结果的详细信息

**list-analyzers**
> 列出当前区域的所有分析器

**list-findings**
> 检索某个分析器生成的发现结果

**start-policy-generation**
> 根据 CloudTrail 活动生成 IAM 策略

**validate-policy**
> 检查策略的错误及违反最佳实践之处

# CAVEATS

需要相应的 IAM 权限才能创建和管理分析器。组织级别的外部访问分析器需要 AWS Organizations 及受信任访问。策略生成要求启用 CloudTrail 日志记录。资源变更后某些发现结果可能最长需要 30 分钟才会出现。

# HISTORY

**AWS IAM Access Analyzer** 在 **AWS re:Invent 2019** 上发布，最初是一项帮助识别与外部实体共享的资源的服务。随后逐步扩展了未使用访问分析、策略验证和策略生成等能力，成为一套全面的 IAM 安全与治理工具。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-iam](/man/aws-iam)(1), [aws-organizations](/man/aws-organizations)(1), [aws-cloudtrail](/man/aws-cloudtrail)(1), [aws](/man/aws)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/accessanalyzer/)```

<!-- verified: 2026-06-17 -->
