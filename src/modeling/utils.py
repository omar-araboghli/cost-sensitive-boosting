
from .adacost import AdaCost
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree
import numpy as np
import collections
import os


def createClassifier(algorithm, base_estimator, n_estimators, learning_rate, class_weight, random_state,tracker):
    if base_estimator == "SVC":
        base_estimator = svm.SVC(gamma=2, C=1)
    elif base_estimator == "KNN":
        base_estimator = KNeighborsClassifier(3)
    else:
        base_estimator = tree.DecisionTreeClassifier(random_state=random_state, max_depth=5)

    return AdaCost(base_estimator, n_estimators, learning_rate, algorithm, class_weight, random_state, tracker)

# returns classes sorted by number of instances
def classes_ordered_by_instances(data):
    classes = dict(collections.Counter(data.tolist()))
    keys,values=zip(*sorted(zip(classes.keys(),classes.values()),reverse=True))
    sorted_classes=keys
    return sorted_classes

def store_results(dataset, all_measures, root_path):
    dataset_name = os.path.splitext(dataset)[0]
    dataset_path = os.path.join(root_path, 'data', 'results', dataset_name)

    if not os.path.exists(dataset_path):
        os.makedirs(dataset_path)

    for measure in all_measures.items():
        file_name = '{}_{}.png'.format(dataset_name, measure[0])
        file_path = os.path.join(dataset_path, file_name)
        measure[1]['plot'].savefig(file_path)