# TAGLINE

功能丰富的终端文件传输与文件浏览器

# TLDR

**启动交互式文件传输界面**

```termscp```

**通过 SFTP 连接远程主机**

```termscp sftp://[user]@[192.168.1.10]:22```

**浏览 S3 存储桶**

```termscp s3://[my-bucket]```

# SYNOPSIS

**termscp** [_options_] [_protocol_://_user_@_host_:_port_]

# DESCRIPTION

**termscp** 是一款终端 UI 文件传输工具，支持 SCP、SFTP、FTP/FTPS、Kubernetes、S3、SMB 和 WebDAV 协议。它提供面向本地和远程文件系统的双窗格文件浏览器，内置书签、SSH 密钥存储、可自定义主题、大传输量的桌面通知，以及嵌入式终端。

# HISTORY

**termscp** 由 **Veeso**（Christian Visintin）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S termscp```

```zypper: sudo zypper install termscp```

```brew: brew install termscp```

```nix: nix profile install nixpkgs#termscp```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scp](/man/scp)(1), [sftp](/man/sftp)(1), [rclone](/man/rclone)(1)
