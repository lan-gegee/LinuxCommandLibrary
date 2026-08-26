# TAGLINE

将编译后的 gettext MO 文件转回人类可读的 PO 格式

# TLDR

**将 MO 转换为 PO**

```msgunfmt [messages.mo] -o [messages.po]```

**转换 Java properties**

```msgunfmt --java -d [classes/] -l [locale] -o [output.po]```

**指定输出编码**

```msgunfmt --output-encoding=[UTF-8] [messages.mo] -o [messages.po]```

# SYNOPSIS

**msgunfmt** [_options_] _inputfile_

# PARAMETERS

**-o** _file_
> 输出文件。

**--java**
> Java ResourceBundle 模式。

**-d** _dir_
> Java 模式的类目录。

**-l** _locale_
> Java 模式的语言环境。

**--output-encoding** _enc_
> 输出字符编码。

**--no-wrap**
> 不对长的消息行折行。

**--sort-output**
> 生成排序后的输出。

**-v, --verbose**
> 提高详细程度级别。

# DESCRIPTION

**msgunfmt** 将编译后的 gettext MO（machine object）文件转回人类可读的 PO（portable object）格式。也可以从 Java ResourceBundle 类中提取翻译。属于 GNU gettext。

# INSTALL

```apt: sudo apt install gettext```

```dnf: sudo dnf install gettext```

```pacman: sudo pacman -S gettext```

```apk: sudo apk add gettext```

```brew: brew install gettext```

```nix: nix profile install nixpkgs#gettext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msgfmt](/man/msgfmt)(1), [msgcat](/man/msgcat)(1), [msgattrib](/man/msgattrib)(1)
