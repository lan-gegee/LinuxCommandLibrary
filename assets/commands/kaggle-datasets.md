# TAGLINE

从命令行管理 Kaggle 数据集

# TLDR

**列出数据集**

```kaggle datasets list```

**搜索数据集**

```kaggle datasets list -s "[search term]"```

**下载数据集**

```kaggle datasets download -d [owner/dataset-name]```

**创建新数据集**

```kaggle datasets create -p [path]```

**获取数据集元数据**

```kaggle datasets metadata -d [owner/dataset-name]```

# SYNOPSIS

**kaggle** **datasets** _subcommand_ [_options_]

# PARAMETERS

**list**
> 列出可用数据集。

**download** **-d** _dataset_
> 下载数据集文件。

**create** **-p** _path_
> 创建新数据集。

**version** **-p** _path_
> 创建新的数据集版本。

**metadata** **-d** _dataset_
> 获取数据集元数据。

**-s** _term_
> 搜索过滤条件。

# DESCRIPTION

**kaggle datasets** 用于在命令行管理 Kaggle 数据集。它是 Kaggle CLI 的一部分，可用于为机器学习项目浏览、下载和发布数据集。

# SEE ALSO

[kaggle](/man/kaggle)(1), [kaggle-competitions](/man/kaggle-competitions)(1)
