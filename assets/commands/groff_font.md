# TAGLINE

Groff 字体文件格式说明

# TLDR

**列出可用字体**

```groff -Tps -Z -f[fontname] < /dev/null```

**查看字体目录**

```ls /usr/share/groff/current/font/```

**查看字体文件内容**

```cat /usr/share/groff/current/font/devps/DESC```

# DESCRIPTION

**groff_font** 描述 GNU troff（groff）所用字体文件的格式。字体文件定义了字符度量、字距调整对（kerning pairs）以及文本排版所需的其他排印信息。

字体文件存放在 /usr/share/groff/ 下特定于设备的子目录中。每个输出设备（ps、pdf、html）都有自己的字体定义，其中 DESC 文件用于指定设备参数。

# FONT FILE FORMAT

```
name fontname
spacewidth n
slant n
ligatures ...
charset
char width type code
...
```

# FONT DIRECTORIES

```
/usr/share/groff/current/font/devps/   PostScript fonts
/usr/share/groff/current/font/devpdf/  PDF fonts
/usr/share/groff/current/font/devutf8/ UTF-8 terminal
/usr/share/groff/current/font/devhtml/ HTML output
```

# STANDARD FONTS

```
R   - Roman (Times)
I   - Italic
B   - Bold
BI  - Bold Italic
CR  - Courier Roman
H   - Helvetica
```

# CAVEATS

字体的可用性取决于设备。自定义字体需要正确安装。PostScript 字体需要 AFM 文件。现代用法可能更适合使用 pdfgroff。

# SEE ALSO

[groff](/man/groff)(1), [troff](/man/troff)(1), [afmtodit](/man/afmtodit)(1)
