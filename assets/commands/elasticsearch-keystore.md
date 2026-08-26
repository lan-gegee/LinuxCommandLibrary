# TAGLINE

管理 Elasticsearch 的加密安全设置

# TLDR

**创建 keystore**

```elasticsearch-keystore create```

**创建受密码保护的 keystore**

```elasticsearch-keystore create -p```

**列出设置**

```elasticsearch-keystore list```

**添加设置**（提示输入值）

```elasticsearch-keystore add [setting.name]```

**从 stdin 添加设置**

```echo "[value]" | elasticsearch-keystore add --stdin [setting.name]```

**从文件添加设置**

```elasticsearch-keystore add-file [setting.name] [file]```

**显示某个设置的值**

```elasticsearch-keystore show [setting.name]```

**移除设置**

```elasticsearch-keystore remove [setting.name]```

**升级 keystore**

```elasticsearch-keystore upgrade```

# SYNOPSIS

**elasticsearch-keystore** _command_ [_options_]

# SUBCOMMANDS

**create**
> 创建新的 keystore。

**list**
> 列出 keystore 中的条目。

**add**
> 添加设置（提示输入值）。

**add-file**
> 从文件添加设置。

**remove**
> 移除设置。

**show**
> 显示设置的值。

**has-passwd**
> 检查 keystore 是否受密码保护。

**upgrade**
> 升级 keystore 格式。

**passwd**
> 更改 keystore 密码。

# PARAMETERS

**--stdin**
> 从 stdin 读取设置值（与 add 配合使用）。

**-f**, **--force**
> 不经提示直接覆盖现有设置。

**-p**
> 创建 keystore 时提示输入密码。

**-o** _file_
> 输出文件（与 show 配合使用）。

**-h**, **--help**
> 显示帮助。

**-s**, **--silent**
> 显示最少输出。

**-v**, **--verbose**
> 显示详细输出。

# DESCRIPTION

**elasticsearch-keystore** 管理 Elasticsearch 的安全设置 keystore。它以加密形式存储密码、API 密钥等敏感配置。

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1), [elasticsearch-certutil](/man/elasticsearch-certutil)(1)
