# TAGLINE

用于模型路由、蒸馏和服务部署的 World Model Optimizer CLI

# TLDR

安装并**配置提供商**

```pip install world-model-optimizer```

```wmo providers set```

从智能体轨迹**构建**模型

```wmo build --file [traces.jsonl] --name [my-model]```

**部署**调优后的路由器/模型

```wmo serve --name [my-model]```

**登录**托管平台

```wmo login```

**运行**托管的智能体或世界模型

```wmo run [agent-id]```

# SYNOPSIS

**wmo** _command_ [_options_]

# PARAMETERS

**providers set**
> 在 `.wmo/pool.toml` 中注册模型提供商和候选模型

**build** **--file** _traces_ **--name** _name_
> 根据 OTel 或智能体轨迹构建世界模型/路由配置

**optimize**
> 用于路由扫描/拟合/报告、蒸馏、harness 和 pin 的子命令

**serve** **--name** _name_
> 部署一个在前沿大模型与较小模型之间进行路由的端点

**login**
> 向 Experiential Labs 托管平台进行身份验证

**run** _id_
> 运行托管的世界模型或智能体 harness

**config telemetry** {_enable_|_disable_|_status_}
> 控制匿名使用情况遥测

**eval**
> 评估 harness/任务（可选 E2B 后端）

# DESCRIPTION

**wmo**（World Model Optimizer）将收集到的智能体轨迹转化为更小的开源模型和具有成本意识的路由器。它可以通过外部 API（如 Tinker）进行蒸馏，在留出的轨迹上拟合路由策略，并提供一个本地端点，在保持前沿模型质量的同时降低推理成本。

该项目还提供用于闭环智能体测试的世界模型仿真 API，以及用于 harness 优化的可选 E2B 沙箱后端。本地状态保存在 `.wmo/` 目录下。

# CAVEATS

需要 Python 安装包（`pip install world-model-optimizer`），大多数 optimize/serve 工作流还需要提供商 API 密钥。托管功能需要 `wmo login`。遥测默认开启；可用 `wmo config telemetry disable` 或 `DO_NOT_TRACK=1` / `WMO_TELEMETRY=0` 关闭。

# HISTORY

由 **Experiential Labs** 开发的开源 CLI，用于基于生产轨迹持续改进智能体模型。

# SEE ALSO

[pip](/man/pip)(1), [python](/man/python)(1)

# RESOURCES

```[Source code](https://github.com/experientiallabs/world-model-optimizer)```

```[Homepage](https://platform.experientiallabs.ai)```

<!-- verified: 2026-07-28 -->
