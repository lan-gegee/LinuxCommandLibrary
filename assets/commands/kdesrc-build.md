# TAGLINE

从源码仓库构建 KDE 软件的工具

# TLDR

**初始化** kdesrc-build

```kdesrc-build --initial-setup```

**构建** KDE 组件及其依赖

```kdesrc-build [component_name]```

构建时**不更新代码**也不构建依赖

```kdesrc-build --no-src --no-include-dependencies [component_name]```

编译前**刷新**构建目录

```kdesrc-build --refresh-build [component_name]```

从指定的依赖处**恢复**

```kdesrc-build --resume-from [dependency_component] [component_name]```

**运行**已构建的组件

```kdesrc-build --run --exec [executable_name] [component_name]```

构建**所有**已配置的组件

```kdesrc-build```

# SYNOPSIS

**kdesrc-build** [_options_] [_components_]

# PARAMETERS

**--initial-setup**
> 初始化配置

**--no-src**
> 不更新源代码

**--no-include-dependencies**
> 不构建依赖

**--refresh-build**
> 构建前清理构建目录

**--resume-from** _COMPONENT_
> 从指定组件恢复

**--run** **--exec** _NAME_
> 运行已构建的可执行文件

**--no-stop-on-failure**
> 某个组件失败时继续构建

# DESCRIPTION

**kdesrc-build** 是一个从源码仓库构建 KDE 软件的工具。它通过妥善处理依赖关系，自动完成 KDE 组件的下载、配置和编译。

该工具管理 KDE 源代码的本地检出，可以构建单个组件或整个桌面环境。配置存储在 ~/.config/kdesrc-buildrc 中。

# CAVEATS

需要大量磁盘空间和时间。必须安装构建依赖。可以考虑使用 kde-builder 作为性能更好的现代替代品。

# HISTORY

多年来，kdesrc-build 一直是 KDE 开发者从源码构建 KDE 软件的标准工具。它正逐渐被 kde-builder 取代。

# SEE ALSO

[kde-builder](/man/kde-builder)(1), [cmake](/man/cmake)(1), [make](/man/make)(1)
