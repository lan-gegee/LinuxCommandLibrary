# TAGLINE

轻量级的 Ruby 版本切换器

# TLDR

**列出可用的 Ruby 版本**

```chruby```

**切换到指定的 Ruby 版本**

```chruby ruby-3.2.0```

**切换到系统 Ruby**

```chruby system```

**显示当前 Ruby 版本**

```chruby | grep '\*'```

# SYNOPSIS

**chruby** [_ruby_version_ | system]

# DESCRIPTION

**chruby** 通过修改 PATH 和相关环境变量在多个 Ruby 版本之间切换。它是 RVM 和 rbenv 的轻量级替代品，仅有 90 行 Shell 脚本。

支持由 ruby-install 安装的 Ruby 或从源码构建的 Ruby。

# SETUP

添加到 ~/.bashrc 或 ~/.zshrc：

```bash
source /usr/local/share/chruby/chruby.sh
```

若需自动切换：

```bash
source /usr/local/share/chruby/auto.sh
```

# AUTO-SWITCHING

加载 auto.sh 后，chruby 会读取 .ruby-version 文件：

```bash
echo "ruby-3.2.0" > .ruby-version
```

会自动检查当前目录及父目录。

# DEFAULT VERSION

在 ~/.bashrc 或 ~/.zshrc 中设置：

```bash
chruby ruby-3.2.0
```

# ENVIRONMENT

**RUBIES**
> Ruby 安装路径数组

**RUBY_ROOT**
> 当前 Ruby 的安装路径

**GEM_HOME** / **GEM_PATH**
> Gem 目录

# CAVEATS

只负责切换版本——请使用 ruby-install 来安装 Ruby。不会覆盖 cd 命令（使用 pre-prompt 钩子）。

# INSTALL

```brew: brew install chruby```

```nix: nix profile install nixpkgs#chruby```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rbenv](/man/rbenv)(1), [rvm](/man/rvm)(1)
