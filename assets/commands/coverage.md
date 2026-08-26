# TAGLINE

Python 代码覆盖率测量工具

# TLDR

**以覆盖率运行 Python 脚本**

```coverage run [script.py]```

**以覆盖率运行 pytest**

```coverage run -m pytest```

**在终端显示覆盖率报告**

```coverage report```

**生成 HTML 覆盖率报告**

```coverage html```

**总覆盖率低于 80% 时失败**（退出码 2）

```coverage report --fail-under=80```

**合并多次运行的覆盖率数据**

```coverage combine```

**清除已收集的覆盖率数据**

```coverage erase```

**显示特定文件的覆盖率**

```coverage report --include=[path/to/file.py]```

**以分支覆盖方式**测量运行

```coverage run --branch -m pytest```

**生成 XML 报告**（Cobertura 格式，供 CI 使用）

```coverage xml```

# SYNOPSIS

**coverage** _command_ [_options_] [_args_]

# PARAMETERS

**run** [_options_] _program_
> 运行程序并收集覆盖率数据。

**report**
> 在终端显示覆盖率报告。

**html**
> 在 htmlcov/ 中生成 HTML 报告。

**xml**
> 生成 Cobertura XML 报告。

**json**
> 生成 JSON 报告。

**combine**
> 合并多个覆盖率文件中的数据。

**erase**
> 删除已收集的覆盖率数据。

**annotate**
> 用覆盖率标记注释源文件。

**lcov**
> 生成 LCOV 报告。

**-m** _module_
> 将库模块作为脚本运行（类似 python -m）。

**--source** _paths_
> 将覆盖率测量限制在指定的软件包/目录。

**--include** _patterns_
> 只包含匹配模式的文件。

**--omit** _patterns_
> 排除匹配模式的文件。

**--branch**
> 启用分支覆盖率测量。

**--fail-under** _n_
> 覆盖率低于 n% 时以失败状态退出。

# DESCRIPTION

**Coverage.py** 测量 Python 程序的代码覆盖率，显示测试期间执行了哪些行和分支。它帮助识别未经测试的代码路径，确保测试套件的完整性。

该工具通过插桩 Python 字节码来跟踪执行。使用 **coverage run** 运行测试后，报告会显示每个文件的行覆盖率百分比。HTML 报告会直观地高亮显示已覆盖和未覆盖的代码行。

分支覆盖率（**--branch**）还会跟踪哪些条件分支被执行到，从而捕捉 if 语句两个分支未都被测试的情况。

# CONFIGURATION

**pyproject.toml**
> 在 [tool.coverage.run] 和 [tool.coverage.report] 小节中配置源码路径、分支覆盖和报告阈值。

**setup.cfg**
> 备选配置位置，使用 [coverage:run] 和 [coverage:report] 小节。

**.coveragerc**
> coverage 专用的配置文件，用于设置排除模式、报告选项等。

# CAVEATS

覆盖率测量会增加运行时开销。动态代码生成和 exec() 可能无法被正确跟踪。100% 的行覆盖率并不能保证代码没有缺陷。分支覆盖率更彻底但更难达成。多进程需要特殊配置。

# HISTORY

Coverage.py 由 **Ned Batchelder** 创建，首次发布于 **2004** 年。它已成为 Python 的标准代码覆盖率工具，与 pytest 和 unittest 等测试运行器集成。该工具广泛用于 CI/CD 流水线，并得到 Codecov 和 Coveralls 等覆盖率报告服务的支持。

# INSTALL

```apk: sudo apk add py3-coverage```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pytest](/man/pytest)(1), [python](/man/python)(1), [tox](/man/tox)(1), [codecov](/man/codecov)(1)
