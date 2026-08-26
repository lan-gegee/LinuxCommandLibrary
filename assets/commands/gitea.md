# TAGLINE

带 Web 界面的自托管 Git 服务

# TLDR

**启动 Gitea 服务器**

```gitea```

**以指定配置启动**

```gitea --config [/etc/gitea/app.ini]```

**生成密钥**

```gitea generate secret [INTERNAL_TOKEN]```

**创建管理员用户**

```gitea admin user create --username [admin] --password [password] --email [admin@example.com] --admin```

**运行健康检查**

```gitea doctor check```

**将完整安装转储为归档文件**

```gitea dump```

**执行待处理的数据库迁移**

```gitea migrate```

# SYNOPSIS

**gitea** [_global options_] _command_ [_command options_]

# PARAMETERS

**web**
> 启动 Web 服务器。

**admin**
> 执行管理操作：管理用户（**user**）、认证源（**auth**），或重新生成钩子/密钥（**regenerate**）。

**cert**
> 生成自签名 SSL 证书。

**doctor**
> 诊断并可选地修复安装问题（**check**、**recreate-table**）。

**dump**
> 将完整安装（数据库、仓库、配置等）导出为压缩归档。

**dump-repo** / **restore-repo**
> 在 Gitea 实例之间迁移仓库数据。

**generate**
> 生成随机密钥/令牌：`INTERNAL_TOKEN`、`JWT_SECRET`、`SECRET_KEY`、`LFS_JWT_SECRET`。

**keys**
> 提供用于 SSHD 集成的 `AuthorizedKeysCommand` 输出。

**manager**
> 控制正在运行的实例：关机、重启、刷新队列、调整日志。

**migrate**
> 执行待处理的数据库迁移；通常在首次启动前运行一次。

**-c**, **--config** _FILE_
> 配置文件的路径（默认 `custom/conf/app.ini`）。

**-w**, **--work-path** _PATH_
> Gitea 的基础工作目录。

**-C**, **--custom-path** _PATH_
> 自定义文件夹的路径。

**--port** _PORT_
> 服务器端口（web 命令）。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**gitea** 是一个用 Go 编写的自托管 Git 服务。它提供类似 GitHub 的功能，包括仓库、议题、pull request 和 CI/CD，全部封装在单个二进制文件中。

Gitea 轻量快速，适合个人或小团队使用。它支持 OAuth、LDAP 以及多种数据库后端，可满足企业部署需求。

# CONFIGURATION

**/etc/gitea/app.ini**
> 主配置文件，控制服务器设置、数据库、身份验证和仓库默认值。

# CAVEATS

生产环境需要进行配置。需要设置数据库。建议使用反向代理。

# HISTORY

Gitea 于 **2016 年**从 **Gogs** 分叉而来，成为由社区驱动的项目，拥有活跃的开发和更丰富的功能集。

# INSTALL

```pacman: sudo pacman -S gitea```

```apk: sudo apk add gitea```

```brew: brew install gitea```

```nix: nix profile install nixpkgs#gitea```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [gitlab-runner](/man/gitlab-runner)(1), [gitlab](/man/gitlab)(1)

# RESOURCES

```[Source code](https://github.com/go-gitea/gitea)```

```[Homepage](https://about.gitea.com/)```

```[Documentation](https://docs.gitea.com/)```

<!-- verified: 2026-07-17 -->
