package com.linuxcommandlibrary.shared

/* Copyright 2022 Simon Schubert
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
*/

sealed class CommandElement {
    data class Text(val text: String) : CommandElement()
    data class Man(val man: String) : CommandElement()
    data class Url(val command: String, val url: String) : CommandElement()
}

/**
 * Return a list of sealed Elements for visual representation
 */
fun String.getCommandList(
    mans: String,
    hasBrackets: Boolean = false,
): List<CommandElement> {
    var command = " $this"
    val list = mutableListOf<CommandElement>()
    mans.split(",").filterNot { it.isEmpty() }.map { it.replace("(", "").replace(")", "") }
        .forEach {
            command = if (it.startsWith("url:")) {
                val cmd = it.substring(4).split("|").first()
                command.replace(cmd, " ü${it}ä")
            } else {
                if (hasBrackets) {
                    val escapedIt = Regex.escape(it)
                    val regex = "(?:[\\s,])($escapedIt)".toRegex()
                    command.replace(regex, " ü${it}ä")
                } else {
                    command.replace(it, " ü${it}ä")
                }
            }
        }

    var currentText = ""
    var currentCommand = ""
    var isCommand = false
    command.trim().forEach {
        if (it == 'ü') {
            list.add(CommandElement.Text(currentText.replace("\n", "")))
            currentText = ""
            isCommand = true
        } else if (it == 'ä') {
            if (currentCommand.isNotBlank()) {
                when {
                    currentCommand.startsWith("url:") -> {
                        val url = currentCommand.split("|").last()
                        val cmd = currentCommand.substring(4).split("|").first()
                        list.add(CommandElement.Url(cmd, url))
                    }

                    else -> {
                        list.add(CommandElement.Man(currentCommand))
                    }
                }
            }
            currentCommand = ""
            isCommand = false
        } else {
            if (isCommand) {
                currentCommand += it
            } else {
                currentText += it
            }
        }
    }
    list.add(CommandElement.Text(currentText.replace("[cmd]", "[command]").replace("\n", "")))
    return list.toList()
}

val onlyCharactersRegex = "[^a-z]".toRegex()

/**
 * Man page section titles are structural keys parsed from markdown (must stay English in files).
 * This map localizes them for display only.
 */
private val sectionTitleZh =
    mapOf(
        "TAGLINE" to "简介",
        "TLDR" to "快速示例",
        "SYNOPSIS" to "语法",
        "PARAMETERS" to "参数",
        "DESCRIPTION" to "描述",
        "CAVEATS" to "注意事项",
        "HISTORY" to "历史",
        "INSTALL" to "安装",
        "SEE ALSO" to "另请参阅",
        "RESOURCES" to "资源链接",
        "CONFIGURATION" to "配置",
        "COMMANDS" to "命令",
        "SUBCOMMANDS" to "子命令",
        "EXAMPLES" to "示例",
        "WORKFLOW" to "工作流程",
    )

fun localizeSectionTitle(title: String): String =
    sectionTitleZh[title.uppercase()] ?: title

val basicsSortOrder =
    listOf(
        "oneliners",
        "aitools",
        "systeminformation",
        "systemcontrol",
        "systemrecovery",
        "usersgroups",
        "filesfolders",
        "input",
        "printing",
        "json",
        "network",
        "searchfind",
        "git",
        "ssh",
        "videoaudio",
        "packagemanager",
        "textprocessing",
        "compressionarchiving",
        "backupimaging",
        "hackingtools",
        "terminalgames",
        "cryptocurrencies",
        "shellscripting",
        "tmux",
        "regularexpressions",
        "vimtexteditor",
        "emacstexteditor",
        "nanotexteditor",
        "picotexteditor",
        "microtexteditor",
    )

/**
 * Only allow characters in html file names to guarantee matching on the website and app deep linking
 */
fun String.toHtmlFileName(): String = this.lowercase().replace(onlyCharactersRegex, "")
