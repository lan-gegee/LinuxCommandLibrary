# TAGLINE

UUID 生成守护进程服务

# TLDR

以守护进程方式**运行 uuidd**

```uuidd -d```

向正在运行的守护进程**请求**一个随机 UUID

```uuidd -r```

向正在运行的守护进程**批量请求**随机 UUID

```uuidd -r -n [number_of_uuids]```

向正在运行的守护进程**请求**一个基于时间的 UUID

```uuidd -t```

**终止**正在运行的 uuidd 守护进程

```uuidd -k```

**以超时方式运行**，空闲后自动退出

```uuidd -d -T [seconds]```

# SYNOPSIS

**uuidd** [_OPTIONS_]

# PARAMETERS

**-d, --debug**
> 以调试模式运行（不会转为守护进程）

**-F, --no-fork**
> 不使用双重 fork 转入后台守护进程

**-k, --kill**
> 终止当前正在运行的 uuidd 守护进程

**-n, --uuids** _N_
> 批量请求 N 个 UUID

**-P, --no-pid**
> 不创建 pid 文件

**-p, --pid** _FILE_
> 指定 pid 文件的路径名

**-q, --quiet**
> 抑制部分失败消息

**-r, --random**
> 通过请求一个随机 UUID 进行测试

**-s, --socket** _PATH_
> 使用指定路径名作为 Unix 域套接字

**-S, --socket-activation**
> 从调用进程接收套接字（隐含 --no-fork 和 --no-pid）

**-t, --time**
> 通过请求一个基于时间的 UUID 进行测试

**-T, --timeout** _N_
> 空闲 N 秒后退出

**-C, --cont-clock** [_N_]
> 为基于时间的 UUID 启用连续时钟处理；默认偏移量为 2 小时

# DESCRIPTION

**uuidd** 是 UUID 库用于生成通用唯一标识符（UUID）的守护进程，尤其是基于时间的 UUID。即使不同 CPU 上的多个线程同时请求 UUID，它也能以安全且保证唯一的方式完成生成。

该守护进程既可以生成随机（版本 4）也可以生成基于时间（版本 1）的 UUID。属于 **util-linux** 软件包。

# CAVEATS

基于时间的 UUID 可能会暴露 MAC 地址信息。以守护进程方式运行需要相应的权限。-r 和 -t 标志是测试/请求操作，它们连接到正在运行的守护进程而不是直接生成 UUID。

# INSTALL

```apt: sudo apt install uuid-runtime```

```dnf: sudo dnf install uuidd```

```zypper: sudo zypper install uuidd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uuid](/man/uuid)(1), [uuidgen](/man/uuidgen)(1), [uuidparse](/man/uuidparse)(1)
