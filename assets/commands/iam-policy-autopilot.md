# TAGLINE

从应用程序源代码生成基线 AWS IAM 策略

# TLDR

从源代码**生成策略**（美化 JSON 输出）

```iam-policy-autopilot generate-policies [./src/app.py] --pretty```

使用服务提示**限制分析范围**

```iam-policy-autopilot generate-policies [./src/app.py] --service-hints s3 iam organizations --pretty```

在资源 ARN 中**包含区域和账户**

```iam-policy-autopilot generate-policies [./src] --region [us-east-1] --account [123456789012] --pretty```

为 AccessDenied 错误**建议修复方案**

```iam-policy-autopilot fix-access-denied "[error message text]"```

为 AI 编码助手**启动 MCP 服务器**

```iam-policy-autopilot mcp-server```

**基于 HTTP 的 MCP**

```iam-policy-autopilot mcp-server --transport http```

# SYNOPSIS

**iam-policy-autopilot** *command* [*options*]

# DESCRIPTION

**IAM Policy Autopilot** 是 AWS Labs 开发的开源 CLI 和 MCP 服务器，它在本地分析应用代码，并针对发现的 AWS SDK 调用生成基线的基于身份的 IAM 策略。支持的语言和 SDK 包括 Python（Boto3/Botocore）、Go（AWS SDK v2）、Java（SDK v2）以及 JavaScript/TypeScript（AWS SDK v3）。

它还能帮助解读 **AccessDenied** 错误，并可运行为 MCP 服务器，让 AI 编码助手请求生成策略。可通过 **uvx iam-policy-autopilot**、**pip install iam-policy-autopilot** 安装，或通过项目安装脚本安装到 **/usr/local/bin/iam-policy-autopilot**。

生成的策略只是起点：在生产使用前请审查并收紧。该工具不生成基于资源的策略（存储桶策略、KMS 密钥策略）、SCP、RCP 或权限边界。

# PARAMETERS

**generate-policies** *source_files*...

> 分析源代码并输出 IAM 策略文档。
>
> **--region** *REGION* – 资源 ARN 使用的区域
>
> **--account** *ACCOUNT* – ARN 中使用的 AWS 账户 ID
>
> **--service-hints** *SERVICES* – 将分析限制在指定的服务（推荐）
>
> **--upload-policies** *PREFIX* – 以名称前缀将生成的策略上传到 IAM
>
> **--pretty** – 美化打印 JSON

**fix-access-denied** *message*

> 分析 AccessDenied 错误字符串并建议策略修改。**--yes** 无需确认直接应用更改。

**mcp-server**

> 启动 MCP 服务器。**--transport** 可选 **stdio**（默认）或 **http**。

**-h**, **--help** / **-V**, **--version**

> 帮助与版本信息。

# CAVEATS

当方法名匹配多个服务时，静态分析可能包含多余的动作；请使用 **--service-hints**。运行时的资源名称并不总是可知，因此资源 ARN 可能过于宽泛。AI 助手在生成 IaC 时可能进一步修改策略；部署前务必审查。部分命令需要已配置 AWS 凭据（AWS CLI 的 profile/region）。企业代理可能需要为 AWS 端点配置网络白名单。

# SEE ALSO

[aws](/man/aws)(1), [iam-policy-json-to-terraform](/man/iam-policy-json-to-terraform)(1), [policy_sentry](/man/policy_sentry)(1)

# RESOURCES

```[Source code](https://github.com/awslabs/iam-policy-autopilot)```

```[Documentation](https://github.com/awslabs/iam-policy-autopilot#readme)```

<!-- verified: 2026-07-19 -->
