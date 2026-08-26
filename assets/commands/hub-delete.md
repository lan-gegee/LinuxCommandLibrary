# TAGLINE

删除 GitHub 仓库

# TLDR

**删除你自己名下的仓库**

```hub delete [name]```

**删除组织仓库**

```hub delete [organization]/[name]```

**跳过确认提示**

```hub delete -y [user]/[name]```

# SYNOPSIS

**hub delete** [**-y**] [_organization_/]_name_

# PARAMETERS

[_ORGANIZATION_/]_NAME_
> GitHub 上仓库的名称，可选地以组织名作为前缀。

**-y**, **--yes**
> 跳过确认提示，立即删除仓库。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hub delete** 删除一个 GitHub 仓库。仓库名称为必填项；对于不属于当前用户的仓库，可在名称前加上组织前缀。

除非提供了 **-y**，否则该命令需要交互式确认。它会永久删除仓库，包括其中所有的 issue、pull request 和 wiki 数据。

# CAVEATS

具有破坏性且不可逆。需要进行认证，且 GitHub token 必须具有 **delete_repo** 权限范围。还要求对目标仓库拥有所有者或管理员权限。

# HISTORY

hub delete 是 **hub** 的组成部分。hub 是 GitHub 最早的仓库管理命令行工具。

# INSTALL

```apt: sudo apt install hub```

```pacman: sudo pacman -S hub```

```zypper: sudo zypper install hub```

```brew: brew install hub```

```nix: nix profile install nixpkgs#hub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hub](/man/hub)(1), [gh](/man/gh)(1), [hub-create](/man/hub-create)(1)
