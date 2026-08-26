# TAGLINE

Linux 文件能力查看器

# TLDR

获取**能力**

```getcap path/to/file```

**递归**搜索

```getcap -r path/to/dir```

显示**所有**条目

```getcap -v path/to/file```

# SYNOPSIS

**getcap** [_OPTIONS_] _files_...

# DESCRIPTION

**getcap** 显示指定文件的能力。Linux capabilities 提供细粒度的特权控制，作为以 root 身份运行的替代方案，可以在不完全取得 root 权限的情况下赋予特定的提升权限。

# PARAMETERS

**-r**
> 递归搜索目录

**-v**
> 即使未设置能力也显示所有被搜索的条目

**-n**
> 以数字形式显示能力值

# CAVEATS

capabilities 是 setuid 程序的替代方案，提供更细粒度的特权控制。默认情况下只显示设置了能力的文件的输出。

# HISTORY

**getcap** 是 **libcap** 的一部分，在 Linux 上实现 POSIX 1003.1e capabilities。

# INSTALL

```apt: sudo apt install libcap2-bin```

```apk: sudo apk add libcap-getcap```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[setcap](/man/setcap)(8), [capabilities](/man/capabilities)(7)

# RESOURCES

```[Source code](https://git.kernel.org/pub/scm/libs/libcap/libcap.git/)```

```[Documentation](https://manpages.debian.org/getcap)```

<!-- verified: 2026-07-15 -->
