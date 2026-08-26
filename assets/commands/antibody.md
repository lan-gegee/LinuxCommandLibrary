# TAGLINE

快速的 Zsh 插件管理器

# TLDR

**打包加载**插件

```antibody bundle < [plugins.txt]```

打包加载**单个插件**

```antibody bundle [zsh-users/zsh-autosuggestions]```

**更新**所有插件

```antibody update```

**列出**已安装插件

```antibody list```

在 zshrc 中**初始化**

```source <(antibody init)```

# SYNOPSIS

**antibody** _command_ [_options_]

# DESCRIPTION

**antibody** 是一个用 Go 编写的快速 Shell 插件管理器。它从 GitHub 或其他来源下载并加载 Zsh 插件，类似 Antigen 但性能更快。

插件在一个文本文件中指定，每行一个仓库。Antibody 将它们打包成可在 .zshrc 中 source 的 Shell 代码。

> **antibody 已被弃用。** 不再添加新功能或修复缺陷。维护者推荐使用 **antidote** 作为直接替代品。

# PARAMETERS

**bundle** [_plugin_]
> 下载插件并打印其 source 加载命令

**update**
> 更新所有已安装插件

**list**
> 列出已安装插件

**init**
> 输出初始化代码

**purge** _plugin_
> 移除一个插件

**home**
> 打印 antibody 的主目录

# USAGE

典型的 .zshrc 配置：
```
source <(antibody init)
antibody bundle < ~/.zsh_plugins.txt
```

或者更快的启动方式：
```
antibody bundle < ~/.zsh_plugins.txt > ~/.zsh_plugins.sh
source ~/.zsh_plugins.sh
```

# CAVEATS

插件更新需要手动运行 antibody update；不会自动更新。静态加载（使用生成的文件）速度更快，但更改后需要重新生成。

# HISTORY

**antibody** 由 **Carlos Alexandro Becker** 创建，作为流行的 Zsh 插件管理器 Antigen 的更快替代品，利用 Go 语言提升了性能。该项目后来已被弃用，由 mattmc3 用 Zsh 重写的 **antidote** 取代。

# INSTALL

```aur: yay -S antibody```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[zsh](/man/zsh)(1), [antigen](/man/antigen)(1), [zinit](/man/zinit)(1)

# RESOURCES

```[Source code](https://github.com/getantibody/antibody)```

```[Homepage](https://getantibody.github.io/)```

<!-- verified: 2026-06-11 -->
