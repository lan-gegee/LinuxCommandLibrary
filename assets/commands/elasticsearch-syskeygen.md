# TAGLINE

生成 Elasticsearch 系统加密密钥

# TLDR

**生成系统密钥**

```elasticsearch-syskeygen```

# SYNOPSIS

**elasticsearch-syskeygen** [_options_]

# DESCRIPTION

**elasticsearch-syskeygen** 在 Elasticsearch 配置目录中创建一个 **system_key** 文件。该密钥用于对称加密敏感数据，例如防止 Watcher 返回并存储包含明文凭证的信息。

# CAVEATS

该工具属于 X-Pack。生成的系统密钥在集群的所有节点上必须相同。较新版本请使用 **elasticsearch-keystore** 管理安全设置。

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1), [elasticsearch-keystore](/man/elasticsearch-keystore)(1)
