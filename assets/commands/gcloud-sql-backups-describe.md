# TAGLINE

显示备份信息

# TLDR

**查看备份详情**

```gcloud sql backups describe [backup_id] --instance [instance_name]```

**以 JSON 格式查看备份详情**

```gcloud sql backups describe [backup_id] --instance [instance] --format json```

# SYNOPSIS

**gcloud** **sql** **backups** **describe** _backup_id_ **--instance**=_instance_ [_options_]

# PARAMETERS

**--instance** _name_
> Cloud SQL 实例名称。

**--format** _format_
> 输出格式。

# DESCRIPTION

**gcloud sql backups describe** 显示特定 Cloud SQL 备份的详细信息。它会获取包括备份状态、类型（按需或自动）、创建时间戳、完成时间和备份大小在内的元数据。

该命令可用于确认备份是否完成、在恢复前检查备份完整性，以及审计备份操作。输出可格式化为 JSON 或 YAML，以便进行程序化处理或与自动化脚本集成。

# SEE ALSO

