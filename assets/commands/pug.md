# TAGLINE

将 Pug 模板编译为 HTML

# TLDR

**将 Pug 编译为 HTML**

```pug [file.pug]```

**编译到指定输出位置**

```pug [file.pug] -o [output/]```

**监视文件变化**

```pug -w [file.pug]```

**格式化输出**

```pug -P [file.pug]```

**编译目录**

```pug [src/] -o [dist/]```

# SYNOPSIS

**pug** [_options_] _files_...

# PARAMETERS

**-o**, **--out** _dir_
> 输出目录。

**-P**, **--pretty**
> 格式化打印输出。

**-w**, **--watch**
> 监视文件变化。

**-c**, **--client**
> 编译为客户端版本。

**-O**, **--obj** _json_
> locals 对象。

**--name** _name_
> 模板函数名称。

# DESCRIPTION

**Pug**（原名 Jade）是 Node.js 的模板引擎。它以简洁、对空白敏感的语法编译为 HTML，省去了闭合标签。

# EXAMPLES

```bash
# Compile file
pug index.pug

# Pretty output
pug -P template.pug

# Watch directory
pug -w -P views/ -o public/

# With data
pug -O '{"title":"Hello"}' page.pug

# Client-side template
pug -c template.pug
```

# PUG SYNTAX

```pug
doctype html
html
  head
    title= pageTitle
  body
    h1 Hello World
    p.intro Welcome
    ul
      each item in items
        li= item
```

# CAVEATS

需要 Node.js。对空白敏感（请保持一致的缩进）。因商标问题由 Jade 更名而来。

# HISTORY

Pug 由 **TJ Holowaychuk** 于 2010 年创建，名为 Jade；2016 年因商标问题更名为 Pug。

# INSTALL

```brew: brew install pug```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[node](/man/node)(1)
