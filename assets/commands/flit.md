# TAGLINE

简洁的 Python 打包与发布工具

# TLDR

**初始化新项目**

```flit init```

**构建软件包**

```flit build```

**以开发模式安装**

```flit install --symlink```

**发布到 PyPI**

```flit publish```

**发布到 TestPyPI**

```flit publish --repository testpypi```

**只安装依赖**（不安装包本身）

```flit install --only-deps```

**检查项目配置**

```flit check```

# SYNOPSIS

**flit** [_options_] _command_ [_args_]

# PARAMETERS

**init**
> 以交互方式创建 pyproject.toml。

**build**
> 构建 wheel 和 sdist。

**install**
> 在本地安装。

**install --symlink**
> 以符号链接方式将模块链接到 site-packages 进行开发。

**install --pth-file**
> 使用 .pth 文件进行开发（在 Windows 上可用）。

**install --deps** _DEPS_
> 安装哪些依赖：all、production、develop 或 none（默认：all）。

**install --only-deps**
> 只安装依赖，不安装包本身。

**install --python** _PATH_
> 为其他 Python 解释器安装。

**publish**
> 上传到 PyPI。

**publish --repository** _name_
> 目标仓库（pypi、testpypi）。

**check**
> 校验项目配置。

# DESCRIPTION

**flit** 是一款简单的 Python 打包工具，使用 pyproject.toml 进行配置。它只需极少的设置即可完成 wheel 和源码发行版的构建以及发布到 PyPI。

Flit 面向需求简单的纯 Python 包设计。它从模块的 docstring 和 __version__ 属性读取包元数据，因此所需配置非常少。

# PYPROJECT.TOML EXAMPLE

```toml
[build-system]
requires = ["flit_core"]
build-backend = "flit_core.buildapi"

[project]
name = "mypackage"
authors = [{name = "Me"}]
dynamic = ["version", "description"]

[project.scripts]
mycli = "mypackage:main"
```

# CAVEATS

最适合没有复杂构建需求的纯 Python 包。不支持编译扩展。需要模块 docstring 作为描述。发布需要 PyPI 凭据。

# HISTORY

flit 由 **Thomas Kluyver** 创建，作为纯 Python 包使用 setuptools 的更简替代方案。它推动了 pyproject.toml 的普及，也是 PEP 517/518 构建标准的早期实现之一。

# INSTALL

```dnf: sudo dnf install flit```

```apk: sudo apk add py3-flit```

```brew: brew install flit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [poetry](/man/poetry)(1), [hatch](/man/hatch)(1), [twine](/man/twine)(1)
