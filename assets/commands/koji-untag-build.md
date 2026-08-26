# TAGLINE

从一个或多个 Koji 构建中移除标签

# TLDR

从构建中**移除标签**

```koji untag-build [tag] [name-version-release]```

从多个构建中**移除标签**

```koji untag-build [tag] [nvr1] [nvr2]```

移除软件包**所有版本**的标签

```koji untag-build [tag] [package] --all```

移除除**最新版本**外所有版本的标签

```koji untag-build [tag] [package] --non-latest```

以**试运行**预览变更

```koji untag-build [tag] [nvr] --test```

移除标签并带**详细**输出

```koji untag-build [tag] [nvr] --verbose```

# SYNOPSIS

**koji untag-build** [_options_] _tag_ _pkg_ [_pkg_...]

# DESCRIPTION

**koji untag-build** 从 Koji 构建系统中的一个或多个构建上移除标签。可以通过 name-version-release（NVR）指定构建；配合 `--all` 或 `--non-latest` 时也可以按软件包名称指定。该命令用于将软件包从仓库中移除或清理旧构建。

# PARAMETERS

**--all**
> 移除该标签下此软件包所有版本的标签。

**--non-latest**
> 移除除最新版本外所有版本的标签。

**-n**, **--test**
> 测试模式 -- 只显示将要执行的操作而不实际执行。

**-v**, **--verbose**
> 输出详细信息。

**-h**, **--help**
> 显示帮助信息。

# CAVEATS

移除构建的标签可能影响仓库内容及其下游使用者。应用变更前先用 `--test` 预览。需要相应的 Koji 权限。

# SEE ALSO

[koji](/man/koji)(1), [koji-tag-build](/man/koji-tag-build)(1), [koji-build](/man/koji-build)(1)
