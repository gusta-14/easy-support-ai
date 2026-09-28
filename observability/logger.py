import json
import logging
from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_PATH = LOG_DIR / "app.jsonl"

LOG_DIR.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def log_event(data: dict) -> None:
    """Regista eventos estruturados em formato JSONL para auditoria."""
    payload = {
        "timestamp": datetime.utcnow().isoformat(),
        **data
    }
    try:
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(json.dumps(payload, ensure_ascii=False) + "\n")
    except Exception as e:
        logging.error(f"Falha ao escrever log estruturado: {e}")