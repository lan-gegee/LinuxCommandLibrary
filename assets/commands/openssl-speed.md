# TAGLINE

对加密算法性能进行基准测试

# TLDR

**运行所有默认基准测试**

```openssl speed```

**测试特定算法**

```openssl speed [aes-256-cbc]```

**测试多个算法**

```openssl speed [sha256] [sha512] [aes-128-gcm]```

**通过 EVP 接口进行测试**

```openssl speed -evp [aes-256-gcm]```

**以指定时长（秒）运行基准测试**

```openssl speed -seconds [10] [rsa2048]```

**使用指定缓冲区大小运行基准测试**

```openssl speed -bytes [8192] [aes-256-cbc]```

**使用多个并行操作**

```openssl speed -multi [4] [sha256]```

**以机器可读格式输出结果**

```openssl speed -mr [aes-256-cbc]```

# SYNOPSIS

**openssl** **speed** [_options_] [_algorithm ..._]

# PARAMETERS

**-help**
> 显示用法信息并退出。

**-elapsed**
> 计算吞吐量时使用实际经过时间（wall-clock）而非 CPU 用户时间。

**-evp** _algo_
> 通过 EVP 接口使用指定的密码算法或消息摘要算法。测试预编译列表之外的算法时必须使用此选项。

**-hmac** _digest_
> 使用指定的消息摘要对 HMAC 进行基准测试。

**-cmac** _cipher_
> 使用指定的密码算法对 CMAC 进行基准测试。

**-multi** _num_
> 同时运行 _num_ 个并行基准测试。

**-async_jobs** _num_
> 启用异步模式并启动指定数量的作业。

**-misalign** _num_
> 将测试缓冲区偏移 _num_ 字节，以测试非对齐访问的性能。

**-decrypt**
> 测量解密而非加密（仅限 EVP 测试）。

**-mb**
> 为支持多块模式的 EVP 密码启用多块模式。

**-aead**
> 以类似 TLS 的序列对 AEAD 密码进行基准测试。

**-primes** _num_
> 生成含 _num_ 个素数的多素数 RSA 密钥（仅限 RSA 测试）。

**-seconds** _num_
> 每项基准测试运行 _num_ 秒，而不是默认的 3 秒。

**-bytes** _num_
> 在大小为 _num_ 字节的缓冲区上运行基准测试。

**-mr**
> 以机器可读格式输出结果。

**-rand** _files_
> 指定用于给随机数生成器播种的文件。

**-writerand** _file_
> 退出时将随机数据写入指定文件。

**-engine** _id_
> 按 ID 选择引擎（在 OpenSSL 3.0 中已弃用）。

**-provider** _name_
> 加载并使用指定的 provider。

# DESCRIPTION

**openssl speed** 通过重复执行操作并测量吞吐量来测试加密算法的性能。它报告公钥算法的每秒操作数以及对称密码和哈希的每秒字节数，并在多个缓冲区大小（16、64、256、1024、8192 和 16384 字节）上进行测试。

不带参数运行时，它会对一组预编译的常用算法进行基准测试，包括 AES、SHA、RSA 和椭圆曲线。可以将特定算法作为参数选择，而 **-evp** 标志允许测试 OpenSSL EVP 接口提供的任何算法。

结果有助于确定给定系统上最高效的算法，并能揭示硬件加速带来的收益（例如 AES-NI 指令）。

# CAVEATS

只有预编译算法子集可以直接按名称测试；其他算法请使用 **-evp**。**-multi** 选项派生独立进程而非使用线程，因此结果可能无法反映真实的多线程应用性能。基准测试测量的是不含协议开销的原始加密吞吐量，因此实际 TLS 性能会有所不同。自 OpenSSL 3.0 起，**-engine** 选项已被弃用，建议改用 provider。

# HISTORY

**speed** 子命令自 OpenSSL 最早的版本起就是其组成部分，继承自 **SSLeay**（Eric Young 的 SSL 库），可追溯至 **20 世纪 90 年代末**。它随时间不断扩展，陆续支持了 EVP、AEAD、多素数 RSA、异步作业，以及 **OpenSSL 3.0**（2021 年 9 月）引入的 provider 架构。

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

[openssl](/man/openssl)(1), [openssl-dgst](/man/openssl-dgst)(1), [openssl-rand](/man/openssl-rand)(1)
