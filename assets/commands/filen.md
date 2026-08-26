# TAGLINE

端到端加密云存储的命令行工具

# TLDR

**登录账户**

```filen login```

**上传文件到云端**

```filen upload [local_file] [cloud_path]```

**从云端下载文件或目录**

```filen download [cloud_path] [local_destination]```

**列出目录内容**

```filen ls [cloud_path]```

**持续同步本地目录与云端**

```filen sync [local_dir] [cloud_dir] --continuous```

**启动本地 WebDAV 服务器**

```filen webdav```

**显示当前用户信息**

```filen whoami```

# SYNOPSIS

**filen** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 操作类型：upload、download、ls、sync、login 等。

**upload** _LOCAL_ _CLOUD_PATH_
> 将本地文件或目录上传到云端。

**download** _CLOUD_PATH_ _LOCAL_DEST_
> 从云端下载文件或目录。

**ls** _PATH_
> 列出目录内容。

**sync** _LOCAL_ _REMOTE_
> 同步目录。配合 --continuous 可保持持续同步。

**login**
> 登录 Filen 进行身份验证。

**logout**
> 退出 Filen 登录。

**whoami**
> 显示当前用户。

**mkdir** _PATH_
> 在云端创建目录。

**rm** _PATH_
> 删除文件或目录。使用 --no-trash 可永久删除。

**mv** _FROM_ _TO_
> 移动文件或目录。

**cp** _FROM_ _TO_
> 复制文件或目录。

**stat** _PATH_
> 显示文件或目录的信息。

**webdav**
> 启动一个镜像你 Filen Drive 的本地 WebDAV 服务器。

**s3**
> 启动一个镜像你 Filen Drive 的本地 S3 服务器。

**--skip-update**
> 跳过更新检查。

**--data-dir** _PATH_
> 覆盖默认数据目录的位置。

**--help**
> 显示帮助信息。

# DESCRIPTION

**filen** 是 Filen——一项端到端加密云存储服务——的命令行界面。它提供文件上传、下载、同步以及本地 WebDAV/S3 服务器功能，全程采用零知识加密。

所有文件在上传前都会在客户端完成加密，确保服务器永远无法接触到未加密的数据。有了这个 CLI，无需桌面应用就能实现脚本化的备份和文件管理。

不带任何命令调用时，filen 会进入交互模式。它支持文件夹同步以搭建自动化备份流程，并可使用 --continuous 标志进行不间断的同步。

# CAVEATS

需要 Filen 账户。加密会增加处理开销。存储配额取决于订阅等级。

# HISTORY

filen 是 **Filen** 的 CLI。Filen 是一家德国云存储服务商，强调以端到端加密保障隐私，希望成为主流云存储的加密替代品。

# SEE ALSO

[rclone](/man/rclone)(1), [aws](/man/aws)(1), [gsutil](/man/gsutil)(1)
