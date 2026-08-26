# TAGLINE

按项目管理多个 Ruby 版本

# TLDR

**列出已安装的版本**

```rbenv versions```

**列出可用的版本**

```rbenv install -l```

**安装 Ruby 版本**

```rbenv install [3.2.0]```

**设置全局版本**

```rbenv global [3.2.0]```

**设置本地版本**

```rbenv local [3.2.0]```

**显示当前版本**

```rbenv version```

**设置 shell 专属版本**

```rbenv shell [3.2.0]```

**重建 shims**

```rbenv rehash```

# SYNOPSIS

**rbenv** _command_ [_args_...]

# DESCRIPTION

**rbenv** 用于管理多个 Ruby 安装。它允许在全局、按项目或按 shell 的粒度切换 Ruby 版本，而无需修改系统 Ruby。

该工具通过 shims 拦截 Ruby 命令，并根据上下文将其路由到相应的版本。

# PARAMETERS

**versions**
> 列出已安装的版本。

**version**
> 显示当前版本。

**install** _version_
> 安装 Ruby 版本。

**uninstall** _version_
> 移除 Ruby 版本。

**global** _version_
> 设置全局默认版本。

**local** _version_
> 设置目录级版本。

**shell** _version_
> 设置 shell 版本。

**rehash**
> 重建 shims。

**which** _name_
> 显示可执行文件路径。

**init**
> 在当前 shell 中初始化 rbenv shims。

**exec** _command_
> 使用选定的 Ruby 版本运行可执行文件。

# CAVEATS

安装需要 ruby-build 插件。安装 gem 后需要重新 rehash。通过 .ruby-version 文件实现按项目的版本管理。

# HISTORY

**rbenv** 由 **Sam Stephenson** 于 **2011 年**创建，是 RVM 的更简单替代品。它专注于把一件事做好——版本切换——而不修改 shell，也不管理 gemset。

# INSTALL

```dnf: sudo dnf install rbenv```

```pacman: sudo pacman -S rbenv```

```zypper: sudo zypper install rbenv```

```brew: brew install rbenv```

```nix: nix profile install nixpkgs#rbenv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ruby](/man/ruby)(1), [gem](/man/gem)(1), [bundle](/man/bundle)(1), [rvm](/man/rvm)(1), [asdf](/man/asdf)(1)
