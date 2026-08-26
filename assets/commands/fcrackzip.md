# TAGLINE

破解受密码保护的 ZIP 归档

# TLDR

对字母数字密码（4-8 位）**暴力破解**

```fcrackzip [-b|--brute-force] [-l|--length] 4-8 [-c|--charset] aA1 [archive]```

使用**自定义字符集**暴力破解

```fcrackzip [-v|--verbose] [-b|--brute-force] [-l|--length] 3 [-c|--charset] a:$% [archive]```

包含**特殊字符**的暴力破解

```fcrackzip [-b|--brute-force] [-l|--length] 4 [-c|--charset] a! [archive]```

从指定密码**开始**暴力破解

```fcrackzip [-b|--brute-force] [-l|--length] 5 [-c|--charset] 1 [-p|--init-password] 12345 [archive]```

使用**词典**破解

```fcrackzip [-u|--use-unzip] [-D|--dictionary] [-p|--init-password] [wordlist] [archive]```

对破解性能**基准测试**

```fcrackzip [-B|--benchmark]```

# SYNOPSIS

**fcrackzip** [_options_] _archive_

# DESCRIPTION

**fcrackzip** 使用暴力破解或字典攻击破解受密码保护的 ZIP 归档。它可以针对归档的加密测试密码。

用于安全研究和找回遗忘的密码。

# PARAMETERS

**-b, --brute-force**
> 使用暴力破解模式

**-D, --dictionary**
> 使用字典模式

**-l, --length** _min-max_
> 密码长度范围

**-c, --charset** _set_
> 字符集（a=小写、A=大写、1=数字、!=特殊字符）

**-p, --init-password** _pass_
> 起始密码或词典

**-u, --use-unzip**
> 用 unzip 验证

**-v, --verbose**
> 详细输出

**-B, --benchmark**
> 性能基准测试

# CAVEATS

只可用于你拥有或有权访问的归档。长密码的暴力破解很慢。对于常见密码，字典攻击更快。

# INSTALL

```apt: sudo apt install fcrackzip```

```pacman: sudo pacman -S fcrackzip```

```brew: brew install fcrackzip```

```nix: nix profile install nixpkgs#fcrackzip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zip](/man/zip)(1), [unzip](/man/unzip)(1), [john](/man/john)(1)

# RESOURCES

```[Source code](https://github.com/hyc/fcrackzip)```

```[Homepage](http://oldhome.schmorp.de/marc/fcrackzip.html)```

<!-- verified: 2026-07-15 -->
