# TAGLINE

/etc 目录的版本控制

# TLDR

在 /etc 中**初始化** Git 仓库

```sudo etckeeper init```

**提交** /etc 中的所有更改

```sudo etckeeper commit [message]```

运行**任意 Git** 命令

```sudo etckeeper vcs [status]```

**检查**是否存在未提交的更改

```sudo etckeeper unclean```

**停止跟踪**并销毁仓库

```sudo etckeeper uninit```

# SYNOPSIS

**etckeeper** _command_ [_arguments_]

# DESCRIPTION

**etckeeper** 使用版本控制（Git、Mercurial、Bazaar 或 Darcs）跟踪 /etc 中的系统配置文件。它与 apt、yum、pacman、dnf 等软件包管理器无缝集成，在软件包操作前后自动提交更改。

这提供了所有系统配置修改的审计轨迹，让你可以审查何时改了什么、弄清系统为何在更新后行为不同，并回退有问题的更改。该工具还会保留 Git 通常不跟踪的文件权限和元数据。

etckeeper 对于管理多台服务器的系统管理员、排查配置问题以及维护合规文档都很有价值。

# PARAMETERS

**init**
> 在 /etc 中初始化仓库

**commit** _message_
> 提交所有更改

**vcs** _command_
> 在仓库上运行 VCS 命令

**unclean**
> 检查未提交的更改

**uninit**
> 移除仓库

**pre-install**
> 在安装软件包之前运行

**post-install**
> 在安装软件包之后运行

# CONFIGURATION

**/etc/etckeeper/etckeeper.conf**
> 主配置文件，指定要使用的 VCS、要启用的软件包管理器钩子以及要忽略的文件。

# CAVEATS

需要 root 权限。init 必须在 /etc 目录下运行。与 apt、yum、pacman 集成。敏感文件可能需要添加 gitignore 条目。

# INSTALL

```dnf: sudo dnf install etckeeper```

```pacman: sudo pacman -S etckeeper```

```apk: sudo apk add etckeeper```

```zypper: sudo zypper install etckeeper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [cron](/man/cron)(8)

# RESOURCES

```[Source code](https://git.joeyh.name/index.cgi/etckeeper.git/)```

```[Homepage](https://etckeeper.branchable.com/)```

<!-- verified: 2026-07-15 -->
