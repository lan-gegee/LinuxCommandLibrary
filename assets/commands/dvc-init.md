# TAGLINE

在仓库中初始化数据版本控制

# TLDR

**在 Git 仓库中初始化 DVC**

```dvc init```

**不集成 Git 进行初始化**

```dvc init --no-scm```

**在 Git 仓库的子目录中初始化**

```dvc init --subdir```

**强制重新初始化 DVC**

```dvc init -f```

# SYNOPSIS

**dvc** **init** [_options_]

# PARAMETERS

**--no-scm**
> 不与 Git 集成而初始化 DVC。DVC 将不会创建或修改任何与 Git 相关的文件。

**--subdir**
> 在 Git 仓库的子目录而非仓库根目录中初始化 DVC。

**-f**, **--force**
> 强制重新初始化，覆盖任何已存在的 .dvc 目录。

**-q**, **--quiet**
> 抑制除错误外的所有输出。

**-v**, **--verbose**
> 显示详细的跟踪信息。

# DESCRIPTION

**dvc init** 在目录中初始化数据版本控制，创建 `.dvc/` 目录结构。这会让 DVC 与 Git 版本控制协同工作，用于跟踪大文件、数据集和机器学习模型。

应在 Git 仓库中运行以获得完整功能，不过 `--no-scm` 选项允许独立运行。该命令会创建配置文件和缓存目录，并通过更新 `.gitignore` 和暂存新的 `.dvc/` 目录来与 Git 集成。

创建的 `.dvc/` 目录包含 `config`（仓库配置）、`.gitignore`（用于排除缓存和临时文件），以及一个内部使用的 `tmp/` 目录。

# CONFIGURATION

**.dvc/config**
> 本地仓库配置，包括远程存储、缓存设置和执行参数。

**.dvc/config.local**
> 不由 Git 跟踪的本机特定设置，例如凭据和缓存位置。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc](/man/dvc)(1), [dvc-config](/man/dvc-config)(1), [dvc-destroy](/man/dvc-destroy)(1), [git-init](/man/git-init)(1)
