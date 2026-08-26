# TAGLINE

Oh My Zsh 管理 CLI

# TLDR

**更新 Oh My Zsh**

```omz update```

**列出所有可用插件**

```omz plugin list```

**启用插件**

```omz plugin enable [plugin_name]```

**禁用插件**

```omz plugin disable [plugin_name]```

**列出可用主题**

```omz theme list```

**设置主题**

```omz theme set [theme_name]```

**显示当前主题**

```omz theme use [theme_name]```

**显示更新日志**

```omz changelog```

**重新加载 Zsh 配置**

```omz reload```

# SYNOPSIS

**omz** _command_ [_subcommand_] [_args_]

# PARAMETERS

**update**
> 将 Oh My Zsh 更新到最新版本。

**plugin list**
> 列出所有可用插件。

**plugin enable** _NAME_
> 通过将插件添加到 .zshrc 的 plugins 数组来启用它。

**plugin disable** _NAME_
> 通过从 .zshrc 的 plugins 数组中移除来禁用插件。

**plugin info** _NAME_
> 显示某个插件的信息。

**theme list**
> 列出所有可用主题。

**theme set** _NAME_
> 在 .zshrc 中设置主题。

**theme use** _NAME_
> 仅为当前会话临时加载主题。

**changelog**
> 显示近期变更和发布说明。

**reload**
> 以更新后的配置重新加载当前 Zsh 会话。

**--help**
> 显示帮助信息。

# DESCRIPTION

**omz** 是 Oh My Zsh 框架的命令行管理工具。它提供更新框架、管理插件与主题以及重新加载配置的命令。对插件和主题的更改通过修改 `.zshrc` 文件持久保存。

# CAVEATS

需要已安装 Oh My Zsh。仅适用于 Zsh Shell。插件/主题更改会直接修改 ~/.zshrc。`theme use` 命令只对当前会话生效；要持久化请使用 `theme set`。

# SEE ALSO

[zsh](/man/zsh)(1), [oh-my-zsh](/man/oh-my-zsh)(1)
