# TAGLINE

支持 Turbo 模式的快速 Zsh 插件管理器

# TLDR

**从 GitHub 加载插件**

```zinit light [username/repository]```

**以报告模式加载插件**（较慢但提供信息）

```zinit load [username/repository]```

**安装并加载 Oh-My-Zsh 插件**

```zinit snippet OMZ::plugins/[plugin]/[plugin].plugin.zsh```

**以 Turbo 模式加载**（异步、延迟加载）

```zinit ice wait lucid; zinit light [username/repository]```

**从仓库加载补全**

```zinit ice as"completion"; zinit snippet [url]```

**更新所有插件**

```zinit update --all```

**更新特定插件**

```zinit update [username/repository]```

**列出已安装的插件**

```zinit list```

# SYNOPSIS

**zinit** [_light_|_load_|_snippet_|_ice_|_update_|_delete_|_list_|_self-update_|_compile_|_uncompile_|_report_] [_arguments_]

# PARAMETERS

**light** _plugin_
> 以 light 模式加载插件，不进行跟踪/报告（快速）。

**load** _plugin_
> 以完整跟踪和报告方式加载插件。

**snippet** _url_
> 从 URL 或 Oh-My-Zsh/Prezto 加载单个文件或片段。

**ice** _modifiers..._
> 为下一条 zinit 命令设置修饰符（compile、wait、pick 等）。

**update** [_plugin_|_--all_]
> 更新指定插件或所有插件。

**delete** _plugin_
> 移除插件。

**list**
> 列出所有已加载的插件。

**loaded**
> 显示当前已加载的插件。

**self-update**
> 更新 zinit 本身。

**compile** _plugin_
> 编译插件脚本以加快加载速度。

**uncompile** _plugin_
> 移除编译后的文件。

**report** _plugin_
> 显示某个已加载插件的报告。

**times**
> 显示各插件的加载耗时。

# ICE MODIFIERS

**wait**
> Turbo 模式：延迟加载（可指定时间，如 wait"1"）。

**lucid**
> 跳过 "Loaded plugin" 消息。

**as"program"**
> 将插件目录加入 PATH。

**as"completion"**
> 作为补全脚本加载。

**pick"file"**
> 选择要 source 的特定文件。

**from"gitlab"**
> 从 GitLab 而非 GitHub 克隆。

**depth"1"**
> 深度为 1 的浅克隆。

**atload"command"**
> 加载后运行命令。

**atinit"command"**
> 加载前运行命令。

# DESCRIPTION

**Zinit**（原名 Zplugin）是一个灵活且快速的 Zsh 插件管理器，支持 Oh-My-Zsh 和 Prezto 插件、用于延迟加载的 Turbo 模式以及多种安装方式。它将插件编译为字节码以加快 Shell 启动速度。

其关键特性是 Turbo 模式，它在 Zsh 启动后异步加载插件，显著缩短 Shell 初始化时间。Ice 修饰符提供了对插件下载、编译和加载方式的细粒度控制。

Zinit 支持从 GitHub、GitLab、Bitbucket 或任意 URL 加载。它可以处理插件、补全、脚本和二进制程序。**light** 命令提供无跟踪的快速加载，而 **load** 则启用完整的报告功能。

配置通常放在 **.zshrc** 中 source zinit 之后的位置。插件默认存储在 **~/.zinit/plugins/**，编译版本会被缓存以提升性能。

# CAVEATS

需要 Zsh 5.1 或更高版本。Turbo 模式可能在相互依赖的插件之间造成竞争条件。某些 Oh-My-Zsh 插件需要特定的 OMZ 基础设施才能正常工作。大量使用 ice 修饰符会使配置复杂且难以调试。

# HISTORY

Zinit 由 Sebastian Gniazdowski 创建，最初于 **2016 年**以 **Zplugin** 的名称发布。2019 年更名为 Zinit 以避免与其他工具混淆。该项目开创了 Zsh 中异步插件加载的 Turbo 模式。原始仓库于 2021 年归档，社区分支在 **zdharma-continuum/zinit** 下继续维护。

# INSTALL

```brew: brew install zinit```

```nix: nix profile install nixpkgs#zinit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zsh](/man/zsh)(1), [oh-my-zsh](/man/oh-my-zsh)(1), [antibody](/man/antibody)(1), [zplug](/man/zplug)(1), [antigen](/man/antigen)(1)
