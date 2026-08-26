# TAGLINE

管理 Bash 插件、别名和主题的框架。

# TLDR

**启用**插件

```bash-it enable plugin [git]```

**禁用**插件

```bash-it disable plugin [git]```

**启用**别名

```bash-it enable alias [git]```

**显示**可用插件

```bash-it show plugins```

**搜索**组件

```bash-it search [docker]```

**更新** Bash-it

```bash-it update```

# SYNOPSIS

**bash-it** _command_ [_type_] [_name_]

# DESCRIPTION

**bash-it** 是面向 bash 3.2+ 的社区 Bash 命令与脚本合集。它提供管理 Bash 别名、补全、插件和主题的框架，类似于 oh-my-zsh，但面向 bash。

该工具帮助以模块化方式组织并启用/禁用各种 bash 定制。

# PARAMETERS

**enable** _type_ _name_
> 启用别名、插件或补全

**disable** _type_ _name_
> 禁用别名、插件或补全

**show** _type_
> 显示可用或已启用的条目

**search** _term_
> 搜索组件

**update**
> 更新 Bash-it 框架

**reload**
> 重新加载 bash 配置。

**doctor**
> 运行诊断。

**help** _type_
> 显示已安装别名、插件或补全的帮助。

**migrate**
> 将 Bash-it 结构迁移到最新版。

**profile**
> 管理 Bash-it profile。

# COMPONENT TYPES

**aliases**
> 命令快捷方式

**plugins**
> 额外功能

**completions**
> Tab 补全脚本

**themes**
> 提示符主题

# FEATURES

- 模块化插件系统
- 主题支持
- Git 集成
- 自动补全
- 常用命令的别名
- 轻松启用/禁用

# WORKFLOW

```bash
# Enable git plugin and aliases
bash-it enable plugin git
bash-it enable alias git

# Set theme
bash-it enable theme bobby

# Show enabled plugins
bash-it show plugins

# Update
bash-it update
```

# CONFIGURATION

**~/.bash_it/**
> Bash-it 主安装目录，包含所有插件、别名、补全和主题。

**~/.bash_it/custom/**
> 用户自定义脚本、别名和插件，会自动加载。

**~/.bashrc**
> 必须 source Bash-it 的加载脚本才能激活框架。

# CAVEATS

需要手动安装和配置。启用的插件过多可能拖慢 Shell 启动。可能与现有 bash 配置冲突。插件质量参差不齐。

# HISTORY

**Bash-it** 由 Bobby Brito 于 **2010** 年前后创建，作为 oh-my-zsh 的 bash 对应品，提供模块化的 bash 定制能力。

# SEE ALSO

[bash](/man/bash)(1), [oh-my-zsh](/man/oh-my-zsh)(1)
