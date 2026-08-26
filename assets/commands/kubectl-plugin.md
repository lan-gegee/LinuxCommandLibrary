# TAGLINE

管理 kubectl 插件

# TLDR

**列出所有可用插件及其完整路径**

```kubectl plugin list```

**只列出插件二进制名称而不含路径**

```kubectl plugin list --name-only```

# SYNOPSIS

**kubectl plugin** list [**--name-only**] [_options_]

# PARAMETERS

**list**
> 列出用户 PATH 上所有可用的插件可执行文件。

**--name-only**
> 只显示每个插件的二进制名称，而不是完整路径。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**kubectl plugin** 提供与插件交互的工具。它会发现在 PATH 中以 **kubectl-** 前缀开头的插件可执行文件。例如，名为 **kubectl-foo** 的二进制文件会以 **kubectl foo** 的形式可用。

运行 **kubectl plugin list** 会遍历 PATH 中的所有目录，并按出现顺序显示匹配的可执行文件。对于任何以 **kubectl-** 开头但不可执行的文件，以及相互遮蔽的有效插件文件（不同 PATH 目录中的重名文件），都会显示警告。

插件可以通过将可执行文件放入 PATH 手动安装，也可以通过 **krew**（kubectl 插件管理器）管理。Krew 提供社区插件的精选索引，并处理安装、升级和卸载。

# CAVEATS

插件必须是带有 **kubectl-** 前缀的可执行文件。只有 **list** 子命令可用；没有内置的安装或卸载命令（请使用 krew）。如果多个插件在不同 PATH 目录中同名，则只会使用第一个并显示警告。

# HISTORY

kubectl 插件支持被加入 **Kubernetes**，借鉴 git 插件系统的模式，以实现可扩展的命令行功能。

# INSTALL

```apt: sudo apt install kubectl```

```pacman: sudo pacman -S kubectl```

```apk: sudo apk add kubectl```

```brew: brew install kubectl```

```nix: nix profile install nixpkgs#kubectl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kubectl](/man/kubectl)(1), [krew](/man/krew)(1)
