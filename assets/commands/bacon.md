# TAGLINE

后台 Rust 代码检查器

# TLDR

**在当前项目中运行默认的检查任务**

```bacon```

**运行指定任务**

```bacon [test]```

**运行 clippy 检查**

```bacon --job [clippy]```

**列出可用任务**

```bacon --list-jobs```

**在指定的项目目录中运行**

```bacon --path [path/to/project]```

**初始化 bacon.toml 配置文件**

```bacon --init```

**打开偏好设置文件路径**

```bacon --prefs```

# SYNOPSIS

**bacon** [_options_] [_job_]

# PARAMETERS

**-j**, **--job** _name_
> 运行指定任务。无歧义时也可以不带该选项，直接作为位置参数传入。

**--list-jobs**
> 列出所有可用任务并退出。

**--path** _dir_
> 设置项目目录（默认为当前目录）。

**--config** _file_
> 使用特定的 bacon.toml 配置文件。

**-w**, **--watch** _path_
> 额外监视变更的路径。

**--init**
> 若当前项目不存在 bacon.toml 配置文件则创建一个。

**--prefs**
> 偏好设置文件不存在时创建它，并打印其路径。

**-s**, **--summary**
> 完成时显示结果摘要。

**--no-default-features**
> 禁用 cargo 默认特性。

**--features** _features_
> 要启用的 cargo 特性列表，逗号分隔。

**--all-features**
> 启用所有可用的 cargo 特性。

# DESCRIPTION

**bacon** 是一款后台 Rust 代码检查器，以监视模式运行 cargo 命令。它会持续检查代码中的编译错误、警告和 clippy 提示，并在终端 UI 中显示结果。

该工具能在开发过程中提供即时反馈，无需手动运行 cargo 命令。当不存在歧义时，任务名可以直接作为位置参数传入（例如 `bacon clippy` 而不是 `bacon --job clippy`）。

默认任务包括 **check**（cargo check）、**clippy**（clippy 检查）、**test**（运行测试）、**doc**（生成文档）以及 **run**（构建并运行）。自定义任务可在 bacon.toml 中定义。

# CAVEATS

需要已安装 Rust 工具链。持续检查可能导致大型项目的 CPU 占用偏高。终端 UI 需要兼容的终端模拟器。

# HISTORY

**bacon** 由 Denys Séguret (Canop) 于 **2021** 年前后创建，旨在通过持续反馈为 Rust 项目提供更好的开发体验。

# INSTALL

```apt: sudo apt install bacon```

```pacman: sudo pacman -S bacon```

```brew: brew install bacon```

```nix: nix profile install nixpkgs#bacon```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[cargo](/man/cargo)(1), [cargo-watch](/man/cargo-watch)(1), [clippy](/man/clippy)(1), [rustc](/man/rustc)(1)
