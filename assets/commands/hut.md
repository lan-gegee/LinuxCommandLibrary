# TAGLINE

SourceHut 服务的命令行客户端

# TLDR

**设置 hut 的配置**（会提示输入 OAuth2 访问令牌）

```hut init```

**列出你的 Git 仓库**

```hut git list```

**创建新的 Git 仓库**

```hut git create [repo-name]```

**列出构建任务**

```hut builds list```

**列出 issue 追踪器**

```hut todo list```

**从文件创建 paste**

```hut paste create [file]```

# SYNOPSIS

**hut** _service_ _command_ [_options_]

# PARAMETERS

_SERVICE_
> 要操作的 SourceHut 服务。

_COMMAND_
> 该服务下的命令（常见有 **list**、**create**、**show**、**update**、**delete**）。

**builds**
> 管理 builds.sr.ht 上的构建任务。

**git**
> 管理 git.sr.ht 上的 Git 仓库。

**hg**
> 管理 hg.sr.ht 上的 Mercurial 仓库。

**lists**
> 管理 lists.sr.ht 上的邮件列表和补丁集。

**meta**
> 管理账号设置、SSH/PGP 密钥以及个人资料信息。

**pages**
> 将静态网站发布到 pages.sr.ht。

**paste**
> 在 paste.sr.ht 上创建并分享文本片段。

**todo**
> 管理 todo.sr.ht 上的 issue 追踪器和工单。

**graphql**
> 对指定服务执行原始 GraphQL 查询。

**init**
> 使用 OAuth2 令牌设置 hut 的配置文件。

**export** / **import**
> 备份或恢复账号数据。

**--config** _FILE_
> 使用指定的配置文件。

**--instance** _NAME_
> 选择要使用的 sr.ht 实例。

**--debug**
> 将底层的 GraphQL 请求打印到标准错误输出。

# DESCRIPTION

**hut** 是 SourceHut（sr.ht）服务的官方命令行客户端。它提供对构建服务、Git 与 Mercurial 仓库、issue 追踪器、邮件列表、文本片段（paste）、静态站点托管以及账号管理的访问，全部基于各服务的 GraphQL API。

命令遵循 **hut** _service_ _command_ 模式，因此大多数操作都直接对应某个 sr.ht 服务。**graphql** 子命令还允许对任意服务执行任意 GraphQL 查询，可用于其他方式无法覆盖的任务。

# CAVEATS

需要 SourceHut 账号和 OAuth2 访问令牌，通过 **hut init** 进行配置。可用服务及其子命令因 sr.ht 实例和 hut 版本而异；请运行 **hut help** 或 **hut** _service_ **--help** 查看本地支持的命令。

# HISTORY

hut 是 **SourceHut**（sr.ht）的官方 CLI。SourceHut 是由 **Drew DeVault** 创建的轻量级、注重隐私的软件开发平台。hut 使用 Go 编写，取代了早期为在命令行中编写 SourceHut 服务脚本而临时编写的各类脚本。

# INSTALL

```apt: sudo apt install hut```

```dnf: sudo dnf install hut```

```pacman: sudo pacman -S hut```

```apk: sudo apk add hut```

```zypper: sudo zypper install hut```

```brew: brew install hut```

```nix: nix profile install nixpkgs#hut```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [gh](/man/gh)(1), [hub](/man/hub)(1)
