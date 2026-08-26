# TAGLINE

F-Droid 软件仓库管理工具

# TLDR

**更新仓库索引**

```fdroid update```

**从源码构建应用**

```fdroid build [app.id]```

**初始化仓库**

```fdroid init```

**发布已签名的应用**

```fdroid publish```

**检查元数据问题**

```fdroid lint [app.id]```

**检查应用更新**

```fdroid checkupdates [app.id]```

# SYNOPSIS

**fdroid** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：update、build、init、publish、lint 等。

**update**
> 更新软件仓库索引。

**build** _APP_
> 从源码构建应用。

**init**
> 初始化新仓库。

**publish**
> 发布已签名的应用。

**lint** _APP_
> 检查元数据问题。

**checkupdates** _APP_
> 检查可用的上游更新。

**scanner** _APP_
> 扫描 APK 中已知的非自由库。

**rewritemeta** _APP_
> 重新格式化并规范化元数据文件。

**deploy**
> 将仓库部署到服务器。

**import**
> 从源码仓库导入新应用。

**readmeta**
> 读取并验证元数据。

**-v**, **--verbose**
> 更详细的输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**fdroid** 是用于管理 F-Droid 仓库的服务端工具。它从源码构建 Android 应用，维护仓库元数据，并生成 F-Droid 客户端使用的索引文件。

该工具处理应用发布的完整工作流：从源码构建 APK、签名、生成元数据并发布到仓库。它通过从源码构建来践行 F-Droid 对开源的承诺。

fdroid 被 F-Droid 官方仓库以及托管开源 Android 应用的第三方仓库使用。

# CONFIGURATION

**config.yml**
> 仓库配置，包括仓库名称、描述和密钥库设置。

**metadata/**
> 存放各应用元数据文件的目录，描述构建配方和应用信息。

# CAVEATS

需要 Android SDK。构建应用需要大量资源。仓库搭建较复杂。签名需要进行密钥管理。

# HISTORY

fdroid 是 **F-Droid** 的服务端组件。F-Droid 是创立于 2010 年的开源 Android 应用仓库，让任何人都能够托管自己的自由软件 Android 应用仓库。

# SEE ALSO

[fdroidcl](/man/fdroidcl)(1), [apktool](/man/apktool)(1), [adb](/man/adb)(1)
