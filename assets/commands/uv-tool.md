# TAGLINE

安装和运行 Python CLI 工具

# TLDR

**不安装直接运行工具**

```uv tool run [tool]```

**从指定软件包运行工具**

```uv tool run --from [package] [command]```

**全局安装工具**

```uv tool install [tool]```

**安装带额外依赖的工具**

```uv tool install [tool] --with [extra_package]```

**列出已安装的工具**

```uv tool list```

**升级指定的工具**

```uv tool upgrade [tool]```

**升级所有已安装的工具**

```uv tool upgrade --all```

**卸载工具**

```uv tool uninstall [tool]```

# SYNOPSIS

**uv** **tool** _command_ [_options_]

# PARAMETERS

**run** _tool_
> 在临时的隔离环境中运行工具。别名：**uvx**。

**install** _tool_
> 在隔离的虚拟环境中全局安装工具。

**uninstall** _tool_
> 移除已安装的工具及其环境。

**list**
> 列出已安装的工具及其可执行文件。

**upgrade** _tool_
> 升级已安装的工具。

**upgrade** **--all**
> 升级所有已安装的工具。

**dir**
> 显示工具的安装目录。

**update-shell**
> 将工具可执行文件目录添加到 shell 配置文件的 PATH 中。

**--from** _package_
> 指定要从中安装或运行命令的软件包。

**--with** _package_
> 在工具环境中包含额外的软件包。

**--python** _version_
> 指定要使用的 Python 解释器或版本。

# DESCRIPTION

**uv tool** 在隔离的虚拟环境中管理 Python CLI 工具。每个工具都有自己带依赖的环境，保持系统整洁。类似于 **pipx**，但由于 uv 基于 Rust 的解析器和安装器而显著更快。

可以使用 **uv tool run**（别名为 **uvx**）临时运行工具，它会创建一次性环境；也可以使用 **uv tool install** 持久安装工具，使其在 PATH 中永久可用。**--from** 选项允许从指定软件包运行特定的命令，**--with** 则向工具环境添加额外依赖。工具升级会遵循安装时设置的版本约束。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [uv-run](/man/uv-run)(1), [uv-pip](/man/uv-pip)(1), [uvx](/man/uvx)(1), [pipx](/man/pipx)(1)
