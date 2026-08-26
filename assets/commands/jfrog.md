# TAGLINE

JFrog Platform 官方 CLI

# TLDR

以交互方式**配置**服务器连接

```jfrog config add [server-id]```

将制品**上传**到 Artifactory

```jfrog rt upload [file_pattern] [repo/path/]```

从 Artifactory **下载**制品

```jfrog rt download [repo/path/pattern]```

在 Artifactory 中**搜索**制品

```jfrog rt search [repo/path/pattern]```

将构建信息**发布**到 Artifactory

```jfrog rt build-publish [build-name] [build-number]```

对当前项目进行安全漏洞**扫描**

```jfrog audit```

将 Docker 镜像推送到 Artifactory Docker 镜像仓库（registry）

```jfrog docker push [image:tag] [repo]```

删除匹配某模式的制品

```jfrog rt delete [repo/path/pattern]```

# SYNOPSIS

**jfrog** _command_ [_subcommand_] [_options_] [_arguments_]

# PARAMETERS

**config**
> 管理服务器配置（add、edit、remove、show、export、import）。

**rt**
> Artifactory 命令（upload、download、search、delete、copy、move、build-publish 等）。

**xr**
> Xray 命令，用于安全扫描和漏洞管理。

**audit**
> 扫描项目依赖的安全漏洞与许可证合规性。

**docker**
> Docker registry 集成（通过 Artifactory 进行推送和拉取）。

**npm**, **pip**, **go**, **maven**, **gradle**, **nuget**
> 各软件包管理器集成，并附带构建信息收集功能。

**--url** _URL_
> JFrog Platform 的 URL。

**--access-token** _TOKEN_
> 用于身份验证的访问令牌。

**--user** _USER_
> 用于身份验证的用户名。

**--password** _PASSWORD_
> 用于身份验证的密码。

**--server-id** _ID_
> 使用指定的已配置服务器。

**--help**
> 显示命令的帮助信息。

# DESCRIPTION

**jfrog** 是 JFrog Platform 的官方 CLI。它提供统一的命令行访问方式，用于操作 Artifactory、Xray、Distribution、Pipelines 以及其他 JFrog 服务。

该工具管理所有主流包类型的二进制制品，包括 Maven、npm、PyPI、Docker、Go、NuGet 和通用文件。它可与 CI/CD 流水线集成，用于构建信息收集、晋级和安全扫描。该 CLI 支持文件规格（基于 JSON 的查询语法）以进行高级制品操作。

在较新的版本中，**jfrog** 可执行文件已更名为 **jf**，不过 **jfrog** 名称仍可作为别名继续使用。

# CAVEATS

需要 JFrog 服务器（自托管或 SaaS）。Xray 扫描等企业级功能需要相应的许可证。服务器配置按用户存储在本地，使用前必须先通过 **jfrog config add** 进行设置。

# HISTORY

JFrog CLI 由 **JFrog** 创建，旨在为其制品管理平台提供统一的命令行访问。从 2022 年起，CLI 可执行文件由 **jfrog** 更名为 **jf**，但两个名称均可用。

# SEE ALSO

[jf](/man/jf)(1), [docker](/man/docker)(1), [mvn](/man/mvn)(1), [npm](/man/npm)(1), [pip](/man/pip)(1), [go](/man/go)(1), [gradle](/man/gradle)(1)
