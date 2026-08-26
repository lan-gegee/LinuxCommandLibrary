# TAGLINE

向 Google Photos 批量上传媒体文件夹

# TLDR

**初始化**默认配置

```gphotos-uploader-cli init```

**覆盖**现有配置

```gphotos-uploader-cli init --force```

**认证** Google Photos（浏览器流程）

```gphotos-uploader-cli auth```

**上传**已配置的文件夹

```gphotos-uploader-cli push```

**试运行**上传（不发送文件）

```gphotos-uploader-cli push --dry-run```

**列出**相册

```gphotos-uploader-cli list albums```

**显示版本**

```gphotos-uploader-cli version```

# SYNOPSIS

**gphotos-uploader-cli** [*global-options*] *command* [*args*]

# DESCRIPTION

**gphotos-uploader-cli** 是一个 Google Photos 命令行客户端，适用于 Linux（以及其他能运行 Go 二进制文件的平台）。官方 Google 备份工具只面向 macOS 和 Windows；本项目填补了批量文件夹上传、相册整理以及列出现有媒体库内容的空白。

工作流程：**init** 在 **~/.gphotos-uploader-cli** 下创建配置（可用 **--config** 覆盖），你在 **config.hjson** 中设置 Google API 应用凭据和上传任务，**auth** 在浏览器中完成 OAuth，然后 **push** 扫描已配置的源文件夹并上传新对象。文件跟踪器可避免重复上传已知媒体。

# PARAMETERS

**init**

> 创建默认配置。**--force** 会覆盖现有配置。

**auth**

> 针对 Google Photos 运行 OAuth 认证流程。

**push**

> 上传配置任务中定义的本地文件夹。**--dry-run** 只报告将要执行的工作而不实际上传。

**list albums** / 与媒体相关的 **list** 子命令

> 列出 Google Photos 中已有的相册或媒体条目。

**version**

> 打印 CLI 版本。

**reset**

> 重置本地跟踪状态（见 **gphotos-uploader-cli reset --help**）。

全局标志包括 **--config**（配置目录）、**--debug** 以及 **--silent**（与 debug 互斥）。

# CONFIGURATION

默认目录：**~/.gphotos-uploader-cli**，配置文件为 **config.hjson**。你必须提供 Google Photos API 应用凭据（**APIAppCredentials**）并定义 **jobs**（源文件夹、包含/排除模式、相册策略）。完整的配置结构请参阅项目文档。

# CAVEATS

需要 Google API 凭据和交互式浏览器 OAuth（无头环境需要将 SSH 端口转发到本地回调端口）。该项目曾公开招募新维护者；请在 GitHub 上查看当前状态。需遵守 Google Photos API 的配额和策略限制。不能完全替代 Google Takeout 或官方备份客户端。

# INSTALL

```brew: brew install gphotos-uploader-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rclone](/man/rclone)(1), [gdrive](/man/gdrive)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/gphotosuploader/gphotos-uploader-cli)```

```[Documentation](https://gphotosuploader.github.io/gphotos-uploader-cli)```

<!-- verified: 2026-07-19 -->
