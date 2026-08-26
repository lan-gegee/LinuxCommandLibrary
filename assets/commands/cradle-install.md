# TAGLINE

安装 Cradle PHP 框架及其软件包

# TLDR

**以默认选项运行交互式安装器**

```cradle install```

**强制安装，覆盖已有文件**

```cradle install -f```

**安装时不执行 SQL 设置**

```cradle install --skip-sql```

**安装时不更新软件包版本**

```cradle install --skip-versioning```

**安装时不创建缓存目录**

```cradle install --skip-mkdir```

**安装时不调整文件权限**

```cradle install --skip-chmod```

**在命令行上提供数据库凭据**

```cradle install -h [127.0.0.1] -u [root] -p [password]```

# SYNOPSIS

**cradle** **install** [_options_]

# PARAMETERS

**-f**, **--force**
> 强制安装，覆盖任何先前已安装的文件。

**--skip-sql**
> 跳过 SQL 设置步骤（数据库、种子数据、schema 导入）。

**--skip-versioning**
> 跳过更新软件包版本元数据。

**--skip-mkdir**
> 跳过创建缓存、上传和日志目录。

**--skip-chmod**
> 跳过为生成的目录设置文件系统权限。

**-h** _HOST_
> 启用 SQL 设置时所使用的数据库主机。

**-u** _USER_
> 数据库用户名。

**-p** _PASSWORD_
> 数据库密码。

# DESCRIPTION

**cradle install** 是 **Cradle** PHP 框架 CLI 的引导子命令。它会完成首次运行的各项设置：导入 SQL schema、在 `config/` 下写入配置、创建缓存与上传目录、应用文件权限，并向框架注册启用的软件包。

在不指定 **-f** 时该命令是幂等的；已有的配置和文件会被保留，并且可以通过各个 `--skip-*` 标志单独关闭某些阶段，以便在 Docker 镜像、CI 或部分重新部署中使用。

# CAVEATS

必须在 Cradle 项目根目录下运行。通过 **-p** 在命令行传入的凭据会出现在进程列表中；在有安全要求时，应优先使用环境变量或预先准备好的 `config/settings.php`。

# HISTORY

**cradle install** 是 **CradlePHP** 项目（github.com/CradlePHP）的一部分。它最初是一个实验性的后台软件包管理器，后来被合并进核心 `cradle` CLI，成为标准安装器。

# SEE ALSO

[cradle](/man/cradle)(1), [composer](/man/composer)(1), [php](/man/php)(1)
