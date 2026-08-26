# TAGLINE

从命令行管理 Kaggle 机器学习模型

# TLDR

**列出模型**

```kaggle models list```

**获取模型详情**

```kaggle models get -m [owner/model-name]```

**初始化模型元数据**

```kaggle models init -p [path]```

**创建新模型**

```kaggle models create -p [path]```

**下载模型实例版本**

```kaggle models instances versions download -m [owner/model/framework/instance] -v [version]```

# SYNOPSIS

**kaggle** **models** _subcommand_ [_options_]

# PARAMETERS

**list**
> 列出可用模型。

**get** **-m** _model_
> 获取模型详情。

**init**
> 初始化模型元数据。

**create**
> 创建新模型。

**update**
> 更新已有模型。

**delete**
> 删除模型。

**instances**
> 管理模型实例（get、init、create、update、delete、files）。

**instances versions**
> 管理模型实例版本（create、download、delete、files）。

# DESCRIPTION

**kaggle models** 用于在命令行管理 Kaggle 机器学习模型。它是 Kaggle CLI 的一部分，可以访问预训练模型，也允许向社区发布自定义模型。

命令层级有三层：**models**（顶层仓库）、**instances**（特定框架实现）和 **instance versions**（带版本的快照）。可以用简写 **kaggle m** 代替 **kaggle models**。

# SEE ALSO

[kaggle](/man/kaggle)(1), [kaggle-datasets](/man/kaggle-datasets)(1), [kaggle-competitions](/man/kaggle-competitions)(1), [kaggle-kernels](/man/kaggle-kernels)(1)
