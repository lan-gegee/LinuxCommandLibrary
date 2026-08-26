# TAGLINE

支持 HTTP、GraphQL、gRPC、WebSocket 和 SSE 的终端 API 客户端

# TLDR

**启动 API 客户端 TUI**

```resterm```

在 TUI 中**打开请求文件**

```resterm --file [path/to/request.http]```

直接从终端**运行请求**

```resterm run --file [path/to/request.http]```

**用示例初始化新工作区**

```resterm init```

在指定环境中**运行某个命名请求**

```resterm run --file [requests.http] --request [getUser] --env [staging]```

将 curl 命令**导入 .http 文件**

```resterm --from-curl "[curl https://example.com]"```

将 OpenAPI 3 规范**转换为请求文件**

```resterm --from-openapi [spec.yaml]```

# SYNOPSIS

**resterm** [_options_] [_file_]

**resterm** **run** [_options_]

**resterm** **init** [_options_]

**resterm** **collection** _import_|_export_ [_options_]

# COMMANDS

**run**
> 从终端执行一个或多个 `.http` / `.rest` 请求。

**init**
> 用示例请求和环境文件引导创建工作区。

**collection export**
> 将工作区导出为适合 Git 的打包文件。

**collection import**
> 将打包文件导入另一个工作区。

# PARAMETERS

**--file** _PATH_
> 指定目标请求文件。

**--workspace** _DIR_
> 指定工作区目录。

**--env** _NAME_
> 选择工作区中的某个环境。

**--env-file** _PATH_
> 使用 dotenv 文件（需显式启用）。

**--request** _NAME_
> 运行指定的命名请求。

**--timeout** _DURATION_
> 设置请求超时时间。

**--insecure**
> 跳过 TLS 证书验证。

**--follow**
> 跟随重定向。

**--proxy** _URL_
> 使用指定的 HTTP/HTTPS 代理。

**--recursive**
> 递归处理文件。

**--compare**
> 在多个环境中运行同一请求并对比响应差异。

**--dry-run**
> 执行前预览操作。

**--force**
> 导入时替换已存在的文件。

**--from-curl** _CMD_
> 将 curl 命令导入为请求。

**--from-openapi** _SPEC_
> 将 OpenAPI 3 规范转换为请求文件。

**--http-out** _FORMAT_
> 指定响应的输出格式。

**--check-update**
> 检查是否有更新的版本。

**--update**
> 下载并安装最新版本。

# DESCRIPTION

**resterm** 是一个键盘驱动的终端 API 客户端，支持 HTTP、GraphQL、gRPC、WebSocket 和 SSE。请求以纯文本的 `.http` / `.rest` 文件存储，因此可以随代码一起进行版本控制。

功能包括 OAuth 2.0 认证、SSH 隧道、Kubernetes 端口转发、条件逻辑与多步骤工作流、响应对比、性能剖析，以及 WebSocket 和 SSE 会话的流式记录。

# HISTORY

**resterm** 由 **unkn0wn-root** 创建，使用 **Go** 编写。

# INSTALL

```brew: brew install resterm```

```nix: nix profile install nixpkgs#resterm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [posting](/man/posting)(1), [httpie](/man/httpie)(1)
