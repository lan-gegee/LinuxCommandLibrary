# TAGLINE

Flutter 的 Dart 软件包依赖管理器

# TLDR

**获取依赖**

```flutter pub get```

**更新依赖**

```flutter pub upgrade```

**添加软件包**

```flutter pub add [package_name]```

**移除软件包**

```flutter pub remove [package_name]```

**运行 build runner**

```flutter pub run build_runner build```

# SYNOPSIS

**flutter pub** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 操作类型：get、upgrade、add、remove、run 等。

**get**
> 根据 pubspec.yaml 安装依赖。

**upgrade**
> 更新到最新的兼容版本。

**add** _PACKAGE_
> 将软件包添加到依赖。

**remove** _PACKAGE_
> 从依赖中移除软件包。

**run** _SCRIPT_
> 运行软件包脚本。

**outdated**
> 显示过时的软件包。

**deps**
> 显示依赖树。

**publish**
> 将软件包发布到 **pub.dev**。

**downgrade**
> 将依赖降级到 **pubspec.yaml** 允许的最低版本。

**cache**
> 检查、修复或清理本地 pub 软件包缓存。

**--help**
> 显示帮助信息。

# DESCRIPTION

**flutter pub** 为 Flutter 项目管理 Dart 软件包依赖。它从 Dart 软件包仓库 pub.dev 安装、更新和解析软件包。

该工具读取 pubspec.yaml 中的依赖声明，并生成 pubspec.lock 以确保可复现构建。它会自动处理传递依赖和版本冲突。

借助数千个社区软件包，flutter pub 支持在网络请求、状态管理、UI 组件等方面的代码复用。

# CONFIGURATION

**pubspec.yaml**
> 项目配置文件，定义依赖、开发依赖以及软件包元数据。

**pubspec.lock**
> 生成的锁定文件，确保各环境中依赖版本可复现。

# CAVEATS

版本冲突可能需要手动解决。某些软件包仅限特定平台。庞大的依赖树会拖慢首次构建。**flutter pub run** 对于可执行脚本已弃用——请改用 **dart run**（只有当可执行文件依赖 Flutter SDK 时才使用 **flutter pub run**）。

# HISTORY

flutter pub 封装了 **Dart 的 pub** 工具以便用于 Flutter 开发。pub.dev 仓库同时服务于 Dart 和 Flutter 软件包，通过共享的软件包规范格式管理。

# INSTALL

```nix: nix profile install nixpkgs#flutter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[flutter](/man/flutter)(1), [dart](/man/dart)(1)
