# TAGLINE

基于 Web 的文件管理界面

# TLDR

**启动 Web 文件浏览器**

```filebrowser```

**服务指定目录**

```filebrowser -r [/path/to/directory]```

**指定地址和端口**

```filebrowser -a [0.0.0.0] -p [8080]```

**使用配置文件**

```filebrowser -c [config.json]```

**创建管理员用户**

```filebrowser users add [admin] [password] --perm.admin```

**配置数据库**

```filebrowser -d [database.db]```

# SYNOPSIS

**filebrowser** [_options_]

# PARAMETERS

**-r**, **--root** _path_
> 要对外服务的根目录。

**-a**, **--address** _addr_
> 监听地址。

**-p**, **--port** _port_
> 监听端口。

**-d**, **--database** _file_
> 数据库文件路径。

**-c**, **--config** _file_
> 配置文件路径。

**-b**, **--baseURL** _path_
> 应用的基础 URL。

**-t**, **--cert** _file_
> TLS 证书。

**-k**, **--key** _file_
> TLS 密钥。

**--noauth**
> 禁用身份验证。

**--log** _output_
> 日志输出位置（默认 "stdout"）。

# CONFIGURATION

**config.json**
> 用于服务器设置、身份验证和权限的配置文件。

**database.db**
> 存储 users、permissions 和设置的 SQLite 数据库。

# DESCRIPTION

**filebrowser** 提供一个可自托管的基于 Web 的文件管理界面，任何浏览器都可以访问。它构建出一个完整的文件服务器，具备上传、下载、预览、搜索和分享能力，还内置了面向文本文件的代码编辑器。

该应用支持带有细粒度权限控制的用户认证，可为不同的目录分配不同的访问级别。可以创建多个用户，每个用户都有独立的权限，分别控制读、写、执行和分享能力。

filebrowser 非常适合个人云存储、团队文件共享，或者在不开放 SSH 的情况下对服务器目录提供受控访问。它还提供拖拽上传、多文件批量操作和自定义命令执行钩子等功能。

# INSTALL

```brew: brew install filebrowser```

```nix: nix profile install nixpkgs#filebrowser```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nginx](/man/nginx)(8)
