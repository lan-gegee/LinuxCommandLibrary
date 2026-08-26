# TAGLINE

自动化 tmux 会话配置

# TLDR

**启动项目**

```tmuxinator start [project]```

**创建新项目**

```tmuxinator new [project]```

**编辑项目**

```tmuxinator edit [project]```

**列出项目**

```tmuxinator list```

**删除项目**

```tmuxinator delete [project]```

**复制项目**

```tmuxinator copy [existing] [new_name]```

**停止项目**

```tmuxinator stop [project]```

**显示项目配置**

```tmuxinator debug [project]```

# SYNOPSIS

**tmuxinator** [_start_] [_new_] [_edit_] [_list_] [_delete_] [_options_] [_project_]

# PARAMETERS

**start** _PROJECT_
> 启动项目会话。

**new** _PROJECT_
> 创建新项目。

**edit** _PROJECT_
> 编辑项目配置。

**open** _PROJECT_
> edit 的别名。

**list**, **ls**
> 列出项目。

**delete** _PROJECT_
> 删除项目。

**stop** _PROJECT_
> 终止项目会话。

**copy** _SRC_ _DEST_
> 复制项目。

**debug** _PROJECT_
> 显示生成的脚本。

**doctor**
> 检查配置。

**version**
> 显示版本。

**-p** _FILE_
> 使用指定的项目文件。

**-n** _NAME_
> 覆盖会话名称。

# DESCRIPTION

**tmuxinator** 自动化 tmux 会话的搭建。项目文件定义窗口、窗格和命令，一条命令即可全部启动。

YAML 配置描述会话布局。窗口具有名称、工作目录和窗格配置。

窗格打开时命令自动运行。开发服务器、编辑器和监控工具会在各自指定的位置启动。

布局预设处理常见的窗格排列。自定义布局可指定精确的窗格尺寸。

项目文件位于 ~/.config/tmuxinator。它们可在机器之间移植，也可以纳入版本控制。

启动项目会创建或连接 tmux 会话。后续启动直接附加而不会重建。

# CONFIGURATION

**~/.config/tmuxinator/*.yml**
> YAML 格式的项目配置文件，定义会话布局、窗口、窗格和启动命令。

# CAVEATS

需要 Ruby。复杂布局需要仔细配置。某些 tmux 版本可能存在兼容性问题。

# HISTORY

**Tmuxinator** 创建于 **2010 年**前后，用于自动化 tmux 会话创建。它已成为管理开发环境配置的标准工具。

# INSTALL

```apk: sudo apk add tmuxinator```

```brew: brew install tmuxinator```

```nix: nix profile install nixpkgs#tmuxinator```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tmux](/man/tmux)(1), [screen](/man/screen)(1), [byobu](/man/byobu)(1)
