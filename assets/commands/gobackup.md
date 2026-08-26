# TAGLINE

面向数据库和文件的备份工具

# TLDR

**备份**数据库

```gobackup perform```

使用指定配置进行**备份**

```gobackup -c [/path/to/config.yml] perform```

**列出**可用的备份

```gobackup list```

从备份中**恢复**

```gobackup restore [backup-id]```

# SYNOPSIS

**gobackup** [_options_] _command_

# PARAMETERS

**perform**
> 运行备份任务

**list**
> 列出所有备份

**restore** _ID_
> 从备份恢复

**-c, --config** _FILE_
> 配置文件（默认：~/.gobackup/gobackup.yml）

**--model** _MODEL_
> 指定要运行的备份模型

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**gobackup** 是一款备份工具，支持数据库（MySQL、PostgreSQL、Redis、MongoDB）和文件备份。它可以压缩、加密备份，并将其上传到各种存储服务。

该工具通过 YAML 文件进行配置，支持多个备份模型、调度计划和保留策略。

# CONFIGURATION

配置文件示例：

```yaml
models:
  my_backup:
    compress_with:
      type: tgz
    store_with:
      type: s3
      bucket: my-bucket
    databases:
      my_db:
        type: mysql
        host: localhost
        database: myapp
```

# CAVEATS

需要进行正确的配置。数据库凭据必须妥善保管。执行远程备份需要存储服务的凭据。

# HISTORY

**gobackup** 的定位是一套灵活的备份解决方案，支持多种数据库和存储后端。

# INSTALL

```brew: brew install gobackup```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[restic](https://restic.net/), [borg](https://borgbackup.readthedocs.io/), [duplicity](http://duplicity.nongnu.org/)
