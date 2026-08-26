# TAGLINE

管理 DigitalOcean Functions 无服务器计算

# TLDR

**连接到 serverless 命名空间**

```doctl serverless connect```

**部署函数**

```doctl serverless deploy [path]```

**列出函数**

```doctl serverless functions list```

**调用一个函数**

```doctl serverless functions invoke [name]```

**获取函数日志**

```doctl serverless activations logs [activation_id]```

**初始化一个项目**

```doctl serverless init --language [js] [path]```

开发时**每次更改都重新部署**

```doctl serverless watch [path]```

# SYNOPSIS

**doctl** **serverless** _command_ [_arguments_] [_flags_]

# SUBCOMMANDS

**install**
> 安装其他子命令所依赖的 serverless 支持插件。

**upgrade** / **uninstall**
> 使 serverless 插件与当前版本的 doctl 保持一致，或将其移除。

**connect** [_namespace_]
> 将本地 serverless 支持连接到一个函数命名空间。

**namespaces**
> 创建、列出和删除函数命名空间。

**status**
> 显示是否已安装 serverless 支持以及当前连接的命名空间。

**init** _path_
> 创建一个函数项目目录。**--language** 选择运行时（`js`、`py`、`go`、`php` 等），**--overwrite** 会替换现有目录。

**deploy** _path_
> 将函数项目部署到已连接的命名空间。

**watch** _path_
> 监视项目目录，并在每次更改时增量重新部署。

**undeploy**
> 从命名空间中移除已部署的函数或包。

**get-metadata** _path_
> 打印函数项目的元数据。

**functions**
> 操作命名空间中的函数：**list**、**get** 和 **invoke**。

**activations**
> 获取激活（activation）记录：**list**、**get**、**logs** 和 **result**。

**key**
> 管理函数命名空间的访问密钥。

# DESCRIPTION

**doctl serverless** 管理 DigitalOcean Functions——一种无需管理基础设施即可部署和运行代码的无服务器计算平台。Functions 响应事件和 HTTP 请求，并根据需求自动伸缩。

该平台支持多种编程语言，包括 JavaScript（Node.js）、Python、PHP 和 Go。函数按命名空间组织，以项目为单位部署，每个项目包含一个或多个函数定义。每次函数激活都会被记录，可用于调试检查。

无服务器计算非常适合事件驱动型工作负载、API 端点、后台处理以及流量模式多变的应用。DigitalOcean Functions 自动处理伸缩、负载均衡和基础设施管理。

该平台底层基于 **Apache OpenWhisk** 构建，这就是为什么项目用 `project.yml` 文件描述，以及为什么每次调用都会产生一条带有独立 ID、日志和结果的 *activation* 记录。

# CAVEATS

serverless 子命令并不包含在 doctl 二进制文件本身中：需要先通过 **doctl serverless install** 下载插件，并且在 doctl 更新后必须重新运行 **doctl serverless upgrade**，否则这些命令将拒绝工作。部署前还必须先 **connect** 到一个命名空间，而命名空间只属于唯一一个区域。函数受平台在执行时间、内存和载荷大小方面的限制；长时间运行或有状态的工作负载应改用 App Platform 或 Droplet。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl](/man/doctl)(1), [doctl-apps](/man/doctl-apps)(1)

# RESOURCES

```[Source code](https://github.com/digitalocean/doctl)```

```[Documentation](https://docs.digitalocean.com/reference/doctl/reference/serverless/)```

<!-- verified: 2026-07-14 -->
