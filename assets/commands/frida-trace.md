# TAGLINE

基于 Frida 的动态函数调用跟踪器

# TLDR

**跟踪**进程中匹配某模式的函数

```frida-trace -i "[pattern]" [process_name]```

**跟踪**特定**模块**中的所有函数

```frida-trace -I "[module]" [process_name]```

**跟踪**匹配模式的 Objective-C 方法

```frida-trace -m "[pattern]" [process_name]```

在 Android 设备上**跟踪 Java** 方法

```frida-trace -U -f [com.example.app] -j "[pattern]"```

**启动**一个程序并跟踪其**导入**

```frida-trace -T -f [/path/to/binary]```

**跟踪**去符号二进制文件中特定**偏移处**的函数

```frida-trace -p [pid] -a "[module]![0xoffset]"```

在 **USB 连接的**设备上带模块修饰地**跟踪**函数

```frida-trace -U --decorate -i "[pattern]" [app_name]```

**附加到** USB 设备上**最前端**的应用

```frida-trace -U -F -i "[pattern]"```

# SYNOPSIS

**frida-trace** [_options_] [_target_]

# PARAMETERS

**-i** _FUNCTION_, **--include** _FUNCTION_
> 包括 [MODULE!]FUNCTION（glob 模式）。

**-x** _FUNCTION_, **--exclude** _FUNCTION_
> 排除 [MODULE!]FUNCTION（glob 模式）。

**-I** _MODULE_, **--include-module** _MODULE_
> 包括 MODULE 中的所有函数（glob 模式）。

**-X** _MODULE_, **--exclude-module** _MODULE_
> 排除 MODULE 中的所有函数（glob 模式）。

**-a** _MODULE!OFFSET_, **--add** _MODULE!OFFSET_
> 添加 MODULE 中位于 OFFSET 处的函数（用于去符号的二进制文件）。

**-T**, **--include-imports**
> 包括程序的导入项。

**-t** _MODULE_, **--include-module-imports** _MODULE_
> 包括 MODULE 的导入项。

**-m** _METHOD_, **--include-objc-method** _METHOD_
> 包括 Objective-C 方法 METHOD（glob 模式）。

**-M** _METHOD_, **--exclude-objc-method** _METHOD_
> 排除 Objective-C 方法 METHOD（glob 模式）。

**-y** _FUNC_, **--include-swift-func** _FUNC_
> 包括 Swift 函数 FUNC（glob 模式）。

**-Y** _FUNC_, **--exclude-swift-func** _FUNC_
> 排除 Swift 函数 FUNC（glob 模式）。

**-j** _METHOD_, **--include-java-method** _METHOD_
> 包括 Java 方法 METHOD（glob 模式）。

**-J** _METHOD_, **--exclude-java-method** _METHOD_
> 排除 Java 方法 METHOD（glob 模式）。

**-d**, **--decorate**
> 在生成的 onEnter 日志语句中添加模块名。

**-q**, **--quiet**
> 不对输出消息进行格式化。

**-o** _FILE_, **--output** _FILE_
> 将消息转储到文件。

**-S** _PATH_, **--init-session** _PATH_
> 用于初始化会话的 JavaScript 文件路径。

**-s** _DEBUG_SYMBOL_, **--include-debug-symbol** _DEBUG_SYMBOL_
> 包括 DEBUG_SYMBOL（glob 模式）。

**-f** _TARGET_, **--file** _TARGET_
> 将 FILE 作为新进程启动。

**-F**, **--attach-frontmost**
> 附加到最前端的应用。

**-n** _NAME_, **--attach-name** _NAME_
> 按名称附加到进程。

**-N** _IDENTIFIER_, **--attach-identifier** _IDENTIFIER_
> 按标识符附加到进程。

**-p** _PID_, **--attach-pid** _PID_
> 按 PID 附加到进程。

**-W** _PATTERN_, **--await** _PATTERN_
> 等待启动与 PATTERN 匹配的程序。

**-U**, **--usb**
> 连接到 USB 设备。

**-R**, **--remote**
> 连接到远程 frida-server。

**-H** _HOST_, **--host** _HOST_
> 连接到 HOST 上的远程 frida-server。

**-D** _ID_, **--device** _ID_
> 连接到具有给定 ID 的设备。

**--runtime** _{qjs,v8}_
> 要使用的脚本运行时。

**-O** _FILE_, **--options-file** _FILE_
> 包含额外命令行选项的文本文件。

**-P** _JSON_, **--parameters** _JSON_
> 以 JSON 形式给出的参数，暴露为名为 parameters 的全局变量。

# DESCRIPTION

**frida-trace** 是一个用于动态跟踪运行进程中函数调用的工具。它可以挂钩**原生函数**（C/C++）、**Objective-C** 方法、**Swift** 函数和 **Java** 方法，并记录它们的调用参数和返回值。

当你跟踪一个函数时，frida-trace 会自动生成 JavaScript 处理器存根，放在 **\_\_handlers\_\_/** 目录中，你可以自定义这些存根来记录参数、修改返回值或实现任意插桩逻辑。如果处理器文件已存在，则不会被覆盖。

包含（**-i**、**-I**）和排除（**-x**、**-X**）选项是按顺序处理的；每个选项都作用于当前的函数工作集，因此它们的顺序很重要。

# CAVEATS

使用过宽的 glob 模式（如 **-i "\*"**）跟踪大量函数可能严重拖慢甚至冻结目标进程。对于没有符号信息的去符号二进制文件，必须使用 **-a MODULE!OFFSET**，这要求事先通过 Ghidra 或 IDA Pro 等静态分析工具了解函数偏移。处理器目录（**\_\_handlers\_\_/**）创建在当前工作目录中；已有的处理器不会被覆盖，当跟踪目标变化时这可能造成困扰。在桌面系统上进行跨进程注入通常需要 root 或提升的权限。

# HISTORY

**frida-trace** 是最早基于 Frida 核心构建的工具之一，自 Frida 于 **2014** 年公开发布起就包含在 **frida-tools** 软件包中。它的函数跟踪能力利用了 Frida 的 **Stalker** 代码跟踪组件。多年来陆续增加了对 Objective-C 方法、Swift 函数和 Java 方法的支持，反映了该工具随移动安全研究社区共同演进的过程。

# SEE ALSO

[frida](/man/frida)(1), [frida-ps](/man/frida-ps)(1), [strace](/man/strace)(1), [ltrace](/man/ltrace)(1)
