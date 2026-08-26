# TAGLINE

用 Zig 编写的自主 AI 助手基础设施

# TLDR

**启动交互式 agent** 对话

```nullclaw agent```

**发送单条消息**后退出

```nullclaw agent -m "[message]"```

**在自定义端口启动 HTTP 网关**

```nullclaw gateway --port [3000]```

交互式**运行引导向导**

```nullclaw onboard --interactive```

**启动消息通道**

```nullclaw channel start [telegram]```

**检查系统健康状态**和配置

```nullclaw status```

**运行诊断**

```nullclaw doctor```

**安装为系统服务**

```nullclaw service install```

# SYNOPSIS

**nullclaw** [_command_] [_options_]

# PARAMETERS

**agent**
> 交互式或单条消息对话模式。

**-m**, **--message** _MESSAGE_
> 执行单条消息然后退出（配合 agent 使用）。

**gateway**
> 启动集成各通道的 HTTP 运行时。

**--port** _PORT_
> 网关监听端口（默认：3000）。

**onboard**
> 用于初始设置的配置向导。

**--api-key** _KEY_
> 引导期间直接设置 API 密钥。

**--provider** _PROVIDER_
> 引导期间指定模型提供商。

**--interactive**
> 分步交互式配置。

**channel** {**start**|**stop**|**status**} [_CHANNEL_NAME_]
> 管理消息集成。

**service** {**install**|**status**|**stop**}
> 后台守护进程管理。

**status**
> 显示系统健康状态和配置摘要。

**doctor**
> 运行全面的系统诊断。

**migrate** **openclaw** [**--dry-run**]
> 从兼容系统导入数据。使用 --dry-run 可预览而不实际应用。

# DESCRIPTION

**nullclaw** 是一个完全用 Zig 构建的极简 AI agent 框架，交付为单个 678 KB 的静态二进制文件，启动时间不足 2 ms，峰值内存占用约 1 MB。它可以在任何带 CPU 的硬件上运行——支持 ARM、x86 和 RISC-V 架构而无需修改。

该框架集成了 22+ 个 AI 提供商（包括 Anthropic、OpenAI、Ollama 和 OpenRouter）、18 个通信通道（Telegram、Signal、Discord、Slack、iMessage、Matrix、WhatsApp、IRC 等）以及可自定义的工具——除 libc 外零外部运行时依赖。

所有子系统均使用 vtable 接口，无需更改代码即可替换实现。这涵盖提供商、通道、内存后端、工具、运行时和安全沙箱。内存系统在 SQLite 中结合 FTS5 全文索引与向量相似度进行混合搜索。

# CONFIGURATION

配置位于 **~/.nullclaw/config.json**，遵循 OpenClaw 兼容模式并采用 snake_case 格式。

```
{
  "models": {
    "providers": {
      "anthropic": {
        "api_key": "sk-..."
      }
    }
  },
  "agents": {
    "defaults": {
      "model": {
        "primary": "claude-sonnet-4-20250514"
      }
    }
  }
}
```

提供商嵌套在 **models.providers** 下，默认模型位于 **agents.defaults.model.primary**，通道则使用 **accounts** 包装。

# CAVEATS

从源码构建需要 **Zig 0.15.2**（精确版本）。该二进制文件除 libc 外没有外部依赖，但各个提供商和通道需要各自的 API 密钥或服务账户才能工作。该项目与 OpenClaw 兼容但并非直接替代品——通过 **nullclaw migrate openclaw** 迁移配置可能需要手动调整。

# HISTORY

**NullClaw** 是 claw 系列 AI agent 框架的继任者，承接 **OpenClaw** 和 **ZeroClaw**。它完全用 **Zig** 编写，专为极致精简和可移植性设计，面向传统运行时难以适用的边缘计算和资源受限环境。该项目维护着包含 3,230 多项测试的测试套件。

# INSTALL

```brew: brew install nullclaw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ollama](/man/ollama)(1)
