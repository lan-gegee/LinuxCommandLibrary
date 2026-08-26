# TAGLINE

按项目管理多个 PHP 版本

# TLDR

**列出已安装的 PHP 版本**

```phpenv versions```

**显示当前版本**

```phpenv version```

**设置全局 PHP 版本**

```phpenv global [8.2.0]```

**设置项目本地版本**

```phpenv local [8.1.0]```

**设置 shell 专属版本**

```phpenv shell [8.0.0]```

**安装 PHP 版本**

```phpenv install [8.2.0]```

**列出可用版本**

```phpenv install --list```

**重建 shim**

```phpenv rehash```

# SYNOPSIS

**phpenv** [_install_] [_global_] [_local_] [_shell_] [_versions_] [_options_] [_version_]

# PARAMETERS

**install** _VERSION_
> 安装 PHP 版本。

**install --list**
> 列出可安装的版本。

**versions**
> 列出已安装的版本。

**version**
> 显示当前版本。

**global** [_VERSION_]
> 设置/显示全局版本。

**local** [_VERSION_]
> 设置/显示项目本地版本。

**shell** [_VERSION_]
> 设置 shell 专属版本。

**rehash**
> 重建 shim 可执行文件。

**which** _CMD_
> 显示命令对应的路径。

**root**
> 显示 phpenv 根目录。

# DESCRIPTION

**phpenv** 按项目管理多个 PHP 版本。它使用 shim 拦截 PHP 命令并将其路由到正确的版本。

版本选择遵循一个层级：PHPENV_VERSION 环境变量、当前及父级目录中的 .php-version 文件、全局版本设置。

local 命令会在当前目录创建 .php-version 文件。进入该目录时，phpenv 会自动使用指定的版本。

安装功能需要 php-build 插件，它从源码编译 PHP。必须先安装构建依赖。

安装 PHP 扩展或 PEAR 软件包后，请运行 rehash 为新的可执行文件创建 shim。

其架构仿照 Ruby 的 rbenv，为多语言开发者提供熟悉的版本管理方式。

# CAVEATS

编译 PHP 需要构建依赖。构建耗时可能较长。需要初始化 shell。某些扩展可能需要手动配置。

# HISTORY

**phpenv** 以 **rbenv** 为蓝本，为 PHP 提供类似的版本管理方式。它采用相同的 shim 方案和插件架构，使 PHP 的版本管理与其他语言环境保持一致。

# SEE ALSO

[php](/man/php)(1), [composer](/man/composer)(1), [rbenv](/man/rbenv)(1), [php-build](/man/php-build)(1)
