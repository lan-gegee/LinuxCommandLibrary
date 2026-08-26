# TAGLINE

管理多个 Perl 安装版本

# TLDR

**列出已安装的版本**

```plenv versions```

**显示当前版本**

```plenv version```

**设置全局版本**

```plenv global [5.38.0]```

**设置本地版本**

```plenv local [5.36.0]```

**安装 Perl 版本**

```plenv install [5.38.0]```

**列出可用版本**

```plenv install --list```

**安装 cpanm**

```plenv install-cpanm```

**重建 shims**

```plenv rehash```

# SYNOPSIS

**plenv** [_install_] [_global_] [_local_] [_versions_] [_options_] [_version_]

# PARAMETERS

**install** _VERSION_
> 安装 Perl 版本。

**install --list**
> 列出可用版本。

**versions**
> 列出已安装的版本。

**version**
> 显示当前版本。

**global** [_VERSION_]
> 设置/显示全局版本。

**local** [_VERSION_]
> 设置/显示本地版本。

**shell** [_VERSION_]
> 设置当前 Shell 特有的版本。

**rehash**
> 重建 shim 可执行文件。

**which** _CMD_
> 显示命令路径。

**exec** _CMD_
> 使用当前 Perl 运行命令。

**install-cpanm**
> 安装 cpanminus。

# DESCRIPTION

**plenv** 管理多个 Perl 版本。它把各版本安装到 ~/.plenv，并使用 shims 将命令路由到正确的 Perl。

版本选择优先级依次为：PLENV_VERSION 环境变量、当前及上级目录中的 .perl-version 文件、全局设置。

本地版本会创建 .perl-version 文件，为项目指定专用的 Perl。进入该目录时版本自动切换。

安装过程使用 Perl-Build 从源码编译。构建选项可用于自定义安装。

cpanm 安装后提供了一个可与所有受管 Perl 版本配合使用的模块安装器。安装带可执行文件的模块后请运行 rehash。

其设计仿照 rbenv，为熟悉该模式的开发者提供了跨语言一致的版本管理体验。

# CONFIGURATION

**~/.plenv/versions/**
> 存放已安装 Perl 版本的目录。

**~/.plenv/version**
> 全局 Perl 版本设置文件。

**.perl-version**
> 按目录生效的 Perl 版本文件，用于项目级设置。

**PLENV_VERSION**
> 用于覆盖当前活动 Perl 版本的环境变量。

# CAVEATS

编译 Perl 需要开发工具。切换版本时某些模块需要重新编译。需要进行 Shell 初始化。

# HISTORY

**plenv** 由 **Tokuhiro Matsuno** 于 **2011 年前后**创建，灵感来自 rbenv。它沿用使 rbenv 在 Ruby 社区取得成功的同一套理念，为 Perl 提供版本管理。

# INSTALL

```brew: brew install plenv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perlbrew](/man/perlbrew)(1), [cpanm](/man/cpanm)(1), [perl](/man/perl)(1), [rbenv](/man/rbenv)(1)
