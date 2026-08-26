# TAGLINE

解析并锁定项目依赖

# TLDR

**创建或更新**锁文件

```uv lock```

**将所有软件包升级**到最新的兼容版本

```uv lock --upgrade```

**将指定软件包升级**到其最新版本

```uv lock --upgrade-package [package]```

**检查锁文件是否为最新**而不修改它

```uv lock --check```

**使用指定的 Python 版本锁定**

```uv lock --python [3.12]```

# SYNOPSIS

**uv** **lock** [_options_]

# PARAMETERS

**--upgrade**
> 允许所有软件包升级到其最新的兼容版本。

**--upgrade-package** _pkg_
> 允许指定的软件包升级。

**--check**
> 检查锁文件是否为最新；若需要更新则报错。

**--frozen**
> 直接使用现有锁文件，不检查其是否为最新。

**--locked**
> 断言锁文件与 pyproject.toml 一致；否则报错。

**--no-sources**
> 解析依赖时忽略 tool.uv.sources 表。

**--python** _VERSION_
> 针对特定的 Python 版本进行解析。

# DESCRIPTION

**uv lock** 解析 pyproject.toml 中声明的项目依赖，并将精确的固定版本写入 uv.lock 文件。锁文件确保跨环境的可复现安装。修改 pyproject.toml 的依赖后请运行此命令。

运行 **uv sync**、**uv run** 或 **uv add** 时会自动执行锁定，但也可以显式运行此命令来更新锁文件而不安装软件包。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [uv-sync](/man/uv-sync)(1), [uv-add](/man/uv-add)(1)
