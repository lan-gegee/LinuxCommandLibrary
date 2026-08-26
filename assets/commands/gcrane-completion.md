# TAGLINE

生成 Shell 自动补全脚本

# TLDR

为你使用的 **Shell** 生成自动补全脚本

```gcrane completion [shell_name]```

**禁用**补全描述

```gcrane completion [shell_name] --no-descriptions```

在**当前 Shell 会话**中加载补全（Bash/Zsh）

```source <(gcrane completion bash)```

在当前 Shell 会话中加载补全（**fish**）

```gcrane completion fish | source```

为**每个新的 Bash 会话**加载补全

```gcrane completion bash > /etc/bash_completion.d/gcrane```

为**每个新的 Zsh 会话**加载补全

```gcrane completion zsh > "${fpath[1]}/_gcrane"```

为**每个新的 fish 会话**加载补全

```gcrane completion fish > ~/.config/fish/completions/gcrane.fish```

显示**帮助**

```gcrane completion [shell_name] -h```

# SYNOPSIS

**gcrane completion** _shell_ [_options_]

# PARAMETERS

**bash**
> 生成 Bash 补全脚本

**zsh**
> 生成 Zsh 补全脚本

**fish**
> 生成 fish 补全脚本

**powershell**
> 生成 PowerShell 补全脚本

**--no-descriptions**
> 禁用补全描述

**-h**, **--help**
> 显示 completion 命令的帮助信息

# DESCRIPTION

**gcrane completion** 为 gcrane 命令行工具生成 Shell 自动补全脚本。gcrane 是一个操作容器镜像仓库的工具，属于 Google 的 go-containerregistry 项目。

补全功能为 gcrane 的命令、标志和参数提供 Tab 补全，提高命令行操作效率。生成的脚本必须按照你所使用 Shell 的补全机制进行 source 或安装。

若要永久启用补全，请将输出安装到对应 Shell 的适当位置（Bash 为 bash_completion.d，Zsh 为 fpath，fish 为 ~/.config/fish/completions）。

# CAVEATS

安装路径因系统配置而异。Zsh 要求在调用 compinit 之前补全目录已在 fpath 中。某些系统可能需要注销并重新登录才能生效。

# INSTALL

```zypper: sudo zypper install gcrane```

```nix: nix profile install nixpkgs#gcrane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcrane](/man/gcrane)(1), [gcrane-gc](/man/gcrane-gc)(1), [gcrane-ls](/man/gcrane-ls)(1), [crane](/man/crane)(1), [docker](/man/docker)(1), [podman](/man/podman)(1)
