# TAGLINE

显示 Poetry 的调试信息

# TLDR

**显示 Poetry 和环境信息**

```poetry debug info```

**调试依赖解析**

```poetry debug resolve```

**解析特定软件包**

```poetry debug resolve [package_name]```

# SYNOPSIS

**poetry debug** _command_ [_options_]

# PARAMETERS

**info**
> 显示 Poetry 版本、Python 版本、系统平台和虚拟环境详情。

**resolve** [_package_]
> 以详细模式运行依赖解析器。可选指定软件包名以仅解析该依赖。

# DESCRIPTION

**poetry debug** 提供用于排查 Poetry 问题的诊断信息。**info** 子命令显示 Poetry 版本、Python 版本、系统平台和虚拟环境详情。

**resolve** 子命令以调试模式执行依赖解析，展示求解器的决策过程。这有助于诊断版本冲突，或理解为何选中了特定版本的软件包。

# CAVEATS

必须在包含 **pyproject.toml** 文件的目录中运行。依赖较多的项目中 **resolve** 子命令可能耗时较长。

# HISTORY

**debug** 子命令作为 Poetry 内置诊断工具的一部分添加，帮助用户和维护者排查环境与解析问题。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-check](/man/poetry-check)(1), [poetry-env](/man/poetry-env)(1), [poetry-show](/man/poetry-show)(1)
