# TAGLINE

为一个或多个构建应用标签

# TLDR

为构建**打标签**

```koji tag-build [tag] [nvr]```

为**多个构建**打标签

```koji tag-build [tag] [nvr1] [nvr2]```

打标签但**不等待**

```koji tag-build [tag] [nvr] --nowait```

**强制**执行打标签操作

```koji tag-build [tag] [nvr] --force```

显示**帮助**

```koji tag-build --help```

# SYNOPSIS

**koji tag-build** [_options_] _tag_ _nvr_ [_nvr_...]

# DESCRIPTION

**koji tag-build** 为一个或多个构建应用标签。Koji 中的标签用于组织构建，并控制哪些软件包出现在仓库中。

# PARAMETERS

**tag**
> 要应用的标签名称

**nvr**
> 以 Name-Version-Release 指定的构建（可指定多个）

**--nowait**
> 不等待任务完成

**--force**
> 即使策略会阻止也强制打标签

**-h, --help**
> 显示帮助信息

# CAVEATS

打标签需要相应的权限。某些标签带有策略，限制哪些软件包可以被打上该标签。

# SEE ALSO

[koji](/man/koji)(1), [koji-untag-build](/man/koji-untag-build)(1), [koji-taginfo](/man/koji-taginfo)(1)
