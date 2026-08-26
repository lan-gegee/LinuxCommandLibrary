# TAGLINE

探索并提取 Docker registry 的内容

# TLDR

**列出 registry 中的所有仓库**

```dockdiver -url [registry_host] -list```

**导出指定的仓库**

```dockdiver -url [registry_host] -dump [repository]```

**将所有仓库**导出到一个目录

```dockdiver -url [registry_host] -dump-all -dir [output_dir]```

**使用 basic 凭据进行身份验证**

```dockdiver -url [registry_host] -username [user] -password [pass] -list```

**使用 bearer token** 并跳过 TLS 校验

```dockdiver -url [registry_host] -bearer [token] -insecure -dump-all```

# SYNOPSIS

**dockdiver** [_options_]

# PARAMETERS

**-url** _STRING_
> Docker registry 的基础 URL 或主机名（必需）。

**-port** _INT_
> URL 中未指定端口时使用的 registry 端口。默认为 5000。

**-list**
> 列出 registry 中的所有仓库。

**-dump** _REPOSITORY_
> 下载单个仓库（manifest、配置 blob 和各层 tar 包）。

**-dump-all**
> 下载 registry 中发现的所有仓库。

**-dir** _DIRECTORY_
> 导出文件的输出目录。默认为 docker_dump。

**-username** _STRING_
> 用于 HTTP Basic 身份验证的用户名。

**-password** _STRING_
> 用于 HTTP Basic 身份验证的密码。

**-bearer** _STRING_
> 用于 Authorization 头的 bearer token。

**-headers** _JSON_
> 以 JSON 表示的自定义请求头，例如 '{"X-Custom": "Value"}'。

**-insecure**
> 跳过 TLS 证书校验。

**-rate** _INT_
> 每秒请求数。默认为 3。

**-timeout** _DURATION_
> HTTP 请求超时时间，如 10s 或 500ms。默认为 30s。

**-proxy** _URL_
> 代理 URL（http、https 或 socks5）。

**-proxy-username** _STRING_
> SOCKS5 代理身份验证的用户名。

**-proxy-password** _STRING_
> SOCKS5 代理身份验证的密码。

# DESCRIPTION

**dockdiver** 是一个 Go 实用程序，用于枚举和提取通过 Registry HTTP API V2 暴露出来的 Docker registry 内容。它可以列出仓库、导出单个仓库或导出所有仓库，获取 manifest、配置 blob 和各层 tar 包，并用 SHA256 摘要逐一校验每个 blob。

它面向渗透测试、漏洞赏金和 CTF 场景：此时某个 registry（通常是运行在 5000 端口上的自建服务）可以访问，且其中可能包含带有源代码、配置或凭据的镜像。支持 Basic 凭据或 bearer token 认证、自定义请求头、代理以及可配置的请求速率，使其适合应对有访问控制或速率限制的 registry。

此工具针对的是 registry 本身而非公开的 Docker Hub 网页界面，它会下载原始镜像数据供离线检查，而不会自行扫描各层中的机密信息。

# CAVEATS

只支持可通过 HTTP API V2 访问的 registry。仅可用于你有权访问的 registry。导出所有仓库可能传输大量数据；默认每秒 3 个请求的速率可以限制负载，并有助于避免触发速率限制。

# HISTORY

dockdiver 是由 MachiavelliII 发布在 GitHub 上的开源 Go 工具。其 lab 目录中附带了用于安全测试的 registry 实验环境。

# SEE ALSO

[dive](/man/dive)(1), [trivy](/man/trivy)(1), [grype](/man/grype)(1), [docker-pull](/man/docker-pull)(1)
