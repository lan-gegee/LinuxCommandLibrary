# TAGLINE

Fedora 社区仓库管理器

# TLDR

**启用 COPR 仓库**

```sudo dnf copr enable [owner]/[project]```

**禁用 COPR 仓库**

```sudo dnf copr disable [owner]/[project]```

**列出已启用的 COPR 仓库**

```dnf copr list```

**搜索 COPR 项目**

```dnf copr search [keyword]```

**移除 COPR 仓库**及其软件包

```sudo dnf copr remove [owner]/[project]```

**启用 COPR 仓库的特定发行版**

```sudo dnf copr enable [owner]/[project] [fedora-39-x86_64]```

# SYNOPSIS

**dnf copr** _command_ [_options_] [_project_]

# PARAMETERS

**enable** _OWNER/PROJECT_
> 启用某个 COPR 仓库以便安装其中的软件包。

**disable** _OWNER/PROJECT_
> 禁用某个 COPR 仓库但不将其移除。

**remove** _OWNER/PROJECT_
> 移除 COPR 仓库配置。

**list**
> 列出所有已启用的 COPR 仓库。

**search** _KEYWORD_
> 按名称或描述搜索 COPR 项目。

**--hub** _URL_
> 使用其他 Copr 实例。

**-y**
> 对所有提示自动回答 yes。

# DESCRIPTION

**COPR**（Cool Other Package Repo）是 Fedora 的社区构建系统，允许用户创建并分享自定义 RPM 仓库。**dnf copr** 插件让你可以通过 DNF 软件包管理器轻松管理 COPR 仓库。

COPR 让开发者能够构建和分发官方 Fedora 仓库中没有的软件包，包括更新版本的软件、实验性软件包，或因许可证原因无法收入官方仓库的软件。用户只需一条命令即可启用这些仓库。

该系统会自动处理 GPG 密钥导入和仓库配置。项目以 owner/project 的格式标识，例如 **user/myproject**。每个项目可以为多个 Fedora 和 EPEL 版本进行构建。

# CAVEATS

COPR 软件包由社区维护，不受 Fedora 官方支持。只应启用你信任的仓库，因为其中可能包含任意软件。这些软件包可能与官方仓库中的版本冲突。仓库的安全与更新由其所有者负责。

# HISTORY

COPR 由 Fedora 项目创建，是一个社区构建服务，类似 Ubuntu 的 PPA。它于约 **2013** 年上线，为 Fedora 用户提供在官方发行版之外分享软件包的途径。与手动配置相比，DNF 插件简化了仓库管理。

# SEE ALSO

[dnf](/man/dnf)(1), [copr-cli](/man/copr-cli)(1), [rpm](/man/rpm)(1)

# RESOURCES

```[Source code](https://github.com/fedora-copr/copr)```

```[Homepage](https://copr.fedorainfracloud.org/)```

```[Documentation](https://docs.pagure.org/copr.copr/)```

<!-- verified: 2026-06-23 -->
