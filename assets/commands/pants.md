# TAGLINE

面向 monorepo 的可扩展构建系统

# TLDR

**列出目标**

```pants list ::```

**运行测试**

```pants test ::```

**格式化代码**

```pants fmt ::```

**运行 lint 检查**

```pants lint ::```

**构建软件包**

```pants package [path/to:target]```

**运行指定目标**

```pants run [path/to:target]```

**检查类型**

```pants check ::```

**显示依赖**

```pants dependencies [path/to:target]```

# SYNOPSIS

**pants** [_options_] _goal_ [_targets_...]

# PARAMETERS

**list**
> 列出匹配的目标。

**test**
> 为匹配的测试目标运行测试。

**fmt**
> 用已配置的格式化工具原地格式化源文件。

**lint**
> 对匹配的目标运行 lint 检查。

**check**
> 运行类型/编译检查（例如 mypy、javac）。

**package**
> 构建可部署的产物（wheel、pex、jar、Docker 镜像等）。

**run**
> 运行一个可执行目标。

**publish**
> 将可部署产物发布到远程 registry。

**dependencies**
> 显示某个目标的传递依赖。

**dependents**
> 显示依赖于给定目标的那些目标。

**roots**
> 列出所有匹配的根目标。

**peek**
> 打印匹配目标的详细元数据。

**repl**
> 启动预加载了指定目标的交互式 REPL。

**tailor**
> 自动生成或更新 BUILD 文件。

**update-build-files**
> 对现有 BUILD 文件应用弃用修复。

**--changed-since** _REF_
> 将目标限定为自给定 git ref 以来发生变更的那些。

**--changed-dependents=**_MODE_
> 包含已变更目标的依赖方（_none_、_direct_、_transitive_）。

**-l**, **--level** _LEVEL_
> 日志级别（trace、debug、info、warn、error）。

**--keep-sandboxes=**_MODE_
> 保留执行沙盒以便调试（_always_、_on_failure_、_never_）。

**--no-local-cache**, **--no-remote-cache**
> 在本次运行中禁用本地或远程构建缓存。

# DESCRIPTION

**pants** 是面向 monorepo 的可扩展构建系统。它支持 Python、Go、Java、Scala、Shell 和 Docker。

目标写法用冒号分隔路径和目标名。双冒号（::）会递归匹配所有目标。

缓存和记忆化让重复构建速度很快。远程缓存则支持团队级的构建共享。

依赖推断会自动发现代码中的导入。显式依赖也可以在 BUILD 文件中声明。

细粒度失效只重建受影响的目标。并发执行会充分利用可用核心。

# CAVEATS

需要有定义目标的 BUILD 文件。初始配置有一定学习曲线。大型代码库的首次运行可能较慢。

# HISTORY

**Pants** 最初在 **2011 年**前后由 **Twitter** 开发。2.x 版本是一次彻底重写，重点改进 Python 方面的易用性。现在由 **Toolchain** 作为开源项目维护。

# SEE ALSO

[bazel](/man/bazel)(1), [buck](/man/buck)(1), [make](/man/make)(1), [gradle](/man/gradle)(1)
