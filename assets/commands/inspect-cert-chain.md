# TAGLINE

无需 OpenSSL 检查和调试 TLS 证书链

# TLDR

**检查远程主机的证书链**

```inspect-cert-chain [example.com]```

**用交互式 TUI 检查**

```inspect-cert-chain -i [example.com]```

**检查本地 PEM 文件**

```inspect-cert-chain --file [path/to/cert.pem]```

**检查指定端口**

```inspect-cert-chain [example.com:8443]```

# SYNOPSIS

**inspect-cert-chain** [**-i**] [**--file** _path_] _host_[_:port_]

# DESCRIPTION

**inspect-cert-chain** 是一款 CLI 和 TUI 工具，用于探测和读取 TLS 证书链，无需依赖 **OpenSSL**。它可以支持 SNI 地从远程服务器获取完整证书链，或解析本地文件的 PEM/DER 输入，并为每个证书打印简洁的 OpenSSL 风格文本。

该工具可解码主题、签发者、序列号、有效期区间、算法、密钥长度、X.509 扩展、SCT 列表、CRL 分发点以及密钥用途位。交互式 TUI 模式（**-i**）在左侧列出证书，右侧显示可滚动的详情，支持 Vim 风格导航和鼠标操作。

# CAVEATS

不执行完整的证书验证或吊销检查。TUI 模式需要宽度足够的终端才能显示分栏布局。

# HISTORY

**inspect-cert-chain** 为系统管理员、渗透测试人员和开发者设计，让他们无需安装或依赖 OpenSSL 即可快速检查证书。

# SEE ALSO

[openssl](/man/openssl)(1), [curl](/man/curl)(1)
