# TAGLINE

Amazon Web Services 的统一命令行界面

# TLDR

**列出** S3 存储桶

```aws s3 ls```

将文件**上传到** S3

```aws s3 cp [file.txt] s3://[bucket-name]/```

**列出** EC2 实例

```aws ec2 describe-instances```

**获取**调用者身份

```aws sts get-caller-identity```

**调用** Lambda 函数

```aws lambda invoke --function-name [MyFunction] [output.json]```

使用**指定的 profile**

```aws --profile [production] s3 ls```

**配置** AWS 凭证

```aws configure```

用 JMESPath 查询**过滤输出**

```aws ec2 describe-instances --query "Reservations[*].Instances[*].[InstanceId,State.Name]" --output table```

# SYNOPSIS

**aws** [_options_] _service_ _command_ [_parameters_]

# DESCRIPTION

**aws** 是 Amazon Web Services 的统一命令行界面。它通过一致的接口提供对 EC2、S3、Lambda、DynamoDB 等数百个 AWS 服务的直接访问。

该 CLI 让你可以从终端自动化、脚本化地管理 AWS 资源，而无需使用 Web 控制台。

# PARAMETERS

**--profile** _name_
> 使用指定的 AWS 凭证 profile

**--region** _region_
> 覆盖默认区域

**--output** _format_
> 输出格式（json、text、table、yaml）

**--query** _query_
> 用于过滤输出的 JMESPath 查询

**--debug**
> 启用调试日志

**--no-cli-pager**
> 禁用输出分页

**--endpoint-url** _url_
> 覆盖服务端点

**--no-verify-ssl**
> 禁用 SSL 校验

**--no-paginate**
> 禁用结果的自动分页

**--cli-binary-format** _format_
> 控制二进制参数的编码方式（raw-in-base64-out 或 raw-in-raw-out）

**--version**
> 显示 AWS CLI 版本

# COMMON SERVICES

- **s3** - 对象存储
- **ec2** - 虚拟服务器
- **lambda** - 无服务器函数
- **dynamodb** - NoSQL 数据库
- **iam** - 身份与访问管理
- **cloudformation** - 基础设施即代码
- **sts** - 安全令牌服务
- **logs** - CloudWatch 日志

# CONFIGURATION

**~/.aws/credentials**
> 各命名 profile 的访问密钥和秘密密钥。

**~/.aws/config**
> 区域、输出格式和 profile 设置，包括角色担任和 SSO 配置。

# CAVEATS

需要已配置有效的 AWS 凭证。API 有速率限制。某些操作具有破坏性且立即生效。大输出可能被截断。API 调用可能产生费用。可用时请使用 --dry-run。

# HISTORY

**AWS CLI** 由 Amazon 于 **2013 年**发布，以统一界面取代多个服务专用工具。版本 2 于 **2020 年**发布，改进了安装方式和功能。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws-configure](/man/aws-configure)(1), [aws-s3](/man/aws-s3)(1), [aws-vault](/man/aws-vault)(1), [terraform](/man/terraform)(1)
