# TAGLINE

通过命令行上传分享文件

# TLDR

**上传文件**

```curl --upload-file [file.txt] https://transfer.sh/[filename]```

**上传并限制最大下载次数**

```curl --upload-file [file.txt] -H "Max-Downloads: [1]" https://transfer.sh/```

**上传并设置过期时间**

```curl --upload-file [file.txt] -H "Max-Days: [7]" https://transfer.sh/```

**删除已上传的文件**

```curl -X DELETE [delete-url]```

**加密后上传**

```cat [file] | gpg -c | curl --upload-file - https://transfer.sh/[file.gpg]```

# SYNOPSIS

**curl** --upload-file _file_ [_-H headers_] https://transfer.sh/[_name_]

# PARAMETERS

**--upload-file**
> 要上传的文件。

**Max-Downloads:** _N_
> 下载次数上限。

**Max-Days:** _N_
> 距过期的天数。

**-X DELETE**
> 删除文件。

# DESCRIPTION

**transfer.sh** 是一个专为命令行便捷使用而设计的文件分享服务。文件通过 curl 以标准 HTTP PUT 请求上传，服务会返回一个可供分享的唯一下载 URL。基本上传无需账号或注册。

可以通过 HTTP 头配置上传的过期时间和下载次数限制，从而控制文件的可用时长和可被下载的次数。文件会在指定的过期时间之后自动删除。该服务还支持在上传前将文件经 GPG 管道处理来实现加密。

Transfer.sh 可以作为开源 Go 应用自行部署，也可以使用 transfer.sh 上的公共实例。它支持最大数 GB 的上传，并提供用于手动删除已上传文件的删除 URL。

# CAVEATS

外部服务。有大小限制。URL 公开可见。

# HISTORY

**transfer.sh** 的定位是一个可通过 curl 在命令行使用的简单文件分享服务。

# SEE ALSO

[curl](/man/curl)(1), [wormhole](/man/wormhole)(1), [ffsend](/man/ffsend)(1)
