# TAGLINE

新一代的递归式 metalink/文件/网站下载器

# TLDR

**下载文件**

```wget2 [https://example.com/file.zip]```

**下载为指定文件名**

```wget2 -O [output.zip] [url]```

**继续未完成的下载**

```wget2 -c [url]```

**递归下载**

```wget2 -r [https://example.com]```

**镜像网站**

```wget2 -m [https://example.com]```

**以分块并行传输下载**

```wget2 --chunk-size=[1M] [url]```

**限制下载速率**

```wget2 --limit-rate=[1M] [url]```

**指定压缩支持进行下载**

```wget2 --compression=[gzip,br,zstd] [url]```

# SYNOPSIS

**wget2** [_options_] [_urls_]

# PARAMETERS

**-O** _FILE_
> 保存到指定的输出文件名。

**-c**, **--continue**
> 继续部分下载的文件。

**-r**, **--recursive**
> 递归下载。

**-m**, **--mirror**
> 镜像网站（-r -N -l inf --no-remove-listing 的快捷方式）。

**--chunk-size** _SIZE_
> 以给定大小的多线程分块下载大文件。

**--limit-rate** _RATE_
> 将带宽限制在指定速率（如 1M）。

**--http2**
> 强制使用 HTTP/2 协议。

**--http2-request-window** _NUM_
> 设置每条 HTTP/2 连接的最大并行流数（默认：30）。

**--compression** _TYPE_
> 设置可接受的压缩类型（identity、gzip、deflate、br、zstd、lzip 等）。

**-q**, **--quiet**
> 安静模式，不输出信息。

**-P** _DIR_
> 将文件保存到指定的目录前缀。

**--no-clobber**
> 不覆盖已有文件或截断未完成的文件。

**-d**, **--debug**
> 打印调试输出。

# DESCRIPTION

**wget2** 是 GNU Wget 的下一代版本，为支持现代协议和并行下载而重构。它原生支持 HTTP/2 多路复用流，与支持该协议的服务器通信更高效。

并行下载通过复用的连接同时获取多个文件，相比原版 wget 的顺序方式显著加速批量下载。**--chunk-size** 选项将大型单文件下载拆分为并行分块。递归下载和网站镜像仍使用熟悉的 -r 和 -m 标志。

wget2 还支持 Metalink 文件，可实现感知镜像的下载并自动校验完整性，此外还支持压缩协商和现代 TLS。该工具在基本操作上保持与 wget 的命令行兼容性，同时通过现代化的网络栈提升性能。

# CAVEATS

并非支持原版 wget 的所有选项。与 wget 存在一些行为差异。--chunk-size 功能对支持 HTTP range 请求的服务器效果最佳。

# HISTORY

**wget2** 由 Tim Ruehsen 开发，是 GNU Wget 的现代化重写版本。开发始于 2012 年前后，2.0.0 版本于 2021 年发布。它在保持向后兼容的同时增加了 HTTP/2、并行下载和 Metalink 支持。

# INSTALL

```apt: sudo apt install wget2```

```dnf: sudo dnf install wget2```

```apk: sudo apk add wget2```

```zypper: sudo zypper install wget2```

```brew: brew install wget2```

```nix: nix profile install nixpkgs#wget2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [aria2c](/man/aria2c)(1)
