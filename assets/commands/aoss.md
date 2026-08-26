# TAGLINE

通过 ALSA 仿真运行 OSS 应用

# TLDR

**以 ALSA OSS 仿真运行应用程序**

```aoss [application]```

**运行需要 OSS 音频的游戏**

```aoss [game_binary]```

**选择 OSS /dev/dsp 映射到的 ALSA PCM 设备**

```ALSA_OSS_PCM_DEVICE=[plughw:0,0] aoss [application]```

# SYNOPSIS

**aoss** _osscommand_ [_arguments_]

# DESCRIPTION

**aoss** 是一个包装脚本，让为开放声音系统（OSS）API 编写的应用能够配合 ALSA（Advanced Linux Sound Architecture）工作。它会预加载一个兼容性库，拦截 OSS 系统调用并将其转换为对应的 ALSA 调用。

许多较早的 Linux 应用和游戏使用 OSS 的 **/dev/dsp** 和 **/dev/mixer** 设备接口编写。由于现代 Linux 系统主要使用 ALSA，没有兼容层这些应用将无法发声。aoss 包装器透明地提供了这种转换。

该包装器设置 **LD_PRELOAD** 环境变量来加载 **libaoss.so**，它挂接应用对 OSS 设备节点的文件操作，并通过 ALSA 的 PCM 接口进行重定向。要打开的 PCM 设备可通过 **ALSA_OSS_PCM_DEVICE** 环境变量显式指定，覆盖默认值（dsp0）。

# CAVEATS

对静态链接的应用或直接使用内核接口的应用无效。某些复杂的 OSS 特性可能无法完全仿真。64 位系统上的 32 位应用需要 32 位版本的 ALSA OSS 库。原生使用 ALSA 的应用不需要此包装器。

# HISTORY

aoss 包装器作为 **alsa-oss** 软件包的一部分开发，目的是在 **21 世纪初**缓解从 OSS 向 ALSA 过渡的问题。OSS 是 Linux 最初的声音系统，但后来基本被 ALSA 取代，后者自 Linux 内核 2.6 起成为标准。对于从未更新为使用 ALSA 或 PulseAudio 的旧应用，这个包装器至今仍然有用。

# SEE ALSO

[padsp](/man/padsp)(1), [alsamixer](/man/alsamixer)(1), [aplay](/man/aplay)(1)

# RESOURCES

```[Source code](https://github.com/alsa-project/alsa-oss)```

```[Homepage](https://www.alsa-project.org/)```

<!-- verified: 2026-06-11 -->
