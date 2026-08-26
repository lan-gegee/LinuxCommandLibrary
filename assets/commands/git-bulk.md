# TAGLINE

跨多个仓库执行 Git 命令

# TLDR

**对所有已注册的工作区运行 git 命令**

```git bulk -a [git-command]```

**从目录添加工作区**

```git bulk --addworkspace [name] [path]```

**将当前目录添加为工作区**

```git bulk --addcurrent [name]```

**列出所有已注册的工作区**

```git bulk --listall```

**对特定工作区运行命令**

```git bulk -w [name] [git-command]```

**在每个仓库前弹出确认提示再运行**

```git bulk -g -a [git-command]```

# SYNOPSIS

**git** **bulk** [_options_] [_git-command_]

# PARAMETERS

**-a**
> 对所有已注册工作区及其中的仓库运行 git 命令。

**-w** _name_
> 对指定工作区运行 git 命令。

**-g**
> 保护模式：在每个仓库上执行前先请求确认。

**--addworkspace** _name_ _path_
> 以逻辑名称和根目录路径注册一个工作区。根目录下的所有仓库都会被纳入。可选地使用 **--from** _url-or-file_ 直接将仓库克隆进工作区。

**--removeworkspace** _name_
> 移除指定名称的已注册工作区。

**--addcurrent** _name_
> 将当前目录添加为工作区。

**--purge**
> 移除所有已定义的仓库位置。

**--listall**
> 列出所有已注册的工作区及其路径。

# DESCRIPTION

**git bulk** 是一个 git-extras 工具，可以在多个仓库上同时执行 Git 命令。它管理工作区（workspace），即可以按项目、团队或任意逻辑分组组织的仓库路径集合。

该工具免去了手动进入每个仓库重复执行相同命令的麻烦。状态检查、分支更新或拉取等操作可以在一次调用中作用于数十个仓库。

工作区保存在配置中，只需定义一次仓库分组即可反复使用。对于管理微服务、类 monorepo 架构或多个客户项目的开发者而言，同步操作十分常见，这一点尤其宝贵。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-extras](/man/git-extras)(1)
