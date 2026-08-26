# TAGLINE

解析并显示 ASN.1 编码数据

# TLDR

**解析** ASN.1 数据

```openssl asn1parse -in [file.der]```

解析 **PEM** 编码文件

```openssl asn1parse -in [file.pem] -inform PEM```

从指定**偏移量**开始解析

```openssl asn1parse -in [file.der] -offset [100]```

以十六进制转储显示**结构**

```openssl asn1parse -in [file.der] -dump```

解析给定偏移处的**嵌套** ASN.1 结构

```openssl asn1parse -in [file.pem] -strparse [offset]```

# SYNOPSIS

**openssl asn1parse** [**-help**] [**-inform** _DER|PEM_] [**-in** _filename_] [**-out** _filename_] [**-noout**] [**-offset** _number_] [**-length** _number_] [**-i**] [**-dump**] [**-dlimit** _num_] [**-strparse** _offset_] [**-genstr** _string_] [**-genconf** _file_] [**-strictpem**]

# DESCRIPTION

**asn1parse** 是 OpenSSL 的诊断工具，用于解析 ASN.1（抽象语法标记一）编码的数据。它以人类可读的格式显示证书、密钥和其他密码学对象的结构。

该工具对调试证书问题、理解数据结构以及分析编码数据非常有价值。

# PARAMETERS

**-help**
> 打印用法信息。

**-in** _filename_
> 输入文件，默认为标准输入。

**-inform** _DER|PEM_
> 输入格式；默认为 PEM。

**-out** _filename_
> 用于存放 DER 编码数据的输出文件。

**-noout**
> 不输出输入文件的解析结果。

**-offset** _number_
> 开始解析的起始偏移量，默认为文件开头。

**-length** _number_
> 要解析的字节数，默认解析到文件末尾。

**-i**
> 按结构的深度缩进输出。

**-dump**
> 以十六进制格式转储未知数据。

**-dlimit** _num_
> 与 **-dump** 类似，但只输出前 num 个字节。

**-strparse** _offset_
> 解析从 offset 开始的 ASN.1 对象的内容八位组。

**-genstr** _string_
> 根据 ASN1_generate_nconf 格式，基于字符串生成编码数据。

**-genconf** _file_
> 根据 ASN1_generate_nconf 格式，从文件生成编码数据。

**-strictpem**
> 忽略 PEM 中 BEGIN 标记之前或 END 标记之后的任何数据。

# CAVEATS

需要理解 ASN.1 结构。对于复杂对象，输出可能很冗长。主要用于调试而非日常使用。

# HISTORY

**asn1parse** 是 OpenSSL 的一部分，OpenSSL 自 **1990** 年代末以来一直是标准的密码学工具集。

# SEE ALSO

[openssl](/man/openssl)(1), [openssl-x509](/man/openssl-x509)(1), [openssl-req](/man/openssl-req)(1)
