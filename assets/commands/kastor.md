# TAGLINE

使用 HCL 规范为 AI 智能体提供 Terraform 风格的单一事实来源层

# TLDR

**校验**智能体规范

```kastor validate examples/weather```

将规范**编译**为可运行的 LangGraph 代码

```kastor build examples/weather```

为托管智能体**规划**变更（Terraform 风格）

```kastor plan examples/weather```

**应用**计划以创建或更新智能体

```kastor apply examples/weather```

通过 Homebrew 或 Go **安装**

```brew install kastor```

# SYNOPSIS

**kastor** <command> [options] [path]

# DESCRIPTION

Kastor 为 AI 智能体提供声明式的、可版本化的单一事实来源。你在 HCL 文件（`.agent`、`.tool`、`.prompt`、`kastor.hcl`）中定义智能体、工具、提示词、模型和部署目标。Kastor 校验规范，可以生成可运行的框架代码（当前支持 LangGraph），并支持带状态、diff 和漂移检测的 plan/apply/destroy 操作。

它不是智能体运行时或执行器；它管理的是围绕智能体的契约与调和过程。

# COMMANDS

**validate** [path]
> 解析并校验 Kastor 模块中的引用。

**build** [path]
> 将模块编译为可运行的框架代码（例如 LangGraph 项目）。

**plan** [path]
> 显示相对目标状态的变更计划。

**apply** [path]
> 应用变更以创建/更新智能体和状态。

**destroy** [path]
> 销毁由该模块管理的智能体。

# PARAMETERS

通用选项是包含声明式文件的模块路径。许多命令作用于一个目录（模块根目录）。

# CAVEATS

- 早期概念验证；CLI 表面稳定，但托管 provider 支持有限。
- 生成的代码只是输出；`.agent`/`.tool` 文件才是事实来源。
- 运行生成的智能体需要相应的凭据（如 OPENAI_API_KEY）。

# SEE ALSO

[terraform](/man/terraform)(1)

# RESOURCES

```[Source code](https://github.com/weirdGuy/kastor)```

```[Homepage](https://www.getkastor.dev)```

```[Documentation](https://github.com/weirdGuy/kastor#readme)```

<!-- verified: 2026-07-11 -->
