# TAGLINE

本地优先的只读 AI SRE，用于告警分诊与事件调查

# TLDR

**启动**Web 控制台

```python -m ninoxai serve```

从 JSON 文件**导入**告警

```python -m ninoxai import data/mock_alerts.json```

对告警**重新聚类**并刷新建议

```python -m ninoxai reprocess```

为测试**生成**模拟告警数据

```python -m ninoxai generate-mocks```

使用 Docker Compose**运行**

```docker compose up --build```

# SYNOPSIS

**ninoxai** _subcommand_

# PARAMETERS

**serve**
> 默认在端口 8765 启动控制台和 API

**import** _file_
> 从 JSON 或 CSV 加载告警

**reprocess**
> 执行归一化、聚类、噪声评分，并重建推荐

**generate-mocks**
> 创建用于离线演示的合成告警数据

**investigate**
> 针对某个事件运行只读的 AI 调查器

# DESCRIPTION

**ninoxai**（又称 Nightwatch）是一个开源的 AI SRE 层，架设在 Prometheus、Checkmk、Icinga2、Zabbix 以及通用 webhook 等监控系统之上。它摄取状态异常的告警，把相关的噪声归组为事件，给不稳定的检查项打分，并提出调优建议。

该工具在设计上是只读的。它通过类型化的白名单能力观察运行中的系统（覆盖 Docker、Kubernetes、AWS、Grafana、GitHub、Git 镜像和主机指标），然后形成根因假设，提出修复方案供人工批准。它不会执行修复操作、不会确认告警，也不会向生产环境写回任何内容。

**template** LLM 模式完全离线运行，无需 API 密钥即可生成摘要和基于规则的建议。接入 Anthropic、OpenAI、Mistral 或本地模型后，即可启用调查 agent。

分布式的 **ninox** runner 能够从中央大脑无法直接触达的环境中暴露只读能力。Runner 仅通过出站连接向外通信，并把凭据保存在本地。

# CONFIGURATION

**.env**
> 设置 **NINOXAI_SECRET_KEY** 以及可选的 LLM 提供商凭据

**docker-compose.yml**
> 一并运行控制台、数据库和可选的嵌入服务

**/connections**（位于 UI 中）
> 存储监控连接器的加密凭据

# CAVEATS

远程 LLM 提供商会收到经过脱敏处理的告警与调查上下文。如果不希望任何数据离开主机，请使用离线的 **template** 提供商。

连接器适配器是只读的，但配置不当的凭据仍可能将敏感的基础设施元数据暴露给控制台和调查器。

沙箱验证功能需要 Docker，且目前标记为 beta。

# SEE ALSO

[docker](/man/docker)(1), [kubectl](/man/kubectl)(1), [python](/man/python)(1)
