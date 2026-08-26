# TAGLINE

文字转语音服务守护进程

# TLDR

**启动 speech-dispatcher 守护进程**

```speech-dispatcher```

**以调试模式启动**

```speech-dispatcher -D```

**以指定的通信方式启动**

```speech-dispatcher -c [unix_socket|inet_socket]```

**使用自定义配置文件启动**

```speech-dispatcher -C [path/to/speechd.conf]```

**以指定端口启动**

```speech-dispatcher -p [6560]```

# SYNOPSIS

**speech-dispatcher** [_options_]

# PARAMETERS

**-d**, **--spawn**
> 以守护进程（后台进程）方式启动。

**-D**, **--debug**
> 启用调试模式并提供详细输出。

**-l**, **--log-level** _level_
> 设置日志级别（1-5，数字越大越详细）。

**-c**, **--communication-method** _method_
> 通信方式：**unix_socket** 或 **inet_socket**。

**-S**, **--socket-path** _path_
> unix_socket 方式的套接字路径。

**-p**, **--port** _port_
> inet_socket 方式的端口号（默认：6560）。

**-a**, **--address** _address_
> 监听的网络地址。

**-C**, **--config-file** _path_
> 使用自定义配置文件。

**-P**, **--pid-file** _path_
> PID 文件位置。

**-m**, **--module-dir** _path_
> 输出模块所在目录。

**-v**, **--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# DESCRIPTION

**speech-dispatcher** 是一个管理 Linux 系统上文字转语音输出的服务守护进程。它为应用程序提供统一的语音合成请求接口，基于优先级处理并发请求，并抽象不同的语音合成后端。

守护进程监听客户端连接，并将文本分发给已配置的语音合成模块，如 eSpeak NG、Festival、Piper 等。它支持可调节的语速、音调、音量、嗓音选择以及多语言等功能。

应用程序通过客户端库（libspeechd）或 **spd-say** 命令行工具与 speech-dispatcher 通信。用户专属配置存储在 **~/.config/speech-dispatcher/** 中，系统配置位于 **/etc/speech-dispatcher/**。

# CONFIGURATION

**/etc/speech-dispatcher/speechd.conf**
> 系统级配置，涵盖默认输出模块、嗓音、语言和音频设置。

**~/.config/speech-dispatcher/speechd.conf**
> 覆盖系统默认值的每用户配置。

**/etc/speech-dispatcher/modules/**
> 各语音合成后端的输出模块配置文件（espeak-ng.conf, festival.conf 等）。

# CAVEATS

守护进程必须正在运行，**spd-say** 等客户端才能工作。至少需要配置一个语音合成后端（输出模块）。音频系统兼容性取决于所配置的输出模块。运行多个实例需要不同的套接字路径或端口。

# HISTORY

**Speech Dispatcher** 的创建目的是为 Linux 无障碍功能和桌面应用提供统一的文字转语音接口。它被设计为与屏幕阅读器及其他辅助技术协同工作。该项目作为 Free(b)soft 自由操作系统无障碍计划的一部分进行开发。开发仍在继续，不断加入对新合成器和音频系统的支持。

# INSTALL

```apt: sudo apt install speech-dispatcher```

```dnf: sudo dnf install speech-dispatcher```

```pacman: sudo pacman -S speech-dispatcher```

```apk: sudo apk add speech-dispatcher```

```zypper: sudo zypper install speech-dispatcher```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[spd-say](/man/spd-say)(1), [espeak-ng](/man/espeak-ng)(1), [festival](/man/festival)(1)
