# TAGLINE

面向资源受限设备的超轻量级 AI 助手

# TLDR

**初始化**配置并设置凭证

```picoclaw onboard```

与 AI 代理**启动交互式** CLI 聊天会话

```picoclaw agent```

**发送一次性消息**，不进入交互模式

```picoclaw agent -m "[question or task]"```

为聊天平台集成**启动多通道网关**

```picoclaw gateway```

# SYNOPSIS

**picoclaw** [_command_] [_options_]

# PARAMETERS

**onboard**
> 初始化配置并为首次使用搭建环境。配置文件创建于 **~/.picoclaw/config.json**。

**agent**
> 与 AI 代理启动交互式 CLI 聊天会话。

**agent -m** _message_
> 向代理发送单条消息并接收回复，不进入交互模式。

**gateway**
> 启动用于聊天平台集成的多通道网关，支持 Telegram、Discord、WhatsApp、QQ、Slack、Matrix、IRC、钉钉、LINE 和企业微信。

# DESCRIPTION

**picoclaw** 是一个用 Go 编写的超轻量级个人 AI 助手，设计目标是在极度资源受限的硬件上运行。它的内存占用低于 10MB，以单个自包含二进制文件分发，启动时间不到一秒。

PicoClaw 原生支持 RISC-V、ARM64、ARM32、MIPS、LoongArch 和 x86 架构，可以部署在从价值 10 美元的 RISC-V 开发板到高性能服务器的各类设备上。尽管占用极小，它仍提供完整的代理能力，包括规划、网页搜索集成、命令执行和自动化工作流。

该工具支持 30 多家 LLM 提供商，包括 OpenAI、Anthropic (Claude)、Google Gemini、DeepSeek、Mistral、Groq、Qwen、Ollama 和智谱。通过 gateway 命令可与聊天平台集成，部署 Telegram、Discord、WhatsApp、Slack、Matrix、IRC 等消息服务上的机器人。

# CONFIGURATION

配置存储在 **~/.picoclaw/config.json** 中。运行 **picoclaw onboard** 进行交互式设置。

关键配置字段：

```
{
  "agents": {
    "defaults": {
      "workspace": "/path/to/workspace",
      "model_name": "claude-opus-4-5",
      "max_tokens": 8192,
      "temperature": 0.7,
      "max_tool_iterations": 10
    }
  },
  "model_list": [
    {
      "model_name": "claude",
      "model": "claude-opus-4-5",
      "api_key": "sk-ant-xxx"
    }
  ]
}
```

可通过 **tools** 配置启用网页搜索，支持 Brave、Tavily 和 DuckDuckGo 搜索提供商。

# CAVEATS

PicoClaw 以你的用户权限在你的机器上执行命令。在新版本中，API 密钥等敏感数据可以单独存储在 **.security.yml** 中。该项目大部分由 AI 自举构建，约 95% 的核心系统由 AI 代理生成，这可能影响代码质量和可维护性。由于基于 Go，需要下载预编译的二进制文件或从源码构建，而无法通过软件包管理器安装。

# HISTORY

PicoClaw 由以 RISC-V 硬件闻名的 **Sipeed** 公司开发，是为他们的低成本开发板优化的 AI 助手。它于 **2025 年**首次发布，通过自举过程用 Go 编写——AI 代理本身主导了架构设计和代码优化。该项目因能在低至 10 美元的硬件上运行完整的代理能力而受到关注。

# INSTALL

```brew: brew install picoclaw```

```nix: nix profile install nixpkgs#picoclaw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nanobot](/man/nanobot)(1), [claude](/man/claude)(1)
