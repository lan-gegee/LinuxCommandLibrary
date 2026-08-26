# TAGLINE

从源码仓库构建 KDE 软件的工具

# TLDR

**初始化** kde-builder

```kde-builder --initial-setup```

**构建** KDE 组件及其依赖

```kde-builder [component_name]```

构建时**不更新代码**也不构建依赖

```kde-builder -SD [component_name]```

编译前**刷新**构建目录

```kde-builder -r [component_name]```

从指定依赖处**恢复**编译

```kde-builder -f [dependency_component] [component_name]```

**运行**已构建的组件

```kde-builder --run [executable_name]```

安装**登录会话**

```kde-builder --install-login-session-only```

# SYNOPSIS

**kde-builder** [_options_] [_components_]

# PARAMETERS

**--initial-setup**
> 初始化 kde-builder 配置

**-S**, **--no-src**
> 不更新源代码

**-D**, **--no-include-dependencies**
> 不构建依赖

**-r**, **--refresh-build**
> 清理并刷新构建目录

**-f**, **--resume-from** _COMPONENT_
> 从指定组件恢复构建

**--run** _EXECUTABLE_
> 运行已构建的组件

**--install-login-session-only**
> 安装登录会话文件

**--no-stop-on-failure**
> 某个组件失败时继续构建

# DESCRIPTION

**kde-builder** 是一个从源码仓库构建 KDE 软件的工具。它处理 KDE 组件的依赖解析、源码更新、配置和编译。

该工具是 kdesrc-build 的直接替代品，具有更好的性能和易用性。它可以构建单个组件或 Plasma 这样的完整桌面环境。

# CAVEATS

需要大量磁盘空间和构建时间。构建依赖必须单独安装。针对特定环境可能需要自定义配置文件。

# HISTORY

kde-builder 作为 kdesrc-build 的现代化替代品而开发，让从源码构建 KDE 软件的安装更简单、性能更好。

# SEE ALSO

[kdesrc-build](/man/kdesrc-build)(1), [cmake](/man/cmake)(1), [ninja](/man/ninja)(1)
