# TAGLINE

反解码（demangle）C++ 和 Java 符号名

# TLDR

**反解码 C++ 符号**

```c++filt [_Z1fv]```

**从 stdin 反解码**

```echo "[_Z3fooi]" | c++filt```

**不显示函数参数**的反解码

```c++filt -p [symbol]```

**连同类型一起**反解码

```c++filt -t [symbol]```

**去除前导下划线**

```c++filt -_ [symbol]```

**反解码 ELF 的动态符号**

```readelf -W --dyn-syms [binary] | c++filt```

# SYNOPSIS

**c++filt** [_options_] [_symbol_...]

# DESCRIPTION

**c++filt** 将 C++ 和 Java 的底层符号名解码（demangle）为用户可读的原始形式。C++ 编译器为支持重载会对函数名进行编码，此工具可逆转该过程。

不带参数时从 stdin 读取符号。可以处理包含编码名称的完整汇编源文件。

# PARAMETERS

**-_**, **--strip-underscore**
> 去除符号开头的下划线

**-n**, **--no-strip-underscore**
> 不去除开头的下划线

**-p**, **--no-params**
> 不显示函数参数类型

**-t**, **--types**
> 除函数名外也解码类型

**-s** _format_, **--format**=_format_
> 指定编码格式（gnu、lucid、arm、hp、edg、gnu-v3、java、gnat、dlang、rust）

**-r**, **--no-recurse-limit**
> 禁用递归限制（默认：2048 层）

**--help**
> 显示帮助

**--version**
> 显示版本

# EXAMPLES

```
$ c++filt _Z3fooi
foo(int)

$ c++filt _ZN3Bar3bazEv
Bar::baz()
```

# CAVEATS

编码名必须是完整的词法单元——末尾的标点会导致无法解码。不同编译器使用不同的编码方案；可用 -s 指定格式。

# INSTALL

```apt: sudo apt install binutils```

```dnf: sudo dnf install binutils```

```pacman: sudo pacman -S binutils```

```apk: sudo apk add binutils```

```zypper: sudo zypper install binutils```

```brew: brew install binutils```

```nix: nix profile install nixpkgs#binutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nm](/man/nm)(1), [objdump](/man/objdump)(1), [readelf](/man/readelf)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/binutils/)```

```[Documentation](https://sourceware.org/binutils/docs/)```

<!-- verified: 2026-06-22 -->
