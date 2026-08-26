# TAGLINE

Docker Registry v2 命令行客户端

# TLDR

**列出**镜像仓库中的**仓库**

```reg ls [registry.example.com]```

**列出**镜像的**标签**

```reg tags [registry.example.com/image]```

**显示 manifest** JSON

```reg manifest [registry.example.com/image:tag]```

**显示镜像摘要（digest）**

```reg digest [registry.example.com/image:tag]```

**删除**一个引用

```reg rm [registry.example.com/image@sha256:digest]```

**下载层到文件**

```reg layer -o [layer.tar] [registry.example.com/image@sha256:digest]```

# SYNOPSIS

**reg** [*global-flags*] *command* [*args*]

# DESCRIPTION

**reg** 是一个 Docker Registry HTTP API v2 客户端，可用于列出仓库和标签、获取 manifest 和摘要、删除引用、下载层、运行一个简单的镜像仓库 UI，并可选择查询 Clair 服务器获取漏洞信息。它可以使用 Docker 配置中的凭据，也可以使用显式的 **-u**/**-p** 标志。

它面向 Open Source Distribution 风格的镜像仓库。对于 Docker Hub 的差异化 API，**reg ls** 无法工作。

# PARAMETERS

**ls** *registry*

> 列出仓库（大型镜像仓库上可能较慢）。

**tags** *repository*

> 列出某个仓库的标签。

**manifest** *ref*

> 打印镜像 manifest JSON。

**digest** *ref*

> 打印内容摘要。

**layer** *ref*

> 下载层 blob（**-o** 指定输出路径）。

**rm** *ref*

> 删除 manifest 引用（仓库必须允许删除）。

**vulns** **--clair** *url* *ref*

> 通过 Clair 出具漏洞报告。

**server**

> 为镜像仓库运行静态 UI 服务器。

**version**

> 显示版本。

**-u**, **--username** *user*

> 镜像仓库用户名。

**-p**, **--password** *pass*

> 镜像仓库密码。

**-k**, **--insecure**

> 跳过 TLS 证书验证。

**-f**, **--force-non-ssl**

> 允许非 TLS 镜像仓库。

**-d**

> 调试日志。

**--timeout** *duration*

> HTTP 超时时间（默认 1 分钟）。

# CAVEATS

删除镜像需要仓库配置启用删除功能。不支持 hub.docker.com 的列表操作。请谨慎处理凭据；尽量优先使用 Docker 凭据助手。

# INSTALL

```brew: brew install reg```

```nix: nix profile install nixpkgs#reg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker](/man/docker)(1), [skopeo](/man/skopeo)(1), [crane](/man/crane)(1)

# RESOURCES

```[Source code](https://github.com/genuinetools/reg)```

```[Homepage](https://r.j3ss.co)```

<!-- verified: 2026-07-19 -->
