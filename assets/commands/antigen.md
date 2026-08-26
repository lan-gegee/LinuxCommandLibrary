# TAGLINE

受 Vundle 启发的 Zsh 插件管理器

# TLDR

**加载 oh-my-zsh** 框架

```antigen use oh-my-zsh```

**安装并加载**插件 bundle

```antigen bundle [git]```

从 GitHub 仓库**加载插件**

```antigen bundle [zsh-users/zsh-autosuggestions]```

从 oh-my-zsh **加载主题**

```antigen theme [robbyrussell]```

**应用所有更改**（.zshrc 末尾必须调用）

```antigen apply```

**更新所有插件**

```antigen update```

**列出已加载的 bundle**

```antigen list```

**清除缓存**并重新加载配置

```antigen reset```

# SYNOPSIS

**antigen** _command_ [_arguments_]

# PARAMETERS

**bundle** _spec_
> 安装（如需要）并加载一个插件；接受 GitHub 简写（user/repo）或完整 URL

**bundles**
> 通过 heredoc 语法批量加载多个插件（每行一个）

**use** _framework_
> 加载预打包的框架，例如 oh-my-zsh 或 prezto

**theme** _name_
> 加载并激活一个 zsh 主题（应在 antigen use 之后调用）

**apply**
> 提交配置；必须在所有 bundle 声明之后调用

**update** [_bundle-name_]
> 更新指定的 bundle；未给出名称时更新全部

**list** [**--long**]
> 显示当前加载的 bundle；--long 显示详细信息

**revert**
> 将所有插件回滚到上一次更新之前的状态

**reset**
> 清除生成的缓存，以重新加载配置变更

**selfupdate**
> 将 Antigen 自身更新到最新版本

**cleanup**
> 移除配置中已不再加载的插件

**purge** _bundle_
> 从系统中移除指定的 bundle

**snapshot**
> 将每个 bundle 的确切提交记录到快照文件中，便于复现环境

**restore** _snapshot_
> 按快照文件中记录的版本重新安装所有 bundle

# DESCRIPTION

**Antigen** 是一款 zsh 插件管理器，灵感来自 vim 的 Vundle 和 Pathogen。它自动处理插件的安装、加载和更新，简化了 Shell 插件的管理（插件在这里称为 bundle）。

Bundle 可以从 oh-my-zsh、prezto 或任意 Git 仓库加载。典型工作流是：source antigen.zsh，用 **antigen bundle** 声明各个 bundle，可选地加载主题，最后调用 **antigen apply** 使一切生效。

示例 **.zshrc** 配置：
```
source ~/antigen.zsh
antigen use oh-my-zsh
antigen bundle git
antigen bundle zsh-users/zsh-syntax-highlighting
antigen theme robbyrussell
antigen apply
```

Antigen 会缓存编译后的配置以加快 Shell 启动。修改 bundle 声明后，使用 **antigen reset** 清除缓存并重新加载变更。

# CAVEATS

需要 zsh 4.3.11 或更高版本。oh-my-zsh 的主题可能依赖框架函数，因此应在 **antigen theme** 之前调用 **antigen use oh-my-zsh**。通过 **antigen update** 下载的更新需要新开 Shell 才会生效。

# HISTORY

Antigen 由 **Shrikant Sharat Kandula** 于 **2012 年**前后创建，旨在将 Vundle 风格的插件管理带入 zsh。它是最早流行的 zsh 插件管理器之一，推动了模块化 Shell 配置的普及。该项目目前由 GitHub 上的 zsh-users 社区持续维护。

# INSTALL

```aur: yay -S antigen```

```brew: brew install antigen```

```nix: nix profile install nixpkgs#antigen```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[oh-my-zsh](/man/oh-my-zsh)(1), [zsh](/man/zsh)(1), [zinit](/man/zinit)(1), [zplug](/man/zplug)(1)

# RESOURCES

```[Source code](https://github.com/zsh-users/antigen)```

```[Documentation](https://github.com/zsh-users/antigen/wiki)```

<!-- verified: 2026-06-11 -->
