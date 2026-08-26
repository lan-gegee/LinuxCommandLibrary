# TAGLINE

Amazon S3 存储桶的交互式 TUI 浏览器

# TLDR

**启动 S3 浏览器**

```stu```

**在指定区域浏览特定存储桶**

```stu --region [us-east-1] --bucket [my-bucket]```

**连接到 S3 兼容端点**

```stu --profile [myprofile] --endpoint-url [https://s3.example.com]```

# SYNOPSIS

**stu** [**--region** _region_] [**--bucket** _bucket_] [**--prefix** _prefix_] [**--profile** _profile_] [**--endpoint-url** _url_] [**--path-style**]

# PARAMETERS

**--region** _REGION_
> 要使用的 AWS 区域。

**--bucket** _BUCKET_
> 要浏览的 S3 存储桶。

**--profile** _PROFILE_
> AWS 配置文件名称。

**--endpoint-url** _URL_
> 自定义的 S3 兼容端点 URL。

**--path-style**
> 使用路径式（path-style）寻址。

# DESCRIPTION

**stu** 是一个基于终端的 Amazon S3 交互式浏览器。它允许用户浏览存储桶和对象、以语法高亮方式预览文件以及递归下载条目。它支持 S3 兼容存储服务和自定义按键绑定。

# HISTORY

**stu** 由 **lusingander** 创建，使用 **Rust** 编写。

# INSTALL

```apk: sudo apk add stu```

```brew: brew install stu```

```nix: nix profile install nixpkgs#stu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stree](/man/stree)(1), [aws](/man/aws)(1), [s3cmd](/man/s3cmd)(1)
