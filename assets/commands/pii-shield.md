# TAGLINE

检测并遮蔽文本中的个人身份信息

# TLDR

在内联字符串中**检测 PII**

```pii-shield detect "Contact john@example.com for help"```

**遮蔽**PII，即用实体类型标签**替换**

```pii-shield mask "My email is john@example.com" --strategy [replace]```

**删除** PII（完全移除匹配片段）

```pii-shield mask "SSN 123-45-6789" --strategy [redact]```

将 PII **哈希**为稳定且确定的值

```pii-shield mask "Card 4111-1111-1111-1111" --strategy [hash]```

**处理一个文件**并将遮蔽后的输出写入另一个文件

```pii-shield file [input.txt] -o [output.txt] --strategy [redact]```

# SYNOPSIS

**pii-shield** _command_ _input_ [**--strategy** _STRATEGY_] [**-o** _output_]

# PARAMETERS

**detect** _TEXT_
> 打印在 _TEXT_ 中发现的 PII 实体（实体类型、位置、分数），不修改输入。

**mask** _TEXT_
> 返回按 **--strategy** 重写了所检测 PII 的 _TEXT_。

**file** _INPUT_
> 从 _INPUT_ 文件读取 PII，并将遮蔽后的输出发送到 **stdout** 或 **-o** 给出的路径。

**--strategy** _STRATEGY_
> 如何重写每个检测到的实体。可选值：
>
> **replace** — 替换为实体标签，如 `<EMAIL_ADDRESS>`。
> **redact** — 完全删除匹配片段。
> **mask** — 将每个字符替换为 `*`（默认值）。
> **hash** — 替换为原值的确定性哈希。

**-o** _FILE_
> 将遮蔽后的输出写入 _FILE_ 而不是标准输出（与 **file** 配合使用）。

# DESCRIPTION

**pii-shield** 是一个双引擎 PII 检测库的命令行前端。每个输入都会先在本地经过 **Microsoft Presidio** 处理（使用 spaCy NER 模型加正则表达式模式），配置后还会在云端经过 **Microsoft Foundry / Azure Language Service**。两个引擎的结果会被合并，让高置信度的云端检测结果补充本地结果；未配置 Azure 端点时流量保持在本地。

该库开箱即可识别常见实体类型，包括人名、电子邮件地址、电话号码、信用卡号、社会安全号、IBAN/银行账号、IP 地址和 URL。检测到的实体会经四种遮蔽策略之一（**replace**、**redact**、**mask**、**hash**）进行转换，因此同一工具既可用于安全共享日志/数据样本，也可用于生成确定性匿名化的数据集。

该 CLI 用于一次性操作和流水线集成；同一引擎还可通过 Python API 和 REST 服务器访问，以便嵌入更大的应用程序。

# CONFIGURATION

配置从工作目录中的 **.env** 文件（或对应的环境变量）读取。将 **AZURE_FOUNDRY_ENDPOINT** 设置为你的 Azure Cognitive Services 端点并通过 **az login** 认证，即可启用双引擎路径。保持 **AZURE_FOUNDRY_ENDPOINT** 未设置则仅使用本地 Presidio 引擎检测。可选变量可调整模型选择、分数阈值以及实体允许/拒绝列表。

# CAVEATS

PII 检测属于尽力而为：NER 和正则表达式不可避免会有漏检（假阴性），误报也可能破坏合法文本。对高风险输出务必人工复核。**hash** 策略保留了相等性但会暴露频率规律，不能替代正规的匿名化处理。本地模式需要先下载 spaCy 模型；首次调用可能较慢。云端模式会将输入文本发送到 Azure——启用前请确认你的数据处理政策允许这样做。

# HISTORY

**pii-shield** 由 Microsoft 发布，属于 AI Build 内部转开源流水线的一部分，位于 **github.com/MSFT-AI-BUILD-INTERNAL/pii-shield**。它在 **Presidio**（Microsoft 于 **2019 年**首次发布的开源数据保护 SDK）基础上构建，增加了通过 **Azure Foundry / Azure Language Service** 的云协同检测，并以一个轻量 CLI 的形式对外提供结果。

# SEE ALSO
