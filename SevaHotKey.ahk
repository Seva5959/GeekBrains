#Requires AutoHotkey v2.0
д


; Переключить Caps Lock при нажатии Shift + Caps Lock
+CapsLock::
{
    SetCapsLockState(GetKeyState("CapsLock", "T") ? 0 : 1)
}

; Отключить Caps Lock при одиночном нажатии
CapsLock::Return
F11::Return
F12::Return

^p::{  
    Send("^c")                ; Копирует выделенный текст
    Sleep(100)                ; Задержка для завершения копирования
    Click(20, 371)           ; Кликает по координатам в окне Яндекс Переводчика
    Sleep(100)                ; Задержка для завершения клика
    Send("^v")                ; Вставляет скопированный текст
}

return
