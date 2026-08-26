# TAGLINE

Elixir 版本管理器

# TLDR

**列出已安装的版本**

```exenv versions```

**列出可用的版本**

```exenv install --list```

**安装某个版本**

```exenv install [1.14.0]```

**设置全局版本**

```exenv global [1.14.0]```

**设置本地版本**

```exenv local [1.14.0]```

**显示当前版本**

```exenv version```

**重建 shims**

```exenv rehash```

# SYNOPSIS

**exenv** _command_ [_args_]

# SUBCOMMANDS

**versions**
> 列出已安装的版本。

**version**
> 显示当前版本。

**install**
> 安装某个版本。

**uninstall**
> 卸载某个版本。

**global**
> 设置全局版本。

**local**
> 设置目录级版本。

**shell**
> 设置 Shell 级版本。

**rehash**
> 重建 exenv shims。

**which**
> 显示可执行文件的路径。

# DESCRIPTION

**exenv** 管理多个 Elixir 版本，支持按项目或全局切换版本。与 Ruby 的 rbenv 类似。

# CONFIGURATION

**~/.exenv/version**
> 全局默认的 Elixir 版本。

**.exenv-version**
> 目录级 Elixir 版本文件，由 `exenv local` 写入。

# SEE ALSO

[elixir](/man/elixir)(1), [mix](/man/mix)(1), [rbenv](/man/rbenv)(1)

# RESOURCES

```[Source code](https://github.com/mururu/exenv)```

<!-- verified: 2026-07-15 -->
