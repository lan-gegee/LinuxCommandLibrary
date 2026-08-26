# TAGLINE

为 in-toto 元数据文件添加加密签名

# TLDR

**签名链接文件**

```in-toto-sign -k [key.pem] -f [link_file]```

**签名布局文件**

```in-toto-sign -k [key] -f [root.layout]```

将签名**追加**到已有签名之后

```in-toto-sign -k [key] -f [file] -a```

将签好名的元数据**输出**到指定文件

```in-toto-sign -k [key] -f [input] -o [output]```

**验证**元数据文件上的签名

```in-toto-sign --verify -k [key.pub] -f [file]```

使用 GPG 密钥**签名**

```in-toto-sign -g [gpg_keyid] -f [file]```

# SYNOPSIS

**in-toto-sign** [_options_]

# PARAMETERS

**-k** _KEY_
> 用于签名的私钥文件。

**-f** _FILE_
> 要签名的文件（链接或布局）。

**-a**, **--append**
> 追加签名而不是替换。

**-o** _OUTPUT_
> 输出文件的路径。

**-g** [_KEYID ..._]
> 用于签名或验证的 GPG keyid

**--gpg-home** _PATH_
> GPG 主目录路径

**--verify**
> 验证签名而不是签名

**-v**
> 详细输出

**-q**
> 安静输出

**--version**
> 显示版本信息

**--help**
> 显示帮助信息

# DESCRIPTION

**in-toto-sign** 为 in-toto 元数据文件添加加密签名。它既可以签名构建步骤产生的链接文件，也可以签名定义供应链策略的布局文件。

可以为多方验证添加多个签名。该工具支持 GPG 和 PEM 两种密钥格式。

# CAVEATS

属于 in-toto 框架。需要兼容的密钥格式。签名必须与验证密钥匹配。

# HISTORY

in-toto-sign 是 **in-toto** 的一部分，由 **纽约大学** 安全系统实验室开发，用于供应链完整性验证。

# SEE ALSO

[in-toto-run](/man/in-toto-run)(1), [in-toto-record](/man/in-toto-record)(1)
