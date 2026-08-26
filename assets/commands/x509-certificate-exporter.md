# TAGLINE

用于 X.509 证书过期的 Prometheus exporter

# TLDR

**监视目录中的所有 PEM 文件**

```x509-certificate-exporter --watch-dir [/etc/ssl/certs] --listen-address :[9793]```

**监视指定文件**

```x509-certificate-exporter -f [/etc/nginx/ssl/site.pem] -f [/etc/nginx/ssl/api.pem]```

**监视 kubeconfig 引用的证书**

```x509-certificate-exporter --watch-kubeconf [~/.kube/config]```

**使用 YAML 配置文件运行**并开启调试日志

```x509-certificate-exporter --config [exporter.yaml] --debug```

**通过 TLS / BasicAuth 提供指标服务**

```x509-certificate-exporter --web.config.file [web-tls.yaml] -b :[9793]```

# SYNOPSIS

**x509-certificate-exporter** [**--watch-file** _file_]... [**--watch-dir** _dir_]... [**--watch-kubeconf** _file_]... [**--listen-address** _addr_] [_flags_]

# PARAMETERS

**-C**, **--config** _file_
> 从 YAML 文件加载配置。

**-f**, **--watch-file** _file_
> 监视单个证书或 PEM 包（可重复使用）。

**-d**, **--watch-dir** _dir_
> 监视目录中的每个证书文件（可重复使用）。

**-k**, **--watch-kubeconf** _file_
> 解析 kubeconfig 并监视其引用的所有证书。

**--watch-kube-secrets**
> 在集群内运行时，监视存储在 Kubernetes Secrets 中的证书。

**-b**, **--listen-address** _addr_
> 指标端点的地址（默认 `:9793`）。

**--web.config.file** _file_
> Prometheus exporter-toolkit 配置，用于指标端点上的 TLS 和 BasicAuth。

**--probe.listen-address** _addr_
> 就绪/存活探测端点的绑定地址。

**--debug**
> 启用调试日志。

**--profile**
> 启用 Go pprof 端点以进行性能分析。

**-v**, **--version**
> 显示版本并退出。

# DESCRIPTION

**x509-certificate-exporter** 是一个 **Prometheus** exporter，它从磁盘和 Kubernetes 集群中抓取 X.509 证书，并在 **/metrics** 上将它们的生存期暴露为指标。找到的每个证书——包括链中的每个叶子证书——都会成为一条独立的时间序列，带有主体、签发者、SAN、序列号和来源等标签，因此可以基于 **x509_cert_not_after** 等知名指标编写告警。

该 exporter 能理解 PEM 包、Kubernetes **Secret** 对象、**ConfigMap** 条目、kubeconfig 文件以及带密码保护的 **PKCS#12** 密钥库。解析出的证书会在多次抓取之间缓存，以保持较低的 CPU 和 I/O 开销；同时集成了标准的 Prometheus **exporter-toolkit**，为指标端点提供 TLS 和 BasicAuth。

以单个静态 Go 二进制文件分发，支持 Linux、macOS、Windows 及多个 BSD 平台，覆盖 amd64/arm64/armv7/riscv64 架构。Helm chart 和容器镜像使其在 Kubernetes 中部署非常简单。

# CAVEATS

该 exporter 只检查**磁盘上**的证书（或通过 Kubernetes API），**不会**与远程服务器建立 TLS 连接。要监控远程端点，请将其与 **blackbox_exporter** 结合使用。PKCS#12 密钥库的密码需要通过 YAML 配置文件提供。若不修改，默认端口 **9793** 可能与其他服务冲突。

# HISTORY

由 **ENIX**（一家法国基础设施公司）开发，以 **MIT** 许可证发布。项目在 GitHub 的 **enix/x509-certificate-exporter** 上持续活跃开发并频繁发布新版本。

# SEE ALSO

[prometheus](/man/prometheus)(1)
