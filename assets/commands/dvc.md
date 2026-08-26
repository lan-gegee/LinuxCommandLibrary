# TAGLINE

面向机器学习项目的版本控制系统

# TLDR

**初始化 DVC 仓库**

```dvc init```

**跟踪一个数据文件或目录**

```dvc add [data/dataset.csv]```

**将被跟踪的数据推送到远程存储**

```dvc push```

**从远程存储拉取被跟踪的数据**

```dvc pull```

**重现一条流水线**

```dvc repro```

**显示流水线 DAG**

```dvc dag```

**配置远程存储**

```dvc remote add -d [myremote] [s3://bucket/path]```

**显示被跟踪数据的差异**

```dvc diff```

# SYNOPSIS

**dvc** [**--cd** _dir_] _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的 DVC 操作。

**init**
> 在 Git 仓库中初始化 DVC。

**add** _FILE_
> 用 DVC 跟踪一个文件或目录。

**push**
> 将被跟踪的数据上传到远程存储。

**pull**
> 从远程存储下载被跟踪的数据。

**repro**
> 重现流水线阶段。

**diff**
> 显示提交之间被跟踪数据的更改。

**fetch**
> 从远程存储下载被跟踪的数据但不检出。

**checkout**
> 检出与当前 .dvc 文件匹配的数据文件。

**gc**
> 垃圾回收未使用的缓存文件。

**remote add** _NAME_ _URL_
> 添加远程存储。

**config** _OPTION_ [_VALUE_]
> 读取或设置 DVC 配置选项。

**dag**
> 将流水线阶段可视化为有向无环图。

**destroy**
> 从项目中移除所有 DVC 文件和目录。

**--cd** _dir_
> 在执行命令前切换到指定目录。

**-v**, **--verbose**
> 增加输出的详细程度。

**-q**, **--quiet**
> 抑制输出。

**--version**
> 显示 DVC 版本。

**-h**, **--help**
> 显示帮助信息。

# CONFIGURATION

**.dvc/config**
> 仓库级 DVC 配置，包括远程存储设置。

**~/.config/dvc/config**
> 全局用户配置，包含 DVC 的默认值和偏好设置。

**.dvc/config.local**
> 本地仓库配置，用于不提交到 Git 的本机特定设置。

# DESCRIPTION

**DVC**（Data Version Control）是一个面向机器学习项目的版本控制系统。它与 Git 协同跟踪大文件、数据集和模型，而不将它们存入 Git 仓库本身。

DVC 将文件元数据（.dvc 文件）存储在 Git 中，而实际数据则放入可配置的远程存储（S3、GCS、Azure、SSH 等）。这使得大文件版本控制和团队间数据集共享成为可能。

流水线功能定义可重现的机器学习工作流，通过跟踪依赖项和输出来管理实验。

# CAVEATS

需要 Git 仓库。大数据传输依赖网络速度。远程存储可能产生费用。流水线重现需要匹配的环境。

# HISTORY

DVC 由 **iterative.ai** 创建并于 **2017 年**发布。它解决了大型数据集和机器学习模型不适合放入 Git 的版本控制难题，支持可重现的机器学习工作流。**2025 年**，DVC 被 **lakeFS** 收购。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [dvc-init](/man/dvc-init)(1), [dvc-add](/man/dvc-add)(1), [dvc-diff](/man/dvc-diff)(1), [dvc-fetch](/man/dvc-fetch)(1), [dvc-dag](/man/dvc-dag)(1), [dvc-gc](/man/dvc-gc)(1), [mlflow](/man/mlflow)(1)
