# TAGLINE

管理 Poetry 项目的 Python 版本

# TLDR

**列出环境中可用的 Python 版本**

```poetry python list```

**列出所有版本**包括可供下载的版本

```poetry python list --all```

**仅列出 Poetry 托管的 Python 版本**

```poetry python list --managed```

**安装特定的 Python 版本**

```poetry python install [3.12]```

**安装自由线程（free-threaded）的 Python 版本**

```poetry python install --free-threaded [3.13]```

**安装特定实现**（cpython 或 pypy）

```poetry python install --implementation [pypy] [3.10]```

**移除 Poetry 托管的 Python 版本**

```poetry python remove [3.12]```

# SYNOPSIS

**poetry python** _command_ [_options_]

# PARAMETERS

**install** _VERSION_
> 从 Python Standalone Builds 项目安装指定的 Python 版本。

**list**
> 显示环境中可用的 Python 版本，包括系统安装和 Poetry 托管的版本。

**remove** _VERSION_
> 移除 Poetry 托管的 Python 版本。

## install options

**--clean** (**-c**)
> 检查失败时清理安装。

**--free-threaded** (**-t**)
> 若可用则使用自由线程版本（等同于请求带尾缀 "t" 的版本）。

**--implementation** (**-i**) _IMPL_
> 要使用的 Python 实现（cpython、pypy）。

**--reinstall** (**-r**)
> 安装已存在时重新安装。

## list options

**--all** (**-a**)
> 列出所有版本，包括可供下载的版本。

**--free-threaded** (**-t**)
> 仅列出自由线程的 Python 版本。

**--implementation** (**-i**) _IMPL_
> 按 Python 实现过滤搜索。

**--managed** (**-m**)
> 仅列出 Poetry 托管的 Python 版本。

## remove options

**--free-threaded** (**-t**)
> 移除自由线程版本。

**--implementation** (**-i**) _IMPL_
> 要移除的 Python 实现（cpython、pypy）。

# DESCRIPTION

**poetry python** 将管理 Python 版本的子命令组合在一起。**install** 子命令从 Python Standalone Builds 项目下载并安装 Python 版本。**list** 子命令显示所有发现的 Python 版本，包括系统管理和 Poetry 托管的安装。**remove** 子命令移除 Poetry 托管的 Python 安装。

这是 Poetry 2.1.0 引入的实验性功能，行为可能在后续版本中变化。

# CAVEATS

需要 Poetry 2.1.0 或更高版本。这是一个实验性功能。install 子命令从 Python Standalone Builds 项目下载，且只管理 Poetry 自行安装的版本。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-env](/man/poetry-env)(1), [python](/man/python)(1), [python3](/man/python3)(1), [pip](/man/pip)(1)
