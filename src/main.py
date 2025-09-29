from src.crash_guard import CrashGuard

# Variable global para preferencias
prefs = {
    "media.wmf.vp9.enabled": True
}

# Función global para crash guard
def crash_Guard(name):
    return CrashGuard(name)

def create_Decoder():
    # Simulación de creación de decoder
    return "decoder"

def can_Play_VP9():
    if not prefs.get("media.wmf.vp9.enabled", False):
        return False
    guard = crash_Guard("WMFVPXVideo")
    try:
        decoder = create_Decoder()
    except Exception:
        return False
    if decoder is None:
        return False
    return True

if __name__ == "__main__":
    print("¿Puede reproducir VP9?:", can_Play_VP9())