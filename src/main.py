from src.crash_guard import CrashGuard

# Variable global para preferencias
prefs = {
    "media.wmf.vp9.enabled": True
}

# Función global para crash guard
def crashGuard(name):
    return CrashGuard(name)

def createDecoder():
    # Simulación de creación de decoder
    return "decoder"

def canPlayVP9():
    if not prefs.get("media.wmf.vp9.enabled", False):
        return False
    guard = crashGuard("WMFVPXVideo")
    try:
        decoder = createDecoder()
    except Exception:
        return False
    if decoder is None:
        return False
    return True

if __name__ == "__main__":
    print("¿Puede reproducir VP9?:", canPlayVP9())