# TAGLINE

fossil init 的别名

# TLDR

**创建新仓库**

```fossil new [repo.fossil]```

**创建并设置项目名称**

```fossil new --project-name "[name]" [repo.fossil]```

**创建并指定管理员用户**

```fossil new -A [username] [repo.fossil]```

**以现有仓库的设置为模板创建**

```fossil new --template [existing.fossil] [repo.fossil]```

**创建并设置项目名称和描述**

```fossil new --project-name "[name]" --project-desc "[description]" [repo.fossil]```

# SYNOPSIS

**fossil** **new** [_options_] _repository_

# PARAMETERS

**-A, --admin-user** _USERNAME_
> 选择给定的用户名而非当前登录名作为管理员用户。

**--template** _FILE_
> 从指定的仓库文件复制初始设置。几乎会复制所有可从 setup 页面访问的设置，但不会复制普通用户及其权限。

**--project-name** _STRING_
> 设置项目名称。

**--project-desc** _STRING_
> 设置项目描述。

**--date-override** _DATETIME_
> 使用指定的日期时间作为初始 check-in 的时间。接受 "now" 或 "YYYY-MM-DDTHH:MM:SS.SSS" 格式（可带时区偏移）。

**--sha1**
> 初始哈希策略使用 SHA1 而非默认的 SHA3-256。

# DESCRIPTION

**fossil new** 是 **fossil init** 的别名，功能完全相同。所有选项和行为与 **fossil init** 一致。

# SEE ALSO

[fossil-init](/man/fossil-init)(1), [fossil-commit](/man/fossil-commit)(1)
