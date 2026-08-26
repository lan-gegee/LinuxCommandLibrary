# TAGLINE

用于监控 Claude Code 会话的本地仪表盘

# TLDR

**运行仪表盘**，无需安装（通过 npx 下载并执行）

```npx pulse-for-claude-code```

**将通知与审批钩子接入** Claude 的设置

```claude-pulse install-hooks```

以后台分离模式**启动**服务

```claude-pulse start```

**检查**服务是否正在运行

```claude-pulse status```

**停止**后台服务

```claude-pulse stop```

将丢失的会话**恢复**为可读的对话记录

```claude-pulse recover```

在自定义端口上**运行**仪表盘

```claude-pulse start --port [4317]```

# SYNOPSIS

**claude-pulse** _command_ [_options_]

**npx pulse-for-claude-code** [_command_] [_options_]

# DESCRIPTION

**claude-pulse** 是一个本地、无依赖的 **Claude Code** 仪表盘。它实时显示 token 用量与上下文填充情况，恢复丢失的会话，提供跨历史会话的全文搜索，并可通过通知与审批钩子远程批准工具调用（例如从手机上操作）。

一切都在本机运行：默认情况下仪表盘监听 **127.0.0.1:4317** 并在浏览器中打开。它以 **pulse-for-claude-code** 为名发布在 npm 上，安装后提供 **claude-pulse** 命令；也可以用 **npx** 临时运行，或从克隆的仓库中直接通过 **node bin/cli.js** 运行。

# PARAMETERS

**install-hooks**
> 将通知与审批钩子写入 Claude 的设置。

**start**
> 在后台以分离模式运行 Pulse。

**stop**
> 停止后台服务。

**status**
> 报告服务是否正在运行。

**restart**
> 停止并重启服务。

**recover**
> 将丢失的会话恢复为可读的对话记录。

**export-all**
> 将所有会话导出为一个压缩的 markdown 文件。

**install-service**
> （macOS）在登录时自动启动 Pulse 并支持自动重启。

**uninstall-service**
> 移除系统服务。

**--port** _PORT_
> 在 _PORT_ 上提供仪表盘服务，而非默认的 4317。

**--no-open**
> 启动时不在浏览器中打开仪表盘。

# CAVEATS

需要 Node.js 18 或更高版本。仪表盘仅绑定到 localhost；远程工具调用审批依赖于访问该本地服务，因此将其暴露到机器之外的风险由用户自行承担。钩子会修改 Claude 的设置文件，请检查 **install-hooks** 所做的更改。

# HISTORY

claude-pulse 是一个发布在 npm 上的社区工具（包名为 **pulse-for-claude-code**），旨在让 Claude Code 用户无需外部依赖即可查看 token 用量、上下文与会话历史。它基于 MIT 许可证分发。

# INSTALL

```aur: yay -S claude```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[claude](/man/claude)(1), [npx](/man/npx)(1), [node](/man/node)(1)

# RESOURCES

```[Source code](https://github.com/nikitadoudikov/claude-pulse)```

<!-- verified: 2026-06-22 -->
