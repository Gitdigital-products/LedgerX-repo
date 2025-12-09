#!/bin/bash
# LedgerX Governance Pipeline Script

echo "🔍 Starting compliance scan..."
python3 scripts/scan.py

echo "🏷️ Applying tags..."
python3 scripts/tag.py

echo "📝 Logging results..."
python3 scripts/log.py

echo "✅ Governance pipeline complete."