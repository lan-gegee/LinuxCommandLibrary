# TAGLINE

静态 Composer 软件仓库生成器

# TLDR

**构建仓库**

```satis build [satis.json] [output-dir]```

**构建指定的软件包**

```satis build [satis.json] [output-dir] [package1] [package2]```

**构建时无需用户交互**（例如在 CI 中）

```satis build -n [satis.json] [output-dir]```

**初始化配置**

```satis init [satis.json]```

**添加仓库**

```satis add [https://packagist.org] [satis.json]```

**清理旧文件**

```satis purge [satis.json] [output-dir]```

# SYNOPSIS

**satis** _command_ [_options_] [_args_]

# PARAMETERS

**build**
> 构建仓库。

**init**
> 创建配置。

**add**
> 添加仓库。

**purge**
> 移除旧文件。

**-n**
> 不进行交互。

**-v**
> 详细输出。

**-q**
> 安静输出。

# DESCRIPTION

**satis** 生成静态的 Composer 软件包仓库，为分发私有 PHP 软件包提供自托管的 Packagist 替代方案。它读取一个 JSON 配置文件，其中定义要包含哪些仓库和软件包，然后生成可由任意 Web 服务器提供的静态文件。

生成的仓库充当私有与公共软件包的本地镜像和缓存。团队可以选择性地从 Packagist 或其他来源镜像特定软件包，从而减少对外部的依赖并提高安装速度。由于输出是纯静态文件，除基本的 HTTP 服务器外无需任何特殊的服务端软件。

# CAVEATS

需要 Composer。需要磁盘空间存放软件包。更新时需重新构建。

# HISTORY

**Satis** 与 **Composer** 一同开发，旨在提供一种托管私有 Composer 软件包仓库的简单方式。

# SEE ALSO

[composer](/man/composer)(1), [packagist](/man/packagist)(1)
