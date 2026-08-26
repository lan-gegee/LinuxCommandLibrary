# TAGLINE

读取和设置仓库或全局选项

# TLDR

**设置用户名**

```git config --global user.name "[Name]"```

**设置用户邮箱**

```git config --global user.email "[email@example.com]"```

**获取一个值**

```git config user.name```

**为新仓库设置默认分支名**

```git config --global init.defaultBranch main```

**创建命令别名**

```git config --global alias.co checkout```

**移除一项设置**

```git config --global --unset [key]```

**列出所有设置**及其来源

```git config --list --show-origin```

**编辑配置文件**

```git config --global --edit```

# SYNOPSIS

**git config** [_options_] _name_ [_value_]

# PARAMETERS

_NAME_
> 配置键。

_VALUE_
> 要设置的值。

**--global**
> 用户级配置（~/.gitconfig）。

**--local**
> 仓库配置（.git/config）。

**--system**
> 系统级配置。

**--list**, **-l**
> 列出所有变量。

**--edit**, **-e**
> 在编辑器中打开配置。

**--get** _NAME_
> 获取给定键的值（只给键名时的默认行为）。

**--get-all** _NAME_
> 获取多值键的所有值。

**--unset** _NAME_
> 移除一项设置。

**--show-origin**
> 显示每个配置值来自哪个文件。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git config** 管理 Git 配置变量，这些变量控制着 Git 行为的方方面面，从用户身份和提交设置到合并策略、凭据助手和性能调优等高级选项。配置以 INI 风格的文本文件存储在三个层级中。

系统级配置（/etc/gitconfig）作用于系统上的所有用户，修改需要管理员权限。全局配置（~/.gitconfig 或 ~/.config/git/config）对当前用户的所有仓库生效。本地配置（.git/config）只对特定仓库生效。低层级设置覆盖高层级设置，从而支持项目级的定制。

常见配置任务包括：设置用户身份（user.name 和 user.email，提交所必需）、定义命令别名（alias.*）、配置合并与 diff 工具（merge.tool、diff.tool）、设置默认分支名（init.defaultBranch），以及管理凭据（credential.helper）。

# CONFIGURATION

**~/.gitconfig** 或 **~/.config/git/config**
> 全局用户级配置文件（--global）。

**.git/config**
> 仓库专属配置文件（--local）。

**/etc/gitconfig**
> 系统级配置文件（--system）。

# CAVEATS

本地设置覆盖全局设置，全局设置又覆盖系统设置。同一个键在多个层级都有设置时，作用域最具体的生效。某些设置（如 **core.autocrlf**）如果在不同层级间设置不一致，可能导致意外行为。凭据助手因平台而异，可能需要单独安装。

# HISTORY

git config 是 **Git** 自最初发布就有的核心命令，提供了控制所有 git 行为的配置系统。

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

[git](/man/git)(1), [git-credential](/man/git-credential)(1), [git-init](/man/git-init)(1), [git-commit](/man/git-commit)(1)
