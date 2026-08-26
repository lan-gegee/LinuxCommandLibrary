# TAGLINE

创建和恢复 GitLab 实例备份

# TLDR

**创建完整的 GitLab 备份**

```sudo gitlab-backup create```

**创建备份并跳过选定组件**

```sudo gitlab-backup create SKIP=db,uploads,registry```

**创建增量备份**

```sudo gitlab-backup create INCREMENTAL=yes PREVIOUS_BACKUP=[backup_id]```

**从备份文件恢复**

```sudo gitlab-backup restore BACKUP=[timestamp_version]```

只**恢复选定的组件**

```sudo gitlab-backup restore BACKUP=[timestamp] SKIP=registry,uploads```

# SYNOPSIS

**gitlab-backup** _command_ [_VAR_=_value_ ...]

# SUBCOMMANDS

**create**
> 创建 GitLab 实例的备份归档。

**restore**
> 从先前创建的备份恢复 GitLab 实例。

# PARAMETERS

**SKIP** _components_
> 要跳过的组件的逗号分隔列表。有效值：**db**、**repositories**、**uploads**、**builds**、**artifacts**、**lfs**、**registry**、**pages**、**terraform_state**、**packages**、**ci_secure_files**。

**BACKUP** _id_
> 要恢复的备份标识符（timestamp_version）。执行 **restore** 时必需。

**STRATEGY** _value_
> 使用 **copy** 可在打包 tar 前先把数据复制到临时目录（对活跃站点更安全）；默认直接流式处理。

**INCREMENTAL** _yes_
> 创建增量备份（需要已存在的 PREVIOUS_BACKUP）。

**PREVIOUS_BACKUP** _id_
> 作为增量备份基础的备份 ID。

**GITLAB_BACKUP_MAX_CONCURRENCY** _N_
> 仓库备份的最大并发进程数。

**GZIP_RSYNCABLE** _yes_
> 使用 gzip 的 --rsyncable 模式，使备份能通过 rsync 高效去重。

# DESCRIPTION

**gitlab-backup** 用于创建和恢复 GitLab Omnibus 或源码安装的备份。备份将数据库、Git 仓库、上传文件、CI 产物、容器镜像仓库、Pages 内容等组件打包成单个名为 **TIMESTAMP_VERSION_gitlab_backup.tar** 的 tar 归档。

备份写入由 **gitlab_rails['backup_path']** 配置的目录（默认 **/var/opt/gitlab/backups**）。配置文件（gitlab.rb、secrets.json）**不**包含在内，必须单独备份。

# CAVEATS

需以 root 身份运行（通常通过 **sudo**）。恢复要求 GitLab 的大版本.次版本与备份时相同。恢复前先停止 **puma** 和 **sidekiq**（**gitlab-ctl stop puma sidekiq**）。配置文件（**/etc/gitlab/gitlab.rb**、**/etc/gitlab/gitlab-secrets.json**）**不**包含在备份归档中——必须单独备份，否则恢复时将无法解密密钥。

# HISTORY

**gitlab-backup** 是对 **gitlab:backup:create** 和 **gitlab:backup:restore** Rake 任务的封装，于 **GitLab 12.2**（2019 年 8 月）引入，作为 Omnibus 安装的推荐操作界面。

# INSTALL

```pacman: sudo pacman -S gitlab```

```apk: sudo apk add py3-gitlab```

```nix: nix profile install nixpkgs#gitlab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gitlab-ctl](/man/gitlab-ctl)(8), [gitlab](/man/gitlab)(1)
