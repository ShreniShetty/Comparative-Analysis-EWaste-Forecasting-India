import csv
import unittest
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parents[1]


def read_rows(path):
    with (ROOT / path).open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


class PublishedResultsTest(unittest.TestCase):
    def test_scores_match_chronological_predictions(self):
        history = read_rows("data/processed/national_ewaste_full.csv")
        self.assertEqual([int(row["year_index"]) for row in history],
                         list(range(1, len(history) + 1)))
        predictions = read_rows("outputs/model_results/model_predictions.csv")
        metrics = read_rows("outputs/model_results/model_metrics.csv")
        self.assertEqual(len({row["Model"] for row in metrics}), 7)
        self.assertEqual({row["Model"] for row in metrics},
                         {row["model"] for row in predictions})
        for score in metrics:
            with self.subTest(model=score["Model"]):
                folds = [row for row in predictions if row["model"] == score["Model"]]
                self.assertEqual(sorted(int(row["train_size"]) for row in folds),
                                 list(range(4, len(history))))
                errors = []
                for fold in folds:
                    target = history[int(fold["train_size"])]
                    self.assertEqual(fold["test_fy"], target["financial_year"])
                    actual = float(target["ewaste_generated_tonnes"])
                    self.assertAlmostEqual(float(fold["actual"]), actual)
                    errors.append(abs(float(fold["predicted"]) - actual))
                self.assertAlmostEqual(float(score["MAE_tonnes"]), mean(errors), delta=0.5)

    def test_power_bi_uses_published_model_results(self):
        for name in ("model_metrics.csv", "model_predictions.csv",
                     "model_robustness_results.csv", "forecast_results.csv"):
            with self.subTest(file=name):
                self.assertEqual(read_rows("outputs/model_results/" + name),
                                 read_rows("outputs/power_bi/" + name))
