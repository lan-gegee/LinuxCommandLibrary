# TAGLINE

功能完善的文件传输程序，支持 FTP、HTTP、SFTP、FISH

# TLDR

**连接**到 FTP 服务器

```lftp -u [username] ftp.example.com```

**下载**多个文件

```mget [path/to/*.png]```

**上传**多个文件

```mput [path/to/*.zip]```

**删除**远程文件

```mrm [path/to/*.txt]```

**重命名**远程文件

```mv [original] [new_name]```

将远程目录**镜像**到本地

```mirror [remote_dir] [local_dir]```

向远程**上传**目录

```mirror -R [local_dir] [remote_dir]```

# SYNOPSIS

**lftp** [_options_] [_site_]

# DESCRIPTION

**lftp** 是一个功能完善的文件传输程序，支持 FTP、HTTP、SFTP、FISH 和 torrent 协议。它具备作业控制、书签、镜像等功能，并且可以并行传输多个文件。

# PARAMETERS

**-u, --user USER[,PASS]**
> 使用指定的用户名和可选的密码

**-p PORT**
> 连接到指定端口

**-e COMMANDS**
> 连接后执行命令

**-c COMMANDS**
> 执行命令后退出

**-f FILE**
> 从文件读取并执行命令

**-d**
> 启用调试输出

# INTERACTIVE COMMANDS

**mget PATTERN**
> 下载匹配模式的文件

**mput PATTERN**
> 上传匹配模式的文件

**mrm PATTERN**
> 删除匹配模式的远程文件

**mirror [OPTIONS] REMOTE [LOCAL]**
> 镜像目录（-R 表示反向/上传）

**pget FILE**
> 通过多个连接下载文件

**queue**
> 将命令排队稍后执行

# CAVEATS

mget/mput 等交互式命令需要在 lftp 会话内使用，而不是在 shell 中直接运行。支持并行传输以提升性能。

# INSTALL

```apt: sudo apt install lftp```

```dnf: sudo dnf install lftp```

```pacman: sudo pacman -S lftp```

```apk: sudo apk add lftp```

```zypper: sudo zypper install lftp```

```brew: brew install lftp```

```nix: nix profile install nixpkgs#lftp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ftp](/man/ftp)(1), [sftp](/man/sftp)(1), [wget](/man/wget)(1), [curl](/man/curl)(1)
