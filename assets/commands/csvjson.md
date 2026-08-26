# TAGLINE

CSV 转 JSON 转换器

# TLDR

将 CSV 转换为 JSON 数组

```csvjson [data.csv]```

带缩进转换以便阅读

```csvjson -i [4] [data.csv]```

转换为换行符分隔的 JSON（每行一个对象）

```csvjson --stream [data.csv]```

使用某列作为键生成对象输出

```csvjson -k [id] [data.csv]```

根据经纬度列转换为 GeoJSON

```csvjson --lat [latitude] --lon [longitude] [data.csv]```

使用自定义分隔符转换

```csvjson -d "[;]" [data.csv]```

通过管道从 stdin 转换

```cat [data.csv] | csvjson```

禁用类型推断（所有值保持为字符串）

```csvjson --no-inference [data.csv]```

# SYNOPSIS

**csvjson** [_options_] _file_

# PARAMETERS

_FILE_
> 要转换的 CSV 文件。未指定时使用 stdin。

**-i** _N_, **--indent** _N_
> 格式化输出的缩进级别。

**-k** _COLUMN_, **--key** _COLUMN_
> 用作对象键的列（生成对象而不是数组）。

**--stream**
> 输出换行符分隔的 JSON（每行一个对象）。

**--lat** _COLUMN_
> GeoJSON 输出的纬度列。

**--lon** _COLUMN_
> GeoJSON 输出的经度列。

**-d** _CHAR_, **--delimiter** _CHAR_
> 字段分隔符（默认：逗号）。

**-e** _ENCODING_, **--encoding** _ENCODING_
> 输入文件编码。

**--no-inference**
> 禁用类型推断（所有值保持为字符串）。

**-H**, **--no-header-row**
> 将文件视为没有表头行；列依次标记为 a、b、c 等。

**--snifflimit** _N_
> 将 CSV 方言探测限制在前 N 字节内（0 表示禁用）。

# DESCRIPTION

**csvjson** 是 csvkit 的组成部分，把 CSV 文件转换为 JSON 格式。它支持多种输出格式，包括 JSON 数组、带键对象、用于流式处理的换行符分隔 JSON，以及面向地理数据的 GeoJSON。

默认输出是一个 JSON 对象数组，每一行变成一个以列名为键的对象。**-k** 选项则利用唯一列的值作为键，生成带键的对象。

类型推断会适当地转换数字和布尔值。流式模式每行输出一个 JSON 对象，适合配合 jq 等工具处理，也适合不宜整体加载的大文件。

# CAVEATS

**-k** 选项要求键列的值唯一。不使用流式模式时，大文件可能占用大量内存。GeoJSON 输出要求有效的经纬度值。类型推断有时可能误判某些值。

# HISTORY

csvjson 是 **csvkit** 的一部分，由 Christopher Groskopf 于 **2011** 年创建。它让表格数据能够轻松转换为 JSON——这一 Web API 和 JavaScript 应用的主流格式。

# SEE ALSO

[in2csv](/man/in2csv)(1), [jq](/man/jq)(1), [csvkit](/man/csvkit)(1), [miller](/man/miller)(1), [csvlook](/man/csvlook)(1), [csvsql](/man/csvsql)(1)
