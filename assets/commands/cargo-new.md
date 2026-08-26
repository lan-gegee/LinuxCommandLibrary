# TAGLINE

创建新的 Cargo 软件包

# TLDR

**创建新的二进制项目**

```cargo new [project_name]```

**创建新的库**

```cargo new [project_name] --lib```

**不使用 git 创建**

```cargo new [project_name] --vcs none```

**以指定 edition 创建**

```cargo new [project_name] --edition [2021]```

**以自定义名称创建**

```cargo new [path] --name [custom_name]```

# SYNOPSIS

**cargo new** [_options_] _path_

# DESCRIPTION

**cargo new** 在一个新目录中创建新的 Cargo 软件包。它会生成 Cargo.toml 清单文件、包含 "Hello, World!" 二进制（`main.rs`）或库骨架（`lib.rs`）的 src/ 目录，并默认初始化一个 git 仓库。

生成的 Cargo.toml 包含软件包名称、版本和 Rust edition。该命令会遵循 Cargo 配置中的默认设置，例如作者姓名和邮箱（从 git 配置或环境变量读取）。不支持自定义模板；如需基于模板创建项目，请使用 `cargo-generate`。

# PARAMETERS

**--bin**
> 创建带 src/main.rs 的二进制项目（默认）

**--lib**
> 创建带 src/lib.rs 的库

**--name** _name_
> 软件包名称（默认为目录名）

**--edition** _year_
> Rust edition（2015、2018、2021、2024）。默认为最新的稳定 edition。

**--vcs** _type_
> 版本控制系统（git、hg、pijul、fossil、none）

**--registry** _name_
> 用于发布的注册表

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

**--color** _when_
> 着色方式：auto、always、never。

**--offline**
> 不访问网络运行。

# GENERATED STRUCTURE

```
project_name/
├── Cargo.toml
├── .gitignore
└── src/
    └── main.rs (or lib.rs)
```

# CAVEATS

对于已存在的目录，请使用 `cargo init`。软件包名称只能使用字母数字字符、连字符或下划线。除非工作空间明确排除了该路径，否则不能在现有 Cargo 工作空间内创建。

# HISTORY

**cargo** 是 Rust 编程语言的软件包管理器和构建工具，随 **2015 年**的 Rust 1.0 首次发布。**new** 子命令自诞生以来就是 Cargo 的核心部分，简化了项目初始化流程。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-init](/man/cargo-init)(1), [cargo-build](/man/cargo-build)(1)
