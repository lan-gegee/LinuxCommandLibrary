# TAGLINE

重置 Elasticsearch 内置用户的密码

# TLDR

**重置 elastic 用户密码**

```elasticsearch-reset-password -u elastic```

**使用自动生成的密码重置**

```elasticsearch-reset-password -u [username] -a```

**交互式重置**

```elasticsearch-reset-password -u [username] -i```

**指定批处理模式**

```elasticsearch-reset-password -u [username] -b```

# SYNOPSIS

**elasticsearch-reset-password** **-u** _username_ [_options_]

# PARAMETERS

**-u**, **--username** _user_
> 要重置的用户名。

**-a**, **--auto**
> 将密码重置为自动生成的强密码。这是默认行为。

**-i**, **--interactive**
> 提示输入新密码而不是自动生成。

**-b**, **--batch**
> 运行时不提示确认。

**-f**, **--force**
> 即使在不健康的集群上也强制运行。

**--url** _url_
> Elasticsearch API 的基础 URL。默认取自 elasticsearch.yml 推导出的值。

**-E** _setting=value_
> 配置标准的 Elasticsearch 或 X-Pack 设置。

**-s**, **--silent**
> 显示最少输出。

**-v**, **--verbose**
> 显示详细输出。

# DESCRIPTION

**elasticsearch-reset-password** 重置 native realm 用户或 **elastic**、**kibana_system** 等内置用户的密码。当 elastic 密码丢失时，它是恢复访问的推荐方式。

该工具必须以拥有 Elasticsearch 文件的用户身份，在集群的某个节点上运行，并且要求集群正在运行。不加 **-i** 时它会把新生成的密码打印到控制台；该输出是唯一一次显示密码的机会。

# CAVEATS

仅在启用了 Elasticsearch 安全特性时有效（8 版本起默认启用）。该命令通过 HTTPS 与集群通信，因此处于停机或不可达状态的集群无法重置密码，除非对仍在运行但不健康的集群使用 **-f**。

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1), [elasticsearch-users](/man/elasticsearch-users)(1)

# RESOURCES

```[Source code](https://github.com/elastic/elasticsearch)```

```[Homepage](https://www.elastic.co/elasticsearch)```

```[Documentation](https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/reset-password)```

<!-- verified: 2026-07-14 -->
