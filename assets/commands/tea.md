# TAGLINE

Gitea 命令行客户端

# TLDR

**登录 Gitea 实例**

```tea login add --url [https://gitea.example.com] --token [your_token]```

**列出**当前仓库中的 issue

```tea issues```

**创建新 issue**

```tea issues create --title "[Bug report]" --body "[Description]"```

**列出拉取请求**

```tea pulls```

**创建拉取请求**

```tea pulls create --title "[Feature]" --base [main] --head [feature-branch]```

**在本地检出拉取请求**

```tea pulls checkout [42]```

**列出仓库**

```tea repos```

**克隆仓库**

```tea clone [owner/repo]```

# SYNOPSIS

**tea** _command_ [_subcommand_] [_options_]

# COMMANDS

**logins**
> 管理 Gitea 服务器认证（add、list、delete、default）

**logout**
> 移除对某台 Gitea 服务器的认证

**whoami**
> 显示当前已认证的用户

**issues**
> 创建、列出和管理 issue（create、list、edit、close、reopen）

**pulls**, **pr**
> 管理拉取请求（create、list、checkout、merge、approve、reject）

**repos**
> 显示和管理仓库（list、create、fork、delete、migrate）

**branches**
> 查看和管理分支（list、protect、unprotect）

**labels**
> 管理 issue 标签（create、list、update、delete）

**milestones**
> 跟踪项目里程碑（create、list、close、reopen）

**releases**
> 管理发布（create、list、delete、edit、assets）

**organizations**
> 管理组织（list、create、delete）

**times**
> 跟踪在 issue 上花费的时间

**notifications**
> 查看和管理通知

**comment**
> 为 issue 或拉取请求添加评论

**open**
> 在网页浏览器中打开仓库

**clone**
> 克隆仓库

# PARAMETERS

**--login**, **-l** _name_
> 使用指定的登录配置

**--repo**, **-r** _owner/repo_
> 指定仓库（默认：从当前目录自动检测）

**--output**, **-o** _format_
> 输出格式：simple、table、csv、tsv、yaml、json

**--help**, **-h**
> 显示命令帮助

**--version**, **-v**
> 显示版本

# DESCRIPTION

**tea** 是与 Gitea 服务器交互的命令行客户端。它提供类似于 GitHub 的 **gh** CLI 的功能，可以直接在终端中管理仓库、issue、拉取请求等实体。

当处于 git 仓库中时，该工具会使用当前仓库的上下文，自动检测远程的 Gitea 服务器和仓库。它在 upstream/fork 工作流下工作效果最佳，即本地 main 分支跟踪上游仓库。

可以通过 **tea logins add** 配置多台 Gitea 实例，并将其中一台设为默认。配置存储在 **$XDG_CONFIG_HOME/tea**（通常为 ~/.config/tea）。

常用命令包括用 **tea pulls checkout** 在本地获取并切换到 PR 分支，以及用 **tea open** 快速在浏览器中打开当前仓库。

# CAVEATS

tea 在执行操作前假定本地 git 状态已发布到远程。某些命令需要具备 Gitea 服务器上的相应权限。该工具专为 Gitea 设计，可能无法与其他代码托管平台配合使用。

# HISTORY

**tea** 由 **Gitea** 项目开发，是 Gitea 服务器的官方命令行界面。它使用 **Go** 编写，通过 Gitea SDK 与 Gitea API 交互。项目托管在 Gitea 自己的平台 gitea.com/gitea/tea 上。

# INSTALL

```apt: sudo apt install tea```

```pacman: sudo pacman -S tea```

```apk: sudo apk add tea```

```zypper: sudo zypper install tea```

```brew: brew install tea```

```nix: nix profile install nixpkgs#tea```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [gh](/man/gh)(1), [glab](/man/glab)(1), [hub](/man/hub)(1)
