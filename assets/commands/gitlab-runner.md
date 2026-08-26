# TAGLINE

GitLab 的 CI/CD 任务执行代理

# TLDR

**注册新的 runner**

```sudo gitlab-runner register```

**列出已配置的 runner**

```gitlab-runner list```

**启动 runner 服务**

```sudo gitlab-runner start```

**停止 runner 服务**

```sudo gitlab-runner stop```

在前台运行（用于调试）

```gitlab-runner run```

**验证 runner 连接**

```gitlab-runner verify```

**注销一个 runner**

```sudo gitlab-runner unregister --name [runner_name]```

**检查 runner 状态**

```gitlab-runner status```

**重置 runner 认证令牌**

```sudo gitlab-runner reset-token --name [runner_name]```

# SYNOPSIS

**gitlab-runner** _command_ [_options_]

# PARAMETERS

**register**
> 向 GitLab 实例注册新的 runner。

**list**
> 列出所有已配置的 runner。

**start**
> 启动 runner 服务。

**stop**
> 停止 runner 服务。

**restart**
> 重启 runner 服务。

**status**
> 显示 runner 服务状态。

**run**
> 在前台运行 runner。

**run-single**
> 从 GitLab 实例执行单次构建。

**verify**
> 验证 runner 与 GitLab 的连接。

**unregister**
> 从 GitLab 移除 runner。

**reset-token**
> 重置 runner 的认证令牌。

**install**
> 安装为系统服务。

**uninstall**
> 移除系统服务。

**--debug**
> 启用调试日志。

**--log-level** _level_
> 日志级别：debug、info、warn、error、fatal、panic。

**--log-format** _format_
> 日志格式：runner、text、json。

**--config** _file_
> 使用替代配置文件。

**--working-directory** _path_
> 设置自定义工作目录。

# DESCRIPTION

**gitlab-runner** 是为 GitLab 运行 CI/CD 任务的代理。它连接到 GitLab 实例，接收任务请求，在隔离环境中执行任务，并将结果报告回去。Runner 可以跨项目共享，也可以专用于特定项目。

Runner 支持多种执行器：**shell**（直接在主机上）、**docker**（容器内）、**docker-machine**（自动扩缩的 Docker）、**kubernetes**（K8s Pod 内）、**virtualbox**、**parallels** 和 **ssh**。Docker 执行器最为常用，可提供隔离且可重现的构建。

注册需要提供 GitLab URL 以及来自项目/组/管理员 CI 设置中的注册令牌。Runner 可以作为系统服务运行，也可以为便于调试而在前台运行。

# CONFIGURATION

**/etc/gitlab-runner/config.toml**
> 主配置文件，每个已注册的 runner 在其中表现为一个 `[[runners]]` 区块，包含其 URL、令牌、执行器和设置。

# CAVEATS

Shell 执行器不为作业之间提供隔离。Docker 执行器需要安装 Docker。注册令牌应妥善保密。Runner 能访问传递给作业的任何机密信息。应配置资源限制以防止失控的任务。

# HISTORY

**GitLab Runner** 由 GitLab Inc. 开发，是其 CI/CD 平台的一部分；约在 **2015 年** GitLab CI 并入主产品后成为 GitLab 的组成部分。Runner 已从简单的 shell 执行发展为支持多种复杂执行器，成为现有最灵活多用的 CI 任务执行器之一。

# INSTALL

```pacman: sudo pacman -S gitlab-runner```

```apk: sudo apk add gitlab-runner```

```brew: brew install gitlab-runner```

```nix: nix profile install nixpkgs#gitlab-runner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [gitlab-ctl](/man/gitlab-ctl)(8), [jenkins](/man/jenkins)(1), [kubectl](/man/kubectl)(1)
