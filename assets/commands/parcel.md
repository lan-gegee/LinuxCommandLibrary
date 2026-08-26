# TAGLINE

零配置的 Web 应用打包器

# TLDR

**启动开发服务器**

```parcel [index.html]```

**进行生产构建**

```parcel build [index.html]```

**指定输出目录**

```parcel build [index.html] --dist-dir [dist]```

**不启服务器的监视模式**

```parcel watch [index.html]```

**指定端口并在浏览器中打开**

```parcel [index.html] --port [3000] --open```

**只构建 package.json 中定义的某个目标**

```parcel build [index.html] --target [main]```

**构建时不压缩、不加内容哈希**

```parcel build [index.html] --no-optimize --no-content-hash```

# SYNOPSIS

**parcel** [_command_] [_options_] _entries_...

# PARAMETERS

**build**
> 生产构建然后退出。

**watch**
> 监视变更并重新构建，但不启动开发服务器。

**serve**
> 启动带 HMR 的开发服务器（默认命令）。

**--dist-dir** _dir_
> 输出目录（package.json targets 中 distDir 的默认值）。

**-p**, **--port** _port_
> 开发服务器端口（也可以通过 PORT 环境变量设置）。

**--host** _host_
> 开发服务器主机（默认监听所有接口）。

**--open**
> 自动在默认浏览器中打开入口页面。

**--lazy**
> 延迟构建文件，直到浏览器请求时才处理。

**--https**
> 为开发服务器启用 HTTPS。

**--target** _target_
> 只构建 package.json 中定义的特定目标。可以多次指定。

**--public-url** _url_
> 绝对 URL 的路径前缀。

**--no-cache**
> 禁止读取文件系统缓存。

**--cache-dir** _dir_
> 设置缓存目录（默认为 .parcel-cache）。

**--no-source-maps**
> 禁用 sourcemap。

**--no-optimize**
> 禁用压缩等优化措施。

**--no-content-hash**
> 禁用在输出文件名中加入内容哈希。

**--log-level** _level_
> 设置日志级别（none、error、warn、info、verbose）。

**--config** _config_
> 指定要使用的 Parcel 配置（默认为 @parcel/config-default）。

# DESCRIPTION

**Parcel** 是一个零配置的 Web 应用打包器。它开箱即用地支持 JavaScript、CSS、HTML、图像及其他资源，并自动完成转换。

Parcel 使用工作进程进行并行构建，并内置了支持热模块替换（HMR）的开发服务器。

# CAVEATS

Parcel 2 的命令行界面与 v1 不同。缓存放置在 .parcel-cache 目录。构建目标要在 package.json 中配置，而不能像 v1 那样用 `--target node` 指定。

# HISTORY

Parcel 由 **Devon Govett** 于 **2017 年**创建，作为 webpack 的零配置替代方案。

# SEE ALSO

[webpack](/man/webpack)(1), [vite](/man/vite)(1), [esbuild](/man/esbuild)(1), [rollup](/man/rollup)(1), [npm](/man/npm)(1)
