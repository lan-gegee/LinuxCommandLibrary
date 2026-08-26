# TAGLINE

根据审计日志生成 SELinux 策略 allow 规则。

# TLDR

生成 **allow** 规则

```sudo audit2allow -a```

基于**日志文件**

```sudo audit2allow -i /var/log/audit/audit.log```

创建**策略模块**

```sudo audit2allow -a -M my_module```

**解释**拒绝原因

```sudo audit2allow -a -w```

生成**参考**策略

```sudo audit2allow -a -R```

针对特定**服务**

```sudo ausearch -m avc -c httpd | audit2allow -M httpd_policy```

# SYNOPSIS

**audit2allow** [_OPTIONS_]

# DESCRIPTION

**audit2allow** 从审计日志生成 SELinux 策略 allow 规则。它读取来自审计子系统的拒绝消息，并创建允许这些被拒操作的 type enforcement 规则。

该工具可以生成简单的 allow 规则用于快速排障，也可以通过 **-M** 选项生成完整的可加载策略模块。配合 **-R** 使用时，它使用标准宏生成参考策略，产出更整洁、更易维护的规则。通常在 **audit2why** 找出拒绝的根本原因之后使用本工具。

# PARAMETERS

**-a, --all**
> 从审计日志和系统消息日志读取输入。

**-b, --boot**
> 读取自上次启动以来的审计消息作为输入。

**-d, --dmesg**
> 从 dmesg 输出读取输入。

**-i, --input** _file_
> 从指定文件读取输入。

**-l, --lastreload**
> 只读取自上次策略重载以来的 AVC 拒绝记录。

**-m, --module** _name_
> 生成模块输出（源码形式，不打包）。

**-M** _name_
> 生成可加载的策略模块包（.pp）。

**-o, --output** _file_
> 将输出追加到指定文件。

**-D, --dontaudit**
> 生成 dontaudit 规则而非 allow 规则。

**-R, --reference**
> 使用已安装的接口宏生成参考策略。

**-N, --noreference**
> 不生成参考策略；使用传统 allow 规则。

**-w, --why**
> 将审计消息转换为说明访问被拒原因的描述。

**-e, --explain**
> 完整解释生成的输出。

**-x, --xperms**
> 生成扩展权限（ioctl）规则。

**-t, --type** _regex_
> 按类型正则表达式过滤输出。

**-C**
> 生成 CIL（Common Intermediate Language）格式的输出。

**-r, --requires**
> 为可加载模块生成 require 语句。

**-v, --verbose**
> 启用详细输出。

# CAVEATS

生成的策略在安装前应经过审查。盲目允许所有拒绝操作可能带来安全漏洞。请先用 audit2why 弄清拒绝发生的原因。

# HISTORY

**audit2allow** 属于 **policycoreutils-python-utils** 软件包，提供 SELinux 策略开发工具。

# SEE ALSO

[audit2why](/man/audit2why)(1), [ausearch](/man/ausearch)(8), [semodule](/man/semodule)(8)
