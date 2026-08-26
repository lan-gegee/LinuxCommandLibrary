# TAGLINE

HCL2 配置文件的命令行编辑器

# TLDR

**从 stdin 的 HCL 中获取属性值**

```cat [file.hcl] | hcledit attribute get [resource.foo.bar.attr]```

**设置属性**（打印结果）

```cat [file.hcl] | hcledit attribute set [resource.foo.bar.attr] '["val"]'```

**就地更新文件**

```hcledit attribute set [resource.foo.bar.attr] '["val"]' -f [file.hcl] -u```

**移除属性**

```cat [file.hcl] | hcledit attribute rm [resource.foo.bar.attr]```

**列出块**

```cat [file.hcl] | hcledit block list```

**获取块**

```cat [file.hcl] | hcledit block get [resource.foo.bar]```

**格式化 HCL**

```hcledit fmt -f [file.hcl] -u```

# SYNOPSIS

**hcledit** [*global-flags*] *command*

# DESCRIPTION

**hcledit** 是一个无模式的 **HCL2** 命令行编辑器。它从 stdin（或 **-f** 指定的文件）读取 HCL，应用基于 token 的编辑且保留注释，然后将结果写到 stdout（或用 **-u** 就地更新）。它为 Terraform 风格的重构而设计，但同样适用于任何 HCL2 文件，并且不需要目标应用的二进制程序。

其操作覆盖属性（**get**、**set**、**append**、**rm**、**mv**、**replace**）、块（**list**、**get**、**append**、**new**、**rm**、**mv**）、body 内容提取以及 **fmt**。

可通过 Homebrew、发行版二进制文件或从源码执行 **make install** 安装。

# PARAMETERS

**attribute** get|set|append|rm|mv|replace ...

> 通过点分地址读取或修改属性（例如 **resource.foo.bar.nested.attr**）。

**block** list|get|append|new|rm|mv ...

> 检查或调整块及其标签。

**body** get

> 提取 body 内容。

**fmt**

> 格式化 HCL。

**-f**, **--file** *path*

> 输入文件（默认 **-** 表示 stdin）。

**-u**, **--update**

> 将修改就地写回文件。

# CAVEATS

仅支持 HCL2（不支持 HCL1）。无模式解析可能比应用自身的校验更宽松；批量编辑后务必审查差异，并运行 **terraform validate**（或等效的校验）。在 shell 中设置属性时，请小心地对字符串值加引号。

# INSTALL

```brew: brew install hcledit```

```nix: nix profile install nixpkgs#hcledit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[terraform](/man/terraform)(1), [hclfmt](/man/hclfmt)(1), [jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/minamijoyo/hcledit)```

<!-- verified: 2026-07-19 -->
