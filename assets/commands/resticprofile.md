# TAGLINE

管理 restic 备份配置和定时任务

# TLDR

**运行备份**

```resticprofile backup```

**运行指定配置**

```resticprofile -n [profile] backup```

**显示配置**

```resticprofile show```

**初始化仓库**

```resticprofile -n [profile] init```

**调度备份**

```resticprofile schedule```

**运行 forget 和 prune**

```resticprofile forget```

**取消所有配置的调度**

```resticprofile unschedule --all```

**检查仓库完整性**

```resticprofile -n [profile] check```

**列出快照**

```resticprofile snapshots```

**生成配置模板**

```resticprofile generate```

# SYNOPSIS

**resticprofile** [_-n profile_] [_options_] _command_ [_args_]

# PARAMETERS

**-n**, **--name** _PROFILE_
> 要使用的配置。

**-c**, **--config** _FILE_
> 配置文件。

**-v**, **--verbose**
> 详细输出。

**-q**, **--quiet**
> 安静模式。

**--dry-run**
> 仅模拟。

**-l**, **--log** _FILE_
> 记录日志到文件。

**--no-ansi**
> 禁用 ANSI 彩色输出。

# COMMANDS

**backup**
> 运行备份。

**forget**
> 应用保留策略。

**prune**
> 移除未使用的数据。

**snapshots**
> 列出快照。

**restore**
> 恢复文件。

**schedule**
> 管理定时任务。

**init**
> 初始化仓库。

**check**
> 验证仓库完整性。

**show**
> 显示解析后的配置。

**unschedule**
> 移除已调度的任务。

**status**
> 显示已调度任务的状态。

# DESCRIPTION

**resticprofile** 是 restic 备份工具的配置封装，将备份设置组织为命名配置。每个配置定义仓库位置、备份路径、排除模式、保留策略和调度规则，使复杂的备份策略可以通过单个配置文件管理，而不必依赖冗长的命令行参数。

该工具与系统调度器集成以自动化备份操作。在 Linux 上它创建 systemd timer 或 cron 任务，在 macOS 上使用 launchd。各配置的保留策略可以不同，因此频繁变化的数据可以采用较短的保留期，而归档可以保留更长的历史。前置和后置钩子支持发送通知、在备份前转储数据库以及在完成后执行清理任务。

所有标准 restic 命令（backup、forget、prune、restore、snapshots）都可以通过 resticprofile 运行，并自动应用对应配置的设置。**generate** 命令可创建入门配置模板。

# CONFIGURATION

**profiles.conf** / **profiles.toml** / **profiles.yaml**
> 默认配置文件（在当前目录中查找），定义备份配置、仓库、调度和保留策略。格式根据扩展名自动识别。

# CAVEATS

需要单独安装 restic。其配置文件格式是 resticprofile 特有的，与 restic 自身的选项不通用。所使用的系统调度器因操作系统而异：Linux 上为 systemd timer，macOS 上为 launchd，Windows 上为任务计划程序。

# HISTORY

**resticprofile** 作为 **restic** 备份的配置封装而创建。它简化了多个备份配置的管理和调度。

# INSTALL

```brew: brew install resticprofile```

```nix: nix profile install nixpkgs#resticprofile```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restic](/man/restic)(1), [borgbackup](/man/borgbackup)(1), [cron](/man/cron)(1), [crontab](/man/crontab)(1)
