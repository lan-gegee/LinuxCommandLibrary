# TAGLINE

管理 GitLab CLI 的命令别名

# TLDR

**列出别名**

```glab alias list```

**设置别名**

```glab alias set [name] "[command]"```

**删除别名**

```glab alias delete [name]```

设置一个通过 shell 展开的别名

```glab alias set [name] --shell "[command]"```

# SYNOPSIS

**glab** **alias** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出别名。

**set** _name_ _expansion_
> 为 glab 命令创建别名，或通过 **--shell** 为外部命令创建别名。

**delete** _name_
> 移除一个别名。

# PARAMETERS

**-s**, **--shell**
> 将别名展开内容解释为 shell 命令而非 glab 命令，允许使用管道（`|`）和重定向（`>`）。用 `$1`、`$2`、... 引用传入的参数，`$@` 表示所有参数。

# DESCRIPTION

**glab alias** 管理 GitLab CLI 的命令别名。它可以为常用的 glab 命令创建快捷方式，让常见工作流程执行得更快。

别名存储在 glab 配置文件中，可以引用任何带参数的有效 glab 命令，或者在 **--shell** 下引用任意 shell 命令。

# SEE ALSO

[glab](/man/glab)(1)

# RESOURCES

```[Documentation](https://docs.gitlab.com/cli/alias/)```

```[Source code](https://gitlab.com/gitlab-org/cli)```

<!-- verified: 2026-07-17 -->
