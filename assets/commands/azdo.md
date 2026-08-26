# TAGLINE

Azure DevOps 的终端界面

# TLDR

**启动**交互式 TUI

```azdo```

用逼真的模拟数据**试用**，无需任何设置

```azdo demo```

**设置或更新**Azure DevOps 个人访问令牌

```azdo auth```

**显示**版本号

```azdo --version```

# SYNOPSIS

**azdo** [_command_] [_options_]

# DESCRIPTION

**azdo** 是一个面向 **Azure DevOps** 的终端用户界面。它把拉取请求、工作项和流水线带进键盘驱动的控制台应用，让你无需切换到 Web 门户即可审查和管理这些内容。

在 TUI 中，你可以列出并筛选拉取请求、查看 diff、投票以及添加行内评论；浏览工作项并更改其状态；还可以监控流水线运行情况，深入到单个阶段（stage）、作业（job）和任务（task），并查看日志。可选的指标仪表板提供实时状态和趋势分析；该工具还支持多个项目、多种内置主题，以及在会话之间保留的状态。

身份验证使用 Azure DevOps **个人访问令牌（PAT）**，存储在系统密钥环中（也可通过 **AZDO_PAT** 环境变量提供）。配置（包括组织和项目名称）保存在 **~/.config/azdo-tui/config.yaml**。

# PARAMETERS

**demo**

> 启动填充了模拟数据的界面，无需任何配置即可探索。

**auth**

> 设置或更新已存储的个人访问令牌。

**--version**

> 输出版本信息并退出。

**--help**

> 显示用法信息。

# CONFIGURATION

**~/.config/azdo-tui/config.yaml**

> 保存组织名称、项目列表，以及可选设置，例如轮询间隔、主题和指标选项。

**AZDO_PAT**

> 环境变量，当密钥环中找不到个人访问令牌时作为后备来源。

# CAVEATS

个人访问令牌需要具备适当的作用域（通常为 Build 读取、Code 读/写、Work Items 读/写），所有功能才能正常工作。azdo 是一个年轻的第三方项目，与微软没有隶属关系，其行为可能随版本更迭而变化。

# SEE ALSO

[az](/man/az)(1), [gh](/man/gh)(1), [glab](/man/glab)(1), [lazygit](/man/lazygit)(1), [tig](/man/tig)(1)

# RESOURCES

```[Source code](https://github.com/Elpulgo/azdo)```

<!-- verified: 2026-06-16 -->
