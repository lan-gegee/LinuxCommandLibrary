# TAGLINE

加载、替换和管理 AppArmor 安全配置。

# TLDR

向内核**加载**一个配置

```sudo apparmor_parser -a [profile_file]```

**替换**现有配置

```sudo apparmor_parser -r [profile_file]```

从内核**移除**一个配置

```sudo apparmor_parser -R [profile_name]```

以 **complain 模式**加载配置

```sudo apparmor_parser -C -r [path/to/profile]```

**预处理**配置并将二进制缓存写入文件

```apparmor_parser -p -o [path/to/output.cache] -Q [path/to/profile]```

替换配置的同时**跳过缓存**读取

```sudo apparmor_parser -r -T [path/to/profile]```

# SYNOPSIS

**apparmor_parser** [_options_] _command_ [_profiles_...]

# DESCRIPTION

**apparmor_parser** 用于加载、编译和管理 AppArmor 安全配置。它解析文本格式的配置并加载到内核中。解析器还支持配置缓存，加快后续加载速度。

# PARAMETERS

**-a, --add**
> 将配置添加/加载到内核

**-r, --replace**
> 替换内核中的现有配置

**-R, --remove**
> 从内核移除一个配置

**-C, --Complain**
> 强制配置以 complain 模式加载（记录违规但不阻止）。

**-B, --binary**
> 将输入视为预编译的二进制缓存文件而非文本配置。

**-p, --preprocess**
> 通过展开 include 预处理配置，但不加载。

**-o, --ofile file**
> 将编译后的二进制配置写入指定文件。

**-S, --stdout**
> 将编译后的二进制配置写到 stdout。

**-Q, --skip-kernel-load**
> 执行除实际将配置加载进内核之外的所有操作。

**-T, --skip-read-cache**
> 跳过读取缓存；总是重新编译。

**-W, --write-cache**
> 将编译后的配置写入缓存目录。

**-K, --skip-cache**
> 同时禁用缓存的读取和写入。

**-L, --cache-loc dir**
> 指定缓存目录位置。

**-m, --match-string string**
> 覆盖编译时使用的内核特性集。

**-v, --verbose**
> 报告每个配置的加载情况并显示警告。

**-d, --debug**
> 检查语法正确性；使用两次还会输出解析器的解释结果。

**--warn=n**
> 启用特定的编译警告。

**--abort-on-error**
> 在第一个错误处停止处理，而不是继续。

# CONFIGURATION

**/etc/apparmor.d/**
> 存放启动时加载的 AppArmor 安全配置的目录。

**/etc/apparmor.d/cache/**
> 存放已编译二进制配置缓存的目录。

# CAVEATS

配置必须语法正确，否则加载会失败。加载前可用 **-p** 预处理并检查错误。

# HISTORY

**AppArmor** 应用安全框架的一部分，由 Immunix 开发，后被 Novell 收购，现由 Canonical 维护。

# INSTALL

```apt: sudo apt install apparmor```

```pacman: sudo pacman -S apparmor```

```apk: sudo apk add apparmor```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aa-status](/man/aa-status)(8), [aa-enforce](/man/aa-enforce)(8), [aa-complain](/man/aa-complain)(8), [apparmor](/man/apparmor)(7)

# RESOURCES

```[Source code](https://gitlab.com/apparmor/apparmor)```

```[Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/home)```

<!-- verified: 2026-06-11 -->
