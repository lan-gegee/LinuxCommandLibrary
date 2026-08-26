# TAGLINE

自动化跨版本的 Python 测试

# TLDR

**运行所有测试环境**

```tox```

**运行特定环境**

```tox -e [py39]```

**运行多个环境**

```tox -e [py38,py39,lint]```

**列出可用环境**

```tox -l```

**重建环境**

```tox -r```

**并行运行**

```tox -p```

**向测试命令传递参数**

```tox -- [--verbose]```

**重建并运行**

```tox -r -e [py39]```

# SYNOPSIS

**tox** [_-e envs_] [_-r_] [_-p_] [_-l_] [_options_] [_-- test_args_]

# PARAMETERS

**-e** _ENVLIST_, **--envlist** _ENVLIST_
> 要运行的环境。

**-r**, **--recreate**
> 重建虚拟环境。

**-p**, **--parallel**
> 并行运行各环境。

**-l**, **--list**
> 列出环境。

**-a**, **--listenvs-all**
> 列出所有环境，包括生成的环境。

**--devenv** _PATH_
> 创建开发环境。

**-c** _FILE_, **--conf** _FILE_
> 配置文件路径。

**--skip-missing-interpreters**
> 跳过缺少解释器的环境。

**-v**, **--verbose**
> 详细输出。

**-q**, **--quiet**
> 安静输出。

**--notest**
> 只安装不测试。

**--sdistonly**
> 只创建源码分发包。

**--result-json** _FILE_
> 以 JSON 格式写入结果。

**--**
> 将其余参数传递给测试命令。

# DESCRIPTION

**tox** 自动化跨多个 Python 版本和环境测试 Python 软件包的过程。它会创建隔离的 virtualenv、安装软件包并运行测试。

配置写在 tox.ini 或 pyproject.toml 中，用于定义各个环境。每个环境需指定：Python 版本、依赖项和要运行的命令。常见做法是测试多个 Python 版本（py38、py39、py310），再加上代码检查（linting）环境。

创建环境时会以开发模式安装该软件包以及测试依赖。这能尽早发现安装问题。重建模式（-r）会从头重建环境。

并行模式（-p）同时运行多个环境，在多核机器上可加快多版本测试的速度。输出会在完成后收集并显示。

除测试外，tox 还能运行任何命令：代码检查（flake8、mypy）、文档构建（sphinx）、格式检查等。多条命令可按顺序串联执行。

双连字符（--）会将参数传递给测试命令，从而无需修改 tox.ini 即可使用 pytest 选项或选择要运行的测试。

# CAVEATS

相应的 Python 版本必须已安装才能使用对应环境。首次创建环境会下载依赖项。并行模式可能触及资源限制。复杂配置可能难以调试。某些 CI 系统更适合更简单的方案。

# HISTORY

**tox** 由 **Holger Krekel**（pytest 的创造者）约在 **2010 年**创建，用于解决多版本 Python 测试问题。它成为 Python 软件包测试的标准工具，被众多大型项目采用。第 4 版（2022 年）带来了重大改进和对 pyproject.toml 的支持。

# INSTALL

```dnf: sudo dnf install tox```

```apk: sudo apk add py3-tox```

```brew: brew install tox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pytest](/man/pytest)(1), [nox](/man/nox)(1), [virtualenv](/man/virtualenv)(1), [hatch](/man/hatch)(1)
