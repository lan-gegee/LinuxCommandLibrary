# TAGLINE

对 RDF 数据执行 SPARQL 和 RDQL 查询

# TLDR

**执行 SPARQL 查询**

```roqet -i sparql "[query]" [data.rdf]```

**从文件查询**

```roqet -i sparql [query.rq] [data.rdf]```

**查询并返回结果**

```roqet -r json -i sparql "[SELECT * WHERE { ?s ?p ?o }]" [data.rdf]```

**解释查询**

```roqet -e "[query]"```

# SYNOPSIS

**roqet** [_options_] [_query_] [_data_]

# PARAMETERS

**-i**, **--input** _format_
> 查询格式（sparql、rdql）。

**-r**, **--results** _format_
> 输出格式（xml、json、csv）。

**-e**, **--exec** _query_
> 执行查询字符串。

**-D**, **--data** _uri_
> 数据源。

**-d**, **--dump-query**
> 显示解析后的查询。

# DESCRIPTION

**roqet** 是 Redland RDF 库提供的 SPARQL/RDQL 查询工具。它对 RDF 数据执行查询，并以多种格式输出结果。

属于 Redland RDF 库的一部分。

# EXAMPLES

```bash
# Simple SPARQL query
roqet -i sparql "SELECT * WHERE { ?s ?p ?o } LIMIT 10" data.rdf

# Query from file
roqet -i sparql query.rq data.ttl

# JSON results
roqet -r json -i sparql "SELECT * WHERE { ?s ?p ?o }" data.rdf

# Query remote endpoint
roqet -i sparql "SELECT * WHERE { ?s ?p ?o } LIMIT 5" \
  -D http://dbpedia.org/sparql

# Explain query
roqet -d "SELECT * WHERE { ?s ?p ?o }"
```

# OUTPUT FORMATS

```
xml    - SPARQL Results XML
json   - SPARQL Results JSON
csv    - Comma-separated values
tsv    - Tab-separated values
```

# CAVEATS

属于 Redland RDF 库的一部分。支持 SPARQL 1.0。仅解析请使用 rapper。

# HISTORY

roqet 是 **Dave Beckett** 在 Redland 框架内开发的 **Rasqal** RDF 查询库的组成部分。

# INSTALL

```apt: sudo apt install rasqal-utils```

```dnf: sudo dnf install rasqal```

```pacman: sudo pacman -S rasqal```

```apk: sudo apk add rasqal```

```zypper: sudo zypper install rasqal```

```brew: brew install rasqal```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rapper](/man/rapper)(1), [rdfproc](/man/rdfproc)(1), [redland](/man/redland)(3)
