# TAGLINE

Ruby 依赖管理器

# TLDR

**从 Gemfile 安装依赖**

```bundle install```

**将 gem 添加到 Gemfile**

```bundle add [gem]```

**更新所有 gem**

```bundle update```

**更新特定 gem**

```bundle update [gem]```

**使用捆绑的 gem 执行命令**

```bundle exec [command]```

**初始化新的 Gemfile**

```bundle init```

**显示已安装的 gem**

```bundle list```

**列出有更新版本可用的 gem**

```bundle outdated```

# SYNOPSIS

**bundle** _command_ [_options_] [_arguments_]

# DESCRIPTION

**bundler** 通过跟踪并安装所需的确切 gem 版本来管理 Ruby 应用的依赖。它通过 Gemfile 和 Gemfile.lock 确保开发、预发布和生产环境的一致性。

自 Ruby 2.6 起，Bundler 已成为 Ruby 标准库的一部分。

# COMMANDS

**install**
> 安装 Gemfile 中指定的 gem

**update**
> 在约束范围内将 gem 更新到最新版本

**exec**
> 在 bundle 上下文中执行命令

**add**
> 将 gem 添加到 Gemfile 并安装

**remove**
> 从 Gemfile 中移除 gem

**init**
> 生成一个简单的 Gemfile

**list**
> 显示所有已安装的 gem

**show**
> 显示 gem 的安装位置

**check**
> 验证所有依赖是否已安装

**clean**
> 移除未使用的 gem

**doctor**
> 显示常见问题的警告信息

**gem**
> 创建一个简单的 gem 骨架

**platform**
> 显示平台兼容性信息

# PARAMETERS

**--no-color**
> 禁用彩色输出

**--verbose**
> 启用详细输出

**--path** _directory_
> 将 gem 安装到指定目录

**--without** _groups_
> 安装时排除指定的 gem 分组

**--deployment**
> 以部署模式安装

# CONFIGURATION

**Gemfile**
> 指定项目的 Ruby gem 依赖。位于项目根目录。

**.bundle/config**
> 每个项目的 Bundler 配置，包括安装路径、排除的分组以及部署设置。也会读取 ~/.bundle/config 作为全局默认值。

# CAVEATS

运行 gem 可执行文件时应始终使用 **bundle exec**，以确保版本正确。Gemfile.lock 应提交到版本控制。不带参数运行 bundle update 可能引入破坏性变更。

# INSTALL

```pacman: sudo pacman -S ruby-bundler```

```apk: sudo apk add ruby-bundler```

```nix: nix profile install nixpkgs#bundler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gem](/man/gem)(1), [ruby](/man/ruby)(1), [rake](/man/rake)(1)

# RESOURCES

```[Source code](https://github.com/rubygems/rubygems)```

```[Homepage](https://bundler.io)```

<!-- verified: 2026-06-22 -->
