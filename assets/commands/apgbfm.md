# TAGLINE

管理用于密码检查的布隆过滤器

# TLDR

从字典文件**创建**新的布隆过滤器

```apgbfm -f [filter.bf] -d [dictionary.txt]```

为指定数量的单词**创建**空布隆过滤器

```apgbfm -f [filter.bf] -n [50000]```

**检查**某个单词是否存在于过滤器中

```apgbfm -f [filter.bf] -c [password]```

向现有过滤器**添加**单个单词

```apgbfm -f [filter.bf] -a [word]```

将字典文件中的单词**添加**到现有过滤器

```apgbfm -f [filter.bf] -A [dictionary.txt]```

**显示**过滤器信息

```apgbfm -i [filter.bf]```

# SYNOPSIS

**apgbfm** **-f** _filter_ **-n** _numofwords_ [**-q**] [**-s**]
**apgbfm** **-f** _filter_ **-d** _dictfile_ [**-q**] [**-s**]
**apgbfm** **-f** _filter_ **-a** _word_ [**-q**]
**apgbfm** **-f** _filter_ **-A** _dictfile_ [**-q**]
**apgbfm** **-f** _filter_ **-c** _word_ [**-q**]
**apgbfm** **-f** _filter_ **-C** _dictfile_ [**-q**]
**apgbfm** **-i** _filter_
**apgbfm** [**-v**] [**-h**]

# DESCRIPTION

**apgbfm**（APG Bloom Filter Manager）为 apg 密码生成器创建和管理布隆过滤器。布隆过滤器无需将整个字典载入内存即可进行快速字典检查。它使用 SHA-1 作为哈希函数。

该工具可以独立使用，也可配合 apg/apgd 使用，避免生成出现在常见密码字典中的密码。

# PARAMETERS

**-f** _filter_
> 要使用的布隆过滤器文件名

**-n** _numofwords_
> 为指定数量的单词创建新的空过滤器

**-d** _dictfile_
> 从字典文件创建新过滤器

**-a** _word_
> 向过滤器添加单个单词

**-A** _dictfile_
> 将字典文件中的所有单词加入过滤器

**-c** _word_
> 检查某个单词是否存在于过滤器中

**-C** _dictfile_
> 用过滤器检查字典文件中的每个单词

**-i** _filter_
> 显示过滤器信息

**-s**
> 以不区分大小写模式创建过滤器

**-q**
> 安静模式

**-v**
> 打印版本信息

**-h**
> 打印帮助信息

# CAVEATS

布隆过滤器存在误报但不会漏报。被拒绝的密码可能实际上并不在字典里，但被接受的密码一定不在字典中。过滤器大小影响准确度。

# HISTORY

**apgbfm** 作为 apg 的配套工具而创建，利用布隆过滤器高效地将生成的密码与大型字典进行比对。

# INSTALL

```apt: sudo apt install apg```

```dnf: sudo dnf install apg```

```aur: yay -S apg```

```apk: sudo apk add apg```

```zypper: sudo zypper install apg```

```nix: nix profile install nixpkgs#apg```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apg](/man/apg)(1)
