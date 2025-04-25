# how to set tracking uri 
import warnings
import argparse
import logging
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
import mlflow
import mlflow.sklearn
from pathlib import Path

logging.basicConfig(level=logging.WARN)
logger = logging.getLogger(__name__)

#get arguments from command
parser = argparse.ArgumentParser()
parser.add_argument("--alpha", type=float, required=False, default=0.7)
parser.add_argument("--l1_ratio", type=float, required=False, default=0.6)
args = parser.parse_args()

#evaluation function
def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2


if __name__ == "__main__":
    warnings.filterwarnings("ignore")
    np.random.seed(40)

    # Read the wine-quality csv file from local
    data = pd.read_csv(r"C:\Users\G01889\OneDrive\Documents\DSS\MLflow\data\red-wine-quality.csv")
    # data.to_csv(r"C:\Users\G01889\OneDrive\Documents\DSS\MLflow\data\red-wine-quality.csv", index=False)

    # Split the data into training and test sets. (0.75, 0.25) split.
    train, test = train_test_split(data)
    train.to_csv(r'C:\Users\G01889\OneDrive\Documents\DSS\MLflow\data\train.csv')
    test.to_csv(r'C:\Users\G01889\OneDrive\Documents\DSS\MLflow\data\test.csv')
    # The predicted column is "quality" which is a scalar from [3, 9]
    train_x = train.drop(["quality"], axis=1)
    test_x = test.drop(["quality"], axis=1)
    train_y = train[["quality"]]
    test_y = test[["quality"]]

    alpha = args.alpha
    l1_ratio = args.l1_ratio


    mlflow.set_tracking_uri("") # 
    print('::',Path.cwd())

    # # set experiment
    exp = mlflow.set_experiment(experiment_name='Exp_4')

    mlflow.start_run(experiment_id=exp.experiment_id)  # run id over write 
    # with mlflow.start_run(experiment_id = exp_id):
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=42)
    lr.fit(train_x, train_y)

    predicted_qualities = lr.predict(test_x)

    (rmse, mae, r2) = eval_metrics(test_y, predicted_qualities)

    print("Elasticnet model (alpha={:f}, l1_ratio={:f}):".format(alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)

    param = {'alpha':alpha, 'l1_ratio':l1_ratio}
    metric = {'rmse':rmse, 'mae':mae, 'r2':r2}
    mlflow.log_params(params=param)
    mlflow.log_metrics(metrics=metric)



    # this is used when single file available in folder 
    # mlflow.log_artifact(local_path=r"C:\Users\G01889\OneDrive\Documents\DSS\MLflow\data\red-wine-quality.csv",artifact_path='C:/Users/G01889/OneDrive/Documents/mlrun')
    # mlflow.log_artifact(local_path=r"C:\Users\G01889\OneDrive\Documents\DSS\MLflow\data\red-wine-quality.csv",artifact_path='mlr')
    # mlflow.log_artifact(local_path=r"C:\Users\G01889\OneDrive\Documents\DSS\MLflow\data\red-wine-quality.csv",artifact_path='')
    # when multiple files available like images then use 
    mlflow.log_artifacts(local_dir=r"C:\Users\G01889\OneDrive\Documents\DSS\MLflow\data",artifact_path='')

    # artifect = mlflow.get_artifact_uri()
    
    artifect = mlflow.get_artifact_uri(r'C:\Users\G01889\OneDrive\Documents\DSS\MLflow\mlflow_project1\mlruns\270940324075878896\54de12b8fc3b43bea14258a8c1c080e5\artifacts\red-wine-quality_1.csv')
    print('art:',artifect)




    mlflow.sklearn.log_model(lr,"abc") # here changed artifect location 


    mlflow.end_run(status='FINISHED')

    run1 = mlflow.last_active_run()
    print('run1:',run1.info.run_id)
    print('run1_name:',run1.info.run_name)