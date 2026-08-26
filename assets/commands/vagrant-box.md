# TAGLINE

管理 Vagrant 基础 box 镜像

# TLDR

**列出 box**

```vagrant box list```

**添加 box**

```vagrant box add [name]```

**移除 box**

```vagrant box remove [name]```

**更新 box**

```vagrant box update```

**清理旧版本**

```vagrant box prune```

# SYNOPSIS

**vagrant** **box** _command_ [_options_]

# PARAMETERS

**list**
> 列出已安装的 box。

**add** _name_
> 下载并添加 box。

**remove** _name_
> 移除 box。

**update**
> 更新 box。

**prune**
> 移除旧版本的 box。

**outdated**
> 检查更新。

**--provider** _name_
> 指定提供者。

**--box-version** _version_
> 指定版本。

# DESCRIPTION

**vagrant box** 管理 Vagrant box。box 是用于创建虚拟机的基础镜像。可以从 Vagrant Cloud 下载或从本地文件导入。

# INSTALL

```apt: sudo apt install vagrant```

```dnf: sudo dnf install vagrant```

```nix: nix profile install nixpkgs#vagrant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-init](/man/vagrant-init)(1)
