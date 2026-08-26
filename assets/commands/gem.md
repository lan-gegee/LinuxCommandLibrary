# TAGLINE

Ruby 库的软件包管理器

# TLDR

**安装 gem**

```gem install [package_name]```

**安装特定版本**

```gem install [package_name] -v [1.2.3]```

**列出已安装的 gem**

```gem list```

**更新 gem**

```gem update [package_name]```

**卸载 gem**

```gem uninstall [package_name]```

# SYNOPSIS

**gem** _command_ [_options_] [_arguments_]

# PARAMETERS

_COMMAND_
> 操作：install、uninstall、list、update、search 等。

**install** _GEM_
> 安装 gem 软件包。

**uninstall** _GEM_
> 移除 gem。

**list**
> 列出已安装的 gem。

**update**
> 更新 gem。

**search** _TERM_
> 搜索 gem。

**-v** _VERSION_
> 指定版本。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.gemrc**
> 用户专属的 gem 配置，包括默认 gem 源和安装选项。

**/etc/gemrc**
> 面向所有用户的系统级 gem 配置。

# DESCRIPTION

**gem** 是 RubyGems 的命令行软件包管理器，用于安装、管理和分发 Ruby 库和应用程序。它可以访问 RubyGems.org——托管数十万个社区贡献 Ruby 软件包（称为 "gems"）的中央仓库。

该工具自动处理依赖解析，按正确顺序安装所需的 gem 及其依赖。它支持安装特定版本、更新已有的 gem，以及同时管理同一 gem 的多个版本。每个 gem 都包含指定其依赖、Ruby 版本要求和其他约束条件的元数据。

gem 可以系统级安装软件包（需要 sudo/管理员权限），也可以安装到用户专属位置。它与 bundler 集成实现项目级的依赖管理，让不同项目可以使用不同的 gem 版本而不冲突。由 bundler 管理的 Gemfile 和 Gemfile.lock 工作流已成为 Ruby 应用的标准。

除安装之外，gem 还提供搜索可用软件包、查看文档、构建和发布自己的 gem 以及管理本地 gem 缓存等命令。它是 Ruby 软件包生态的基石，也是所有 Ruby 开发者的必备工具。

自 Ruby 1.9 起，RubyGems 已成为 Ruby 标准库的一部分，因此每次安装 Ruby 都会附带 gem。

# CAVEATS

系统级 gem 可能需要 sudo。没有 bundler 时可能出现冲突。版本解析可能较为复杂。

# HISTORY

RubyGems 创建于 2004 年，旨在标准化 Ruby 库的分发。它在 Ruby 1.9 中成为 Ruby 标准库的一部分，使 gem 成为官方的 Ruby 软件包管理器。

# INSTALL

```dnf: sudo dnf install ruby```

```pacman: sudo pacman -S ruby```

```apk: sudo apk add ruby```

```zypper: sudo zypper install ruby```

```brew: brew install ruby```

```nix: nix profile install nixpkgs#ruby```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bundle](/man/bundle)(1), [ruby](/man/ruby)(1), [rvm](/man/rvm)(1)

# RESOURCES

```[Homepage](https://rubygems.org/)```

```[Documentation](https://guides.rubygems.org/command-reference/)```

```[Source code](https://github.com/rubygems/rubygems)```

<!-- verified: 2026-07-15 -->
