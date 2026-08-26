# TAGLINE

自动化版本管理与软件包发布

# TLDR

在当前项目中**运行 semantic-release**

```npx semantic-release```

**使用指定版本运行**

```npx semantic-release@[25]```

执行**试运行**，预览发布内容而不实际发布

```npx semantic-release --dry-run```

**附加其他插件运行**

```npx --package semantic-release --package @semantic-release/exec semantic-release```

使用指定的 **branches** 配置运行

```npx semantic-release --branches [main]```

运行时忽略 CI 环境检测

```npx semantic-release --no-ci```

**指定仓库 URL**

```npx semantic-release --repository-url [https://github.com/user/repo.git]```

# SYNOPSIS

**semantic-release** [_options_]

**npx semantic-release** [_options_]

# PARAMETERS

**-d**, **--dry-run**
> 以试运行模式执行，预览待发布的内容而不实际发布。跳过 prepare、publish、addChannel、success 和 fail 步骤。将下一个版本号和发布说明打印到控制台。

**--ci**, **--no-ci**
> 切换 CI 环境验证。使用 **--no-ci** 可在 CI 之外的本地环境中运行 semantic-release。适用于测试和调试。

**-b**, **--branches**
> 定义应在哪些分支上发布。接受分支名称或 micromatch glob 模式。

**-p**, **--plugins**
> 定义要使用的插件列表。

**-r**, **--repository-url**
> Git 仓库 URL。

**-t**, **--tag-format**
> 用于识别发布的 Git 标签格式。默认：**v${version}**。

**-e**, **--extends**
> 要扩展的可共享配置。

**--debug**
> 启用调试输出。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**semantic-release** 自动化整个软件包发布流程，包括版本确定、变更日志生成和软件包发布。它基于约定式提交（conventional commit）消息分析自上次发布以来的提交，自动确定下一个语义化版本号。

该工具遵循 Semantic Versioning 规范：fix 提交触发补丁版本发布，feat 提交触发次版本发布，包含 BREAKING CHANGE 的提交触发主版本发布。它通过插件系统与 npm、GitHub、GitLab 及其他平台集成。

配置可以通过 **package.json**、**.releaserc** 文件、**release.config.js** 或命令行参数提供。默认从 **main** 或 **master** 分支发布，并支持预发布渠道（alpha、beta）和维护分支。

# CONFIGURATION

**.releaserc**
> 项目级配置文件（JSON 或 YAML），指定分支、插件和发布选项。

**release.config.js**
> JavaScript 配置文件，是程序化发布配置的替代方式。

**package.json**（release 键）
> 配置也可以嵌入 package.json 的 "release" 键下。

**GH_TOKEN** / **GITHUB_TOKEN**
> GitHub 身份验证令牌，用于创建发布和在 issue 上评论。

**NPM_TOKEN**
> npm 身份验证令牌，用于向 registry 发布软件包。

# CAVEATS

semantic-release 必须在具有仓库推送权限和软件包 registry 发布权限的 CI 环境中运行。试运行模式仍会验证仓库推送权限。提交必须遵循约定式提交格式才能进行自动版本检测。插件选项不能通过 CLI 设置，必须在配置文件中配置。

# HISTORY

**semantic-release** 由 Stephan Boennemann 创建，于 **2015 年**首次发布，旨在解决手动且易出错的软件发布问题。它开创了基于提交消息约定的全自动发布理念。该项目在 JavaScript/Node.js 生态中被广泛采用，并影响了其他语言的类似工具。它在 GitHub 的 semantic-release 组织下持续活跃开发。

# INSTALL

```nix: nix profile install nixpkgs#semantic-release```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [git](/man/git)(1)
