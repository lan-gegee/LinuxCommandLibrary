# TAGLINE

快速且容错的搜索引擎

# TLDR

**启动服务器**

```meilisearch```

**使用主密钥启动**

```meilisearch --master-key=[your-key]```

**指定数据目录**

```meilisearch --db-path=[/var/lib/meilisearch]```

**设置 HTTP 地址**

```meilisearch --http-addr=[127.0.0.1:7700]```

**以生产模式运行**

```meilisearch --env=production --master-key=[key]```

# SYNOPSIS

**meilisearch** [_options_]

# PARAMETERS

**--master-key** _key_
> 主 API 密钥。

**--db-path** _path_
> 数据库目录。

**--http-addr** _addr_
> 监听地址。

**--env** _mode_
> 环境（development/production）。

**--max-indexing-memory** _size_
> 索引时的内存限制。

**--log-level** _level_
> 日志级别。

# DESCRIPTION

**Meilisearch** 是一个快速且容错的搜索引擎。它开箱即用地提供即时搜索，支持容错、过滤、分面和高亮等功能。

Meilisearch 被设计为 Elasticsearch 和 Algolia 在较小规模应用场景下的替代方案。

# API USAGE

```bash
# Add documents
curl -X POST 'http://localhost:7700/indexes/movies/documents' \
  -H 'Content-Type: application/json' \
  --data-binary @movies.json

# Search
curl 'http://localhost:7700/indexes/movies/search?q=batman'
```

# CAVEATS

仅支持单节点（无集群）。索引大小受内存限制。生产环境必须配置主密钥。数据格式较为特殊。

# HISTORY

Meilisearch 由 **Clément Renault** 于 **2018 年**创建，是一个用 Rust 编写、易于使用的开源搜索引擎。

# INSTALL

```pacman: sudo pacman -S meilisearch```

```brew: brew install meilisearch```

```nix: nix profile install nixpkgs#meilisearch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1)
