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

; Переменная для отслеживания состояния "зажатия" клавиши Ё
global IsTabGrabbed := false

; При нажатии Ё "зажимается" текущая вкладка
`:: {
    global IsTabGrabbed  ; Явно указываем, что используем глобальную переменную
    IsTabGrabbed := !IsTabGrabbed  ; Переключаем состояние
    if (IsTabGrabbed) {
        SoundBeep(1000)  ; Звук для индикации активации
    } else {
        SoundBeep(500)   ; Звук для индикации деактивации
    }
}

; Если вкладка "зажата", стрелки перемещают её
Left:: {
    global IsTabGrabbed  ; Явно указываем, что используем глобальную переменную
    if (IsTabGrabbed) {
        Send("^+{PgUp}")  ; Ctrl + Shift + PageUp перемещает вкладку влево
    }
    return
}

Right:: {
    global IsTabGrabbed  ; Явно указываем, что используем глобальную переменную
    if (IsTabGrabbed) {
        Send("^+{PgDn}")  ; Ctrl + Shift + PageDown перемещает вкладку вправо
    }
    return
}


#HotIf
