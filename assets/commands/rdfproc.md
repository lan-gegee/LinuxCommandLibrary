# TAGLINE

处理和查询 RDF 数据存储

# TLDR

**查询 RDF 存储**

```rdfproc [store] query sparql - "[SELECT * WHERE { ?s ?p ?o }]"```

**解析 RDF 文件**

```rdfproc [store] parse [file.rdf]```

**序列化为指定格式**

```rdfproc [store] serialize ntriples```

**添加语句**

```rdfproc [store] add [subject] [predicate] [object]```

**打印所有语句**

```rdfproc [store] print```

# SYNOPSIS

**rdfproc** [_options_] _store_ _command_ [_args_]

# PARAMETERS

**parse** _file_
> 解析并加载 RDF 文件。

**query** _lang_ _uri_ _query_
> 执行查询。

**serialize** _format_
> 以指定格式输出。

**print**
> 打印所有语句。

**add** _s_ _p_ _o_
> 添加三元组。

**remove** _s_ _p_ _o_
> 移除三元组。

# DESCRIPTION

**rdfproc** 是一款基于 Redland RDF 库处理 RDF 数据的命令行工具。它可以解析、存储、查询和序列化 RDF 数据。

# EXAMPLES

```bash
# Create store and parse file
rdfproc mystore parse data.rdf

# SPARQL query
rdfproc mystore query sparql - "SELECT * WHERE { ?s ?p ?o } LIMIT 10"

# Serialize as N-Triples
rdfproc mystore serialize ntriples

# Add triple
rdfproc mystore add "http://example.org/s" "http://example.org/p" "value"

# Print all
rdfproc mystore print
```

# FORMATS

```
rdfxml   - RDF/XML
ntriples - N-Triples
turtle   - Turtle
```

# CAVEATS

属于 Redland RDF 库的一部分。存储默认是持久的。用 - 表示 stdin/stdout。

# HISTORY

rdfproc 属于 **Dave Beckett** 开发的 **Redland** RDF 库，自 2000 年起提供 RDF 处理能力。

# INSTALL

```apt: sudo apt install redland-utils```

```dnf: sudo dnf install redland```

```pacman: sudo pacman -S redland```

```apk: sudo apk add redland```

```zypper: sudo zypper install redland```

```brew: brew install redland```

```nix: nix profile install nixpkgs#redland```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rapper](/man/rapper)(1), [roqet](/man/roqet)(1), [redland](/man/redland)(3)
