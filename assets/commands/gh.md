# TAGLINE

GitHub 官方命令行界面

# TLDR

**克隆仓库**

```gh repo clone [owner]/[repo]```

**创建拉取请求**

```gh pr create --title "[title]" --body "[description]"```

**列出打开的 issues**

```gh issue list```

**查看拉取请求状态**

```gh pr status```

**创建新仓库**

```gh repo create [name] --public```

**查看并检出拉取请求**

```gh pr checkout [pr_number]```

**查看工作流运行状态**

```gh run list```

**在浏览器中打开仓库**

```gh browse```

# SYNOPSIS

**gh** _command_ [_subcommand_] [_flags_]

# PARAMETERS

**repo**
> 管理仓库。

**pr**
> 管理拉取请求。

**issue**
> 管理 issues。

**auth**
> 向 GitHub 进行身份验证。

**browse**
> 在浏览器中打开仓库。

**gist**
> 管理 gists。

**workflow**
> 管理 GitHub Actions 工作流。

**run**
> 查看并管理工作流运行。

**release**
> 管理发布（release）。

**codespace**
> 管理 GitHub Codespaces。

**search**
> 全站搜索仓库、issues 和拉取请求。

**project**
> 管理 GitHub Projects。

**cache**
> 管理 GitHub Actions 缓存。

**secret**
> 管理 GitHub Actions 的 secret。

**variable**
> 管理 GitHub Actions 变量。

**label**
> 管理 issue 和 PR 标签。

**extension**
> 管理 gh CLI 扩展。

**api**
> 发起经过身份验证的 GitHub API 请求。

**status**
> 显示相关 issue、拉取请求和通知的状态。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**gh** 是 GitHub 官方的命令行工具。它把 GitHub 的功能带到终端，让你无需离开开发环境即可管理仓库、issue、拉取请求等。

该工具与 git 工作流深度集成，使本地开发与 GitHub 协作之间可以无缝衔接。它既为复杂操作提供交互式提示，也支持面向 CI/CD 流水线的脚本化自动化。

gh 为 GitHub 的 REST 和 GraphQL API 提供统一接口，并内置身份验证与配置管理。

# CONFIGURATION

**~/.config/gh/config.yml**
> 用户配置文件，包含默认设置、身份验证令牌和个人偏好。

**~/.config/gh/hosts.yml**
> GitHub.com 与各 GitHub Enterprise 实例的身份验证凭据。

# CAVEATS

需要通过 **gh auth login** 进行身份验证。部分功能需要相应的仓库权限。受 API 速率限制约束。

# HISTORY

gh 由 **GitHub** 于 **2020 年**发布，是 hub 的后继者。它使用 Go 语言编写，定位为 GitHub 的官方 CLI 伴侣工具，同时支持 github.com 和 GitHub Enterprise。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [hub](/man/hub)(1), [gh-auth](/man/gh-auth)(1), [gh-pr](/man/gh-pr)(1), [gh-issue](/man/gh-issue)(1), [gh-repo](/man/gh-repo)(1), [gh-run](/man/gh-run)(1), [gh-release](/man/gh-release)(1), [gh-copilot](/man/gh-copilot)(1)
