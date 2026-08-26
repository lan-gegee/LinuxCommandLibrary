# TAGLINE

轻量级 Zsh 插件管理器

# TLDR

**加载 Oh My Zsh**

```zgen oh-my-zsh```

**加载 Oh My Zsh 插件**

```zgen oh-my-zsh plugins/[git]```

**从 GitHub 加载插件**

```zgen load [zsh-users/zsh-autosuggestions]```

**加载主题**

```zgen oh-my-zsh themes/[robbyrussell]```

**保存配置并生成 init 脚本**

```zgen save```

**更新所有插件**

```zgen update```

**重置并重新生成**

```zgen reset```

# SYNOPSIS

**zgen** _command_ [_arguments_]

# SUBCOMMANDS

**oh-my-zsh** [_plugin_or_theme_]
> 加载 Oh My Zsh 或特定组件

**load** _repo_ [_file_]
> 从 GitHub 仓库加载插件

**save**
> 将当前配置保存到 init 脚本

**update**
> 更新所有插件

**reset**
> 删除生成的 init 脚本（下次加载时重新生成）

**list**
> 列出已加载的插件

**selfupdate**
> 更新 zgen 本身

**clone** _repo_
> 仅克隆仓库而不加载

# DESCRIPTION

**zgen** 是一个轻量级的 Zsh 插件管理器。它会根据你的插件配置生成静态的 init 脚本，使 Shell 启动更快，因为插件无需每次都动态加载。

典型工作流程：
1. 在 **.zshrc** 中用 zgen 命令定义插件
2. 运行 **zgen save** 生成 init 脚本
3. 之后的 Shell 启动直接加载预生成的脚本

zgen 支持 Oh My Zsh、Prezto 以及任何托管在 GitHub 上的 Zsh 插件。它负责克隆仓库并加载相应的文件。

.zshrc 中的配置示例：
```
source "${HOME}/.zgen/zgen.zsh"
if ! zgen saved; then
  zgen oh-my-zsh
  zgen oh-my-zsh plugins/git
  zgen load zsh-users/zsh-syntax-highlighting
  zgen save
fi
```

# CAVEATS

修改 .zshrc 中的插件后，运行 **zgen reset** 并重启 Shell 以重新生成 init 脚本。

zgen 的开发不太活跃。可以考虑 **zinit** 或 **sheldon** 等维护活跃的替代品。

插件更新需要手动运行 **zgen update**。没有自动更新机制。

# SEE ALSO

[zsh](/man/zsh)(1), [zplug](/man/zplug)(1), [antigen](/man/antigen)(1)
