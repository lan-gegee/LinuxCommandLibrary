# TAGLINE

构建 Angular 应用并启动开发服务器

# TLDR

**启动开发服务器**

```ng serve```

**在指定端口上运行**

```ng serve --port [4200]```

**运行并打开浏览器**

```ng serve --open```

**运行指定项目**

```ng serve [project-name]```

**以生产配置运行**

```ng serve --configuration=production```

**通过代理运行**

```ng serve --proxy-config [proxy.conf.json]```

# SYNOPSIS

**ng serve** [_project_] [_options_]

# PARAMETERS

**--port** _port_
> 端口号。

**--open**, **-o**
> 在浏览器中打开。

**--host** _host_
> 绑定地址。

**--configuration** _name_
> 构建配置。

**--proxy-config** _file_
> 代理配置。

**--ssl**
> 启用 HTTPS。

**--watch**
> 文件变更时重新构建（默认行为）。

**--live-reload**
> 启用实时重载。

# DESCRIPTION

**ng serve** 构建 Angular 应用并启动开发服务器。它会监视文件变更并自动重新构建，通过实时重载刷新浏览器。

这是 Angular 开发工作流中最常用的命令。

# PROXY CONFIG

```json
// proxy.conf.json
{
  "/api": {
    "target": "http://localhost:3000",
    "secure": false
  }
}
```

# CAVEATS

仅供开发使用；生产环境请改用 ng build。对大型项目来说内存开销较大。属于 Angular CLI 的一部分。

# HISTORY

Angular CLI 的 serve 命令随 **2016 年**发布的 Angular CLI 一同推出，为 Angular 应用提供了完整的开发服务器解决方案。

# SEE ALSO

[ng](/man/ng)(1), [webpack](/man/webpack)(1), [vite](/man/vite)(1)
