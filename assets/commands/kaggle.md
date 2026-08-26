# TAGLINE

Kaggle 数据科学竞赛平台的 CLI

# TLDR

**下载竞赛文件**

```kaggle competitions download -c [competition-name]```

**向竞赛提交结果**

```kaggle competitions submit -c [competition-name] -f [submission.csv] -m "[message]"```

**搜索数据集**

```kaggle datasets list -s "[search-term]"```

**下载数据集**

```kaggle datasets download -d [owner/dataset-name]```

**列出竞赛排行榜**

```kaggle competitions leaderboard [competition-name]```

**下载模型**

```kaggle models download -m [owner/model-name/framework/variation]```

**创建新数据集**

```kaggle datasets create -p [path/to/dataset]```

**查看 API 凭据**

```kaggle config view```

# SYNOPSIS

**kaggle** _command_ _subcommand_ [_options_]

# COMMANDS

**competitions** list|files|download|submit|submissions|leaderboard
> 管理竞赛数据和提交。

**datasets** list|files|download|create|version|init|metadata|status
> 浏览和管理数据集。

**kernels** list|init|push|pull|output|status
> 管理 notebook（kernel）。

**models** list|get|files|download
> 访问 Kaggle 模型。

**config** view|set|unset
> 管理配置。

# PARAMETERS

**-c**, **--competition** _name_
> 竞赛名称。

**-d**, **--dataset** _name_
> owner/dataset 格式的数据集。

**-m**, **--message** _text_
> 提交说明。

**-f**, **--file** _path_
> 要提交或上传的文件。

**-p**, **--path** _directory_
> 本地目录路径。

**-o**, **--output** _directory_
> 下载输出目录。

**--unzip**
> 解压下载的文件。

**-s**, **--search** _term_
> 列表搜索关键字。

**--sort-by** _field_
> 按字段对结果排序。

**--force**
> 不经确认直接覆盖已有文件。

**-q**, **--quiet**
> 抑制详细输出。

**-v**
> 表格列表的详细模式。

**-h**, **--help**
> 显示命令或子命令的帮助信息。

# DESCRIPTION

**kaggle** 是 Kaggle 的 CLI。Kaggle 是一个数据科学竞赛平台。该工具管理竞赛数据、数据集、notebook 和模型。

身份验证需要来自 kaggle.com/account 的 API 凭据。将 **kaggle.json** 放在 **~/.kaggle/** 下并设置合适的权限（chmod 600）。

竞赛工作流：**download** 获取数据文件，在本地处理后再用 **submit** 上传预测结果。**leaderboard** 显示排名；**submissions** 列出你的提交记录。

数据集是带版本的。**download** 获取当前版本；**create** 初始化新数据集；**version** 添加更新。**init** 为新数据集生成 dataset-metadata.json。

Kernel（notebook）可以推送到 Kaggle 进行云端执行。**pull** 下载 notebook；**push** 上传 notebook，由 kernel-metadata.json 定义运行时设置。

# CAVEATS

需要 Kaggle 账户和 API key。部分竞赛有接受条款要求。大数据集可能需要较长时间下载。API 有速率限制。上传数据集需要元数据文件。

# HISTORY

Kaggle 由 **Anthony Goldbloom** 和 **Ben Hamner** 于 **2010** 年创立，是一个预测建模竞赛平台。它于 **2017** 年被 **Google** 收购。CLI 的加入让程序化访问平台资源成为可能。Kaggle 后来扩展到数据集、notebook 和课程领域。它拥有数百万成员，是最大的数据科学社区之一。

# INSTALL

```nix: nix profile install nixpkgs#kaggle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc](/man/dvc)(1), [mlflow](/man/mlflow)(1), [jupyter](/man/jupyter)(1)
