# TAGLINE

用于搭建和管理 Leaf PHP 项目的命令行工具

# TLDR

**创建**新的 Leaf 项目（交互式选择预设）

```leaf create [my-app]```

**创建**纯净的 Leaf 3 项目

```leaf create [my-app] --basic```

从 API 预设**创建**项目

```leaf create [my-app] --api```

从 MVC 预设**创建**项目

```leaf create [my-app] --mvc```

向当前项目**安装** Leaf 模块或 Composer 软件包

```leaf install [package_name]```

在自定义端口上**启动**本地 PHP 开发服务器

```leaf serve -p [8000]```

**启动**本地服务器，支持文件监听与热重载

```leaf serve --watch```

针对当前 Leaf 应用**打开**交互式 Shell

```leaf interact```

# SYNOPSIS

**leaf** _command_ [_options_] [_arguments_]

# PARAMETERS

**create** _name_
> 搭建一个新的 Leaf 项目。可结合 **--basic**、**--api**、**--mvc** 或 **--custom** 选择预设。

**install** _package_
> 向当前项目安装 Leaf 模块（如 **ui**、**auth**、**db**）或任意 Composer 软件包。

**serve** [**-p** _port_] [**--watch**]
> 启动内置 PHP 开发服务器。**-p** 设置端口，**--watch** 在文件变更时启用热重载。

**interact**
> 打开绑定到当前 Leaf 应用上下文的交互式 REPL。

**test**
> 运行项目测试套件。

**deploy**
> 触发当前项目的部署（取决于所配置的驱动）。

**--basic**
> 使用纯净的 Leaf 3 起步模板（仅路由 + 核心组件）。

**--api**
> 使用面向 API 的预设，包含路由、验证和 JSON 辅助函数。

**--mvc**
> 使用 MVC 预设（控制器、视图、模型）。

**--custom**
> 通过交互式设置流程手动挑选模块。

**-h**, **--help**
> 显示 CLI 或特定子命令的帮助信息。

**-v**, **--version**
> 输出已安装的 CLI 版本。

# DESCRIPTION

**leaf** 是 **Leaf PHP** 微框架的官方命令行伴侣工具。它可以基于精选预设搭建新应用、安装官方模块和 Composer 软件包、运行本地开发服务器，并提供用于调试和探索的交互式 Shell。

该工具封装了 **composer** 和 PHP 内置 Web 服务器，免去了项目初始化与模块接线的样板工作。**--api** 和 **--mvc** 等预设定成即可运行的目录布局，路由、环境加载和模块绑定均已预先配置。

在 **--watch** 模式下，**leaf serve** 会在文件变更时重启服务器，提供快速的开发迭代循环。**leaf interact** 会启动应用并让用户进入 Tinker 风格的 REPL，可以直接调用路由、模型和服务。

# CONFIGURATION

通过 Composer 全局安装：

```
composer global require leafs/cli
```

Composer 的 vendor bin 目录必须在 **PATH** 中：

> **Linux:** **$HOME/.config/composer/vendor/bin** 或 **$HOME/.composer/vendor/bin**
> **macOS:** **$HOME/.composer/vendor/bin**
> **Windows:** **%USERPROFILE%\AppData\Roaming\Composer\vendor\bin**

项目级配置位于 **leaf.config.php**（或从 **.env** 加载的环境变量）。CLI 会读取工作目录下的 **composer.json** 来确定项目类型和可用模块。

# CAVEATS

需要 **PHP 7.4+** 和 **Composer**。该 CLI 只管理 PHP 侧的依赖——静态资源和前端工具链仍需另行处理（例如通过 **npm**）。名称 **leaf** 与多个无关项目重名（一个 Go 文件监听工具、一个深度学习框架、一个终端 Markdown 预览器）；请务必安装正确的软件包（**leafs/cli**）。

# HISTORY

Leaf PHP 框架由 **Michael Darko**（"mychi.netlify.app"）和 **leafsphp** 组织创建，**leaf** CLI 的推出是为了简化项目创建和模块管理。该 CLI 以 **leafs/cli** 为名发布在 Packagist 上，采用 **MIT** 许可证分发。

# INSTALL

```brew: brew install leaf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[composer](/man/composer)(1), [php](/man/php)(1), [artisan](/man/artisan)(1)
