# TAGLINE

RDF 数据存储与处理库

# TLDR

**解析 RDF 文件**

```rapper -i rdfxml -o ntriples [file.rdf]```

**查询 RDF 存储**

```roqet -i sparql "[query]" [data.rdf]```

**处理 RDF**

```rdfproc [store] parse [file.rdf]```

# SYNOPSIS

Redland RDF 库及其工具

# UTILITIES

**rapper**
> RDF 解析工具。

**roqet**
> RDF 查询工具。

**rdfproc**
> RDF 处理工具。

# DESCRIPTION

**Redland** 是一套用于处理 RDF（Resource Description Framework，资源描述框架）数据的 C 语言库和命令行工具。它全面支持 RDF 的解析、存储、SPARQL 查询和序列化，涵盖 RDF/XML、Turtle、N-Triples、N-Quads 等多种格式。

该工具集包括用于格式转换和校验的 **rapper**、用于执行 SPARQL 查询的 **roqet**，以及用于管理持久化 RDF 存储的 **rdfproc**。这些工具可以在管道中组合，用于语义网数据的批量处理。

# EXAMPLES

```bash
# Parse RDF/XML to N-Triples
rapper -i rdfxml -o ntriples data.rdf

# Validate RDF
rapper -c data.rdf

# SPARQL query
roqet -i sparql "SELECT * WHERE { ?s ?p ?o } LIMIT 10" data.rdf

# Convert formats
rapper -i turtle -o rdfxml data.ttl > data.rdf

# Create and query store
rdfproc mystore parse data.rdf
rdfproc mystore query sparql - "SELECT * WHERE { ?s ?p ?o }"
```

# FORMATS

```
rdfxml   - RDF/XML
ntriples - N-Triples
turtle   - Turtle
nquads   - N-Quads
trig     - TriG
```

# CAVEATS

基于库（librdf）。不同任务使用不同的工具。支持 SPARQL 1.0。

# HISTORY

Redland 由 **Dave Beckett** 自 2000 年起创建，是一套全面的 RDF 库。

# INSTALL

```dnf: sudo dnf install redland```

```pacman: sudo pacman -S redland```

```zypper: sudo zypper install redland```

```brew: brew install redland```

```nix: nix profile install nixpkgs#redland```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rapper](/man/rapper)(1), [roqet](/man/roqet)(1), [rdfproc](/man/rdfproc)(1)
