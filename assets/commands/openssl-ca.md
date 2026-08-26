# TAGLINE

极简证书颁发机构应用程序

# TLDR

**签署证书请求**

```openssl ca -in [request.csr] -out [certificate.crt]```

**使用指定 CA 签署**

```openssl ca -config [ca.cnf] -cert [ca.crt] -keyfile [ca.key] -in [request.csr] -out [cert.crt]```

**吊销证书**

```openssl ca -revoke [certificate.crt]```

**生成 CRL**

```openssl ca -gencrl -out [crl.pem]```

**列出已签发的证书**

```openssl ca -status [serial_number]```

# SYNOPSIS

**openssl ca** [_options_] [**-in** _csr_] [**-out** _cert_] [**-infiles** _csr_...]

# PARAMETERS

**-in** _file_
> 输入的 CSR（PEM 编码）。若要在一次调用中签署多个 CSR，请改用 **-infiles**。

**-infiles** _file_...
> 签署列在此选项之后的每个 CSR（必须是命令行上的最后一个选项）。

**-out** _file_
> 输出证书文件（默认：stdout）。

**-config** _file_
> OpenSSL 配置文件（默认为 **/etc/ssl/openssl.cnf**）。

**-cert** _file_
> 用于签署的 CA 证书。

**-keyfile** _file_
> CA 私钥（PEM、ENGINE URI 或 PKCS#11 URI）。

**-days** _n_
> 证书有效期（从今天起算的天数）。

**-startdate** _YYMMDDHHMMSSZ_, **-not_before** _date_
> 显式指定的证书生效日期。

**-enddate** _YYMMDDHHMMSSZ_, **-not_after** _date_
> 显式指定的证书到期日期。

**-md** _alg_
> 消息摘要算法（例如 **sha256**、**sha384**）。

**-policy** _name_
> 配置文件中的 CA 策略节（控制哪些 DN 字段必须与 CA 匹配）。

**-extensions** _section_
> 包含要添加的证书扩展的配置节。

**-extfile** _file_
> 从额外的文件读取扩展（与 **-extensions** 搭配使用）。

**-subj** _dn_
> 覆盖来自 CSR 的主题名（例如 `/CN=example/O=Acme`）。

**-batch**
> 非交互模式——无需确认提示直接签署。

**-notext**
> 不在输出中包含人类可读的文本转储。

**-noemailDN**
> 从证书主题中移除 **emailAddress** RDN。

**-create_serial**
> 若序列号文件缺失则生成新的随机序列号。

**-revoke** _file_
> 在 CA 数据库中将给定证书标记为已吊销。

**-crl_reason** _reason_
> 吊销原因（**unspecified**、**keyCompromise**、**CACompromise**、**affiliationChanged**、**superseded**、**cessationOfOperation**、**certificateHold**、**removeFromCRL**）。

**-status** _serial_
> 打印具有给定序列号的证书的吊销状态。

**-gencrl**
> 使用当前数据库生成 CRL。

**-crldays** _n_, **-crlhours** _n_
> 距下一次预期 CRL 的有效时长。

# DESCRIPTION

**openssl ca** 是一个极简的证书颁发机构（CA）应用程序。它签署证书请求（CSR）、维护已签发证书的平面文件数据库（**index.txt**）、跟踪下一个序列号（**serial**），并生成 X.509 证书吊销列表（CRL）。

默认情况下，该命令从 **openssl.cnf** 的 **[ca]** 节读取配置，该节会选择一个默认 CA 节（**default_ca**），描述 CA 证书/密钥的位置、数据库、序列号文件、已签发证书目录（**newcerts/**）、策略以及要应用的扩展。大多数选项都可以在那里设置而不必放在命令行上。

# CA SETUP

```
# Initialize CA
mkdir -p demoCA/{certs,crl,newcerts,private}
touch demoCA/index.txt
echo '01' > demoCA/serial
```

# CAVEATS

生产环境请使用正规的 CA 软件。数据库格式是专有的。配置对初学者来说较复杂。

# HISTORY

openssl ca 命令自早期版本起就是 OpenSSL 的一部分，提供基本的 CA 功能。

# INSTALL

```apt: sudo apt install openssl```

```dnf: sudo dnf install openssl```

```pacman: sudo pacman -S openssl```

```apk: sudo apk add openssl```

```zypper: sudo zypper install openssl```

```brew: brew install openssl```

```nix: nix profile install nixpkgs#openssl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[openssl-req](/man/openssl-req)(1), [openssl-x509](/man/openssl-x509)(1), [openssl-crl](/man/openssl-crl)(1)
