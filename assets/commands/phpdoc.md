# TAGLINE

从 PHP 源码生成 API 文档

# TLDR

**生成文档**

```phpdoc -d [src/] -t [docs/]```

**指定配置文件**

```phpdoc -c [phpdoc.xml]```

**使用特定模板生成**

```phpdoc -d [src/] -t [docs/] --template="clean"```

**解析单个文件**

```phpdoc -f [file.php] -t [docs/]```

# SYNOPSIS

**phpdoc** [_options_]

# PARAMETERS

**-d**, **--directory** _path_
> 源码目录。

**-f**, **--filename** _file_
> 要解析的单个文件。

**-t**, **--target** _path_
> 输出目录。

**-c**, **--config** _file_
> 配置文件。

**--template** _name_
> 要使用的模板。

**--ignore** _pattern_
> 要忽略的模式（支持 glob，如 `"**/*test.php"`）。

**--visibility** _level_
> 按可见性过滤：public、protected、private、api 或 internal。

**--title** _text_
> 设置浏览器和模板标题。

**--encoding** _encoding_
> 设置文件编码（默认：UTF-8）。

# DESCRIPTION

**phpDocumentor**（phpdoc）从 PHP 源码生成 API 文档。它解析 DocBlock 注释以创建可导航的 HTML 文档。默认命令是 `phpdoc run`，也可以直接简写为 `phpdoc`。它支持配置文件（phpdoc.xml 或 phpdoc.dist.xml）以保存持久化设置，并提供多种输出模板。

# DOCBLOCK FORMAT

```php
/**
 * Short description.
 *
 * Long description.
 *
 * @param string $name The name
 * @return bool Success status
 * @throws Exception On failure
 */
```

# CONFIGURATION (phpdoc.xml)

```xml
<?xml version="1.0"?>
<phpdocumentor>
    <paths>
        <output>docs</output>
    </paths>
    <source>
        <path>src</path>
    </source>
</phpdocumentor>
```

# CAVEATS

需要编写规范的 DocBlock。大型项目处理耗时较长。各模板质量参差不齐。

# HISTORY

phpDocumentor 由 **Joshua Eichorn** 创建，现由 **Mike van Riel** 和社区维护。

# SEE ALSO

[doxygen](/man/doxygen)(1), [php](/man/php)(1), [composer](/man/composer)(1), [phpunit](/man/phpunit)(1)
