# TAGLINE

动手式软件工程挑战平台 CLI

# TLDR

**登录** CodeCrafters

```codecrafters login```

为当前挑战阶段**运行测试**

```codecrafters test```

**提交你的解决方案**并进入下一阶段

```codecrafters submit```

**显示当前挑战状态**

```codecrafters status```

**查看当前挑战说明**

```codecrafters instructions```

克隆一个挑战仓库以开始

```codecrafters clone [challenge-slug]```

# SYNOPSIS

**codecrafters** _command_ [_options_]

# PARAMETERS

**login**
> 使用你的 CodeCrafters 账户进行认证。

**test**
> 在本地运行当前挑战阶段的测试。

**submit**
> 将你的解决方案提交给 CodeCrafters 评估。

**status**
> 显示当前进度和阶段信息。

**instructions**
> 显示当前挑战阶段的说明。

**clone** _SLUG_
> 克隆一个挑战仓库，开始着手。

**logout**
> 退出你的 CodeCrafters 账户。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**codecrafters** 是 CodeCrafters 平台的命令行接口，该平台提供从零开始构建真实软件的挑战项目。项目包括构建你自己的 Redis、Git、Docker、SQLite 以及其他复杂系统。

CLI 处理认证、测试执行和解决方案提交。它与 CodeCrafters 平台集成，跟踪多阶段挑战中的进度，每个阶段都会引入新的需求和复杂度。

挑战的完成方式是实现能通过难度递增的测试的代码。本地 test 命令在开发过程中提供快速反馈，而 submit 则针对 CodeCrafters 服务器上的完整测试套件进行验证。

# CAVEATS

需要有效的 CodeCrafters 账户。部分挑战需要付费订阅。CLI 需要网络连接才能提交解决方案和验证进度。挑战仓库必须从 CodeCrafters 克隆，以包含必要的测试配置。

# HISTORY

CodeCrafters 的创立宗旨是为有经验的开发者提供动手学习体验。平台以重现流行软件工具的挑战起步，让开发者深入理解其内部原理。CLI 的开发旨在提供与平台集成的无缝本地开发体验。

# INSTALL

```aur: yay -S codecrafters```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [exercism](/man/exercism)(1)

# RESOURCES

```[Source code](https://github.com/codecrafters-io/cli)```

```[Documentation](https://docs.codecrafters.io/)```

<!-- verified: 2026-06-22 -->
