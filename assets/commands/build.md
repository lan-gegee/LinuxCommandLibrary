# TAGLINE

构建用于发布的 Python 软件包

# TLDR

**构建 Python 包**

```python -m build```

**只构建源码分发包**

```python -m build --sdist```

**只构建 wheel**

```python -m build --wheel```

**以指定输出目录构建**

```python -m build --outdir [dist/]```

**以详细输出构建**

```python -m build -v```

**不使用隔离环境构建**（使用当前环境）

```python -m build --no-isolation```

# SYNOPSIS

**python -m build** [_options_] [_source_directory_]

# PARAMETERS

**--sdist**
> 只构建源码分发包（sdist）。

**--wheel**
> 只构建 wheel。

**--outdir** _directory_
> 构建产物的输出目录（默认：dist/）。

**--no-isolation**
> 不创建隔离环境直接构建。

**--skip-dependency-check**
> 跳过依赖校验。

**--config-setting** _key=value_
> 向构建后端传递设置。

**-v**, **--verbose**
> 提高输出详细程度。

**-C** _setting_
> --config-setting 的简写形式。

# DESCRIPTION

**build** 是标准的 Python 软件包构建器，可从 Python 项目生成源码分发（sdist）和 wheel。它是构建待发布到 PyPI 的软件包的推荐方式，取代了直接调用 **setup.py sdist bdist_wheel** 的做法。

默认情况下，build 会创建一个仅安装了构建依赖的隔离虚拟环境，以确保构建可复现。它从 **pyproject.toml** 读取配置，并将实际构建委托给所配置的构建后端（setuptools、flit、hatch 等）。

输出放在 **dist/** 目录下，包含一个 **.tar.gz** 源码分发包和一个 **.whl** wheel 文件。它们可以用 **twine** 上传到 PyPI，或直接用 **pip** 安装。

# CAVEATS

需要有包含构建系统配置的 **pyproject.toml** 文件。隔离的构建环境在每次构建时都会下载依赖；开发期间可用 **--no-isolation** 加快重复构建。一些缺少规范 pyproject.toml 的旧式软件包可能无法构建。

# HISTORY

**build** 软件包由 Python Packaging Authority（PyPA）创建，是 Python 打包现代化工作的一部分。它于 **2020 年**首次发布，按照 PEP 517 和 PEP 518 规范提供了简单、标准化的软件包构建方式。它取代了以往直接运行 **python setup.py** 命令的旧做法，支持任何符合 PEP 517 的构建后端。

# INSTALL

```zypper: sudo zypper install build```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [twine](/man/twine)(1), [flit](/man/flit)(1), [hatch](/man/hatch)(1)
