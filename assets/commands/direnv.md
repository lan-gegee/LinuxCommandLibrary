# TAGLINE

按目录管理的环境变量切换器

# TLDR

**在 Shell 中启用 direnv**（加入 Shell 配置）

```eval "$(direnv hook bash)"```

**创建新的 .envrc 文件**

```direnv edit .```

**允许**当前目录的 .envrc

```direnv allow```

**拒绝/撤销**某个 .envrc

```direnv deny```

**重新加载当前环境**

```direnv reload```

将当前环境**导出为 Shell 命令**

```direnv export bash```

**显示环境差异**，用于切换目录时

```direnv status```

**打印当前正在使用的 .envrc**

```direnv show```

# SYNOPSIS

**direnv** [_command_] [_arguments_]

# PARAMETERS

**allow** [_path_]
> 批准加载某个 .envrc 文件。这是一项安全措施，防止执行任意代码。

**deny** [_path_]
> 撤销对某个 .envrc 文件的批准。

**edit** [_path_]
> 在 $EDITOR 中打开 .envrc，编辑完成后自动批准。

**reload**
> 手动重新加载当前目录的环境。

**status**
> 显示 direnv 的当前状态和生效的 .envrc。

**export** _shell_
> 为指定的 Shell（bash、zsh、fish 等）导出当前环境。

**hook** _shell_
> 打印用于启用 direnv 的 Shell 钩子代码。

**show**
> 显示当前已加载的 .envrc 文件。

**version**
> 打印 direnv 版本。

**prune**
> 清理旧的已批准文件条目。

**fetchurl** _url_ [_integrity_]
> 获取 URL，带缓存和可选的完整性校验。

**stdlib**
> 打印 .envrc 中可用的标准库函数。

# CONFIGURATION

**.envrc**
> 按目录生效的环境配置脚本，进入该目录时被加载。

**~/.config/direnv/direnv.toml**
> direnv 的全局配置，用于白名单和各项设置。

**~/.config/direnv/direnvrc**
> 全局共享的函数与设置，对所有 .envrc 文件可用。

# DESCRIPTION

**direnv** 是一个环境切换器，根据当前目录加载和卸载环境变量。当你进入包含 **.envrc** 文件的目录时，direnv 会自动将其变量导出到你的 Shell 中；离开时则卸载它们。

.envrc 文件是一个 bash 脚本，通常用 **export** 设置环境变量。Direnv 提供了一个标准库函数集，涵盖设置 PATH、加载 .env 文件、使用 nix-shell 或激活 Python 虚拟环境等常见任务。

出于安全考虑，.envrc 文件必须先被显式批准才会执行。这可以防止进入不可信目录时运行恶意代码。**allow** 命令基于文件内容哈希将文件列入白名单；任何更改都需要重新批准。

集成需要在你的配置中添加一个 Shell 钩子（例如 **~/.bashrc**）。该钩子会修改提示符以显示 direnv 是否激活，并处理自动加载/卸载。Direnv 支持 bash、zsh、fish、tcsh、elvish 等多种 Shell。

常见用例包括项目专属的环境变量、自动激活虚拟环境以及开发环境配置。

# CAVEATS

必须将 Shell 钩子添加到配置中才能自动运行。.envrc 文件必须被显式批准（安全特性）。对 .envrc 的修改需要重新批准。某些 Shell 特性在 .envrc 中的表现可能不完全相同。大型环境在切换目录时可能略有延迟。

# HISTORY

**direnv** 由 Jonas Pfenniger（zimbatm）于 **2013** 年前后创建，用于解决管理按项目环境配置的问题。其灵感来自在不手动 source 文件的情况下切换不同开发环境的需求。该工具在 DevOps 和开发者社区中广受欢迎，尤其是配合 nix 集成使用时。

# INSTALL

```apt: sudo apt install direnv```

```dnf: sudo dnf install direnv```

```pacman: sudo pacman -S direnv```

```apk: sudo apk add direnv```

```zypper: sudo zypper install direnv```

```brew: brew install direnv```

```nix: nix profile install nixpkgs#direnv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[env](/man/env)(1), [export](/man/export)(1), [nix-shell](/man/nix-shell)(1), [virtualenv](/man/virtualenv)(1)
