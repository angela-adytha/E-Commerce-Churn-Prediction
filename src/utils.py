from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.metrics import roc_auc_score, recall_score, precision_score, f1_score, fbeta_score
from sklearn.model_selection import StratifiedKFold, cross_validate
import pandas as pd
import numpy as np

class GroupedMedianImputer(BaseEstimator, TransformerMixin):
    def __init__(self, group_col, target_col):
        self.group_col = group_col
        self.target_col = target_col

    def fit(self, X, y=None):
        df = pd.DataFrame(X, columns=[self.group_col, self.target_col])
        self.group_medians_ = df.groupby(self.group_col)[self.target_col].median()
        self.global_median_ = df[self.target_col].median()
        return self

    def transform(self, X):
        df = pd.DataFrame(X, columns=[self.group_col, self.target_col]).copy()
        mapped_median = df[self.group_col].map(self.group_medians_)
        mapped_median = mapped_median.fillna(self.global_median_)
        df[self.target_col] = df[self.target_col].fillna(mapped_median)
        return df[[self.target_col]].values
    
    def get_feature_names_out(self, input_features=None):
        return np.array([self.target_col])
    
def benchmark_models(pipeline, candidates, x_train, y_train, 
                      scoring='recall', cv=5, random_state=None):
    
    all_cv_result = []

    skf = StratifiedKFold(
        n_splits=cv,
        shuffle=True,
        random_state=random_state
    )

    for name, model in candidates.items():
        classifier = pipeline.set_params(classifier=model)
        cv_result = cross_validate(
            estimator=classifier,
            X=x_train, y=y_train,
            cv=skf,
            scoring=scoring,
            return_train_score=True
        )
        all_cv_result.append({
            "name": name,
            "mean_train_score": np.mean(cv_result["train_score"]),
            "std_train_score": np.std(cv_result["train_score"]),
            "mean_test_score": np.mean(cv_result["test_score"]),
            "std_test_score": np.std(cv_result["test_score"])
        })

    result_df = pd.DataFrame(all_cv_result).sort_values(
        "mean_test_score", ascending=False
    ).reset_index(drop=True)

    return result_df