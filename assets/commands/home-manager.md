# TAGLINE

基于 Nix 的工具，以声明式方式管理用户环境配置

# TLDR

**从默认位置应用 home 配置**

```home-manager switch```

**应用指定的 flake 配置**

```home-manager switch --flake [.#username]```

**初始化**新的基于 flake 的配置

```home-manager init```

**初始化并立即激活**配置

```home-manager init --switch```

**只构建而不激活**

```home-manager build```

**列出各代配置**（配置历史）

```home-manager generations```

**回滚到上一代配置**

```home-manager rollback```

**删除旧代配置**

```home-manager expire-generations "[30 days ago]"```

**编辑配置文件**

```home-manager edit```

**列出已安装的软件包**

```home-manager packages```

# SYNOPSIS

**home-manager** [_options_] _command_ [_args_]

# PARAMETERS

**switch**
> 构建并激活新配置。

**build**
> 构建配置但不激活。

**init** [_--switch_] [_dir_]
> 生成初始的 Home Manager 配置。使用 **--switch** 可同时激活它。

**generations**
> 列出所有配置代。

**rollback**
> 回滚到上一代配置。

**expire-generations** _period_
> 删除早于指定时期的各代配置。

**remove-generations** _IDs_
> 按 ID 删除特定的配置代。

**edit**
> 在 $EDITOR 中打开配置。

**news**
> 显示关于配置的更新公告。

**packages**
> 列出已安装的软件包。

**uninstall**
> 从用户环境中移除 Home Manager。

**option** _name_
> 显示某个配置选项的值。

**--flake** _flake-uri_
> 使用基于 flake 的配置。

**-f**, **--file** _file_
> 配置文件路径。

**-A** _attribute_
> 要从配置构建的属性。

**-b** _ext_
> 为将被覆盖的现有文件指定备份文件扩展名。

**-n**, **--dry-run**
> 显示将执行的操作但不实际执行。

**-v**, **--verbose**
> 增加详细输出。

**--show-trace**
> 显示错误的详细位置信息。

# DESCRIPTION

**home-manager** 是一个基于 Nix 的工具，用于以声明式方式管理用户环境配置。它通过 Nix 表达式处理 dotfiles、用户软件包和环境设置，实现可复现、可版本化的家目录设置。

配置使用 Nix 语言编写，通常位于 **~/.config/home-manager/home.nix**，或作为 Nix flake 的一部分。配置中声明要安装的软件包、要配置的程序、要管理的文件和要运行的服务。

许多程序都有专门的 Home Manager 模块，可自动生成配置文件。例如，配置 **programs.git** 会以正确的语法生成 ~/.gitconfig。这比手动管理 dotfiles 更易维护。

配置代（generation）提供了配置历史。每次 **switch** 都会创建一个新代，你可以回滚到任何先前的状态。这使得实验很安全——损坏的配置可以立即还原。

Home Manager 可以独立运行，也可以与 NixOS 集成。独立模式下，它独立管理用户环境。在 NixOS 上，它可以作为模块导入以实现更紧密的集成。

# CAVEATS

需要 Nix 软件包管理器。Nix 语言有学习曲线。某些程序配置可能与手动管理的 dotfiles 冲突。基于 flake 的配置需要启用实验性特性。配置代管理需要手动清理以防磁盘占用增长。

# HISTORY

**Home Manager** 由 Robert Helgesson（rycee）于 **2017 年**前后创建，目的是把 NixOS 的声明式配置方式带到用户的家目录。它填补了一个空白：让那些想要 Nix 可复现性来管理个人环境、但又不想运行 NixOS 的用户有了选择。该项目现已发展为包含数百个程序的模块。

# INSTALL

```nix: nix profile install nixpkgs#home-manager```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nix](/man/nix)(1), [nix-env](/man/nix-env)(1), [nix-build](/man/nix-build)(1), [nix-shell](/man/nix-shell)(1), [nixos-rebuild](/man/nixos-rebuild)(8), [chezmoi](/man/chezmoi)(1), [stow](/man/stow)(8)
