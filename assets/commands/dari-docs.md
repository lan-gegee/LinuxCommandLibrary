# TAGLINE

用模拟的开发者智能体测试文档清晰度

# TLDR

**检查**本地文档能否支撑某项开发者任务

```dari-docs check . --managed --task "[Install the SDK and make a first API call]"```

**优化**文档并下载建议的修改

```dari-docs optimize . --managed --wait --task "[Install the SDK and make a first API call]"```

**检查**公开文档 URL 而非本地目录

```dari-docs check [https://docs.example.com] --managed --task "[Set up auth]"```

向 dari.dev 托管服务进行**身份验证**

```dari-docs auth login```

在同一次调用中**等待**托管运行完成

```dari-docs check . --managed --wait --task "[...]"```

# SYNOPSIS

**dari-docs** _command_ [_path_|_url_] [_options_]

Commands: **check**, **optimize**, **auth**

# PARAMETERS

**check** _PATH_|_URL_
> 对位于 _PATH_（本地目录）或 _URL_（公开文档站点）的文档运行测试智能体，并报告它们在哪里卡住。

**optimize** _PATH_|_URL_
> 运行测试智能体后再运行编辑智能体；把建议的文档修改下载到 **.dari-docs/updated/**，不改动仓库本身。

**auth login** / **auth logout**
> 针对 dari.dev 托管 Docs 服务进行身份验证（或登出）。

**--task** _STRING_
> 智能体应仅凭文档尝试完成的开发者任务。可重复使用该标志指定多个任务。

**--managed**
> 将运行提交给 Dari 托管的智能体（默认模式）。不加此标志时，CLI 期望由 **dari.yml** 驱动的**自管**环境。

**--wait**
> 阻塞直到运行完成；打印报告，并且（对于 **optimize**）下载建议的修改。

**--run-id** _ID_
> 继续等待之前提交的运行，或获取其结果。

**--help**
> 显示 CLI 或子命令的用法。

# DESCRIPTION

**dari-docs** 是一个用于衡量技术文档是否足够清晰的 CLI——衡量标准是 AI 智能体（进而代表一名新开发者）能否在没有帮助的情况下完成真实任务。它打包本地文档目录（或接受公开文档 URL），连同一条或多条 **--task** 描述一起提交给托管的测试智能体。这些智能体只阅读提供的文档并尝试完成任务，报告它们被卡住、被误导或不得不猜测的确切位置。

**check** 到诊断报告为止。**optimize** 还会进一步运行编辑智能体，提出修复问题的具体文档修改，并将其下载到 **.dari-docs/updated/** 中，供人工审阅后再合入仓库。

默认的 **--managed** 模式使用 Dari 托管的测试与编辑智能体，是获得价值的最快途径。**自管模式**（通过 **dari.yml** 配置）让团队可以在自己的 dari.dev 组织内自定义智能体提示词、技能、安装脚本和执行环境。

# CONFIGURATION

**dari.yml**
> 自管运行的项目级配置。定义测试/编辑智能体的提示词、技能、安装命令以及要暴露的文档范围。仅在未设置 **--managed** 时读取。

**.dari-docs/**
> 由 CLI 在目标目录内创建。**updated/** 存放来自 **optimize** 的建议修改；需人工审阅后手动复制进仓库。

**dari.dev account**
> 托管与自管模式都需要通过 **dari-docs auth login** 进行身份验证，令牌会存储在用户的配置目录中。

# CAVEATS

按 dari.dev 账户计费且需要网络访问；**--managed** 会将打包的文档发送到 Dari 的托管智能体，因此私有文档可能需要自管模式或私有部署。建议的修改由智能体生成，合并前应核实其事实准确性。公开 URL 输入由智能体自行抓取，因此付费墙或需要登录的文档无法以此方式评估。

# HISTORY

**dari-docs** 由 **mupt-ai** 开发，代码位于 **github.com/mupt-ai/dari-docs**，是更大的智能体驱动文档质量平台 **dari.dev** 的一部分。它作为传统文档 lint 工具在智能体时代的继任者推出，把质量衡量标准从风格合规转变为任务可完成性。

# SEE ALSO

[vale](/man/vale)(1), [markdownlint](/man/markdownlint)(1), [alex](/man/alex)(1)
