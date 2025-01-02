#Requires AutoHotkey v2.0

SoundFileRu := A_ScriptDir . "\change_language_ru.mp3"
SoundFileEn := A_ScriptDir . "\change_language_en.mp3"

+F9:: {
    Run '"C:\Program Files\Mozilla Firefox\firefox.exe" "https://github.com/Seva5959?tab=repositories"'
}

+F10:: {
    Run '"C:\Program Files\Mozilla Firefox\firefox.exe" "https://chatgpt.com/?model=auto"'
}

+F11:: {
    Run '"C:\Program Files\Mozilla Firefox\firefox.exe" "https://claude.ai/new"'
}

+F12:: {
    Run '"C:\Program Files\Mozilla Firefox\firefox.exe" "https://vk.com/im?peers=473315238"'
}

; Переключить Caps Lock при нажатии Shift + Caps Lock
+CapsLock:: {
    SetCapsLockState(GetKeyState("CapsLock", "T") ? 0 : 1)
}

; Переключить Caps Lock при нажатии Caps Lock + Shift
CapsLock & Shift:: {
    SetCapsLockState(GetKeyState("CapsLock", "T") ? 0 : 1)
}

; Отключить Caps Lock при одиночном нажатии
CapsLock::Return
F11::Return
F12::Return

~*Shift::
~*Alt::
{
    ; Проверяем, были ли нажаты обе клавиши
    if (GetKeyState("Shift", "P") && GetKeyState("Alt", "P")) {
        ; Воспроизведение звукового файла
        SoundPlay(SoundFileEn)
    }
}

#HotIf WinActive("ahk_exe firefox.exe")

; Навигация по вкладкам
!Left::  ; Alt + Стрелка влево
{
    Send "^{PgUp}"  ; Отправляем Ctrl + Page Up для переключения на предыдущую вкладку
}
!Right::  ; Alt + Стрелка вправо
{
    Send "^{PgDn}"  ; Отправляем Ctrl + Page Down для переключения на следующую вкладку
}

; Навигация назад (Caps Lock Left)
CapsLock & Left:: {
    Send "!{Left}"
}

; Навигация вперед (Caps Lock Right)
CapsLock & Right:: {
    Send "!{Right}"
}




#HotIf
