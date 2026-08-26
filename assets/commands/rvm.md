# TAGLINE

管理多个 Ruby 安装的版本管理器

# TLDR

**安装 Ruby 版本**

```rvm install [3.2.0]```

**列出已安装的版本**

```rvm list```

**使用指定版本**

```rvm use [3.2.0]```

**设置默认版本**

```rvm use [3.2.0] --default```

**创建 gemset**

```rvm gemset create [myproject]```

**使用带 gemset 的版本**

```rvm use [3.2.0]@[myproject]```

**列出可用版本**

```rvm list known```

# SYNOPSIS

**rvm** [_options_] _command_ [_args_...]

# DESCRIPTION

**rvm**（Ruby Version Manager）用于管理多个 Ruby 安装和 gemset。它负责 Ruby 的安装、版本切换，以及相互隔离的 gem 环境。

该工具通过修改 shell 环境来切换 Ruby 版本，并提供 gemset 以实现项目专属的 gem 隔离。

# PARAMETERS

**install** _version_
> 安装 Ruby 版本。

**use** _version_
> 切换到指定版本。

**list**
> 列出已安装的版本。

**list known**
> 列出可用版本。

**gemset create** _name_
> 创建 gemset。

**gemset use** _name_
> 使用指定 gemset。

**gemset list**
> 列出 gemset。

**--default**
> 设为默认版本。

**implode**
> 彻底移除 RVM。

# CAVEATS

会修改 shell 初始化文件。可能与系统自带的 Ruby 冲突。gemset 会增加复杂度。有些人更偏爱 rbenv 更简单的方案。

# HISTORY

**RVM** 由 **Wayne E. Seguin** 于 **2009 年**创建，旨在简化 Ruby 版本管理。在 rbenv 提供更简单的替代方案之前，它曾是最主流的 Ruby 版本管理器。目前由 **Michal Papis** 维护。

# INSTALL

```dnf: sudo dnf install rvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ruby](/man/ruby)(1), [gem](/man/gem)(1), [rbenv](/man/rbenv)(1), [bundler](/man/bundler)(1)
