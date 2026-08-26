# TAGLINE

在云存储之间同步文件

# TLDR

以交互方式**配置新的远程存储**

```rclone config```

**列出已配置的远程存储**

```rclone listremotes```

列出远程目录中的**文件**

```rclone ls [remote]:[path]```

从本地**复制文件**到远程

```rclone copy [source] [remote]:[path]```

**将本地目录同步到远程**（镜像，删除远程多余文件）

```rclone sync [source] [remote]:[path]```

**将远程挂载为文件系统**

```rclone mount [remote]:[path] [/local/mountpoint]```

**检查**源与目标之间的差异

```rclone check [source] [remote]:[path]```

**演练运行**预览同步而不做任何更改

```rclone sync --dry-run [source] [remote]:[path]```

# SYNOPSIS

**rclone** _command_ [_options_] _source_:_path_ [_dest_:_path_]

# PARAMETERS

**config**
> 以交互方式配置远程存储

**copy**
> 将文件从源复制到目标（不删除）

**sync**
> 使目标与源完全一致（删除多余文件）

**move**
> 将文件从源移动到目标

**ls**
> 列出对象及其大小和路径

**lsd**
> 仅列出目录

**mount**
> 将远程挂载为 FUSE 文件系统

**check**
> 检查源与目标是否一致

**delete**
> 删除路径中的文件

**--dry-run**, **-n**
> 预览更改而不执行

**--interactive**, **-i**
> 在破坏性操作前提示确认

**--progress**, **-P**
> 实时显示传输进度

**--transfers** _N_
> 并行文件传输数（默认 4）

**--checkers** _N_
> 并行检查器数量（默认 8）

**--verbose**, **-v**
> 提高输出详细程度（用 -vv 可更详细）

**--config** _FILE_
> 指定配置文件位置

# DESCRIPTION

**rclone** 是一款管理云存储文件的命令行程序，常被称为"云存储版 rsync"。它支持 70 多家云存储服务商，包括 Amazon S3、Google Drive、Dropbox、OneDrive、Backblaze B2，以及 SFTP、WebDAV、FTP 等标准协议。

**sync** 命令使目标与源完全一致，包括删除源中不存在的文件。若要单向复制且不删除，请使用 **copy**。这两个命令都根据大小和修改时间（或校验和）只传输有改动的文件。

配置保存在 **~/.config/rclone/rclone.conf** 中，通过 **rclone config** 以交互方式创建。每个远程存储都有一个名称，在命令中用作前缀（如 **gdrive:**）。

**mount** 命令借助 FUSE 将云存储暴露为本地文件系统，从而可以对远程存储执行标准的文件操作。

# CONFIGURATION

**~/.config/rclone/rclone.conf**
> 主配置文件，保存远程存储的定义，包含服务商类型、凭据和选项。通过 **rclone config** 以交互方式创建。

**RCLONE_CONFIG**
> 覆盖默认配置文件路径的环境变量。

**RCLONE_CONFIG_PASS**
> 为加密配置文件提供密码的环境变量。

# CAVEATS

**sync** 会删除目标上源中不存在的文件。请务必先用 **--dry-run** 预览更改，同步到云存储时尤其如此。

云到云的传输通常会经由你的本地机器中转。对于大规模传输，在云实例上运行 rclone 可以降低延迟并节省带宽。

大多数云服务商都有 API 速率限制。Google Drive 将上传限制在大约每秒 2 个文件。请根据服务商的限制调整 **--transfers** 和 **--checkers**。

加密远程存储增加了一层客户端加密，但也增加了复杂度。在依赖加密之前，先测试备份和恢复流程。

# HISTORY

Rclone 由 **Nick Craig-Wood** 创建，于 **2012 年**首次发布。该项目最初用于与 Google Drive 同步文件，后来扩展到支持数十家云服务商。它用 Go 编写，以单一二进制文件分发。名称由 "rsync" 与 "cloud" 组合而成。

# INSTALL

```apt: sudo apt install rclone```

```dnf: sudo dnf install rclone```

```pacman: sudo pacman -S rclone```

```apk: sudo apk add rclone```

```zypper: sudo zypper install rclone```

```brew: brew install rclone```

```nix: nix profile install nixpkgs#rclone```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [aws](/man/aws)(1), [gsutil](/man/gsutil)(1), [s3cmd](/man/s3cmd)(1)
