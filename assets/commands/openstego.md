# TAGLINE

将数据隐藏在图像中的隐写工具

# TLDR

**将数据嵌入图像**

```openstego embed -mf [secret.txt] -cf [cover.png] -sf [output.png]```

**从隐写图像中提取隐藏数据**

```openstego extract -sf [stego.png] -xd [output_dir]```

**使用口令加密嵌入**

```openstego embed -mf [secret.txt] -cf [cover.png] -sf [output.png] -e -p [password]```

**使用口令提取**

```openstego extract -sf [stego.png] -xd [output_dir] -p [password]```

**生成用于水印的签名**

```openstego gensig -gf [signature.sig] -p [password]```

**检查图像中是否存在水印**

```openstego checkmark -sf [image.png] -gf [signature.sig]```

**列出支持的隐写算法**

```openstego algorithms```

# SYNOPSIS

**openstego** _command_ [_options_]

# PARAMETERS

**embed**
> 使用隐写术将数据隐藏到封面图像中。

**extract**
> 从隐写图像中提取隐藏数据。

**gensig**
> 生成用于水印的签名文件。

**embedmark**
> 使用签名将水印嵌入封面文件。

**checkmark**
> 检查隐写文件中是否存在水印。

**algorithms**
> 显示支持的隐写算法。

**readformats**
> 显示支持的输入图像格式。

**writeformats**
> 显示支持的输出图像格式。

**-mf**, **--messagefile** _file_
> 要嵌入的消息文件（省略时从 stdin 读取）。

**-cf**, **--coverfile** _file_
> 封面图像文件（支持通配符以处理多个文件）。

**-sf**, **--stegofile** _file_
> 隐写文件（embed 时的输出图像，extract/checkmark 时的输入）。

**-gf**, **--sigfile** _file_
> 水印操作使用的签名文件。

**-xf**, **--extractfile** _file_
> 覆盖提取数据的文件名。

**-xd**, **--extractdir** _dir_
> 提取数据存放的目录（默认：当前目录）。

**-p**, **--password** _password_
> 用于加密/解密或签名生成的口令。

**-a**, **--algorithm** _name_
> 要使用的隐写算法。

**-e**, **--encrypt**
> 启用对嵌入消息的加密。

**-E**, **--noencrypt**
> 禁用加密（默认）。

**-c**, **--compress**
> 嵌入前压缩消息（默认）。

**-C**, **--nocompress**
> 跳过消息压缩。

**-A**, **--cryptalgo** _algorithm_
> 加密算法（AES128 或 AES256）。

# DESCRIPTION

**OpenStego** 是一款将数据隐藏在图像中的隐写工具。它支持两大操作：数据隐藏（将秘密消息嵌入封面图像）和数字水印（嵌入并验证不可见签名）。消息在嵌入前可选择进行压缩和加密。

# SUPPORTED FORMATS

```
Cover images: PNG, BMP, GIF, JPEG, WBMP
```

# CAVEATS

需要 Java 才能运行。较大的消息需要有足够大的封面图像。JPEG 有损压缩可能影响嵌入数据的可靠性；推荐使用 PNG。也提供图形界面。

# HISTORY

OpenStego 由 **Samir Vaidya** 创建，是一款支持多种算法的开源隐写应用。

# INSTALL

```aur: yay -S openstego```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[steghide](/man/steghide)(1), [outguess](/man/outguess)(1), [stegsnow](/man/stegsnow)(1)
