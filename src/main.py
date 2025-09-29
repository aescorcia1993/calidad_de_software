from src.crash_guard import CrashGuard

# Variable global para preferencias
prefs = {
    "media.wmf.vp9.enabled": True
}

# Función global para crash guard
def crash_guard(name):
    return CrashGuard(name)

def create_decoder():
    # Simulación de creación de decoder
    return "decoder"

def can_play_vp9():
    if not prefs.get("media.wmf.vp9.enabled", False):
        return False
    guard = crash_guard("WMFVPXVideo")
    try:
        decoder = create_decoder()
    except Exception:
        return False
    if decoder is None:
        return False
    return True

if __name__ == "__main__":
    print("¿Puede reproducir VP9?:", can_play_vp9())