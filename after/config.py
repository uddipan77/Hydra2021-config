from dataclasses import dataclass


@dataclass
class Paths:
    log: str
    data: str


@dataclass
class Files:
    train_data: str
    train_labels: str
    test_data: str
    test_labels: str


@dataclass
class Params:
    epoch_count: int
    lr: float
    batch_size: int


@dataclass
class MNISTConfig:
    paths: Paths
    files: Files
    params: Params

#MNISTConfig acts like the class provides a single entry point for the entire configuration, now my cfg obj in main will refer to this class to access the rest 
#of the config class and their attributes
