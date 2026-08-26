# TAGLINE

将 XML 实体解码为字符

# TLDR

**反转义字符串中的 XML 实体**

```xml unescape "[&lt;text&gt;]"```

**从 stdin 反转义 XML 实体**

```echo "[&lt;text&gt;]" | xml unescape```

**使用短别名**

```xml unesc "[&lt;text&gt;]"```

# SYNOPSIS

**xml unescape** [_options_] [_text_]

# PARAMETERS

_text_
> 含 XML 实体的文本。若未提供则从标准输入读取。

**--help**
> 显示用法信息。

# DESCRIPTION

**xml unescape**（也可写作 `xml unesc`）将 XML 实体转换回原始字符。属于 XMLStarlet 工具集。可解码 &amp;lt; &amp;gt; &amp;amp; &amp;apos; &amp;quot; 以及数字字符引用为原始字符。

# INSTALL

```dnf: sudo dnf install xmlstarlet```

```pacman: sudo pacman -S xmlstarlet```

```apk: sudo apk add xmlstarlet```

```zypper: sudo zypper install xmlstarlet```

```brew: brew install xmlstarlet```

```nix: nix profile install nixpkgs#xmlstarlet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xml-escape](/man/xml-escape)(1), [xml-select](/man/xml-select)(1), [xmlstarlet](/man/xmlstarlet)(1)
