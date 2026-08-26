# TAGLINE

向 GitHub REST 和 GraphQL API 发送经过身份验证的 HTTP 请求

# TLDR

**发起 GET 请求**

```gh api [/repos/owner/repo]```

**发起 POST 请求**

```gh api -X POST [/repos/owner/repo/issues] -f title="[title]"```

**带 JSON 请求体**

```gh api [/endpoint] --input [data.json]```

**使用 GraphQL**

```gh api graphql -f query='[query]'```

**对结果分页**

```gh api [/endpoint] --paginate```

**输出特定字段**

```gh api [/repos/owner/repo] --jq '.[field]'```

# SYNOPSIS

**gh** **api** [_options_] _endpoint_

# PARAMETERS

**-X**, **--method** _method_
> HTTP 方法。

**-f**, **--raw-field** _key=value_
> 添加字符串参数。

**-F**, **--field** _key=value_
> 添加类型化参数（非字符串值、@ 文件引用、布尔值、null）。

**--input** _file_
> 从文件读取请求体。

**--jq** _query_
> 过滤 JSON 输出。

**--paginate**
> 获取结果的所有分页。

**--slurp**
> 与 --paginate 配合，把所有分页合并为单个 JSON 数组。

**-i**, **--include**
> 在输出中包含 HTTP 响应头。

**-p**, **--preview** _name_
> 启用 GitHub API 预览特性。

**-H**, **--header** _header_
> 添加 HTTP 头。

**-t**, **--template** _template_
> 用 Go 模板格式化输出。

**--hostname** _host_
> 向指定的 GitHub 主机名发送请求（如 GHES）。

**--cache** _duration_
> 缓存响应（如 1h、30m）。

# DESCRIPTION

**gh api** 向 GitHub API 发送经过身份验证的 HTTP 请求。同时支持 REST 和 GraphQL API，并提供自动认证。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [curl](/man/curl)(1)
