# TAGLINE

Chef cookbook 的依赖管理器

# TLDR

**安装 cookbook 依赖**

```berks install```

**更新指定的 cookbook**及其依赖

```berks update [cookbook-name]```

**上传 cookbook**到 Chef Infra Server

```berks upload```

**将 cookbook 打包**为归档

```berks package [output.tar.gz]```

**列出已安装的 cookbook**及依赖

```berks list```

**检查是否有更新的**cookbook 版本

```berks outdated```

**生成依赖关系图**可视化

```berks viz```

**显示 cookbook 信息**

```berks info [cookbook-name]```

# SYNOPSIS

**berks** _subcommand_ [_options_]

# DESCRIPTION

**berks**（Berkshelf）是 Chef cookbook 的依赖管理器。它解析并管理 Berksfile 中定义的 cookbook 依赖，类似于 Bundler 管理 Ruby gems 的方式。

Berkshelf 确保 cookbook 版本在开发、测试和生产环境中保持一致。它可以从 Chef Supermarket、Git 仓库或本地路径获取 cookbook。

# SUBCOMMANDS

**install**
> 根据 Berksfile.lock 将 cookbook 安装到本地缓存

**update**
> 更新一个或全部 cookbook 依赖

**upload**
> 将解析后的 cookbook 上传到 Chef Infra Server

**package**
> 将 cookbook 依赖打包成 tar 归档

**list**
> 列出 cookbook 及其依赖

**outdated**
> 显示有更新版本可用的 cookbook

**viz**
> 生成依赖关系图图像

**info**
> 显示指定 cookbook 的元数据

**apply**
> 将版本锁定应用到 Chef 环境

**vendor**
> 将 cookbook 收纳（vendor）到本地目录

**version**
> 显示 Berkshelf 版本

# PARAMETERS

**--format** _value_
> 输出格式：human（默认）、json、null

**--berksfile** _value_
> Berksfile 的路径

**--except** _value_
> 排除指定的 cookbook 组

**--only** _value_
> 仅包含指定的组

**-q, --quiet**
> 抑制输出

**-d, --debug**
> 启用调试输出

# CAVEATS

Berkshelf 已被弃用，不再积极维护。新用户应改用 **Policyfiles**，这是管理 Chef cookbook 依赖的推荐方式。现有的 Berkshelf 用户也建议迁移。

# HISTORY

Berkshelf 由 **Jamie Winsor** 和 **Seth Vargo** 于 **2012 年**创建，用于解决 Chef cookbook 的依赖管理问题。它后来成为 Chef Development Kit（ChefDK）乃至 Chef Workstation 的一部分。Chef 于 **2015 年**宣布 Policyfiles 为其继任者。

# SEE ALSO

[chef](/man/chef)(1), [knife](/man/knife)(1)
