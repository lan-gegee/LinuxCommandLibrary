# TAGLINE

面向开发者与安全研究人员的动态插桩工具集

# TLDR

按名称**附加到**正在运行的进程

```frida [process_name]```

按 **PID 附加到**进程

```frida -p [pid]```

**启动**新进程并对其进行插桩

```frida -f [/path/to/binary]```

**加载** JavaScript 插桩脚本

```frida -l [script.js] [process_name]```

**附加到****USB 连接的**设备上的应用

```frida -U -n [app_name]```

在 USB 设备上**启动**应用并**暂停**主线程

```frida -U -f [com.example.app] --pause```

对一个进程**执行**内联 JavaScript 代码

```frida -e "console.log('hello')" [process_name]```

# SYNOPSIS

**frida** [_options_] [_target_]

# PARAMETERS

**-f** _TARGET_, **--file** _TARGET_
> 将 FILE 作为新进程启动。

**-F**, **--attach-frontmost**
> 附加到最前端的应用。

**-n** _NAME_, **--attach-name** _NAME_
> 按名称附加到进程。

**-p** _PID_, **--attach-pid** _PID_
> 按 PID 附加到进程。

**-U**, **--usb**
> 连接到 USB 设备。

**-R**, **--remote**
> 连接到远程 frida-server。

**-H** _HOST_, **--host** _HOST_
> 连接到 HOST 上的远程 frida-server。

**-D** _ID_, **--device** _ID_
> 连接到具有给定 ID 的设备。

**-l** _SCRIPT_, **--load** _SCRIPT_
> 加载 JavaScript 脚本 SCRIPT（可多次指定）。

**-e** _CODE_, **--eval** _CODE_
> 执行 JavaScript 代码 CODE。

**-c** _URI_, **--codeshare** _URI_
> 从 Frida CodeShare 加载脚本。

**-C** _CMODULE_, **--cmodule** _CMODULE_
> 加载一个 C 模块。

**-P** _JSON_, **--parameters** _JSON_
> 以 JSON 形式给出的参数，与 Gadget 相同。

**--runtime** {**qjs**,**v8**}
> 要使用的脚本运行时。

**--debug**
> 启用与 Node.js 兼容的脚本调试器。

**-q**, **--quiet**
> 安静模式（无提示符），执行完 -l 和 -e 后退出。

**-t** _SECS_, **--timeout** _SECS_
> 安静模式下终止前等待的秒数。

**-o** _FILE_, **--output** _FILE_
> 输出到日志文件。

**--pause**
> 启动程序后让主线程保持暂停。

**--kill-on-exit**
> Frida 退出时杀掉被启动的程序。

**--eternalize**
> 退出前将脚本永久化（eternalize）。

**--auto-perform**
> 将输入的代码用 Java.perform 包装。

**--no-auto-reload**
> 禁用文件变化时的脚本自动重载。

# DESCRIPTION

**frida** 是 Frida 动态插桩工具集的交互式 REPL（Read-Eval-Print Loop）界面。它允许向运行中的进程注入 JavaScript 片段，进行运行时分析、调试和修改。你可以附加到运行中的进程、启动新进程、加载脚本、挂钩函数，以及在运行时检查或修改应用行为。

Frida 可运行于 **Windows**、**macOS**、**GNU/Linux**、**iOS**、**Android**、**FreeBSD** 和 **QNX**。对于远程目标（手机、嵌入式设备），目标设备上必须运行 **frida-server** 二进制程序。

# CAVEATS

向其他进程注入通常需要 **root** 或提升的权限。在 Android 上，frida-server 必须以 root 运行。在 iOS 上通常需要越狱。许多应用（尤其是移动银行和受 DRM 保护的应用）实现了 Frida 检测机制，检测到插桩时可能会自行终止。注入脚本中的 bug 可能使目标进程崩溃。Frida 只应用于你拥有或已获明确授权测试的软件。

# HISTORY

Frida 由 **Ole Andre Vadla Ravnas** 创建，他大约从 **2008** 年开始用 C 构建一个通用的代码插桩库。该项目于 **2014** 年公开发布，其中 Frida 1.6.0（2014 年 5 月）加入了对 Android 的支持。项目由 **NowSecure** 赞助。如今 Frida 提供针对 Node.js、Python、Swift、.NET、Go 和 C 的绑定，并且是 **OWASP Mobile Security Testing Guide** 中引用的标准工具。

# SEE ALSO

[frida-ps](/man/frida-ps)(1), [frida-trace](/man/frida-trace)(1), [gdb](/man/gdb)(1), [strace](/man/strace)(1)
