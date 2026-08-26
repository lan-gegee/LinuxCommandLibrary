# TAGLINE

基于 Nix 的声明式开发环境

# TLDR

**初始化新项目**

```devenv init```

**进入开发 shell**

```devenv shell```

**启动后台进程**（数据库、服务器等）

```devenv up```

**以分离方式在后台启动进程**

```devenv processes up```

**在该环境中运行命令**

```devenv shell -- [command]```

**在 nixpkgs 中搜索软件包**

```devenv search [package_name]```

**更新 inputs 和 lockfile**

```devenv update```

**运行项目测试**

```devenv test```

# SYNOPSIS

**devenv** _command_ [_options_]

# SUBCOMMANDS

**init**
> 初始化一个新的 devenv 项目。

**shell**
> 进入开发 shell。

**up**
> 启动后台进程。

**processes up**
> 在后台启动进程。

**processes down**
> 停止后台进程。

**update**
> 更新 devenv 的 inputs 和 lockfile。

**search** _name_
> 在 nixpkgs 中搜索软件包。

**test**
> 运行 devenv.nix 中定义的项目测试。

**container**
> 构建、复制或运行容器。

**build**
> 构建 devenv.nix 中的任意属性。

**gc**
> 垃圾回收旧的 shell 代际。

**info**
> 显示环境信息。

**repl**
> 启动交互式 REPL 以检查配置。

# DESCRIPTION

**devenv** 是构建于 Nix 之上的开发环境管理工具。它提供声明式、可复现的开发环境，并自动管理依赖。

配置定义在 devenv.nix 中，声明软件包、服务、环境变量和脚本。devenv 通过友好的 API 以及数据库、语言运行时、开发工具等预配置服务，简化了 Nix 在开发环境上的使用。

该工具支持在后台运行服务，配合 direnv 集成实现自动激活环境，并借助 Nix 的可复现性保证实现确定性构建。

# CONFIGURATION

**devenv.nix**
> 主配置文件，定义软件包、语言、服务、环境变量、脚本和 shell 钩子。

**devenv.yaml**
> Nix inputs 配置（nixpkgs 版本、额外的 flake）以及项目导入。

**devenv.lock**
> 锁定文件，固定各 input 的确切版本以保证可复现性。

# CAVEATS

需要已安装 Nix。首次设置可能需要时间下载依赖。Nix store 可能占用大量磁盘空间。部分专有软件可能没有对应的 Nix 软件包。

# INSTALL

```nix: nix profile install nixpkgs#devenv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-shell](/man/nix-shell)(1), [direnv](/man/direnv)(1)
