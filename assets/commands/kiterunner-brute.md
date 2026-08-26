# TAGLINE

对 API 端点执行传统的基于字典的爆破

# TLDR

**爆破 API 端点**

```kr brute [https://api.example.com] -w [wordlist.txt]```

**使用指定 HTTP 方法爆破**

```kr brute [url] -w [wordlist.txt] -X GET,POST```

**携带请求头爆破**

```kr brute [url] -w [wordlist.txt] -H "Authorization: Bearer [token]"```

# SYNOPSIS

**kr** **brute** [_options_] _target_

# PARAMETERS

**-w** _wordlist_
> 用于爆破的字典文件。

**-X** _methods_
> 要使用的 HTTP 方法。

**-H** _header_
> 添加自定义请求头。

**-t** _threads_
> 并发线程数。

**-o** _file_
> 输出文件。

# DESCRIPTION

**kr brute** 对 API 端点执行传统的基于字典的爆破。它是 Kiterunner（Assetnote 出品的 API 端点发现工具）的一部分，通过测试各种 HTTP 方法和路径来发现隐藏的端点。

# INSTALL

```nix: nix profile install nixpkgs#kiterunner```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[kiterunner-wordlist](/man/kiterunner-wordlist)(1), [gobuster](/man/gobuster)(1)
