# TAGLINE

管理 Linode 对象存储

# TLDR

**列出存储桶**

```linode-cli object-storage buckets-list```

**创建存储桶**

```linode-cli object-storage buckets-create --region [us-east] --label [my-bucket]```

**删除存储桶**

```linode-cli object-storage buckets-delete [cluster] [bucket]```

**列出访问密钥**

```linode-cli object-storage keys-list```

**创建访问密钥**

```linode-cli object-storage keys-create --label [my-key]```

# SYNOPSIS

**linode-cli object-storage** _command_ [_options_]

# PARAMETERS

**buckets-list**
> 列出所有存储桶。

**buckets-create**
> 创建存储桶。

**buckets-delete** _cluster_ _bucket_
> 删除存储桶。

**keys-list**
> 列出访问密钥。

**keys-create**
> 创建访问密钥。

**--region** _id_
> 区域 ID（取代已弃用的 --cluster）。

**--label** _name_
> 存储桶或密钥的标签。

# DESCRIPTION

**linode-cli object-storage** 管理 Linode 对象存储（兼容 S3）。可创建存储桶、管理访问密钥和配置存储。是 Linode CLI 的一部分。

# SEE ALSO

[linode-cli](/man/linode-cli)(1), [s3cmd](/man/s3cmd)(1)
