# TAGLINE

打包和导入可移植的 AI 编程智能体配置包

# TLDR

在构建前**校验** agent 清单

```vaen validate```

从当前清单**构建** .agent 归档

```vaen build -f agent.yaml -o my-setup.agent```

**查看** .agent 归档的内容

```vaen inspect my-setup.agent```

将 .agent 包**导入**目标仓库以供 Claude Code 使用

```vaen import my-setup.agent --client claude --target /path/to/repo```

对导入的配置进行**体检**

```vaen doctor --client claude --target /path/to/repo```

验证完成后**清理**本地保存的标准副本

```vaen cleanup```

# SYNOPSIS

**vaen** _subcommand_ [_options_]

# DESCRIPTION

**vaen** 是一个 Python CLI，它把 AI 编程智能体的配置（指令、技能和 MCP 服务器声明）打包成扩展名为 `.agent` 的可移植 OCI 风格归档，从而可以在不同仓库或团队成员之间共享，无需复制粘贴文件。

`.agent` 包会声明存在哪些指令文件、捆绑了哪些技能、期望哪些 MCP 服务器，以及哪些环境变量名用于存放凭据。它绝不包含凭据的实际值，只包含接收者需要在本地填充的变量名。`import` 会将包实例化到面向特定客户端（例如 Claude Code）的目标仓库中，并把文件写入预期的位置。`doctor` 用于验证导入结果的结构是否有效。

vaen 之所以存在，是因为 zip 文件只能移动文件，却无法描述这份配置是什么、文件应该落在哪里，以及接收者必须提供哪些密钥。

# PARAMETERS

**validate**
> 检查清单语法。

**build**
> 构建 `.agent` 归档。标志：`-f` 清单，`-o` 输出文件名。

**inspect** _archive_
> 打印 `.agent` 归档的内容而不执行导入。

**import** _archive_
> 将包实例化到目标位置。标志：`--client`、`--target`、`--target-instructions-file-name`、`--target-skills-directory`。

**doctor**
> 校验导入的结构。接受与 `import` 相同的 client 和 target 标志。

**cleanup**
> 移除本地保存的标准副本。

# CONFIGURATION

包由一个 `agent.yaml` 清单描述，其中列出指令、技能、MCP 服务器、所需的环境变量名以及版本和发布者等元数据。

# INSTALLATION

使用 `pipx` 从项目的 GitHub 仓库安装：

```pipx install git+https://github.com/sjhalani7/vaen.git```

# SEE ALSO

[claude](/man/claude), [pipx](/man/pipx)
