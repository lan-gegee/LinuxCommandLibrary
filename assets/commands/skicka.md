# TAGLINE

命令行 Google Drive 客户端

# TLDR

**上传文件**到 Google Drive

```skicka upload [local-file] [drive-path]```

**从 Google Drive 下载文件**

```skicka download [drive-path] [local-path]```

**列出** Drive 文件夹中的文件

```skicka ls [drive-path]```

**加密上传**

```skicka upload -encrypt [local-file] [drive-path]```

在 Drive 上**创建文件夹**

```skicka mkdir [drive-path]```

**显示** Drive 文件夹的**磁盘用量**

```skicka du [drive-path]```

**打印** Drive 文件的**内容**

```skicka cat [drive-path]```

**从 Drive 删除文件**

```skicka rm [drive-path]```

# SYNOPSIS

**skicka** _command_ [_options_] [_args_]

# COMMANDS

**upload**
> 将文件或目录上传到 Drive

**download**
> 从 Drive 下载文件或目录

**ls**
> 列出 Drive 文件夹的内容

**cat**
> 打印 Drive 文件的内容

**mkdir**
> 创建目录（使用 -p 创建中间目录）

**rm**
> 删除文件或文件夹（使用 -s 跳过回收站）

**du**
> 报告 Drive 文件夹层级的磁盘用量

**df**
> 显示 Drive 的剩余空间

**fsck**
> 检查本地文件与 Drive 文件的一致性

**init**
> 创建初始配置文件

**genkey**
> 生成加密密钥（配合 -encrypt 使用）

# PARAMETERS

**-encrypt**
> 上传前加密文件

**-ignore-times**
> 强制比较内容，而不依赖修改时间

**-p**
> 创建中间目录（用于 mkdir）

**-s**
> 跳过回收站并永久删除（用于 rm）

# DESCRIPTION

**skicka** 是一个 Google Drive 命令行客户端，提供类 Unix 的文件操作，包括上传、下载、列目录、创建目录和删除。它支持递归操作，可传输整个文件夹层级。

一个显著的特性是客户端加密（**-encrypt**），它在上传到 Google Drive 之前先在本地对文件进行加密，确保存储的数据即使对云服务商也保持私密。加密密钥通过 **genkey** 子命令生成。该工具采用 Go 编写。

# CAVEATS

**该项目已于 2023 年 1 月归档，不再维护。**需要 OAuth 设置和 ~/.skicka.config 配置文件。受 Google Drive API 速率限制约束。它并非 Google 官方产品，但曾托管在 Google 的 GitHub 组织下。属于 alpha 软件，生产环境请考虑使用 **rclone**。

# HISTORY

**skicka** 由 **Matt Pharr** 创建，是一个支持客户端加密的 Google Drive 命令行界面。其 GitHub 仓库已于 **2023 年 1 月 10 日**归档。

# SEE ALSO

[rclone](/man/rclone)(1), [gdrive](/man/gdrive)(1), [drive](/man/drive)(1)
