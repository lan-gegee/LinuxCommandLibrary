# TAGLINE

Observal AI 代理注册表与分析平台的 CLI

# TLDR

**安装**独立 CLI 二进制文件

```curl -fsSL https://raw.githubusercontent.com/Observal/Observal/main/install.sh | bash```

通过 Python 工具链**安装**

```uv tool install observal-cli```

**登录**你的 Observal 服务器

```observal auth login```

**检测 harness 并安装**遥测钩子

```observal doctor --patch```

将代理**拉取到指定的编码 harness**

```observal pull [agent-name] --harness [pi|cursor|codex|...]```

**创建脱敏的支持包**

```observal support bundle```

**流式查看**本地开发日志

```observal logs```

# SYNOPSIS

**observal** \<command\> [_options_]

# DESCRIPTION

**observal** 是 **Observal** 的开发者 CLI。Observal 是一个自托管的控制平面和注册表，用于管理内部 AI 组件（技能、MCP 服务器、代理、钩子、提示词和沙箱）。该 CLI 可向已部署的 Observal 服务器进行身份验证，向编码 harness 安装会话遥测，拉取带有 harness 特定配置的版本化代理，并帮助诊断问题。

支持的 harness 包括 Claude Code、Cursor、Kiro、Pi、GitHub Copilot（CLI 和 VS Code）、Codex、OpenCode 和 Antigravity CLI。完成 **auth login** 和 **doctor --patch** 后，Observal 即可捕获会话并为各 harness 生成正确的安装布局。代理是可移植的包：在注册表中定义一次，然后用相应的 **--harness** 进行 **pull**。

该 CLI 可作为独立二进制文件安装（无需 Python），也可通过 **uv** / **pipx** 以 **observal-cli** 软件包的形式安装。服务器端是一个独立的 Docker Compose 堆栈（API、Web UI、PostgreSQL、ClickHouse、Redis 等）；CLI 只与运行中的服务器通信。

# PARAMETERS

**auth login**
> 向你的 Observal 服务器进行身份验证。

**doctor** [**--patch**]
> 诊断本地 harness 配置；**--patch** 会安装遥测钩子并为代理安装做准备。

**pull** _agent_ [**--harness** _name_]
> 将注册表中的代理安装到所选的编码 harness 中，并生成 harness 特定的配置。

**support bundle**
> 生成用于提交缺陷报告的脱敏诊断归档。

**support inspect** _archive_
> 在分享前审查支持包内容。

**logs**
> 流式查看基于 loguru 的开发日志（写入 **~/.observal/logs/** 下）。

# CAVEATS

该 CLI 需要可访问的 Observal 服务器；只装 CLI 是不够的。完整自托管需要拉取多服务的 Docker 堆栈，并要求 Docker Engine ≥ 24 与 Compose v2。遥测和代理安装会修改本地 harness 配置——在共享机器上执行 **--patch** 前请先检查 **doctor** 输出。会话捕获与洞察功能依赖于服务端存储以及用于洞察报告的可选 LLM 配置。

# HISTORY

**Observal** 是一个 Apache-2.0 开源项目，为内部 AI 代理与组件提供受治理的注册表和分析平台，包含 Python（Typer/Rich）CLI 和基于 FastAPI 的服务端。

# SEE ALSO

[uv](/man/uv)(1), [pip](/man/pip)(1), [docker](/man/docker)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/Observal/Observal)```

```[Homepage](https://observal.io)```

```[Documentation](https://docs.observal.io/)```

<!-- verified: 2026-07-21 -->
