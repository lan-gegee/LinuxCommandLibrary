# TAGLINE

嵌入 git 的分布式缺陷跟踪器

# TLDR

**添加新缺陷**

```git bug add```

**列出缺陷**

```git bug ls```

**显示缺陷详情**

```git bug show [bug-id]```

**添加评论**

```git bug comment [bug-id]```

**将缺陷推送到远程**

```git bug push```

**启动 Web 界面**

```git bug webui```

**打开交互式终端界面**

```git bug termui```

# SYNOPSIS

**git bug** _command_ [_options_]

# PARAMETERS

**add** [**-t** _title_] [**-m** _message_]
> 创建新缺陷。

**ls**, **list**
> 列出缺陷。

**show** _ID_
> 显示缺陷详情。

**comment** _ID_
> 为缺陷添加评论。

**label** _ID_ _label_
> 为缺陷添加或移除标签。

**status** _ID_
> 显示或更改缺陷的状态（打开/关闭）。

**push** [_remote_]
> 将缺陷推送到 git 远程。

**pull** [_remote_]
> 从 git 远程拉取缺陷。

**close** _ID_
> 将缺陷标记为已关闭。

**open** _ID_
> 重新打开已关闭的缺陷。

**user**
> 列出、创建或采用身份。

**webui**
> 启动 Web 用户界面。

**termui**
> 启动终端用户界面。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git-bug** 是一个嵌入 git 的分布式缺陷跟踪器。缺陷以 git 对象的形式存储，从而支持离线缺陷管理、分布式同步以及与 git 工作流的集成。

该工具提供完整的 issue 跟踪能力，包括标题、描述、评论、标签和状态。缺陷可通过 git push/pull 同步，无需依赖 GitHub Issues 或 Jira 等外部服务即可实现去中心化的 issue 管理。

缺陷以 git 对象形式存储，可完全离线管理，并通过标准 git push 和 pull 操作与协作者同步。

# CAVEATS

与 GitHub/GitLab 的 issue 相互独立。需要协作者机器上也进行安装配置。Web 界面需单独启动。

# HISTORY

git-bug 由 **Michael Muré** 创建，旨在提供真正分布式的缺陷跟踪，使缺陷与代码一同保存在 git 仓库中。

# INSTALL

```pacman: sudo pacman -S git-bug```

```zypper: sudo zypper install git-bug```

```brew: brew install git-bug```

```nix: nix profile install nixpkgs#git-bug```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [gh](/man/gh)(1)
