import ctypes

def get_keyboard_layout():
    user32 = ctypes.windll.user32
    layout = user32.GetKeyboardLayout(0) & 0xFFFF
    return layout

if __name__ == "__main__":
    layout = get_keyboard_layout()
    print(layout)


# #Requires AutoHotkey v2.0
#
# ; Пути к звуковым файлам
# SoundFileRu := A_ScriptDir "\change_language_ru.mp3"
# SoundFileEn := A_ScriptDir "\change_language_en.mp3"
# PythonFileDir := A_ScriptDir "\get_layout.py"
#
# ; Проверка существования файлов
# if !FileExist(SoundFileRu)
#     MsgBox "Файл " SoundFileRu " не найден!"
# if !FileExist(SoundFileEn)
#     MsgBox "Файл " SoundFileEn " не найден!"
#
#
# +F10:: Run A_ComSpec ' /c "C:\Users\segyn\AppData\Local\Programs\Opera GX\launcher.exe" "https://chatgpt.com/?model=auto"'
#
# +F11:: Run A_ComSpec ' /c "C:\Users\segyn\AppData\Local\Programs\Opera GX\launcher.exe" "https://claude.ai/new"'
#
# +F12:: Run A_ComSpec ' /c "C:\Users\segyn\AppData\Local\Programs\Opera GX\launcher.exe" "https://vk.com/im?peers=473315238"'
#
# +CapsLock:: SetCapsLockState(GetKeyState("CapsLock", "T") ? 0 : 1)
#
# CapsLock::Return
# F11::Return
# F12::Return
#
# ^p:: {
#     Send "^c"
#     Sleep 300
#     Click 15, 420
#     Sleep 100
#     Send "!{d}"
#     Sleep 100
#     Send "^v"
# }
#
# GetKeyboardLayout() {
#     return DllCall("GetKeyboardLayout", "UInt", 0, "UInt")
# }
#
#
#
# PlaySound(file) {
#     try {
#         sound := SoundPlay(file)
#         FileAppend "Попытка воспроизвести звук: " file "`n", "debug_utf8.log", "UTF-8"
#         if !sound {
#             FileAppend "Ошибка воспроизведения звука: " file "`n", "debug_utf8.log", "UTF-8"
#             MsgBox "Не удалось воспроизвести звук: " file
#         }
#     } catch as e {
#         FileAppend "Исключение при воспроизведении звука: " e.Message "`n", "debug_utf8.log", "UTF-8"
#         MsgBox "Ошибка при воспроизведении звука: " e.Message
#     }
# }
#
# ~*Shift::
# ~*Alt:: {
#     ; Получаем текущую раскладку клавиатуры
#     currentLayout := GetKeyboardLayout()
#     FileAppend "Текущая раскладка: " currentLayout "`n", "debug_utf8.log", "UTF-8"
#
#     ; Воспроизводим звук в зависимости от раскладки
#     if (currentLayout & 0xFFFF = 0x0419) { ; Русская раскладка
#         FileAppend "Попытка воспроизвести русский звук`n", "debug_utf8.log", "UTF-8"
#         PlaySound(SoundFileRu)
#     } else if (currentLayout & 0xFFFF = 0x0409) { ; Английская раскладка
#         FileAppend "Попытка воспроизвести английский звук`n", "debug_utf8.log", "UTF-8"
#         PlaySound(SoundFileEn)
#     } else {
#         FileAppend "Неизвестная раскладка`n", "debug_utf8.log", "UTF-8"
#     }
# }