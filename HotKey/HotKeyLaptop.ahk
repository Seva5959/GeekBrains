#Requires AutoHotkey v2.0

SoundFileRu := A_ScriptDir . "\change_language_ru.mp3"
SoundFileEn := A_ScriptDir . "\change_language_en.mp3"

+F10:: {
    Run '"C:\Users\loha8\AppData\Local\Programs\Opera GX\launcher.exe" "https://chatgpt.com/?model=auto"'
}

+F11:: {
    Run '"C:\Users\loha8\AppData\Local\Programs\Opera GX\launcher.exe" "https://claude.ai/new"'
}

+F12:: {
    Run '"C:\Users\loha8\AppData\Local\Programs\Opera GX\launcher.exe" "https://vk.com/im?peers=473315238"'
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

^p:: {
    Send("^c")                ; Копирует выделенный текст
    Sleep(100)                ; Задержка для завершения копирования
    Click(15, 340)            ; Кликает по координатам в окне Яндекс Переводчика для ПК
    Sleep(500)                ; Задержка для завершения клика
    Send("!{d}")
    Sleep(400)
    Send("^v")                ; Вставляет скопированный текст
}

~*Shift::
~*Alt::
{
    ; Проверяем, были ли нажаты обе клавиши
    if (GetKeyState("Shift", "P") && GetKeyState("Alt", "P")) {
        ; Воспроизведение звукового файла
        SoundPlay(SoundFileEn)
    }
}

#HotIf WinActive("ahk_exe opera.exe")


; Навигация по вкладкам
!Left::  ; Alt + Стрелка влево
{
    Send "^{PgUp}"  ; Отправляем Ctrl + Page Up для переключения на предыдущую вкладку
}
!Right::  ; Alt + Стрелка вправо
{
    Send "^{PgDn}"  ; Отправляем Ctrl + Page Down для переключения на следующую вкладку
}

#HotIf