# TAGLINE

Python 静态类型检查器

# TLDR

**对项目做类型检查**

```pyright```

**对特定文件做类型检查**

```pyright [file.py]```

**监视变更**

```pyright --watch```

**以 JSON 输出**

```pyright --outputjson```

**显示版本**

```pyright --version```

**创建配置文件**

```pyright --createstub [package]```

# SYNOPSIS

**pyright** [_options_] [_files_...]

# DESCRIPTION

**pyright** 是 Python 的静态类型检查器。它在不运行代码的情况下分析 Python 代码中的类型错误，可在编辑器和 CI 流水线中提供快速反馈。

该工具实现了 PEP 484 及后续 typing PEP 定义的 Python 类型系统，支持严格检查和 IDE 集成。

# PARAMETERS

**--watch**
> 监视模式，检测变更。

**--outputjson**
> JSON 输出格式。

**--project** _dir_
> 项目根目录。

**--pythonplatform** _platform_
> 目标平台。

**--pythonversion** _version_
> 目标 Python 版本。

**--level** _level_
> 诊断级别（basic、standard、strict）。

**--stats**
> 显示性能统计。

**--verifytypes** _package_
> 校验软件包的类型完整性。

**--createstub** _package_
> 生成 stub 文件。

# CONFIGURATION

**pyrightconfig.json**
> 项目级配置文件，用于设置类型检查严格度、include/exclude 路径、Python 版本和目标平台。

**pyproject.toml**
> 项目配置文件，包含 `[tool.pyright]` 段，支持与 pyrightconfig.json 相同的选项。

# CAVEATS

需要类型注解才能发挥全部作用。某些动态模式难以标注类型。复杂项目需要额外配置。并非所有库都有类型 stub。

# HISTORY

**Pyright** 由 **Microsoft** 开发，于 **2019 年**发布。它通过 Pylance 为 VS Code 提供的 Python 语言支持提供动力。该项目用 TypeScript 编写，专注于性能和标准符合性。

# INSTALL

```pacman: sudo pacman -S pyright```

```brew: brew install pyright```

```nix: nix profile install nixpkgs#pyright```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mypy](/man/mypy)(1), [python](/man/python)(1), [pylint](/man/pylint)(1), [flake8](/man/flake8)(1)
