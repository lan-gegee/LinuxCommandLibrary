# TAGLINE

Internet Archive 命令行工具

# TLDR

从条目**下载所有文件**

```ia download [item-name]```

从条目**下载指定文件**

```ia download [item-name] --glob="[*.pdf]"```

向条目**上传文件**

```ia upload [item-name] [file]```

在归档中**搜索条目**

```ia search "[query]"```

以 JSON 格式**获取条目元数据**

```ia metadata [item-name]```

**列出**条目中的**文件**

```ia list [item-name]```

从条目**删除文件**

```ia delete [item-name] [file]```

**配置** Internet Archive 凭据

```ia configure```

# SYNOPSIS

**ia** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要执行的子命令。

**download**
> 从条目下载文件。

**upload**
> 向条目上传文件。

**delete**
> 从条目删除文件。

**search**
> 搜索 Internet Archive 目录。

**metadata**
> 获取或修改条目元数据。

**list**
> 列出条目中的文件。

**configure**
> 配置 Internet Archive 凭据。

**tasks**
> 获取目录任务的信息。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**ia** 是 Internet Archive 的官方命令行工具，由 **internetarchive** Python 软件包提供。它可用于下载、上传、搜索和管理 archive.org 馆藏中的条目。

该工具支持批量操作和脚本化，适合处理大型数据集的档案工作者和研究人员使用。它可以管理元数据、上传和删除文件，以及查询目录任务队列。身份验证通过从 archive.org 获取的类 S3 API 密钥完成。

# CAVEATS

上传和修改操作需要 archive.org 账户及 API 密钥。批量操作受速率限制约束。大文件传输可能耗时较长。通过 **pip install internetarchive** 安装。

# HISTORY

ia 由 **Internet Archive** 创建，用于以命令行方式访问其数字图书馆。

# SEE ALSO

[wget](/man/wget)(1), [curl](/man/curl)(1), [youtube-dl](/man/youtube-dl)(1), [rclone](/man/rclone)(1)
