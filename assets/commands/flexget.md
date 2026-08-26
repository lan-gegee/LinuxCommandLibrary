# TAGLINE

多用途媒体自动化工具

# TLDR

**运行所有任务**

```flexget execute```

**运行特定任务**

```flexget execute --task [task_name]```

**测试配置**

```flexget check```

**启动守护进程**

```flexget daemon start```

**停止守护进程**

```flexget daemon stop```

**显示任务状态**

```flexget status```

**列出剧集**

```flexget series list```

# SYNOPSIS

**flexget** [_options_] _command_ [_args_]

# SUBCOMMANDS

**execute**
> 运行任务。

**check**
> 校验配置。

**daemon**
> 管理守护进程。

**status**
> 显示状态。

**series**
> 管理剧集。

**movie-list**
> 管理电影列表。

**entry-list**
> 管理条目列表。

**seen**
> 管理已见条目。

# PARAMETERS

**--task** _name_
> 运行特定任务。

**-c**, **--config** _file_
> 配置文件。

**--test**
> 测试模式（不执行任何动作）。

**--no-cache**
> 禁用缓存。

# CONFIGURATION

**~/.flexget/config.yml**
> 主配置文件，定义自动化工作流中的任务、订阅源和过滤器。

# DESCRIPTION

**FlexGet** 是一款强大的媒体内容自动化管理工具，通过可自定义的任务和插件运作。它监控 RSS 订阅源、种子站点和其他来源，根据用户自定义的规则和过滤器自动下载并整理电视剧、电影、播客等媒体内容。

该工具基于在 YAML 配置文件中定义的任务系统运作。任务可以按画质、剧集追踪、发布组或自定义模式过滤内容。FlexGet 与 Transmission、Deluge、qBittorrent 等下载客户端以及 Plex、Kodi 等媒体管理工具集成。

FlexGet 可以作为守护进程持续监控运行，也可以按需执行任务。它维护一个已见条目的数据库以防止重复下载，并支持自动跟进剧集进度的剧集追踪。插件架构支持针对特定工作流进行深度定制。

# INSTALL

```apk: sudo apk add flexget```

```brew: brew install flexget```

```nix: nix profile install nixpkgs#flexget```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[transmission-cli](/man/transmission-cli)(1)

# RESOURCES

```[Homepage](https://flexget.com/)```

```[Source code](https://github.com/Flexget/Flexget)```

<!-- verified: 2026-07-15 -->
