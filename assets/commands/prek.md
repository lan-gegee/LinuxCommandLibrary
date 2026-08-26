# TAGLINE

用 Rust 编写的高速 pre-commit hook 管理器

# TLDR

**安装** prek hook 到当前 Git 仓库

```prek install```

**运行**全部已配置的 hook，检查变更的文件

```prek run```

**运行**所有 hook，检查仓库中的每个被跟踪文件

```prek run --all-files```

只**运行**特定 hook

```prek run [hook_id]```

将 hook 修订版**自动更新**到最新标签

```prek auto-update```

**列出**从配置解析出的所有 hook

```prek list```

将旧式 YAML 配置**转换**为原生 TOML

```prek util yaml-to-toml```

**卸载**之前安装的 Git hook

```prek uninstall```

# SYNOPSIS

**prek** [_global-options_] _command_ [_command-options_] [_args_]

# PARAMETERS

**install** [**--hook-type** _type_] [**--overwrite**]
> 将 Git hook 安装到 _.git/hooks_。重复 **--hook-type** 可安装 pre-commit、commit-msg、pre-push 等。

**uninstall** [**--hook-type** _type_]
> 移除之前安装的 hook，同时保留 prek 的缓存。

**run** [**--all-files**] [**--files** _path..._] [**--hook-stage** _stage_] [**--from-ref** _ref_] [**--to-ref** _ref_] [**--last-commit**] [**--show-diff-on-failure**] [**--no-fail-fast**] [_hook-id_]
> 执行 hook。不带参数时针对暂存文件运行；使用 **--all-files** 时针对每个被跟踪文件运行。

**auto-update** [**--check**] [**--bleeding-edge**] [**--freeze**] [**--cooldown-days** _N_] [**--repo** _url_]
> 将配置中的 **rev:** 条目更新为最新发布标签。**--check** 只校验而不改写。

**list** [**--hook-stage** _stage_]
> 显示当前配置解析出的 hook 列表。

**clean**
> 从 prek 的存储中移除缓存的 hook 环境。

**gc**
> 从 prek 的缓存中垃圾回收未使用的仓库。

**init-templatedir** _directory_
> 填充 Git 模板目录，使新 clone 的仓库自动获得 hook。

**try-repo** _repo_ [**--ref** _ref_]
> 试运行某个 hook 仓库，而无需修改项目配置。

**util yaml-to-toml** [_path_]
> 将 _.pre-commit-config.yaml_ 转换为原生的 _prek.toml_ 格式。

**util list-builtins**
> 列出用 Rust 重新实现的内置 hook。

**util identify** _file..._
> 打印 prek 为给定路径关联的文件类型（用于调试 _types_ 过滤器）。

**self update**
> 将 prek 二进制文件本身升级到最新版本。

**-c** _file_, **--config** _file_
> 使用 _file_ 作为配置，而不是自动发现。

**-v**, **--verbose**
> 提高日志详细程度。重复使用可获得调试级输出。

**-q**, **--quiet**
> 抑制非必要输出。

**--color** _when_
> _auto_、_always_ 或 _never_。

**-V**, **--version**
> 打印版本号并退出。

# DESCRIPTION

**prek** 是一个 Git hook 管理器，旨在作为 **pre-commit** 更快速的即插即用替代品。它读取相同的 _.pre-commit-config.yaml_ 文件并支持相同的 hook 生态，同时以 **Rust** 编写的单个静态二进制文件发行，不依赖 Python 运行时。

prek 将 hook 环境缓存在 _~/.cache/prek_ 下，并在多个仓库间复用。若干常见 hook（文件修正器、JSON/YAML 校验器等）已用 Rust 重新实现并作为内置功能运行，避免了启动解释器的开销。**Python**、**Node.js**、**Bun**、**Go**、**Rust** 和 **Ruby** 的工具链安装在各个 hook 之间共享，Python 环境则通过 **uv** 管理。

除旧式 YAML schema 外，prek 还理解原生的 _prek.toml_ 格式，并提供 _prek util yaml-to-toml_ 来迁移现有配置。工作区模式允许单个配置驱动 monorepo 中多个子项目的 hook，并可通过命令行的 **--project** 和 **--skip-project** 进行过滤。

# CONFIGURATION

prek 在仓库根目录依次查找以下第一个存在的文件：

```
prek.toml
.prek.toml
.pre-commit-config.yaml
```

YAML 和 TOML 配置都声明一个 **repos** 列表，每个仓库固定一个 **rev**，并通过 **id** 暴露一个或多个 **hooks**。每个 hook 可用的键，如 **files**、**exclude**、**types**、**stages**、**language**、**args** 和 **additional_dependencies**，与 pre-commit 保持一致，无需改动。

用户级覆盖配置位于 _~/.config/prek/config.toml_。环境变量 **PREK_HOME** 可重新定位缓存目录；**PREK_NO_COLOR** 与 **NO_COLOR** 会禁用 ANSI 输出。

# CAVEATS

prek 力求与 pre-commit 行为一致，但不完全逐字节相同：Python 虚拟环境由 **uv** 而非 _virtualenv_ 管理，这可能导致解析出的软件包版本不同。某些 hook 若依赖 hook 脚本执行期间系统 Python 位于 **PATH** 上，可能需要显式声明依赖。_~/.cache/prek_ 下的缓存布局独立于 pre-commit，因此两个工具可以共存，但不会共享环境。

# HISTORY

**prek** 由 **Jian Zeng (j178)** 编写，以 Rust crate 以及 PyPI 上的 Python wheel 形式发布，可通过 **pip**、**uv** 或 **pipx** 安装。它将自己定位为"**重新构想的 pre-commit**"，复用现有 hook 生态的同时替换其运行时。早期采用者包括 **CPython**、**Apache Airflow** 和 **FastAPI** 等大型 Python 项目。

# INSTALL

```zypper: sudo zypper install prek```

```brew: brew install prek```

```nix: nix profile install nixpkgs#prek```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pre-commit](/man/pre-commit)(1), [husky](/man/husky)(1), [lefthook](/man/lefthook)(1), [uv](/man/uv)(1)
