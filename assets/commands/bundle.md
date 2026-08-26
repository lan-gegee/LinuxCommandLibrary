# TAGLINE

Ruby 依赖管理器

# TLDR

**安装**依赖

```bundle install```

**更新** gem

```bundle update```

**在 bundle 环境中执行**命令

```bundle exec [rake test]```

**显示** gem 的位置

```bundle show [rails]```

**创建**新 gem

```bundle gem [my_gem]```

# SYNOPSIS

**bundle** _command_ [_options_]

# DESCRIPTION

**bundle**（Bundler）是 Ruby 的依赖管理器。它确保 Gemfile 中指定的确切 gem 版本被安装和加载，防止版本冲突并保证环境一致。

该工具对 Ruby 开发至关重要，自 Ruby 2.6 起随 Ruby 捆绑提供。

# PARAMETERS

**install**
> 从 Gemfile 安装 gem

**update** [_gems_]
> 更新 gem

**exec** _command_
> 在 bundle 环境中执行命令

**show** _gem_
> 显示 gem 的安装路径

**list**
> 列出已安装的 gem

**outdated**
> 显示过时的 gem

**clean**
> 移除未使用的 gem

**lock**
> 创建/更新 Gemfile.lock

**gem** _name_
> 创建新的 gem 骨架

# GEMFILE

Gemfile 用于指定依赖：
```ruby
source 'https://rubygems.org'

gem 'rails', '~> 7.0'
gem 'pg', '>= 1.0'
gem 'puma'

group :development do
  gem 'debug'
end
```

# WORKFLOW

```bash
# Install dependencies
bundle install

# Update specific gem
bundle update rails

# Run command with correct gem versions
bundle exec rails server
bundle exec rake test

# Check for outdated gems
bundle outdated

# Remove unused gems
bundle clean
```

# FEATURES

- 依赖解析
- 版本锁定（Gemfile.lock）
- 隔离的 gem 环境
- gem 分组（development、test、production）
- 本地 gem 路径覆盖
- Git 仓库形式的 gem

# CONFIGURATION

**Gemfile**
> 指定项目的 Ruby gem 依赖。位于项目根目录。

**.bundle/config**
> 每个项目的 Bundler 配置，包括安装路径、排除的分组以及部署设置。也会读取 ~/.bundle/config 作为全局默认值。

# CAVEATS

应用程序（而非 gem）应提交 Gemfile.lock。需要使用 bundle exec 才能以正确的版本运行。本地对 gem 的修改会在 bundle install 时丢失。可能与系统 gem 冲突。大型项目解析速度较慢。

# HISTORY

**Bundler** 由 Carl Lerche、Yehuda Katz 和 André Arko 在 **2009 年**前后创建，用于解决 Ruby 的依赖管理问题，并在 **2010 年**成为事实标准。

# INSTALL

```pacman: sudo pacman -S ruby-bundler```

```apk: sudo apk add ruby-bundler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gem](/man/gem)(1), [ruby](/man/ruby)(1), [rake](/man/rake)(1)

# RESOURCES

```[Source code](https://github.com/rubygems/rubygems)```

```[Homepage](https://bundler.io/)```

<!-- verified: 2026-06-22 -->
