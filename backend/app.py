import argparse
import json
from pathlib import Path
from rich import print_json

import sys
CURRENT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = CURRENT_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.workflows.ecommerce_video_pipeline import EcommerceVideoPipeline


def main():
    parser = argparse.ArgumentParser(description="Run AutoCommerce-Agent demo.")
    parser.add_argument("--case", required=True, help="Path to product case JSON.")
    parser.add_argument("--output", default="outputs/demo_output.json", help="Output JSON path.")
    args = parser.parse_args()

    case_path = Path(args.case)
    product = json.loads(case_path.read_text(encoding="utf-8"))

    pipeline = EcommerceVideoPipeline()
    result = pipeline.run(product)

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    print_json(data=result)
    print(f"\nSaved to: {output_path}")


if __name__ == "__main__":
    main()
