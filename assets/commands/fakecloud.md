# TAGLINE

面向集成测试的本地 AWS 云模拟器

# TLDR

启动模拟器（监听 _http://localhost:4566_）

```fakecloud```

通过一行安装命令安装 fakecloud

```curl -fsSL https://raw.githubusercontent.com/faiscadev/fakecloud/main/install.sh | bash```

启用 SigV4 签名验证（更接近真实 AWS）

```fakecloud --verify-sigv4```

启用严格的 IAM 策略强制执行

```fakecloud --iam [strict]```

针对运行中的模拟器创建 SQS 队列

```aws --endpoint-url http://localhost:4566 sqs create-queue --queue-name [my-queue]```

用 Cargo 安装

```cargo install fakecloud```

在 Docker 中运行

```docker run -p 4566:4566 faisca/fakecloud```

# SYNOPSIS

**fakecloud** [_options_]

# PARAMETERS

**--verify-sigv4**
> 启用加密签名验证，客户端必须像访问真实 AWS 那样对请求进行签名。

**--iam** _MODE_
> IAM 策略强制执行。_soft_ 只评估但不阻止；_strict_ 会拒绝未授权调用。默认关闭。

**--port** _PORT_
> 监听其他 TCP 端口（默认 _4566_）。

**--host** _ADDR_
> 绑定到指定网络接口（默认 _127.0.0.1_）。

**--data-dir** _DIR_
> 用于在多次运行之间持久化模拟状态的目录。

**-h**, **--help**
> 显示帮助信息并退出。

**-V**, **--version**
> 输出版本信息并退出。

# DESCRIPTION

**fakecloud** 是一个自包含的单二进制程序（约 19 MB，约 10 MiB RSS，约 500 ms 启动），在本地模拟最常用的 AWS 服务——S3、SQS、SNS、DynamoDB、Lambda、IAM 等——让集成测试无需云凭据或互联网访问。将任何 AWS SDK 或 **aws** CLI 指向 _http://localhost:4566_ 并使用虚拟凭据（**access_key=test**、**secret_key=test**），它会以与真实服务相同的线上协议作出响应。

官方测试 SDK 支持 TypeScript、Python、Go、PHP、Java 和 Rust。fakecloud 本身在运行时不依赖 Docker，不过为了方便 CI 也提供了容器镜像。

# CONFIGURATION

TypeScript 中的典型测试配置：

```
import { S3Client } from "@aws-sdk/client-s3";

const s3 = new S3Client({
  endpoint: "http://localhost:4566",
  region: "us-east-1",
  credentials: { accessKeyId: "test", secretAccessKey: "test" },
  forcePathStyle: true,
});
```

传入 **--data-dir** 可以在多次测试运行之间持久化状态；否则每次启动都是全新环境。

# CAVEATS

fakecloud 覆盖常用的 AWS 服务，但与生产环境的 AWS 并非逐位一致——冷门的错误码、配额行为和最终一致性的边缘情况可能不同。只应将其用于集成测试，而不是作为生产替代品。本项目采用 **AGPL-3.0** 许可证，如果你计划将其作为 SaaS 的一部分再分发，这一点需要留意。

# HISTORY

**fakecloud** 由 **faiscadev** 于 **2026 年**初推出。当时 **LocalStack** 宣布转向专有许可证，fakecloud 为团队提供了一个永久免费的开源替代方案，实现完全本地的 AWS 测试。

# INSTALL

```brew: brew install fakecloud```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aws](/man/aws)(1), [terraform](/man/terraform)(1)
