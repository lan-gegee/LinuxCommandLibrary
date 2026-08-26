# TAGLINE

Unity 编辑器版本管理器

# TLDR

**列出已安装的版本**

```u3d list```

**安装 Unity 版本**

```u3d install [2022.3.0f1]```

**运行 Unity**

```u3d run -u [2022.3.0f1]```

**查看可用版本**

```u3d available```

**卸载版本**

```u3d uninstall [2022.3.0f1]```

# SYNOPSIS

**u3d** _command_ [_-u version_] [_options_]

# PARAMETERS

**list**
> 列出已安装的 Unity 版本。

**install** _version_
> 下载并安装某个 Unity 版本及其软件包。

**available**
> 列出可供下载的 Unity 版本。

**run**
> 启动 Unity（在项目目录内会自动使用项目所需的版本）。

**uninstall** _version_
> 移除已安装的 Unity 版本。

**licenses**
> 显示当前 Unity 许可证信息。

**prettify**
> 格式化 Unity 编辑器日志文件以提高可读性。

**dependencies**
> 安装 Unity 在 Linux 上缺失的依赖项。

**-u** _VERSION_
> 目标 Unity 版本。

**--verbose**
> 启用调试日志。

**--no-central**
> 跳过中央版本缓存。

# DESCRIPTION

**u3d** 是一个用于并行管理多个 Unity 编辑器安装的命令行工具。它可以列出可用版本、安装特定发行版，并以指定版本启动 Unity，让需要不同 Unity 版本的项目开发变得简单直接。

该工具在 CI/CD 环境中特别有用，因为 Unity 构建需要以无头模式运行。它能从命令行处理许可证激活、版本发现和构建执行。跨平台支持涵盖 macOS、Linux 和 Windows。

# CAVEATS

仅针对 Unity。下载体积大。需要许可证。

# HISTORY

**u3d** 为管理 Unity 编辑器安装而创建，在 CI/CD 环境中尤其有用。

# INSTALL

```aur: yay -S u3d```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[brew](/man/brew)(1)
