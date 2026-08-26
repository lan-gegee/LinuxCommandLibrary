# TAGLINE

管理 Systems Manager 会话、命令和参数。

# TLDR

**列出受管实例**

```aws ssm describe-instance-information```

**启动到实例的 Session Manager 会话**

```aws ssm start-session --target [i-xxxxxxxxxxxxxxxx]```

在实例上**运行命令**

```aws ssm send-command --document-name "AWS-RunShellScript" --targets "Key=instanceids,Values=[i-xxxxxxxx]" --parameters 'commands=["echo hello"]'```

从 Parameter Store **获取参数**

```aws ssm get-parameter --name [/path/to/parameter]```

**获取参数并解密**（用于 SecureString）

```aws ssm get-parameter --name [/path/to/secret] --with-decryption```

向 Parameter Store **写入参数**

```aws ssm put-parameter --name [/path/to/parameter] --value "[value]" --type String```

按路径**列出参数**

```aws ssm get-parameters-by-path --path [/path/prefix/] --recursive```

**列出命令调用**

```aws ssm list-command-invocations --command-id [command-id] --details```

# SYNOPSIS

**aws ssm** _subcommand_ [_options_]

# DESCRIPTION

**aws ssm** 是 AWS CLI 的一个子命令，用于管理 AWS Systems Manager。这是一项面向 AWS 资源运维管理的服务，提供实例管理、配置、修补和安全参数存储等能力。

**Session Manager** 无需 SSH 密钥或开放入站端口即可安全地以 Shell 访问 EC2 实例。它会记录会话并支持基于 IAM 的访问控制。

**Run Command** 无需 SSH 即可跨实例机群执行脚本和命令。**Parameter Store** 为配置数据和机密提供分层存储，并支持可选加密。

大多数操作要求实例上安装 SSM Agent。许多 AWS AMI 已预装该代理。

# PARAMETERS

**describe-instance-information**
> 列出由 SSM 管理的实例。

**start-session**
> 启动交互式 Session Manager 会话。

**send-command**
> 在目标上执行命令。

**list-commands**
> 列出命令历史。

**list-command-invocations**
> 获取命令执行结果。

**get-parameter**
> 获取参数值。

**put-parameter**
> 创建或更新参数。

**get-parameters-by-path**
> 列出某路径下的参数。

**delete-parameter**
> 删除参数。

**get-document**
> 获取 SSM 文档内容。

**describe-document**
> 获取 SSM 文档详情。

**list-documents**
> 列出可用的 SSM 文档。

**describe-patches**
> 列出补丁相关信息。

**--target** _instance-id_
> 会话的目标实例。

**--document-name** _name_
> 要执行的 SSM 文档。

**--targets** _targets_
> 命令的目标实例。

**--parameters** _params_
> 文档参数。

**--name** _name_
> 参数名称（分层路径）。

**--value** _value_
> 参数值。

**--type** _type_
> 参数类型：String、StringList、SecureString。

**--with-decryption**
> 解密 SecureString 参数。

**--overwrite**
> 覆盖现有参数值。

**--recursive**
> 按路径递归获取参数。

# CAVEATS

Session Manager 需要 SSM Agent 和正确的 IAM 实例配置文件。参数名称区分大小写且为分层结构（使用 /path/ 格式）。SecureString 参数使用 KMS，可能产生费用。Run Command 的输出在 48000 字符处截断；大输出请使用 S3。每个账户的默认参数配额为 10000 个标准参数。

# HISTORY

**AWS Systems Manager** 由 **2015 年 10 月**推出的 **EC2 Run Command** 演化而来，并于 **2017 年**统一归入 Systems Manager 品牌。**Session Manager** 在 **re:Invent 2018** 上推出，作为 SSH 的安全替代方案。**Parameter Store** 后来扩展出高级参数和更高吞吐量的层级。该服务已发展为包含 Patch Manager、State Manager、OpsCenter 和 Change Manager 的综合运维体系。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-ec2](/man/aws-ec2)(1), [ssh](/man/ssh)(1), [aws-secretsmanager](/man/aws-secretsmanager)(1)
