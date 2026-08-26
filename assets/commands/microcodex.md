# TAGLINE

面向终端的超轻量级 C++ 编码智能体

# TLDR

**安装**最新二进制文件并登录

```curl -fsSL https://github.com/paoloanzn/microcodex/releases/latest/download/install.sh | sh```

```microcodex login```

在当前目录**启动交互式会话**

```microcodex```

**运行一次性提示词**而不先进入完整的 UI 循环

```microcodex "[Find the failing test, fix it, and run the relevant test suite]"```

在无界面或远程机器上通过设备授权**登录**

```microcodex login --device-auth```

# SYNOPSIS

**microcodex** [_prompt_]

**microcodex** **login** [**--device-auth**]

# PARAMETERS

**login**
> 通过 OAuth 使用 ChatGPT 套餐进行认证。默认打开浏览器 URL。

**--device-auth**
> 为无界面或远程机器使用设备码认证：打印一次性验证码和验证 URL，而不是打开浏览器。

_prompt_
> 可选的一次性任务。提供时，MicroCodex 执行该请求；不提供时，启动交互式终端 UI。

# DESCRIPTION

**microcodex** 是一个用 **C++23** 编写的超轻量编码智能体，可在你的终端中本地运行。它在一个小型原生二进制文件中重新实现了 OpenAI/Codex 风格智能体工作流的核心：一次性提示词、交互式 TUI、本地编程工具（读写/编辑文件、运行 shell 命令、glob 搜索）、持久化对话以及自动上下文压缩。

认证通过 **microcodex login** 使用 ChatGPT 套餐完成。凭据存储在 **$CODEX_HOME** 下，若 **CODEX_HOME** 未设置则为 **~/.codex**——与 OpenAI Codex 相同的主目录布局。MicroCodex 还会从 **$CODEX_HOME/skills**（或 **~/.codex/skills**）发现 Codex 文件系统技能：每个技能是一个包含 **SKILL.md** 文件的目录，其 YAML frontmatter 包含 **name** 和 **description**。技能元数据会在会话开始时注入智能体指令；只有当任务匹配时才会加载完整的技能内容。

Linux 运行时需要 **libcurl** 和 **OpenSSL**。发行版为 Linux 和 macOS（x86_64 和 arm64）提供预构建的二进制文件；安装脚本会自动选择匹配的构建。从源码构建需要 C++23 工具链、**make** 以及相应的开发库。

# CAVEATS

MicroCodex **不是沙箱**。启动用户 shell 之前，它会应用一个简单的**词法拒绝列表**，阻止强制删除文件（**rm -f** / **rm -rf**）、**git reset --hard**、强制 **git clean**、**git checkout --**、磁盘格式化工具和关机命令。该防护不是 shell 解析器，也不是完整的安全边界：未识别的破坏性命令以及所有文件操作都以与 MicroCodex 进程相同的权限运行。

MCP 支持尚未实现。使用交互式 UI 时目前无法从终端复制文本。需要通过 **microcodex login** 提供 ChatGPT 套餐（或兼容的 OAuth 路径）。

# HISTORY

**MicroCodex** 以开源（Apache-2.0 许可证）形式发布，是 OpenAI Codex 风格终端编码智能体的 C++ 重实现，目标是打造一个亚兆字节级的原生二进制文件，配备本地工具和持久化会话，而非庞大的运行时技术栈。

# SEE ALSO

[codex](/man/codex)(1), [claude](/man/claude)(1), [cline](/man/cline)(1), [aider](/man/aider)(1), [opencode](/man/opencode)(1)

# RESOURCES

```[Source code](https://github.com/paoloanzn/microcodex)```

<!-- verified: 2026-08-03 -->
