# TAGLINE

Amazon Web Services 的统一命令行界面。

# TLDR

**配置 AWS 凭证**

```aws configure```

**列出 S3 存储桶**

```aws s3 ls```

**复制文件到 S3**

```aws s3 cp [path/to/file] s3://[bucket]/[key]```

**同步目录到 S3**

```aws s3 sync [path/to/directory] s3://[bucket]/[prefix]```

**列出 EC2 实例**

```aws ec2 describe-instances```

**获取调用者身份（验证凭证）**

```aws sts get-caller-identity```

**调用 Lambda 函数**

```aws lambda invoke --function-name [function_name] [output.json]```

**使用指定的 profile**

```aws --profile [profile_name] s3 ls```

# SYNOPSIS

**aws** [_options_] _service_ _command_ [_parameters_]

# PARAMETERS

**configure**
> 交互式设置凭证和默认区域。

**--profile** _name_
> 使用凭证文件中的命名 profile。

**--region** _region_
> 覆盖默认区域。

**--output** _format_
> 输出格式：json、yaml、text、table。

**--query** _expression_
> 用于过滤输出的 JMESPath 查询。

**--no-cli-pager**
> 禁用输出分页。

**--no-paginate**
> 禁用多页结果的自动分页。

**--endpoint-url** _url_
> 覆盖默认的服务端点 URL。

**--cli-binary-format** _format_
> 二进制输入/输出的格式（base64 或 raw-in-base64-out）。

**--debug**
> 启用调试日志。

**--dry-run**
> 预览操作而不执行（仅限支持的命令）。

**--cli-auto-prompt**
> 启用交互式自动提示模式。

# COMMON SERVICES

**s3**
> Simple Storage Service（对象存储）。

**ec2**
> Elastic Compute Cloud（虚拟服务器）。

**iam**
> Identity and Access Management（身份与访问管理）。

**lambda**
> 无服务器计算函数。

**sts**
> Security Token Service（安全令牌服务）。

**cloudformation**
> 基础设施即代码堆栈。

**rds**
> Relational Database Service（关系型数据库服务）。

**dynamodb**
> NoSQL 数据库服务。

# DESCRIPTION

**aws** 是 Amazon Web Services 的官方命令行界面，提供对所有 AWS 服务的统一访问。它让你能在终端中管理云基础设施、部署应用并自动化运维。

CLI 使用存储在 **~/.aws/credentials** 中的凭证和 **~/.aws/config** 中的配置。多个 profile 支持在不同的 AWS 账户或角色之间切换。命令遵循 **aws service operation --parameters** 的模式。

输出可格式化为 JSON、YAML、文本或表格，并可使用 JMESPath 查询通过 **--query** 过滤。CLI 支持 shell 补全以及用于发现命令和参数的交互式自动提示模式。

# CONFIGURATION

**~/.aws/credentials**
> 存储访问密钥 ID 和秘密访问密钥，按命名 profile 组织。

**~/.aws/config**
> 按 profile 存储默认区域、输出格式、SSO 设置和角色代入配置。

# CAVEATS

凭证以明文存储；为了更好的安全性，请在 EC2 上使用 IAM 角色或凭证辅助工具。大多数 AWS 操作受 API 速率限制。某些命令会产生 AWS 费用。大多数服务必须指定区域或有默认区域。受 MFA 保护的操作需要会话令牌。

# HISTORY

AWS CLI 于 **2012 年**首次发布，用以取代较早的各服务专用命令行工具。**2020 年**发布的版本 2 增加了自动提示、SSO 集成和原生安装包等功能。该 CLI 由 AWS 维护并频繁更新以支持新服务和特性，是 AWS 自动化与管理的主要工具。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-vault](/man/aws-vault)(1), [terraform](/man/terraform)(1), [eksctl](/man/eksctl)(1), [sam](/man/sam)(1)

# RESOURCES

```[Source code](https://github.com/aws/aws-cli)```

```[Homepage](https://aws.amazon.com/cli/)```

```[Documentation](https://docs.aws.amazon.com/cli/latest/reference/)```

<!-- verified: 2026-06-18 -->
