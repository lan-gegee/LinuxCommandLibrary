# TAGLINE

支持断点续传的命令行下载/上传工具

# TLDR

**下载文件**到当前目录

```aim [https://domain.com/file.tar.gz] .```

**上传本地文件**

```aim [local.file] [https://domain.com/destination.file]```

**下载并自动解压**归档

```aim [https://domain.com/file.tar.gz] +```

**交互式浏览远程目录**

```aim [http://192.168.1.5:8080] -i```

**通过 HTTP 共享当前目录**

```aim .```

**下载并进行 SHA256 校验和**验证

```aim [https://domain.com/file] . [sha256hash]```

# SYNOPSIS

**aim** [_options_] _source_ [_destination_] [_checksum_]

# PARAMETERS

**-i**, **--interactive**
> 下载前通过模糊搜索浏览远程目录

**--update**
> 就地自更新二进制文件

**--no-follow-redirects**
> 禁用自动跟随 HTTP 重定向

# DESCRIPTION

**aim** 是一个支持断点续传的命令行下载和上传工具，定位于不需要种子下载支持的用户的 aria2 替代品。它支持 HTTP(S)、FTP、SFTP、SSH 和 S3 协议，其中 HTTP(S)、FTP 和 SFTP 传输支持断点续传。具体动作（下载或上传）由参数顺序决定。

aim 用 Rust 编写，具有交互式模糊搜索远程目录、自动解压归档、SHA256 校验和验证、通过 HTTP 共享文件夹、兼容管道的输出，以及支持 .netrc 和 AWS 凭据认证等特性。

# CAVEATS

SSH 和 S3 协议不支持断点续传。交互模式仅适用于 HTTP(S)。SSH 密钥类型会被自动检测（id_ed25519、id_rsa）。未指定目标位置时，默认输出到 stdout。

# HISTORY

**aim** 由 **Mihai Galos** 创建，是 MIT 许可证下的开源 Rust 项目。它可在 crates.io 上获取，也可从 GitHub releases 下载预构建的二进制文件。

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [aria2c](/man/aria2c)(1), [scp](/man/scp)(1)
