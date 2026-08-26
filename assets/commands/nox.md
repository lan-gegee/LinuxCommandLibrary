# TAGLINE

类似 tox 的 Python 自动化工具

# TLDR

**运行默认会话**

```nox```

**运行指定会话**

```nox -s [tests]```

**列出可用会话**

```nox -l```

**指定 Python 版本运行**

```nox -p [3.12]```

**复用虚拟环境并跳过安装步骤**（快速迭代）

```nox -R```

**使用指定的 venv 后端运行**

```nox --force-venv-backend [uv]```

**向会话传递额外参数**

```nox -s [tests] -- [pytest-args]```

# SYNOPSIS

**nox** [_options_] [-- _args_]

# PARAMETERS

**-s**, **--sessions** _name_
> 运行指定的会话。

**-l**, **--list**
> 列出可用会话后退出。

**-r**, **--reuse-existing-virtualenvs**
> 复用现有虚拟环境，而不是重新创建。

**-R**
> 复用虚拟环境并跳过安装步骤（相当于 -r 加 --no-install）。

**-p**, **--python** _version_
> 按 Python 版本筛选会话。

**-P**, **--force-python** _version_
> 覆盖 Noxfile 中指定的 Python 版本。

**-f**, **--noxfile** _file_
> Nox 配置文件（默认：noxfile.py）。

**-k** _expression_
> 按关键字表达式筛选会话。

**-t**, **--tags** _tag_
> 按标签筛选会话。

**-x**, **--stop-on-first-error**
> 在第一个会话失败后停止。

**--no-install**
> 复用虚拟环境时跳过安装命令。

**-db**, **--default-venv-backend** _backend_
> 默认 venv 后端：virtualenv、venv、uv、conda、mamba、micromamba、none。

**-fb**, **--force-venv-backend** _backend_
> 为所有会话强制使用指定的 venv 后端。

**--envdir** _dir_
> 存放虚拟环境的目录（默认：.nox）。

**--report** _file_
> 输出会话结果的 JSON 报告。

# DESCRIPTION

**Nox** 是一个 Python 自动化工具，用于跨多个 Python 环境自动执行测试。会话以 Python 函数的形式定义在 **noxfile.py** 中，相比 tox 基于 INI 的方式，配置更灵活、更可编程。

Nox 支持多种虚拟环境后端，包括 virtualenv、venv、uv、conda 和 mamba。`-R` 标志通过复用虚拟环境并跳过软件包安装来加快开发迭代速度。

# NOXFILE EXAMPLE

```python
import nox

@nox.session(python=["3.10", "3.11", "3.12", "3.13"])
def tests(session):
    session.install("pytest", ".")
    session.run("pytest")

@nox.session
def lint(session):
    session.install("flake8")
    session.run("flake8", "src")
```

# CAVEATS

需要工作目录中存在 noxfile.py。默认为每个会话创建独立的虚拟环境，若不加 `-r` 或 `-R` 可能会很慢。要求 Python >= 3.9。

# HISTORY

Nox 由 **Thea Flowers** 在 Google 创建，作为 tox 更灵活的替代品，用 Python 函数代替 INI 文件进行配置。

# INSTALL

```dnf: sudo dnf install nox```

```apk: sudo apk add py3-nox```

```brew: brew install nox```

```nix: nix profile install nixpkgs#nox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tox](/man/tox)(1), [pytest](/man/pytest)(1), [virtualenv](/man/virtualenv)(1)
