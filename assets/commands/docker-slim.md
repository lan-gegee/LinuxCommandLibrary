# TAGLINE

优化并缩减 Docker 镜像体积

# TLDR

**分析并瘦身一个镜像**

```docker-slim build [image]```

**分析镜像**

```docker-slim profile [image]```

**检查 Dockerfile**

```docker-slim lint [Dockerfile]```

**从镜像生成 Dockerfile**

```docker-slim xray [image]```

**使用 HTTP 探测进行瘦身**

```docker-slim build --http-probe [image]```

**瘦身时保留 shell 访问能力**

```docker-slim build --include-shell [image]```

# SYNOPSIS

**docker-slim** _command_ [_options_] [_image_]

# SUBCOMMANDS

**build**
> 分析并创建优化后的镜像。

**profile**
> 仅分析镜像而不构建。

**xray**
> 检查镜像内部结构。

**lint**
> 检查 Dockerfile。

**version**
> 显示版本信息。

# PARAMETERS

**--http-probe**
> 启用 HTTP 探测。

**--include-shell**
> 在瘦身后保留 shell。

**--target** _string_
> 目标输出镜像名称。

**--expose** _port_
> 暴露额外的端口。

# DESCRIPTION

**docker-slim**（又称 SlimToolkit）通过静态和动态分析来分析并优化 Docker 镜像，在保持功能的前提下显著减小体积。其工作原理是运行容器，监测实际用到的文件和依赖，然后创建只包含这些组件的最小化镜像。在保持应用功能的同时，最多可将镜像体积缩小 30 倍。

# INSTALL

```brew: brew install docker-slim```

```nix: nix profile install nixpkgs#docker-slim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[docker-build](/man/docker-build)(1), [docker-images](/man/docker-images)(1)

# RESOURCES

```[Source code](https://github.com/slimtoolkit/slim)```

```[Homepage](https://slimtoolkit.org/)```

<!-- verified: 2026-07-11 -->
