# TAGLINE

面向代码库的智能体式开源安全扫描器

# TLDR

**启动**交互式 TUI

```openhack```

以无头模式**扫描**当前目录（适合 CI）

```openhack scan```

**扫描**指定仓库路径

```openhack scan [path/to/repo]```

**列出**已保存的扫描会话

```openhack sessions```

**恢复**被中断的扫描

```openhack resume [session-id]```

无需 LLM 调用即可**分类**框架

```openhack classify [path]```

# SYNOPSIS

**openhack** [_options_]

**openhack** **scan** [_path_]

**openhack** **sessions**

**openhack** **resume** _session-id_

**openhack** **classify** [_path_]

**openhack** **login**

**openhack** **setup**

# PARAMETERS

**--help**
> 显示用法信息。

# DESCRIPTION

**openhack** 是一个智能体式安全扫描器，针对代码库运行多阶段流水线：**recon**（构建项目模型）、**hunters**（按类别和特性搜索漏洞）、**validation**（确认或否决候选问题），以及可选的 **verification**（沙箱或浏览器利用测试）。它被设计为专有智能体安全工具的开源替代品，并通过 OpenHack 推理 API 使用开源模型。

交互式 TUI 是默认入口。首次运行时，**openhack setup** 会引导完成账户登录（浏览器 OAuth，含免费额度）或 API 密钥配置。在 TUI 内部，斜杠命令驱动整个工作流：**/scan** _path_ 启动一次扫描，**Trace** 标签页实时显示智能体活动，**Findings** 标签页列出已确认的问题及其严重性、CVSS 评分、文件位置、存在漏洞的代码和建议修复方法。

无头模式（**openhack scan**）为脚本和 CI 运行同一条流水线，将进度打印到 stdout，并将 JSON 报告写入 **~/.openhack/scans/**_session-id_**.json**。每个阶段完成后都会保存检查点；如果中途被中断，**openhack resume** 会从上一个检查点继续。

可选的 **/verify sandbox**（需要 Docker）会启动应用程序并尝试真实的 HTTP 利用。**/verify browser** 增加无头浏览器检查，用于发现 XSS 和 CSRF 等客户端问题。源代码在本地处理；只有 LLM token 会发送到推理 API，不会发送原始文件。

# CONFIGURATION

**~/.openhack/config**
> 持久化配置，包含 API bearer 令牌（权限模式 **0600**）。

**OPENHACK_API_KEY**
> 用于覆盖推理 API 令牌的环境变量。

**OPENHACK_DEV=1**
> 让 CLI 指向本地开发服务器，用于自托管部署。

# CAVEATS

沙箱和浏览器验证需要正在运行的 Docker 守护进程。TUI 默认捕获鼠标事件；拖拽选择文本时请按住 **Option**（macOS）或 **Shift**（Linux），或运行 **/mouse** 禁用捕获。本项目采用 AGPL-3.0 许可证；不承担 AGPL 义务的商业使用需要向项目维护者获取单独授权。

# SEE ALSO

[semgrep](/man/semgrep)(1), [trivy](/man/trivy)(1), [grype](/man/grype)(1)
