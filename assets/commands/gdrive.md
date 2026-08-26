# TAGLINE

Google Drive 命令行客户端

# TLDR

**列出根目录中的文件**

```gdrive files list```

**上传文件**

```gdrive files upload [file.txt]```

**按 ID 下载文件**

```gdrive files download [file_id]```

**创建文件夹**

```gdrive files mkdir [foldername]```

**列出可用的 Google Drive 账户**

```gdrive account list```

**显示文件信息**

```gdrive files info [file_id]```

# SYNOPSIS

**gdrive** _command_ [_options_] [_arguments_]

# PARAMETERS

**files**
> 文件操作：list、upload、download、info、mkdir、delete、export。

**account**
> 账户管理：add、list、switch、remove。

**about**
> 显示 Drive 账户信息。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gdrive** 是一个 Google Drive 命令行客户端，可直接在终端进行文件管理。与专注于下载的 gdown 不同，gdrive 提供完整的双向操作，包括上传、下载、列出、共享和删除文件及文件夹。

该工具使用服务账号或 OAuth 2.0 进行身份验证，并在首次授权后将凭据存储在本地。它支持添加和切换多个 Google 账户。完成认证后，它为你的 Google Drive 提供终端访问能力，支持可脚本化的操作，用于备份自动化和程序化文件管理。

gdrive v3 采用子命令结构（例如 **gdrive files list**、**gdrive files upload**）。它填补了 Google 缺少官方 Linux 命令行客户端的空白，对服务器环境、自动化工作流和基于终端的文件管理非常有价值。

# CAVEATS

需要 OAuth 身份验证。受 API 配额限制。不适合大规模操作。

# HISTORY

gdrive 作为非官方的 Google Drive 命令行客户端而创建，填补了 Google 缺少官方 Linux 客户端的空白。

# INSTALL

```brew: brew install gdrive```

```nix: nix profile install nixpkgs#gdrive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rclone](/man/rclone)(1), [gdown](/man/gdown)(1)
