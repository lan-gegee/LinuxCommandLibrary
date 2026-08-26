# TAGLINE

将虚拟机导出为 OVF/OVA 格式

# TLDR

**将虚拟机导出为 OVA 文件**

```vboxmanage export [vmname] -o [file.ova]```

**导出虚拟机并生成用于完整性校验的清单文件**

```vboxmanage export [vmname] -o [file.ova] --manifest```

**将多个虚拟机导出到一个 appliance 中**

```vboxmanage export [vm1] [vm2] -o [file.ova]```

**以 OVF 2.0 格式导出**

```vboxmanage export [vmname] -o [file.ovf] --ovf20```

**导出时附带自定义的产品和供应商元数据**

```vboxmanage export [vmname] -o [file.ova] --vsys 0 --product [product_name] --vendor [vendor_name]```

# SYNOPSIS

**vboxmanage** **export** _vmname_... **-o** _file_ [_options_]

# PARAMETERS

**-o**, **--output** _file_
> 输出文件。单文件归档用 .ova，多文件用 .ovf。

**--legacy09**
> 以 OVF 0.9 旧版格式导出。

**--ovf10**
> 以 OVF 1.0 格式导出（默认）。

**--ovf20**
> 以 OVF 2.0 格式导出。

**--manifest**
> 附带含 SHA 摘要的清单文件以供完整性校验。

**--options** _option_[,...]
> 逗号分隔的导出选项：manifest、iso、nomacs、nomacsbutnat。

**--vsys** _n_
> 为每台虚拟机单独设置时指定虚拟系统编号（从 0 开始）。

**--vmname** _name_
> 覆盖导出的 appliance 中的虚拟机名称。

**--product** _name_
> 在 appliance 元数据中设置产品名称。

**--producturl** _url_
> 在 appliance 元数据中设置产品 URL。

**--vendor** _name_
> 在 appliance 元数据中设置供应商名称。

**--vendorurl** _url_
> 在 appliance 元数据中设置供应商 URL。

**--version** _string_
> 在 appliance 元数据中设置版本字符串。

**--description** _text_
> 在 appliance 元数据中设置描述。

**--eula** _text_
> 嵌入最终用户许可协议文本。

**--eulafile** _filename_
> 从文件嵌入 EULA。

# DESCRIPTION

**vboxmanage export** 将一台或多台虚拟机导出为开放虚拟化格式（OVF/OVA）。这会创建可移植的 appliance 包，适合分享、备份或迁移到其他虚拟化平台。OVA 是包含所有 appliance 文件的单文件 tar 归档；OVF 则生成一个目录，其中描述符、磁盘和清单文件各自独立。针对单台虚拟机的元数据选项（product、vendor、description 等）需要通过 **--vsys** 指定适用的虚拟机。

# SEE ALSO

[vboxmanage](/man/vboxmanage)(1), [vboxmanage-import](/man/vboxmanage-import)(1), [vboxmanage-clonevm](/man/vboxmanage-clonevm)(1)
