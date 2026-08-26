# TAGLINE

.NET 微服务开发与部署工具

# TLDR

**运行应用程序**

```tye run```

**在指定端口上运行并启用仪表板**

```tye run --dashboard --port [9000]```

**以 Docker 容器方式运行服务**

```tye run --docker```

**运行时监视文件实现实时重载**

```tye run --watch```

**部署到 Kubernetes**

```tye deploy```

**初始化 tye.yaml 配置文件**

```tye init```

# SYNOPSIS

**tye** _command_ [_options_] [_path_]

# PARAMETERS

**run**
> 在本地运行应用程序。

**build**
> 为应用程序构建容器。

**deploy**
> 将应用程序部署到 Kubernetes。

**init**
> 生成 tye.yaml 配置文件的脚手架。

**--dashboard**
> 运行时启动 Web 仪表板。

**--port** _PORT_
> 仪表板端口（默认：8000）。

**--docker**
> 以 Docker 容器方式运行项目。

**--watch**
> 监视文件更改并重启被修改的服务。

**--no-build**
> 运行前不构建项目。

**--debug** _SERVICE_
> 等待调试器附加到服务。使用 * 表示所有服务。

**--logs** _PROVIDER_
> 将结构化日志写入提供程序（console、elastic、ai、seq）。

**--tags** _TAGS_
> 按标签过滤正在运行的服务。

**-v, --verbosity** _LEVEL_
> 输出详细程度：Debug、Info（默认）、Quiet。

# DESCRIPTION

**Tye** 是 Microsoft 推出的实验性开发工具，用于简化 .NET 微服务应用的运行与部署。它在本地编排多个服务，通过单条命令一起启动它们，并提供 Web 仪表板来监控服务的状态、日志和端点。

该工具自动处理服务发现，让微服务无需手动配置端口和地址就能相互找到。服务的构建和容器化流程被简化，便于部署到 Kubernetes 集群。

配置定义在 **tye.yaml** 文件中，其中列出各个服务、它们的依赖关系以及部署设置。

# CAVEATS

Tye 是一个实验性项目，已不再积极开发。它需要 .NET SDK。Kubernetes 部署需要容器镜像仓库和集群访问权限。

# HISTORY

**Tye** 由 **Microsoft** 创建，是用于开发和部署 .NET 微服务的实验性工具。

# SEE ALSO

[docker-compose](/man/docker-compose)(1), [dotnet](/man/dotnet)(1), [kubectl](/man/kubectl)(1), [helm](/man/helm)(1)
