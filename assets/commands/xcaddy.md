# TAGLINE

使用模块构建自定义 Caddy

# TLDR

**构建带模块的 Caddy**

```xcaddy build --with [github.com/module]```

**构建指定版本的 Caddy**

```xcaddy build [v2.7.0] --with [github.com/module]```

**以特定版本构建模块**

```xcaddy build --with [github.com/module@v1.0.0]```

**用本地副本替换模块**以便开发

```xcaddy build --with [github.com/module=../local/path]```

**运行带有某模块的 Caddy**用于开发和测试

```xcaddy run --config [Caddyfile]```

**将二进制文件写到指定路径**

```xcaddy build --output [/path/to/caddy] --with [github.com/module]```

# SYNOPSIS

**xcaddy** **build** [_caddy_version_] [_--output file_] [_--with module[@version][=replacement]_]... [_options_]

**xcaddy** **run** [_caddy_args_...]

**xcaddy** **version**

# PARAMETERS

**build**
> 构建自定义的 Caddy 二进制文件。可以将可选的 Caddy 版本（如 v2.7.0 或 Git 引用）作为第一个参数。

**run**
> 使用当前 Go 模块中的模块构建并运行 Caddy，把其余参数传递给 caddy 命令。适用于插件开发。

**version**
> 打印 xcaddy 版本。

**--with** _MODULE[@VERSION][=REPLACEMENT]_
> 添加一个 Caddy 模块。重复使用可包含多个模块。可选的 @version 用于固定模块版本，=replacement 将其指向本地路径或分支副本。

**--replace** _OLD=NEW_
> 添加 Go 模块 replace 指令而不导入该模块（用于传递依赖）。

**--output** _FILE_
> 输出二进制文件的路径。默认为 ./caddy。

**--embed** _[ALIAS]:PATH_
> 将一个目录嵌入二进制文件，可通过给定的别名访问。

**--pgo** _FILE_
> 传递给 Go 编译器的基于剖析的优化（PGO）profile 文件。

# DESCRIPTION

**xcaddy** 是一款构建工具，用于创建编译了额外模块的自定义 Caddy Web 服务器二进制文件。它使用 Go 工具链从源码编译包含指定插件的 Caddy，生成一个具备全部所需功能的单一二进制文件。

build 命令编译特定版本的 Caddy 并加入一个或多个模块；run 命令则临时构建并运行带指定模块的 Caddy，用于开发和测试，不生成永久二进制文件。通过重复使用 --with 标志可以包含多个模块。

# CAVEATS

需要可用的 Go 工具链。Caddy 核心版本也可以通过 **CADDY_VERSION** 环境变量设置。其他变量可用于调整构建：**XCADDY_RACE_DETECTOR=1**、**XCADDY_DEBUG=1**、**XCADDY_SKIP_CLEANUP=1** 和 **XCADDY_GO_BUILD_FLAGS**。

# HISTORY

**xcaddy** 由 **Caddy** 项目创建，用于构建带插件的自定义 Caddy 二进制文件。

# INSTALL

```apk: sudo apk add xcaddy```

```nix: nix profile install nixpkgs#xcaddy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[caddy](/man/caddy)(1), [go](/man/go)(1)
