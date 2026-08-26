# TAGLINE

TigerGraph 图数据库查询 Shell

# TLDR

**连接 TigerGraph**

```gsql```

**从文件运行查询**

```gsql [query.gsql]```

**运行内联查询**

```gsql -g [graphname] "[GSQL query]"```

**指定图**

```gsql -g [mygraph]```

**以指定用户运行**

```gsql -u [username] -p [password]```

# SYNOPSIS

**gsql** [_options_] [_file_|_query_]

# PARAMETERS

**-g** _graph_
> 要使用的图名称。

**-u** _user_
> 用户名。

**-p** _password_
> 密码。

**-ip** _host_
> 服务器 IP 地址。

**--ssl**
> 使用 SSL 连接。

# DESCRIPTION

**GSQL** 是 TigerGraph（一款图数据库）的查询语言和 Shell。它提供类 SQL 的语法，用于图查询、数据加载和模式管理。

GSQL 支持模式匹配、图算法以及面向复杂图分析的过程式扩展。

# QUERY EXAMPLE

```gsql
USE GRAPH social

CREATE QUERY findFriends(VERTEX<Person> p) FOR GRAPH social {
  Start = {p};
  Friends = SELECT t FROM Start:s -(Knows:e)- Person:t;
  PRINT Friends;
}

INSTALL QUERY findFriends
RUN QUERY findFriends("person1")
```

# CAVEATS

需要安装 TigerGraph。运行前需要先安装查询。语法与标准 SQL 不同。必须先定义图模式。

# HISTORY

GSQL 由 **TigerGraph**（前身为 GraphSQL）开发，该公司由 **Yu Xu** 于 **2012 年**创立。TigerGraph 专注于海量图上的实时分析，GSQL 既可用于简单查询，也可用于复杂的图算法。

# SEE ALSO

[neo4j](/man/neo4j)(1)
