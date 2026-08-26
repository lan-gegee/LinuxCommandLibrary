# TAGLINE

先吸干 stdin 再写入文件

# TLDR

**用管道输出覆盖文件**

```cat [file.txt] | sort | sponge [file.txt]```

**过滤后原地保存**

```grep "[pattern]" [file.txt] | sponge [file.txt]```

**转换并覆盖**

```sed 's/old/new/g' [file.txt] | sponge [file.txt]```

**追加而非覆盖**

```echo "new line" | sponge -a [file.txt]```

# SYNOPSIS

**sponge** [_options_] _file_

# DESCRIPTION

**sponge** 读取标准输入并写入文件。与 shell 重定向不同，它会先读取全部输入再打开输出文件，因此可以安全地进行原地修改。

该工具是 moreutils 的一部分，解决了在管道中将同一个文件既作输入又作输出的问题。

# PARAMETERS

**-a**
> 追加到文件而非覆盖。

# EXAMPLES

不使用 sponge（会失败）：
```
sort file.txt > file.txt  # Results in empty file!
```

使用 sponge（可行）：
```
sort file.txt | sponge file.txt
```

# CAVEATS

会将整个输入载入内存。非常大的文件可能耗尽内存。属于 moreutils 软件包的一部分。内部会创建临时文件，并在可能的情况下以原子方式重命名。未指定文件时，sponge 输出到 stdout。

# HISTORY

**sponge** 是 **Joey Hess** 创建的 Unix 工具合集 **moreutils** 的一部分。它解决了 shell 脚本中一个常见陷阱：重定向到输入文件会在读取之前将其截断。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tee](/man/tee)(1), [cat](/man/cat)(1), [moreutils](/man/moreutils)(7)
