# TAGLINE

执行 API 端点发现

# TLDR

**扫描 URL**

```kr scan [url] -w [wordlist]```

**使用 Assetnote 字典扫描**

```kr scan [url] -A apiroutes-210228```

**带身份验证扫描**

```kr scan [url] -w [list] -H "Authorization: Bearer [token]"```

**以指定并发数扫描**

```kr scan [url] -w [list] -x [50]```

**过滤状态码**

```kr scan [url] -w [list] --fail-status-codes 404,400```

# SYNOPSIS

**kr scan** [_options_] _target_

# PARAMETERS

_TARGET_
> 要扫描的 URL。

**-w** _WORDLIST_
> 自定义字典文件。

**-A** _KB_
> Assetnote 知识库。

**-H** _HEADER_
> 添加请求头。

**-x** _N_
> 并发请求数。

**--fail-status-codes** _CODES_
> 要忽略的状态码。

**--help**
> 显示帮助信息。

# DESCRIPTION

**kr scan** 是 kiterunner 的主扫描子命令，对目标 URL 执行具备上下文感知能力的 API 端点发现。它不是简单地把字典条目作为路径后缀拼接，而是根据字典中的模式构造带有相应 HTTP 方法、内容类型和路由参数的完整 API 请求，因此在识别真实 API 路由方面要有效得多。

该命令既支持 Assetnote 预构建的知识库字典（通过 -A 标志），也支持自定义字典文件。你可以用 -x 控制并发数，用 -H 添加认证请求头，并按状态码过滤不需要的响应。结果包含检测到的 HTTP 方法、路径、状态码和响应大小，可以清晰呈现目标的 API 攻击面。

# CAVEATS

kiterunner 的子命令。仅限授权测试。可能产生高流量。

# HISTORY

kr scan 是 Assetnote 为 API 安全测试开发的 **kiterunner** 中的主扫描命令。

# INSTALL

```nix: nix profile install nixpkgs#kiterunner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kiterunner](/man/kiterunner)(1), [kiterunner-kb](/man/kiterunner-kb)(1)
