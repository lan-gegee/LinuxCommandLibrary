# TAGLINE

控制 Omnibus GitLab 服务

# TLDR

**启动 GitLab**

```sudo gitlab-ctl start```

**停止 GitLab**

```sudo gitlab-ctl stop```

**重启 GitLab**

```sudo gitlab-ctl restart```

**显示状态**

```sudo gitlab-ctl status```

**重新配置 GitLab**

```sudo gitlab-ctl reconfigure```

**查看日志**

```sudo gitlab-ctl tail```

查看特定服务的日志

```sudo gitlab-ctl tail [nginx]```

# SYNOPSIS

**gitlab-ctl** _command_ [_options_]

# SUBCOMMANDS

**start**
> 启动所有服务。

**stop**
> 停止所有服务。

**restart**
> 重启所有服务。

**status**
> 显示服务状态。

**reconfigure**
> 应用配置。

**tail**
> 查看日志。

**hup**
> 发送 HUP 信号。

**console**
> Rails 控制台。

# DESCRIPTION

**gitlab-ctl** 用于控制 Omnibus GitLab 安装。它管理所有 GitLab 服务（nginx、PostgreSQL、Redis、Puma、Sidekiq 等），应用来自 `/etc/gitlab/gitlab.rb` 的配置更改，并提供调试工具。

修改 `gitlab.rb` 后使用 `reconfigure` 命令来应用新设置。

# CONFIGURATION

**/etc/gitlab/gitlab.rb**
> Omnibus GitLab 安装的主配置文件，控制所有服务和设置。

# SEE ALSO

[gitlab-backup](/man/gitlab-backup)(1)
