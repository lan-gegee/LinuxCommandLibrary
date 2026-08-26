# TAGLINE

编译 Angular 应用

# TLDR

**构建生产版本**

```ng build --configuration production```

**生成 source map 构建**

```ng build --source-map```

**在工作区中构建指定项目**

```ng build [project-name]```

以**监视模式**在文件更改时重新构建

```ng build --watch```

**设置输出路径**

```ng build --output-path [dist/custom]```

**使用自定义 base href 构建**

```ng build --base-href [/my-app/]```

**生成 stats JSON**用于包体积分析

```ng build --stats-json```

**开发环境构建**

```ng build --configuration development```

# SYNOPSIS

**ng** **build** [_project_] [_options_]

# PARAMETERS

_PROJECT_
> 要构建的项目名称，即在 angular.json 中定义的名称。

**-c**, **--configuration** _name_
> 一个或多个命名构建器配置（逗号分隔），在 angular.json 中定义。

**--source-map**
> 为脚本和样式生成 source map（默认：false）。

**--watch**
> 文件更改时重新构建（默认：false）。

**--output-path** _dir_
> 相对于工作区根目录的输出目录。

**--base-href** _url_
> 所构建应用的基础 URL。

**--aot**
> 使用 AOT（预先）编译构建（默认：true）。

**--optimization**
> 启用优化，包括压缩、摇树优化和死代码消除（默认：true）。

**--output-hashing** _mode_
> 缓存失效哈希模式：none、all、media 或 bundles（默认：none）。

**--delete-output-path**
> 构建前删除输出路径（默认：true）。

**--stats-json**
> 生成用于包分析的 stats.json 文件（默认：false）。

**--progress**
> 构建时向控制台输出进度（默认：true）。

**--extract-licenses**
> 将所有许可证提取到单独文件（默认：true）。

**--subresource-integrity**
> 启用子资源完整性校验（默认：false）。

**--verbose**
> 添加详细的输出日志（默认：false）。

**--named-chunks**
> 对懒加载 chunk 使用文件名（默认：false）。

**--poll** _ms_
> 文件监视的轮询时间间隔（毫秒）。

**--ssr**
> 在运行时启用服务端渲染（默认：false）。

**--prerender**
> 在构建期间启用静态站点生成（预渲染）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ng build** 将 Angular 应用或库编译到输出目录。它负责 TypeScript 编译、打包、压缩、摇树优化等处理，生成可部署的制品。

application builder 使用 esbuild 作为构建工具。默认配置选项在工作区配置文件（angular.json）中指定，也可以通过命名的备用配置覆盖。命令行选项优先于 angular.json 中的设置。

使用 CLI 创建项目时通常会默认定义一个启用完整优化的 "production" 配置。此外还有一个构建更快并带 source map 的 "development" 配置。

# CAVEATS

属于 **Angular CLI** 的一部分。构建配置在 angular.json 中管理。命令行选项名采用 dash-case（短横线命名），而配置文件中使用 camelCase。某些选项只能通过 angular.json 设置。`--prod` 标志已在 Angular 12 中移除；请改用 `--configuration production`。

# HISTORY

**ng build** 是 **Angular CLI** 的组成部分，于 **2016 年**随 Angular 2 一同发布。构建系统最初基于 Webpack，但现代版本的 Angular（17 及以上）已迁移到 **esbuild**，构建速度显著提升。

# SEE ALSO

[ng](/man/ng)(1), [ng-serve](/man/ng-serve)(1), [webpack](/man/webpack)(1)
