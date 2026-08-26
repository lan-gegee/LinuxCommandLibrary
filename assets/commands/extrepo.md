# TAGLINE

外部 Debian 软件仓库管理器

# TLDR

**搜索**软件仓库

```extrepo search keyword```

**启用**软件仓库

```sudo extrepo enable repository_name```

**禁用**软件仓库

```sudo extrepo disable repository_name```

**更新**软件仓库

```sudo extrepo update repository_name```

**列出**所有可用的软件仓库

```extrepo search```

# SYNOPSIS

**extrepo** [_command_] [_arguments_]

# DESCRIPTION

**extrepo** 以安全、标准化的方式管理外部 Debian 软件仓库。它提供一个经过 Debian 项目审核的第三方仓库精选集合，每个仓库都具有经过验证的 GPG 密钥和正确的配置。

extrepo 让你无需手动编辑 /etc/apt/sources.list 或使用 add-apt-repository 添加不受信任的来源，而是提供一种安全的方法来启用 Docker、Node.js、Kubernetes 等热门外部仓库。所有仓库配置都集中维护，并包含适当的安全验证。

该工具帮助避免向 Debian 系统添加第三方软件源时的常见问题，如不安全的仓库添加、缺少 GPG 密钥或 sources.list 语法错误。

# PARAMETERS

**search [KEYWORD]**
> 搜索匹配关键字的仓库（不带关键字则列出全部）

**enable REPO**
> 启用指定的仓库

**disable REPO**
> 禁用指定的仓库

**update REPO**
> 更新仓库配置

# CAVEATS

启用/禁用操作需要 root 权限。仅提供经过 Debian 项目审核的仓库。启用仓库后，请运行 apt update 刷新软件包列表。

# HISTORY

**extrepo** 为 Debian 开发，旨在提供一种管理外部仓库的安全方法，用经过验证的仓库配置取代手动编辑 sources.list 的做法。

# SEE ALSO

[apt](/man/apt)(8), [add-apt-repository](/man/add-apt-repository)(1)
