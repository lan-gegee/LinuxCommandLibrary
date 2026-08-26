# TAGLINE

AWS ECS 终端仪表盘（ECS 版 k9s）

# TLDR

**启动** ECS 仪表盘

```e1s```

**连接**到指定的 AWS profile

```e1s --profile [profile_name]```

启动时**查看**特定集群

```e1s --cluster [cluster_name]```

**连接**到指定区域

```e1s --region [us-west-2]```

# SYNOPSIS

**e1s** [_options_]

# PARAMETERS

**--profile** _NAME_
> 要使用的 AWS profile。

**--region** _REGION_
> AWS 区域（默认：来自配置）。

**--cluster** _NAME_
> 默认要查看的 ECS 集群。

**--service** _NAME_
> 默认要查看的 ECS 服务（需要 --cluster）。

**--read-only**
> 以只读模式启动。

**-c**, **--config-file** _FILE_
> 配置文件路径（默认：~/.config/e1s/config.yml）。

**-r**, **--refresh** _SECONDS_
> 自动刷新间隔（秒）（默认：30，-1 表示禁用）。

**-s**, **--shell** _PATH_
> 用于交互式 exec 的 shell（默认：/bin/sh）。

**-d**, **--debug**
> 启用调试日志。

**-l**, **--log-file** _FILE_
> 自定义日志文件路径。

**-j**, **--json**
> 以 JSON 格式输出日志。

**-v**, **--version**
> 显示版本并退出。

**-h**, **--help**
> 显示帮助并退出。

# DESCRIPTION

**e1s** 是 Amazon ECS（Elastic Container Service）的终端用户界面，其灵感来自 Kubernetes 生态中的 k9s。它提供一个实时仪表盘，用于监控 ECS 集群、服务、任务和容器。

该工具让用户无需离开终端即可查看资源状态、查看日志、在容器中执行命令以及管理部署。它与 AWS 凭据集成，并支持多个 profile 和区域。

# KEYBINDINGS

**h/j/k/l**
> Vim 风格导航（左/下/上/右）

**Enter**
> 查看资源详情

**/**
> 过滤资源

**ctrl-p**
> 切换 AWS profile

**ctrl-d**
> 退出交互式 exec 会话

**q**
> 退出

**?**
> 显示所有键绑定

# CAVEATS

需要具有相应 ECS 权限的 AWS 凭据。某些操作需要额外的 IAM 权限。日志流传输可能产生 AWS CloudWatch 费用。需要与 AWS 保持网络连通。

# HISTORY

**e1s** 作为 k9s 的 ECS 对应物而创建，将强大的基于终端的管理体验带给 AWS ECS 用户。它填补了在 ECS 上管理容器化应用的工具空白。

# INSTALL

```brew: brew install e1s```

```nix: nix profile install nixpkgs#e1s```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [k9s](/man/k9s)(1), [docker](/man/docker)(1)
