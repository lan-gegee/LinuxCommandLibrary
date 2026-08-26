# TAGLINE

GitLab 官方 CLI 工具

# TLDR

**向 GitLab 进行身份验证**

```glab auth login```

**创建合并请求**

```glab mr create```

**列出合并请求**

```glab mr list```

**查看合并请求**

```glab mr view [number]```

**创建议题**

```glab issue create```

**克隆仓库**

```glab repo clone [owner/repo]```

**查看 CI/CD 流水线**

```glab ci list```

**发起原始 API 请求**

```glab api [/projects/:id/issues]```

# SYNOPSIS

**glab** _command_ [_options_]

# PARAMETERS

**mr** _subcommand_
> 合并请求操作（create、list、view、merge、close、checkout、approve）。

**issue** _subcommand_
> 议题操作（create、list、view、close、reopen、note）。

**repo** _subcommand_
> 仓库操作（clone、fork、view、archive）。

**ci** _subcommand_
> CI/CD 流水线操作（list、view、run、trace、retry）。

**auth** _subcommand_
> 身份验证（login、status、logout）。

**release** _subcommand_
> 管理发行版（create、list、view、delete）。

**config** _subcommand_
> 配置管理。

**api** _endpoint_
> 向 GitLab 发起经过身份验证的 API 请求。

**snippet** _subcommand_
> 创建和管理代码片段。

**variable** _subcommand_
> 管理 CI/CD 变量。

**label** _subcommand_
> 管理项目标签。

**-R** _repo_, **--repo** _repo_
> 目标仓库（owner/repo 格式）。

# DESCRIPTION

**glab** 是 GitLab 官方的 CLI 工具。它提供对 GitLab 各项功能的命令行访问，包括合并请求、议题、CI/CD 流水线和仓库管理。

该工具仿照 GitHub 的 `gh` CLI 的设计思路，为 GitLab 用户提供了熟悉的操作界面。它同时支持 GitLab.com 和自托管实例。

# CONFIGURATION

**~/.config/glab-cli/config.yml**
> 配置文件，保存身份验证令牌、默认设置和主机配置。

# CAVEATS

需要 GitLab 访问令牌。部分功能可能需要特定权限。自托管实例需要进行主机名配置。API 有速率限制。

# HISTORY

glab 由 **Clement Sam** 创建，后来成为 GitLab 官方 CLI。它的灵感来自 GitHub 的 gh CLI，为 GitLab 用户提供了类似的功能。

# INSTALL

```apt: sudo apt install glab```

```dnf: sudo dnf install glab```

```pacman: sudo pacman -S glab```

```apk: sudo apk add glab```

```zypper: sudo zypper install glab```

```brew: brew install glab```

```nix: nix profile install nixpkgs#glab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [git](/man/git)(1), [gitlab-runner](/man/gitlab-runner)(1)
