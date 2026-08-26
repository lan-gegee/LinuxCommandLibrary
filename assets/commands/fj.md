# TAGLINE

面向终端的 Forgejo CLI

# TLDR

**登录** Forgejo 实例

```fj auth login```

**克隆**仓库

```fj repo clone [owner]/[repository]```

**交互式创建**新 issue

```fj issue create```

**在浏览器中打开**某个 issue

```fj issue browse [issue_number]```

**创建**新的 pull request

```fj pr create```

**本地检出** pull request 分支

```fj pr checkout [pr_number]```

**列出**仓库的发行版

```fj release list```

**显示**当前登录的用户

```fj whoami```

# SYNOPSIS

**fj** [_global options_] _command_ [_subcommand_] [_options_]

# DESCRIPTION

**fj** 是 **Forgejo**——一个自托管的 Git forge（Gitea 的社区驱动分支）——的命令行界面。它让你不必离开终端即可与 Forgejo 实例交互：向一台或多台服务器完成身份验证、管理仓库，以及处理 issue、pull request 和 release。

命令按名词分组，比如 **auth**、**repo**、**issue**、**pr** 和 **release**，各组都有各自的子命令和标志。完成认证后，fj 会读取当前 Git 仓库的远程地址来判断目标实例和项目，因此大多数命令可以直接在克隆目录内运行，不需要额外参数。

# PARAMETERS

**auth**

> 管理身份验证。使用 **fj auth login** 保存实例的凭据，使用 **fj auth logout** 移除凭据。

**repo**

> 操作仓库，包括 **clone**、**create** 和 **view**。

**issue**

> 创建、列出、查看和浏览 issue。

**pr**

> 创建、列出、检出和评审 pull request。

**release**

> 列出并管理仓库发行版。

**whoami**

> 显示当前登录的用户账户。

# CAVEATS

fj 仍在活跃开发之中，命令形态在不同版本之间还会变动。它针对 Forgejo 的 API 设计；某些操作在较旧的 Forgejo 或 Gitea 服务器上可能无法工作。

# SEE ALSO

[tea](/man/tea)(1), [gh](/man/gh)(1), [glab](/man/glab)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://codeberg.org/forgejo-contrib/forgejo-cli)```

<!-- verified: 2026-06-16 -->
