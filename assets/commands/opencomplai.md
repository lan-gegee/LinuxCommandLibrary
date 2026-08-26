# TAGLINE

面向本地仓库和 CI 的欧盟 AI 法案合规检查

# TLDR

**安装** CLI、核心引擎和 Python SDK

```pip install opencomplai```

**发现**仓库中的 AI 信号（无需清单文件，始终退出码为 0）

```opencomplai scan --quick .```

**创建**系统清单

```opencomplai init --system-id [id] --intended-purpose "[purpose]"```

**运行** CI 合规门禁

```opencomplai check```

**输出** JSON 格式的状态工件

```opencomplai check --scan-mode ci --output json```

**在浏览器中打开**欧盟 AI 法案适用性检查器

```opencomplai checker --web```

```opencomplai checker --web --local```

# SYNOPSIS

**opencomplai** _command_ [_options_]

# DESCRIPTION

**opencomplai** 是 OpenComplAI 的命令行前端。OpenComplAI 是一套开放核心工具包，将欧盟 AI 法案义务转化为机器可读、可用于 CI 门禁的检查。**pip install opencomplai** 会安装元软件包（CLI + **opencomplai-core** + Python SDK）。控制台脚本也由 **opencomplai-cli** 提供。要求 Python **3.11+**。没有 **--version** 标志；请使用 **opencomplai --help**。

典型流程：先用 **scan --quick** 查看代码树是否涉及 AI，再用 **init** 写入 **system-manifest.json** 并创建 **~/.opencomplai/**（首次运行时生成 Ed25519 签名密钥对 + **config.yaml**），然后运行 **check** 评估控制项并写出 **compliance-artifact.json**。扫描器会根据代码信号印证所声明的 **intended_purpose**；它绝不会自动进行风险分类。未发现 AI 并不代表通过。

**check** 是契约化的 CI 门禁。退出码：**0** PASS，**1** CONTROL_FAIL，**2** VALIDATION_FAIL，**3** POLICY_BLOCK，**4** TRAP_DETECTED。**TRAP_DETECTED** 仅在有服务支撑的模式（Docker 栈 / **OPENCOMPLAI_API_URL**）下才会触发，本地引擎不会产生。可选的 **--sample-set** 会在 **system_id** 与清单匹配的 **EvalSampleSet** JSON 上运行词汇安全、偏见和数据泄露评估器。

核心引擎中的分类是确定性的、基于规则的。可选的 **opencomplai scan --ai-intent**（插件 **opencomplai-ai**）会对提取出的调用点增加一轮本地模型分析。支持 GitHub/GitLab pre-commit 钩子和 **.ocignore** 扫描配置。社区版采用 **AGPL-3.0** 许可证。

# COMMANDS

**init** **--system-id** _id_ **--intended-purpose** _text_ [_options_]

> 写入 **system-manifest.json**（可用 **-o** 覆盖路径）。**--interactive** 会先运行适用性检查器。首次运行还会创建 **~/.opencomplai/**。

**scan** [**--quick** _path_] [**--manifest** _file_] [**--repo-root** _dir_] [**--fail-on** _none_|_new-major_|_major_|_critical_] [**--output** _human_|_json_] [**--ai-intent**]

> 对照代码树印证清单，或用 **--quick** 运行仅发现模式（始终退出码 **0**，不生成工件）。JSON 输出是带版本号的信封结构，并非已签名的 **check** 工件。

**check** [**-m** _manifest_] [**--commit-ref** _ref_] [**--scan-mode** _local_|_ci_|_airgap_] [**--sample-set** _file_] [**--sign**] [**-o** _human_|_json_]

> 完整合规门禁。总是在当前目录写入 **compliance-artifact.json**。

**checker** [**--web**] [**--local**] [**--answers** _file_] [**-o** _human_|_json_] [**--export-json**|_--export-md_|_--export-pdf_|_--export-all_ _path_] [**--write-manifest** _file_]

> 欧盟 AI 法案适用性向导（checker 版本见上游文档）。**--web** 打开托管的文档页面；**--web --local** 提供离线副本。

**dashboard**

> 高级仪表板的注册与同步（企业版）。参见 **opencomplai dashboard --help**。

# PARAMETERS

**-m**, **--manifest** _file_

> **scan**/**check** 时使用的清单路径（默认 **system-manifest.json**）。

**--scan-mode** _local_|_ci_|_airgap_

> **check** 的运行方式。默认 **local**。

**--fail-on** _policy_

> **scan** 的 CI 门控策略。默认 **none**。只要不是 **none**，非空的 **scan_errors** 就会导致失败。

**--sign** / **--no-sign**

> 使用 **~/.opencomplai/signing.key** 为 **check** 工件签名。默认 **--no-sign**。

# CONFIGURATION

**~/.opencomplai/**
> 由 **init** 创建的安装 ID、**config.yaml** 和 Ed25519 签名密钥。

**.ocignore**
> 每个仓库的扫描限制和忽略规则（首次 **scan** 时自动生成，除非禁用）。默认拒绝符号链接，上限为单文件 1 MiB / 20 000 个文件 / 总计 200 MiB。

**OPENCOMPLAI_API_URL**
> 设置后，**check** 将与网关通信（有服务支撑的模式），而非使用本地引擎。

**OPENCOMPLAI_DOCS_URL**
> 覆盖 **opencomplai checker --web** 打开的 URL。

# CAVEATS

结果仅供参考，不构成法律意见；OpenComplAI 与欧盟无隶属关系。扫描器将清单视为权威依据。**scan --quick** 无法使构建失败。**scan --output json** 不是已签名的 **ScanStatusArtifact**。**--ai-intent** 需要 **opencomplai-ai** 和已下载的本地模型。针对恶意仓库的默认设置会跳过符号链接和超大文件。

# SEE ALSO

[pip](/man/pip)(1), [pre-commit](/man/pre-commit)(1)

# RESOURCES

```[Source code](https://github.com/Opencomplai/opencomplai)```

```[Homepage](https://opencomplai.com)```

```[Documentation](https://docs.opencomplai.com)```

<!-- verified: 2026-08-14 -->
