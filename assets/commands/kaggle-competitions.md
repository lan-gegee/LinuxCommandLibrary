# TAGLINE

从命令行管理 Kaggle 机器学习竞赛

# TLDR

**列出竞赛**

```kaggle competitions list```

**下载竞赛文件**

```kaggle competitions download -c [competition-name]```

**向竞赛提交结果**

```kaggle competitions submit -c [competition-name] -f [submission.csv] -m "[message]"```

**列出竞赛文件**

```kaggle competitions files -c [competition-name]```

**查看排行榜**

```kaggle competitions leaderboard -c [competition-name] -s```

**列出历史提交记录**

```kaggle competitions submissions -c [competition-name]```

按关键字**搜索竞赛**

```kaggle competitions list -s "[search-term]"```

从竞赛中**下载指定文件**

```kaggle competitions download -c [competition-name] -f [filename]```

# SYNOPSIS

**kaggle** **competitions** _subcommand_ [_options_]

# PARAMETERS

**list**
> 列出可用竞赛。支持 --category、--sort-by、--page、--search、--csv。

**download** **-c** _name_
> 下载竞赛数据。用 -f 指定单个文件，-p 指定目标路径，-o 覆盖已有文件。

**submit** **-c** _name_ **-f** _file_ **-m** _message_
> 提交预测结果。-f 和 -m 都是必需的。

**files** **-c** _name_
> 列出竞赛数据文件。

**submissions** **-c** _name_
> 列出你的历史提交及其得分。

**leaderboard** **-c** _name_
> 查看竞赛排行榜。用 -s 显示，-d 以 CSV 下载。

# DESCRIPTION

**kaggle competitions** 用于在命令行管理 Kaggle 机器学习竞赛。它是 Kaggle CLI 的一部分，无需使用 web 界面即可下载数据集、提交预测结果和查看排行榜排名。

# INSTALL

```nix: nix profile install nixpkgs#kaggle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kaggle](/man/kaggle)(1), [kaggle-datasets](/man/kaggle-datasets)(1), [kaggle-kernels](/man/kaggle-kernels)(1)
