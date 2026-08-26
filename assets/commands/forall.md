# TAGLINE

带机器可校验证明的规格驱动编码智能体

# TLDR

**安装** CLI（需要已发布的 release）

```curl -fsSL https://forall.astrio.app/install.sh | bash```

检查**版本**

```forall --version```

在 git 仓库中**初始化** Forall

```forall init```

启动**交互式智能体**

```forall```

# SYNOPSIS

**forall** [_COMMAND_] [_OPTIONS_]

# DESCRIPTION

**forall** 是 Astrio 推出的终端编码智能体，目标是根据规格说明生成软件并附带机器可校验的证明。它以交互式 CLI 运行：安装后，用 Forall 账户的 API 密钥登录，或自带模型密钥（OpenAI / OpenRouter），在 git 仓库内运行 **forall init**，然后在终端中完成智能体工作流。

目前支持的语言包括 TypeScript、Java 和 Rust。对于偏好其他编辑器智能体的团队，Forall 还提供仅做验证的 MCP 服务器（**@astrio/forall-mcp**），报告验证结果而不取代主编码智能体。

# CAVEATS

只有 GitHub Releases 上有可用的二进制文件时安装才会成功。该智能体需要网络访问以及用于模型推理的 API 密钥。证明与验证的覆盖程度取决于项目语言和工具链；应将生成的证明视为审查流程的一部分，而非测试的替代品。

# HISTORY

**forall** 由 **Astrio Labs** 开发，以 Apache-2.0 许可证发布。

# SEE ALSO

[git](/man/git)(1), [cargo](/man/cargo)(1), [npm](/man/npm)(1)

# RESOURCES

```[Source code](https://github.com/astrio-labs/forall)```

```[Homepage](https://forall.astrio.app)```

```[Documentation](https://github.com/astrio-labs/forall/blob/main/docs/getting-started.md)```

<!-- verified: 2026-07-16 -->
