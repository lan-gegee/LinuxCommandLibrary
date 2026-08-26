# TAGLINE

仅当 AI 编码代理工作时保持 macOS 唤醒

# TLDR

在代理会话开始时**获取**阻止睡眠的断言

```adrafinil acquire [session-key] --tool [claude-code] --reason "[long build]"```

在代理空闲时**释放**断言

```adrafinil release [session-key]```

为限时后台任务**保持** Mac 唤醒

```adrafinil hold --for [30m] --reason "[deploy]"```

**查看**当前断言状态

```adrafinil status```

为受支持的代理**安装**钩子集成

```adrafinil install-hooks```

# SYNOPSIS

**adrafinil** _subcommand_ [_options_] [_arguments_]

# PARAMETERS

**acquire** _session-key_
> 注册一个活动的代理会话，并在持有期间阻止系统睡眠。由代理钩子在会话开始或提交提示词时调用。

**release** _session-key_
> 删除一条会话断言；最后一个断言被释放后即恢复睡眠。

**hold** **--for** _duration_
> 在代理完成后让 Mac 保持唤醒一段有限时间（例如漫长的构建或部署）。

**mcp**
> 在标准输入输出上提供 Model Context Protocol 服务，使支持 MCP 的代理可以获取和释放保持锁。

**status**
> 打印守护进程的断言注册表，以及当前是否阻止了睡眠。

**install-hooks** / **uninstall-hooks**
> 在代理配置文件中添加或移除 Adrafinil 钩子条目（Claude Code、Codex、Cursor、Gemini CLI、Aider、Hermes、OpenCode、Cline、Pi）。

**daemon-status**
> 报告后台守护进程和特权辅助程序是否正在运行。

**version**
> 打印 CLI 版本。

# DESCRIPTION

**adrafinil** 是 **Adrafinil** 的命令行界面。Adrafinil 是一款 macOS 工具，只有在一个或多个 AI 编码代理会话持有活动断言时才阻止系统睡眠——包括**合盖（合上顶盖）睡眠**。与 **caffeinate** 或 Amphetamine 这类始终生效的工具不同，adrafinil 在没有任何代理工作时不会做任何事；此时合上盖子，Mac 会照常进入睡眠。

代理钩子系统会在一轮任务开始时调用 **adrafinil acquire**，在代理停止时调用 **adrafinil release**，因此只在真正工作期间阻止睡眠。一个采用引用计数的守护进程负责跟踪相互重叠的会话，并指挥一个小型特权辅助程序切换睡眠阻止状态。该辅助程序使用 **IOPMAssertion** 应对空闲睡眠，使用 **pmset disablesleep** 覆盖合盖行为。

该 CLI 随 Adrafinil.app 应用包一同分发，并在安装过程中通过符号链接加入 **PATH**。**acquire**/**release** 调用的往返耗时目标低于 50 毫秒，以免钩子拖慢代理工作流。

# CAVEATS

仅限 macOS；已在 **macOS Tahoe 26.4** 及更高版本上测试。要覆盖合盖睡眠，需要通过 **SMAppService** 安装特权辅助程序（首次启动需要管理员权限）。辅助程序在重启时会重置 **pmset disablesleep**，以避免崩溃后遗留永久性的睡眠阻止。如果在合盖状态下机身/CPU 温度越过阈值，热保护机制会强制释放所有断言。

# HISTORY

**Adrafinil** 由 **@kageroumado** 创建，于 **2026** 年发布，作为能感知代理工作状态的替代方案，区别于一刀切的防休眠工具。其名称取自促醒化合物阿德拉非尼（adrafinil），恰好呼应了这款工具只在工作进行时保持机器唤醒的特性。

# SEE ALSO

[caffeinate](/man/caffeinate)(1), [pmset](/man/pmset)(8)

# RESOURCES

```[Source code](https://github.com/kageroumado/adrafinil)```

```[Homepage](https://kagerou.glass/adrafinil/)```

<!-- verified: 2026-06-28 -->
