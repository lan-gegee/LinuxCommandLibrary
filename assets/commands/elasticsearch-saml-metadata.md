# TAGLINE

生成 SAML 服务提供方元数据

# TLDR

**生成 SAML 元数据**

```elasticsearch-saml-metadata```

**指定 realm 名称**

```elasticsearch-saml-metadata --realm [realm_name]```

**输出到文件**

```elasticsearch-saml-metadata --out [metadata.xml]```

**附带签名证书**

```elasticsearch-saml-metadata --signing-cert [cert.pem] --signing-key [key.pem]```

# SYNOPSIS

**elasticsearch-saml-metadata** [_options_]

# PARAMETERS

**--realm** _name_
> 要描述的 SAML realm。配置了多个 SAML realm 时必填。

**--out** _file_
> 输出文件路径。默认为 saml-elasticsearch-metadata.xml。

**--batch**
> 运行时不提示输入。

**--attribute** _name_
> 为指定的属性添加一个 `<RequestedAttribute>` 元素。可重复使用。

**--service-name** _name_
> `<ServiceName>` 的值。默认为 "elasticsearch"。

**--locale** _name_
> 元数据元素使用的区域设置。默认为 JVM 的区域设置。

**--contacts**
> 提示输入并包含 `<ContactPerson>` 元素。

**--organisation-name** _name_
> 包含一个使用此名称的 `<Organization>` 元素。

**--organisation-display-name** _name_
> 组织的显示名称。

**--organisation-url** _url_
> 组织的 URL。

**--signing-cert** _file_
> 用于签署元数据的 PEM 证书。

**--signing-key** _file_
> 与签名证书匹配的 PEM 私钥。

**--signing-key-password** _password_
> 保护签名私钥的密码。

**--signing-bundle** _file_
> 保存签名密钥对的 PKCS#12 文件，可作为 cert/key 对的替代方案。

**-E** _setting=value_
> 配置一个 Elasticsearch 设置。

# DESCRIPTION

**elasticsearch-saml-metadata** 生成 SAML 服务提供方元数据文档，身份提供方（IdP）需要该文档来信任 Elasticsearch。它从 elasticsearch.yml 读取 SAML realm 配置，并将实体 ID、断言消费者服务 URL 和单点注销端点写入一个 XML 文件，可以交给 IdP 管理员。

运行该命令之前 realm 必须已经配置好：该工具只是描述配置中的内容，并不创建配置。

# SEE ALSO

[elasticsearch](/man/elasticsearch)(1), [elasticsearch-users](/man/elasticsearch-users)(1)

# RESOURCES

```[Source code](https://github.com/elastic/elasticsearch)```

```[Homepage](https://www.elastic.co/elasticsearch)```

```[Documentation](https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/saml-metadata)```

<!-- verified: 2026-07-14 -->
