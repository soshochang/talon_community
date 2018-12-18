# https://github.com/JonathanNickerson/talon_voice_user_scripts

from talon.voice import Key, Context

ctx = Context("custom")  # , bundle='com.microsoft.VSCode')

keymap = {
    "chom slash": Key("cmd-/"), 
    "boldline": Key("cmd-left cmd-shift-right cmd-b right"), 
    "italicline": Key("cmd-left cmd-shift-right cmd-i right"), 
    "underline": Key("cmd-left cmd-shift-right cmd-u right"), 
    "strikeline": Key("cmd-left cmd-shift-right cmd-ctrl-k right"),
    "paisley": Key("alt-left backspace alt-right"),
    "question": "//Q:",
    "answer": "//A:",
}

ctx.keymap(keymap)