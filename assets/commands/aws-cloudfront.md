# TAGLINE

管理内容分发网络的分发和缓存。

# TLDR

为指定路径**创建缓存失效**

```aws cloudfront create-invalidation --distribution-id [EDFDVBD6EXAMPLE] --paths "/[path/to/file.jpg]" "/[images/*]"```

**使分发中的所有文件失效**

```aws cloudfront create-invalidation --distribution-id [EDFDVBD6EXAMPLE] --paths "/*"```

**列出所有分发**

```aws cloudfront list-distributions```

**获取分发详情**

```aws cloudfront get-distribution --id [EDFDVBD6EXAMPLE]```

从配置文件**创建分发**

```aws cloudfront create-distribution --distribution-config file://[distribution.json]```

**列出一个分发的失效请求**

```aws cloudfront list-invalidations --distribution-id [EDFDVBD6EXAMPLE]```

**获取失效请求的状态**

```aws cloudfront get-invalidation --distribution-id [EDFDVBD6EXAMPLE] --id [I2J0I21PCUYOIK]```

**等待分发完成部署**

```aws cloudfront wait distribution-deployed --id [EDFDVBD6EXAMPLE]```

# SYNOPSIS

**aws cloudfront** _command_ [_options_]

# PARAMETERS

**create-invalidation**
> 使边缘节点的缓存对象失效

**list-invalidations**
> 列出某个分发的失效请求

**get-invalidation**
> 获取失效请求的状态

**create-distribution**
> 创建新的 CloudFront 分发

**get-distribution**
> 获取分发的配置和状态

**list-distributions**
> 列出账户中的所有分发

**update-distribution**
> 修改分发设置

**delete-distribution**
> 移除一个分发（必须先禁用）

**create-origin-access-control**
> 创建 OAC 以实现安全的 S3 访问。

**get-distribution-config**
> 仅获取分发配置（不含状态元数据）。

**create-function**
> 创建用于轻量级边缘计算的 CloudFront Function。

**sign**
> 为私有内容签名 CloudFront URL 或 cookie。

**wait**
> 等待分发达到特定状态（如 deployed）。

**--distribution-id** _id_
> 分发标识符（如 EDFDVBD6EXAMPLE）

**--paths** _paths_
> 要使其失效的路径，以空格分隔（支持 * 通配符）

**--invalidation-batch** _json_
> 包含路径和调用者引用的 JSON

**--distribution-config** _json_
> 分发配置文件

**--id** _id_
> 资源标识符（失效请求、分发）

**--if-match** _etag_
> 用于条件更新/删除的 ETag

# DESCRIPTION

**aws cloudfront** 管理 Amazon CloudFront——一种内容分发网络（CDN），在全球边缘节点缓存内容以实现低延迟交付。

**失效（invalidation）**会在 TTL 到期之前将缓存对象从边缘节点移除。路径支持通配符（/images/*），可一次使多个文件失效。每月前 1000 个失效路径免费。

**分发（distribution）**定义源站（S3、ALB、自定义 HTTP）、缓存行为、SSL 证书及其他交付设置。更改会向全球传播，可能需要 15-30 分钟。

**Origin Access Control（OAC）**通过限制对存储桶的直接访问来保护 S3 源站，要求请求必须经过 CloudFront。

**CloudFront Functions** 和 **Lambda@Edge** 允许在边缘节点运行代码，自定义请求/响应的处理逻辑。

在 shell 命令中，含通配符的路径要用引号包裹，以防被 glob 展开。

# CAVEATS

删除分发必须先禁用，然后等待状态变为 `Deployed`。每月前 1000 个失效路径之后会产生费用。分发的更改向全球传播需要时间。更新配置时需要通过 **--if-match** 提供当前的 ETag 值。

# HISTORY

**Amazon CloudFront** 于 **2008 年 11 月**推出，是 AWS 的内容分发网络服务。它已从基本的静态内容交付发展为支持动态内容、流媒体、WebSocket，并通过 Lambda@Edge（2016 年）和 CloudFront Functions（2021 年）支持边缘无服务器计算。

# INSTALL

```dnf: sudo dnf install aws```

```pacman: sudo pacman -S aws-cli```

```apk: sudo apk add aws-cli```

```zypper: sudo zypper install aws-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aws](/man/aws)(1), [aws-s3](/man/aws-s3)(1), [aws-acm](/man/aws-acm)(1), [aws-route53](/man/aws-route53)(1)
