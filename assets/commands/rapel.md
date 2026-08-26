# TAGLINE

支持并发下载和分块后处理钩子的分块可断点续传 HTTP 下载器

# TLDR

以默认 100 MiB 分块下载文件

```rapel download https://example.com/large.iso```

以 4 个并发任务和 50 MiB 分块下载

```rapel download -c 50M --jobs 4 https://example.com/file.bin```

恢复中断的下载（自动进行）

```rapel download https://example.com/file.bin```

通过 SOCKS5 代理下载，并在每个分块完成后运行命令

```rapel download -x socks5h://127.0.0.1:9050 --post-part 'rclone move {part} remote:bucket/' URL```

手动合并先前下载的分块

```rapel merge -o final.iso --delete```

# SYNOPSIS

**rapel** download [_options_] _URL_

**rapel** merge [_options_]

# DESCRIPTION

**rapel** 是一个现代的跨平台下载器，可将大文件拆分为多个分块并发下载，并支持中断后的可靠续传。它会将下载参数记录在一个伴随（sidecar）文件中，因此即使跨不同会话或机器也能安全地续传。

下载成功后（或按需），可以将各分块合并为最终文件。`--post-part` 钩子让你能在每个分块落地时立即上传、校验或处理它——适合流式上传到对象存储或触发下游流水线。

该工具用 Go 编写，除二进制文件外零运行时依赖，可在 Linux、macOS、Windows、FreeBSD 和 Raspberry Pi（armv6/armv7）上运行。

# PARAMETERS (download)

**-c**, **--chunk-size** _SIZE_  
> 分块大小，带 K/M/G 后缀（默认 100M）

**--jobs** _N_  
> 并发分块下载数量（默认 1）

**-x**, **--proxy** _URL_  
> 代理（支持 socks5h://、http:// 等）

**-r**, **--retries** _N_  
> 每个分块请求的重试次数（默认 10）

**--merge**  
> 下载完成后自动合并分块

**--post-part** _CMD_  
> 每个分块完成后运行的 Shell 命令（支持 {part}、{idx}、{base}）

**--force**  
> 忽略任何已有状态，从头开始

# SEE ALSO

[curl](/man/curl)(1), [wget](/man/wget)(1), [aria2c](/man/aria2c)(1)
