# TAGLINE

面向关联数据的原生图数据库平台

# TLDR

**启动 Neo4j 服务器**

```neo4j start```

**停止服务器**

```neo4j stop```

**检查状态**

```neo4j status```

**以控制台（前台）方式运行**

```neo4j console```

**打开 Cypher shell**

```cypher-shell```

**设置初始密码**

```neo4j-admin dbms set-initial-password [password]```

# SYNOPSIS

**neo4j** _command_ [_options_]

# PARAMETERS

**start**
> 在后台启动服务器。

**stop**
> 停止服务器。

**restart**
> 重启服务器。

**status**
> 检查服务器状态。

**console**
> 在前台运行。

**version**
> 打印 Neo4j 版本信息后退出。

**help**
> 打印 **neo4j** 启动器的用法信息。

# DESCRIPTION

**Neo4j** 是一款面向关联数据的原生图数据库平台。它使用 Cypher 查询语言，以节点和关系的形式存储数据。

对于涉及复杂关系的查询——在关系型数据库中需要代价高昂的联接操作——Neo4j 表现尤为出色。

# CYPHER EXAMPLES

```cypher
// Create node
CREATE (n:Person {name: 'Alice'})

// Create relationship
MATCH (a:Person), (b:Person)
WHERE a.name = 'Alice' AND b.name = 'Bob'
CREATE (a)-[:KNOWS]->(b)

// Query
MATCH (n:Person)-[:KNOWS]->(m)
RETURN n.name, m.name
```

# CONFIGURATION

```
/etc/neo4j/neo4j.conf
~/.neo4j/neo4j.conf
```

# CAVEATS

大型图的内存开销较高。社区版仅支持单节点。自 2025 年日历化版本发布起需要 Java 21 或更高版本。默认端点：Neo4j Browser 在端口 **7474**，Bolt 协议在端口 **7687**。管理操作（初始密码、dump/load、创建数据库）由 **neo4j-admin** 而非 **neo4j** 处理。

# HISTORY

Neo4j 由 **Neo4j, Inc.**（原名 Neo Technology）开发，1.0 版于 **2010 年**发布。它是属性图模型的开创者。

# INSTALL

```apk: sudo apk add neo4j```

```brew: brew install neo4j```

```nix: nix profile install nixpkgs#neo4j```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cypher-shell](/man/cypher-shell)(1), [redis-cli](/man/redis-cli)(1), [mongosh](/man/mongosh)(1)
