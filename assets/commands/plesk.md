# TAGLINE

Plesk 主机管理面板的命令行界面

# TLDR

**显示版本**

```plesk version```

**列出域名**

```plesk bin domain --list```

**创建备份**

```plesk bin pleskbackup --domains-name [domain] --output-file [backup]```

**修复安装**

```plesk repair all```

**检查状态**

```plesk bin service --status```

# SYNOPSIS

**plesk** [_command_] [_options_]

# PARAMETERS

**bin** _COMMAND_
> 运行 Plesk 工具。

**repair** _COMPONENT_
> 修复组件。

**version**
> 显示版本。

**--help**
> 显示帮助。

# DESCRIPTION

**plesk** 是 Plesk 网站托管控制面板的命令行界面。无需使用网页界面，它即可访问域名管理、备份操作、服务控制和系统诊断功能。

**bin** 子命令运行执行特定任务的各个 Plesk 工具，如域名配置、数据库管理和邮件设置。**repair** 命令可诊断并修复常见的安装问题。

# CAVEATS

商业软件。需要 root 权限。面向服务器管理。

# HISTORY

Plesk CLI 为 Plesk 托管面板提供 **命令行管理** 能力。

# SEE ALSO

[apache2ctl](/man/apache2ctl)(1), [nginx](/man/nginx)(1)
