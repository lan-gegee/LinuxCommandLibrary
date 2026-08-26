# TAGLINE

将每个 FILE 的前 10 行输出到标准输出

# TLDR

显示文件的**前 10 行**

```head path/to/file```

显示文件的前 **5 行**

```head -n 5 path/to/file```

显示文件的前 **100 字节**

```head -c 100 path/to/file```

显示除**最后 5 行**以外的所有内容

```head -n -5 path/to/file```

显示**多个文件**的开头几行

```head path/to/file1 path/to/file2```

不显示**文件名标题**

```head -q path/to/file1 path/to/file2```

# SYNOPSIS

**head** [_OPTION_]... [_FILE_]...

# DESCRIPTION

**head** 将每个 FILE 的前 10 行输出到标准输出。处理多个文件时，会在每个文件的内容前面加上含有文件名的标题。如果未指定文件，或 FILE 为 "-"，则从标准输入读取。

# PARAMETERS

**-c, --bytes=[-]NUM**
> 打印每个文件的前 NUM 字节；带前导 "-" 时，打印除最后 NUM 字节之外的所有内容

**-n, --lines=[-]NUM**
> 打印前 NUM 行而不是默认的 10 行；带前导 "-" 时，打印除最后 NUM 行之外的所有内容

**-q, --quiet, --silent**
> 从不打印含文件名的标题

**-v, --verbose**
> 总是打印含文件名的标题

**-z, --zero-terminated**
> 使用 NUL 作为行分隔符而不是换行符

# CAVEATS

NUM 可以带有倍数后缀：b（512）、kB（1000）、K（1024）、MB（1000*1000）、M（1024*1024），G、T、P、E、Z、Y 依此类推。也支持 KiB、MiB 等二进制前缀。

# HISTORY

**head** 自 Unix 早期版本起就一直是其组成部分，现收录于 GNU **coreutils**。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tail](/man/tail)(1), [cat](/man/cat)(1), [less](/man/less)(1), [more](/man/more)(1)
