# TAGLINE

支持并行加载的 Zsh 插件管理器

# TLDR

**从 GitHub 加载插件**

```zplug "[user/repo]"```

**加载 Oh My Zsh 插件**

```zplug "plugins/[git]", from:oh-my-zsh```

**以命令形式加载**

```zplug "[user/repo]", as:command```

**加载主题**

```zplug "[user/repo]", as:theme```

**安装插件**

```zplug install```

**更新所有插件**

```zplug update```

**加载所有插件**

```zplug load```

# SYNOPSIS

**zplug** "_repo_" [, _tag_:_value_...]

**zplug** _command_

# TAGS

**from:**_source_
> 插件来源（github、oh-my-zsh、local 等）

**as:**_type_
> 类型：plugin、command 或 theme

**use:**_pattern_
> 指定要 source 的文件的 glob 模式

**at:**_branch/tag_
> 使用的分支、标签或提交

**rename-to:**_name_
> 重命名命令

**frozen:**_bool_
> 不更新此插件

**defer:**_level_
> 延迟加载（0-3，数值越大加载越晚）

**if:**_condition_
> 条件加载

**hook-build:**_command_
> 安装后运行的命令

# SUBCOMMANDS

**install**
> 安装尚未安装的插件

**update**
> 更新所有插件

**load**
> source 各个插件

**list**
> 列出已安装的插件

**clean**
> 移除未使用的插件

**status**
> 检查插件更新状态

**check**
> 检查插件是否已安装

# DESCRIPTION

**zplug** 是新一代 Zsh 插件管理器，具有并行安装、延迟加载和依赖管理等特点。它支持从 GitHub、Oh My Zsh、Prezto、本地文件和 gist 加载内容。

典型的 .zshrc 配置：
```
source ~/.zplug/init.zsh
zplug "zsh-users/zsh-autosuggestions"
zplug "zsh-users/zsh-syntax-highlighting", defer:2
if ! zplug check; then zplug install; fi
zplug load
```

zplug 不仅能管理 Zsh 插件，还能管理命令和二进制文件，并将它们安装到一个受管理的目录中。

# CAVEATS

zplug 的开发节奏已经放缓。可以考虑 **zinit** 或 **sheldon** 这类仍在积极维护的替代品。

首次运行时安装插件可能较慢。之后的加载会很快。

包含大量延迟加载插件的复杂配置会加大调试难度。

# INSTALL

```brew: brew install zplug```

```nix: nix profile install nixpkgs#zplug```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zsh](/man/zsh)(1), [zgen](/man/zgen)(1), [antigen](/man/antigen)(1), [zinit](/man/zinit)(1)
